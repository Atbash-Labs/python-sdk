import pysftp
import requests


class Sftp:
    def __init__(self, api_key, ip_addr, port=8080):
        """Constructor Method"""
        # Set connection object to None (initial value)
        self.connection = None
        self.api_key = api_key
        self.ip_addr = ip_addr
        self.port = port

    def _connect(self):
        """Connects to the sftp server and returns the sftp connection object"""

        try:
            # Get the sftp connection object
            self.connection = pysftp.Connection(
                host=self.ip_addr,
                username=self.username,
                password=self.password,
                port=self.port,
            )
        except Exception as err:
            raise Exception(err)
        finally:
            print(f"Connected to {self.ip_addr} as {self.username}.")

    def get_connection(self):
        """Initiate a sftp connection"""

        enclave_url = "https://{}:{}/get_creds".format(self.ip_addr, self.port)

        payload = {"api_key": self.api_key}
        r = requests.get(enclave_url, params=payload)
        creds = r.json()

        self.username = creds["username"]
        self.password = creds["password"]

        self._connect()

    def disconnect(self):
        """Closes the sftp connection"""
        self.connection.close()
        print(f"Disconnected from host {self.ip_addr}")

    def upload(self, source_local_path):
        """
        Uploads the source files from local to the sftp server.

        Args:
            source_local_path: local file path for patient data
        """

        try:
            remote_path = "/var/sftp/Data"

            print(
                f"uploading to {self.hostname} as {self.username} from source local path: {source_local_path}"
            )

            # Upload file with SFTP
            self.connection.put(source_local_path, remote_path)
            print("upload completed")

        except Exception as err:
            raise Exception(err)

    def listdir(self, remote_path):
        """lists all the files and directories in the specified path and returns them

        Args:
            remote_path: remote file path for patient data files list retrieval
        """
        for obj in self.connection.listdir(remote_path):
            yield obj


class Buyer:
    def __init__(self, api_key, ip_addr, port=8080, use_https=False):
        """Constructor Method"""
        self.api_key = api_key
        self.query_count = 0
        self.all_queries = []
        self.ip_addr = ip_addr
        self.port = port
        self.terminator = "s" if use_https else ""
        self.url = f"http{self.terminator}://{self.ip_addr}:{self.port}"
        self.key_list = self.get_key_list()
        if not self.key_list:
            self.key_list = [self.get_key()]

    def get_key(self):
        """Return the sub key for this buyer

        Returns:
            returns a subkey
        """
        subkey_url = f"{self.url}/get_subkey"

        payload = {"buyer_api_key": self.api_key}
        r = requests.get(subkey_url, params=payload)
        rsp = r.json()

        if r.status_code != 200:
            error = rsp["message"]
            print(error)

        try:
            subkey = rsp["subkey"]
            self.key_list = [subkey] + self.key_list

            return subkey
        except:
            print(rsp)
            return None

    def get_key_list(self):
        """Return the list of sub keys for this buyer

        Returns:
            returns the list of sub keys
        """
        subkey_list_url = f"{self.url}/list_subkeys"

        payload = {"buyer_api_key": self.api_key}
        r = requests.get(subkey_list_url, params=payload)
        rsp = r.json()

        if r.status_code != 200:
            error = rsp["message"]
            print(error)

        subkey_list = rsp["subkeys"]

        return subkey_list

    def query(self, query_key=None, query=""):
        """Initiate the query and return the result

        Args:
            query_key: [optional] subkey query key
            query: sql query string

        Returns:
            returns the accuracy,result of the query
        """
        if query_key is None:
            query_key = self.key_list[0]
        query_url = f"{self.url}/execute_query"

        curr_query = {}

        payload = {"buyer_api_key": self.api_key, "subkey": query_key, "query": query}
        r = requests.get(query_url, params=payload)
        rsp = r.json()

        if r.status_code != 200:
            error = rsp["message"]
            if error == "list index out of range":
                return (
                    [],
                    "No results had sufficiently large cell sizes to be nonidentifying",
                )
            return error, []

        result = rsp["result"]
        accuracy = rsp["accuracy"]

        # record query and results
        curr_query["query"] = query
        curr_query["result"] = result
        self.all_queries.append(curr_query)
        self.query_count += 1

        return result, accuracy

    def get_columns(self, query_key):
        """Return table ddl columns
        Args:
            query_key: subkey query key

        Returns:
            returns the list of columns
        """
        query_url = f"{self.url}/list_columns"

        payload = {"buyer_api_key": self.api_key, "subkey": query_key}
        r = requests.get(query_url, params=payload)
        rsp = r.json()

        if r.status_code != 200:
            error = rsp["message"]
            print(error)
            return None
        else:
            return rsp["columns"]

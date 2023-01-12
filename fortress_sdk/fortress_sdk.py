import requests


class Buyer:
    """
    ``Buyer`` object to interact with the network

    :param api_key: The ``API KEY`` from the website console
    :type api_key: str

    :param ip_addr: The ``IP Address`` key from the website console
    :type ip_addr: str

    :param port: The ``PORT`` from the website console
    :type port: int

    :param use_https: the boolean for the https toggle
    :type use_https: bool
    """

    def __init__(self, api_key, ip_addr, port=8080, use_https=False):
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
        """
        Return the sub key for this buyer

        :return: the sub key for the instantiated buyer object
        :rtype: str
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
        """
        Return the list of sub keys for this buyer

        :return: returns the list of sub keys
        :rtype: list
        """
        subkey_list_url = f"{self.url}/list_subkeys"

        payload = {"buyer_api_key": self.api_key}
        r = requests.get(subkey_list_url, params=payload)
        rsp = r.json()

        if r.status_code != 200:
            error = rsp["message"]
            print(error)

        try:
            subkey_list = rsp["subkeys"]
            return subkey_list
        except:
            return None

    def query(self, query_key=None, query=""):
        """
        Initiate the query and return the result

        :param str query_key: [optional] subkey query key
        :param str query: query string

        :return: return ``result`` and ``accuracy`` of the query
        :rtype: list,str
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
        accuracy_num = float(accuracy.split("within: ")[1].split("%")[0])
        accuracy_num = 10 * accuracy_num
        accuracy = (
            f"Results of this query can be expected to be within: "
            f"{round(accuracy_num, 2)}%"
            f" of the true value "
            f"with 95% probability"
        )

        # record query and results
        curr_query["query"] = query
        curr_query["result"] = result
        curr_query["accuracy"] = accuracy
        self.all_queries.append(curr_query)
        self.query_count += 1

        return result, accuracy

    def get_columns(self, query_key=None):
        """
        Return table ddl columns

        :param str query_key: [optional] subkey query key

        :return: returns the list of columns
        :rtype: list
        """

        if query_key is None:
            query_key = self.key_list[0]
        query_url = f"{self.url}/list_columns"

        payload = {"buyer_api_key": self.api_key, "subkey": query_key}
        r = requests.get(query_url, params=payload)
        rsp = r.json()

        if r.status_code != 200:
            error = rsp["message"]
            print(error)
            return None
        else:
            columns = rsp["columns"]
            return columns

    def print_query_history(self):
        """Pretty print the history queries with accuracy and results"""

        query_format = " query ===> {q} \n result ===> {r} \n accuracy ===> {a} \n"

        table_frame = "+" + "-" * 80 + "+"

        for query in self.all_queries:
            print(table_frame)
            query_string = query_format.format(
                q=query["query"],
                r=query["result"],
                a=query["accuracy"][44:],
            )
            print(query_string)

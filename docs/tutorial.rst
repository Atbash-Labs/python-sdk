Tutorial
========

The best way to interact with the network is to use the ``Buyer`` & ``Sftp`` extension objects and its associated methods.


1. Querying health datasets
-----------------------------
Executing a query :
For executing a query, we get the api key and ip address from the web dashboard and then create a
``Buyer`` instance and then call a query method on that buyer instance with a SQL query string and then print recieved query accuracy and results.


.. code-block:: python

    from fortress_sdk import Buyer

    api_key = "buyer_key"  # get this from the fortress web dashboard
    ip_addr = "127.0.0.1"

    # Initialize a buyer instance
    buyer = Buyer(api_key, ip_addr)

    # Initiate a query
    sql_query = "select count(*) as numpeople from public.condition_era_death"
    result, accuracy = buyer.query(query=sql_query)

    # execution result and accuracy of the query
    print(result)
    print(accuracy)

Pretty print query history :

.. code-block:: python

    ###########################################
    ####        Print Query History        ####
    ###########################################

    buyer.print_query_history()

    +--------------------------------------------------------------+--------------------------+-----------------------------------------------------+
    |                            Query                             |          Result          |                       Accuracy                      |
    +--------------------------------------------------------------+--------------------------+-----------------------------------------------------+
    | select count(*) as numpeople from public.condition_era_death | [['numpeople'], [30297]] | within: 0.1% of the true value with 95% probability |
    | select count(*) as numpeople from public.condition_era_death | [['numpeople'], [30297]] | within: 0.1% of the true value with 95% probability |
    +--------------------------------------------------------------+--------------------------+-----------------------------------------------------+


2. Uploading data to Fortress Network
--------------------------------------
Uploading data :
For uploading data, we get the api key and ip address from the web dashboard and then create a
``Sftp`` instance and then create a connection with ``get_connection()`` , now give the local path of files to be 
uploaded with ``sftp.uploadlocal_path()``

.. code-block:: python

    from fortress_sdk import Sftp

    api_key = "apikey1234"
    ip_addr = "0.0.0.8080"

    # Initialize a SFTP instance
    sftp = Sftp(api_key, ip_addr)

    # Connect to SFTP
    sftp.get_connection()

    # upload files to enclave SFTP location from local
    local_path = "/prince/health/person.csv"
    sftp.upload(local_path)

    # list files at enclave SFTP location after upload
    path = "/healthfiles"
    print(f"List of files at location {path}:")
    print([f for f in sftp.listdir(path)])

    # Disconnect from SFTP
    sftp.disconnect()
Tutorial
========

The best way to interact with the network is to use the ``Buyer`` & ``Sftp`` extension objects and its associated methods.


1. Querying Fortress Network
-----------------------------
Executing a query :

.. code-block:: python

    import pandas as pd
    from fortress_sdk import Buyer

    api_key = "buyer_key"  # get this from the fortress web dashboard
    ip_addr = "127.0.0.1"

    # Initialize a buyer instance
    buyer = Buyer(api_key, ip_addr)

    # Initiate a query
    sql_query = "select count(*) as numpeople from public.condition_era_death"
    result, accuracy = buyer.query(query=sql_query)

    # execution result and accuracy of the query
    print(pd.DataFrame(result))
    print(accuracy)

Iterate over query history :

.. code-block:: python

    ###########################################
    ####          Query History            ####
    ###########################################

    # you can access the query history with:
    all_queries = buyer.all_queries 
    print(all_queries)

2. Uploading data to Fortress Network
--------------------------------------
Uploading data :

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
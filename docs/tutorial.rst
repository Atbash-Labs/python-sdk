Tutorial
========

The best way to interact with the network is to use the ``Buyer`` extension objects and its associated methods.


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

    +--------------------------------------------------------------------------------+
    query ===> select count(*) as numpeople from public.condition_era_death
    result ===> [['numpeople'], [30297]]
    accuracy ===> within: 0.1% of the true value with 95% probability

    +--------------------------------------------------------------------------------+
    query ===> select count(*) as numpeople from public.condition_era_death
    result ===> [['numpeople'], [30297]]
    accuracy ===> within: 0.1% of the true value with 95% probability

    +--------------------------------------------------------------------------------+
    query ===> select count(*) as numpeople from public.condition_era_death
    result ===> [['numpeople'], [30297]]
    accuracy ===> within: 0.1% of the true value with 95% probability

    +--------------------------------------------------------------------------------+

Tutorial
========

The best way to interact with the network is to use the ``Buyer`` extension objects and its associated methods.


Querying health datasets 
----------------------------
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

    sql_query = "select count(*) as people_per_condition from person"
    result, accuracy = buyer.query(query=sql_query)

    # execution result and accuracy of the query
    print(result)
    print(accuracy)


NOTE!! : Related to SQL querying rules
----------------------------------------

- **allowed**:  Group by, selection of count, sum/min/max/avg of limited columns, of raw columns that are the group-by columns, any where conditions
- **not allowed**:  join, selection of columns that aren't in the group by, arbitrary sum/min/max/avgs


Pretty print query history 
------------------------------

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
    query ===> select count(*) as people_per_condition from person
    result ===> [['people_per_condition'], [2000000]]
    accuracy ===> within: 0.0% of the true value with 95% probability



Get queryable table columns
------------------------------

.. code-block:: python
    
    ###########################################
    ####      Print Table DDL columns      ####
    ###########################################


    print("-----------------------COLUMNS-----------------------")
    columns = buyer.get_columns()
    print(columns["PERSON"])
    print(columns["PERSON_VISIT_OCCURRENCE"])

    -----------------------COLUMNS--------------------
    ['birth_datetime', 'care_site_id', 'day_of_birth', 'ethnicity_concept_id', 
    'ethnicity_source_concept_id', 'ethnicity_source_value', 'gender_concept_id', 
    'gender_source_concept_id', 'gender_source_value', 'location_id', 'month_of_birth', 
    'person_id', 'person_source_value', 'provider_id', 'race_concept_id', 'race_source_concept_id', 
    'race_source_value', 'year_of_birth']

    ['admitted_from_concept_id', 'admitted_from_source_value', 'birth_datetime', 
    'care_site_id', 'day_of_birth', 'discharged_to_concept_id', 'discharged_to_source_value', 
    'ethnicity_concept_id', 'ethnicity_source_concept_id', 'ethnicity_source_value', 
    'gender_concept_id', 'gender_source_concept_id', 'gender_source_value', 'location_id', 
    'month_of_birth', 'person_id', 'person_source_value', 'preceding_visit_occurrence_id', 
    'provider_id', 'race_concept_id', 'race_source_concept_id', 'race_source_value', 
    'visit_concept_id', 'visit_end_date', 'visit_end_datetime', 'visit_occurrence_id', 
    'visit_source_concept_id', 'visit_source_value', 'visit_start_date', 'visit_start_datetime', 
    'visit_type_concept_id', 'year_of_birth']
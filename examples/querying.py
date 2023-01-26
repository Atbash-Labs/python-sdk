###########################################
####      EXAMPLE Querying USAGE       ####
###########################################
from fortress_sdk import Buyer

###########################################
####      Buyer Interaction Flow       ####
###########################################


api_key = "buyer_key"  # get this from the fortress web dashboard
ip_addr = "test-enclave.fortressenclaves-dev.com"

# Initialize a buyer instance
buyer = Buyer(api_key, ip_addr, use_https=True)


# Initiate a query
sql_query = "select count(*) as numpeople from public.condition_era_death"
result, accuracy = buyer.query(query=sql_query)

sql_query = "select count(*) as people_per_condition from person"
result, accuracy = buyer.query(query=sql_query)

# execution result and accuracy of the query
print(result)
print(accuracy)

# Pretty print query history
buyer.print_query_history()


# Print columns
print("-----------------------COLUMNS-----------------------")
columns = buyer.get_columns()
print(columns["PERSON"])
print(columns["PERSON_VISIT_OCCURRENCE"])

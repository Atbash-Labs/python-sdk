###########################################
####      EXAMPLE Querying USAGE       ####
###########################################

from fortress_sdk import Buyer

###########################################
####      Buyer Interaction Flow       ####
###########################################


api_key = "buyer_key"  # get this from the fortress web dashboard
ip_addr = "127.0.0.1"

payload = {"buyer_api_key": api_key}
buyer = Buyer(api_key, ip_addr)

# retrieve the query sub key
query_key = buyer.get_key()

# Initiate a query
sql_query = "select count(*) as numpeople from public.condition_era where condition_concept_id = 313217"  # we can also take in .sql file path and parse and send it internally
result, accuracy = buyer.query(query_key, sql_query)

# execution result and accuracy of the query
print(result)
print(accuracy)

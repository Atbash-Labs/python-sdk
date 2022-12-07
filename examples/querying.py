###########################################
####      EXAMPLE Querying USAGE       ####
###########################################
from fortress_sdk import Buyer

###########################################
####      Buyer Interaction Flow       ####
###########################################


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

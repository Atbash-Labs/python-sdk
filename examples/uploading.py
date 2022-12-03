###########################################
####      EXAMPLE Uploading USAGE      ####
###########################################

from fortress_sdk import Sftp


###########################################
####           Uploading Data          ####
###########################################

api_key = "apikey1234"
ip_addr = "0.0.0.8080"

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

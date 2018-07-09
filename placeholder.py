import pyTAPI  # my module (also sounds like PI THE PI)

# how to generate a random hash
print('Generate a hash! \n')
_hash = pyTAPI.generate_hash('some data', 'salt here ma dudes')  # generates a random hash
print(_hash)
print('\n')

# how to generate a random fernet key
print('Generate a key! \n')
_key = pyTAPI.generate_key()  # generates a random fernet key
print(_key)
print('\n')

# how to encrypt data
print('encrypting some data! \n')
_data = 'this is a message'
_data_converted = bytes(_data, encoding='UTF-8')  # converting string to bytes array
_encrypted_data = pyTAPI.encrypt_data(_key, _data_converted)  # encrypting data
print('encrypted data: \n')
print(_encrypted_data)  # printing the encrypted data
print('\n')

# how to decrypt data
print('decrypted some data! \n')
_decrypted_data = pyTAPI.decrypt_data(_key, _encrypted_data)  # decrypting data
print('decrypted data: \n')
print(_decrypted_data.decode('UTF-8'))  # printing a decoded bytes array into a string
print('\n')

# how to use the mysql connector object
_connector = pyTAPI.MysqlConnector()  # creating a new mysqlconnector object

_connector.server = 'mysql.server.io'  # MySQL server ip/hostname
_connector.username = 'admin'  # MySQL username
_connector.password = 'password'  # MySQL password
_connector.database_name = 'database_schema'  # MySQL Database Schema name

_session = _connector.connect()  # connecting to mysql database

_session.query('')  # querying database

# if you intend on inserting a value or updating it, use this additional line to apply your query:
# _session.commit()

_result = _session.store_result()  # store the results

_row = _result.fetch_row()  # fetching a row
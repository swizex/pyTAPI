# pyTAPI

Stands for py(why not? gotta respect tradition...) Teddys Application Programming Interface.

this api is a collection of stuff i often use and or wanted to make easier/faster for myself to implement stuff
without hassle.

so far this api has the following functionalitys:

* [Generate a Hash (using the flask_hashing library)](#generating-a-hash)
* [Generate a Fernet encryption key (using cryptography.fernet library)](#generating-a-fernet-key)
* [Encrypt a bytes array (using cryptography.fernet library)](#encrypting-data)
* [Decrypt a bytes array (using cryptography.fernet library)](#decrypting-data)
* [MysqlClient custom object for faster integration (using mysql-client library)](#using-the-custom-mysql-client-object)
* [Convert a variable to a string (UTF-8) (Built in Python 3.x libraries)](#converting-a-variable-to-string)
* [Sending an email using google mail smtp (Built in Python 3.x smtplib library)](#using-the-custom-google-mail-smtp-email-sender-object)
* [tor requests (using requests library)](#using-tor-requests)

to install the latest version of this module, simply use pip to install it

`pip install pyTAPI`

## Example Usages

### Generating a hash

to generate a hash simply use the following commands:

```python
_content = 'some content'
_salt = 'some salt'

h = pyTAPI.generate_hash(_content, _salt)
```

### Generating a Fernet key

to generate a fernet key simply use the following command:

```python
key = pyTAPI.generate_key()
```

### Encrypting Data

to encrypt a bytes array simply use the following commands:

```python

_key = b'keyhere'
_data = b'message'

encrypted_data = pyTAPI.encrypt_data(_key, _data)

```

where `_key` is a fernet key and where `_data` is a bytes array

### Decrypting Data

to decrypt a fernet token simply use the following commands:

```python

decypted_data = pyTAPI.decrypt_data(_key, _token)

```

where `_key` is your fernet key, and `_token` is the generated fernet token

### Using the custom mysql-client object

```python

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

```

### Converting a variable to string

use the following command to convert any variable (that has a .decode() function) to string format (UTF-8):

```python
_example_var = b'message'

_str_converted = pyTAPI.Tostring(_example_var)

```

### Using the custom google mail smtp email sender object

to send an email using google smtp use the following commands:

```python

gmail = pyTAPI.GoogleMail()  # declaring custom object

gmail.sender = '***@gmail.com'  # account the email will display as sender
gmail.login = '***@gmail.com'  # account that is used to send the email
gmail.password = '***'  # 2-step verification app password
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple senders possible)
gmail.subject = 'SUBJECT'  # subject of the email
gmail.content = 'CONTENT'  # contents of the email

temp = gmail.send()  # send the email

print(temp)  # debugging purposes


```

### Using tor requests

to request something via the tor network, simply have a local tor instance running and use the following commands:

```python

res = pyTAPI.tor_request('url', 'type')  # types: 'text','content','links'

```

function returns a text version of the reply if reply type is set to `text`, returns contents of the request if set to `content`, returns links if set to `links`
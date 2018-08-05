# Custom MySQL-Client Object

This custom object will let you set-up MySQL database connections easier and faster.

Code Snippet:

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

Explanation:

Declaring new custom MySQL connector

```python
_connector = pyTAPI.MysqlConnector()  # creating a new mysqlconnector object
```

Adding server IP/hostname

```python
_connector.server = 'mysql.server.io'  # MySQL server ip/hostname
```

Adding MySQL account username

```python
_connector.username = 'admin'  # MySQL username
```

Adding MySQL account password

```python
_connector.password = 'password'  # MySQL password
```

Adding the database schema we will be accessing

```python
_connector.database_name = 'database_schema'  # MySQL Database Schema name
```

Connecting to MySQL server

```python
_session = _connector.connect()  # connecting to mysql database
```

Querying the database

```python
_session.query('')  # querying database
```

Commit changes to the database

```python
_session.commit()
```

Storing query results

```python
_result = _session.store_result()  # store the results
```

Fetching row/s

```python
_row = _result.fetch_row()  # fetching a row
```

**NOTE:** *you can use* 
`_result.fetch_row()[x][y]`
*to fetch a specific row and collumn (x - row, y - collumn)* 
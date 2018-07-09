from cryptography.fernet import Fernet
import MySQLdb
from flask_hashing import Hashing

hashing = Hashing()
# note to myself, this is using mysqlclient-1.3.12


class MysqlConnector(object):
    server = ''
    username = ''
    password = ''
    database_name = ''

    def connect(self):
        _connector = MysqlConnector()
        _connector.server = self.server
        _connector.username = self.username
        _connector.password = self.password
        _connector.database_name = self.database_name

        db = MySQLdb.connect(host=_connector.server, user=_connector.username, passwd=_connector.password, db=_connector.database_name)

        return db


def generate_hash(_content, _salt):  # generates a random hash...
    h = hashing.hash_value(_content, _salt)
    return h


def generate_key():  # generates a random key...
    _key = Fernet.generate_key()
    return _key


def encrypt_data(_key, _data):  # encrypts data using fernet encryption (symmetric encryption)
    f = Fernet(_key)

    token = f.encrypt(_data)

    return token


def decrypt_data(_key, _token):  # decrypts data using fernet decryption (symmetric encryption)
    f = Fernet(_key)

    _decrypted_data = f.decrypt(_token)

    return _decrypted_data


def Tostring(_var):

    temp01 = _var.decode('UTF-8')

    return temp01


# written by teddy morduhovich,2018
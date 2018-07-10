from cryptography.fernet import Fernet
import MySQLdb
from flask_hashing import Hashing
import smtplib
from email.message import EmailMessage
import requests
hashing = Hashing()


# note to myself, this is using mysqlclient-1.3.12

def tor_request(url, reply_type):
    try:
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5h://localhost:9150'
        session.proxies['https'] = 'socks5h://localhost:9150'

        if reply_type == 'text':
            _res = session.get(url).text

        if reply_type == 'content':
            _res = session.get(url).content

        if reply_type == 'links':
            _res = session.get(url).links

        return _res
    except Exception as e:
        return e.__str__()


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

        try:
            db = MySQLdb.connect(host=_connector.server, user=_connector.username, passwd=_connector.password, db=_connector.database_name)
            return db

        except Exception as e:
            return 'failed to connect to database!' + e.__str__()


class GoogleMail(object):
    sender = ''
    to = ['']
    subject = ''
    content = ''
    login = ''
    password = ''

    def send(self):
        _object = GoogleMail()
        _object.sender = self.sender
        _object.to = self.to
        _object.subject = self.subject
        _object.content = self.content
        _object._login = self.login
        _object._password = self.password

        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # ssl connection
            server_ssl.ehlo()

            server_ssl.login(_object._login, _object._password)

            msg = EmailMessage()

            msg['Subject'] = _object.subject
            msg['From'] = _object.sender
            msg['To'] = _object.to
            msg.set_content('From: %s \n' % _object.sender + _object.content)

            server_ssl.send_message(msg, _object.sender, _object.to)

            server_ssl.quit()

            return 'sent mail successfully!'

        except Exception as e:
            return 'failed to send mail! Exception: ' + e.args.__str__()


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


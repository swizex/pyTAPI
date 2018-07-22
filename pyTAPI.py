from cryptography.fernet import Fernet
import MySQLdb
from flask_hashing import Hashing
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import sys
import mistune
from pygments import highlight
from pygments.lexers.python import PythonLexer
from pygments.formatters.html import HtmlFormatter
import uuid

hashing = Hashing()

# note to myself, this is using mysqlclient-1.3.12


def string_to_binary(_str):  # encodes any string to binary
    _temp = bin(int.from_bytes(_str.encode(), 'big'))

    return _temp


def binary_to_string(_binary):  # decodes any binary back to actual ascii string representation of the binary
    n = int(_binary, 2)
    _temp04 = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

    return _temp04.__str__()


def generate_uuid():  # generates random uuid

    _uuid = uuid.uuid4()

    return _uuid


def generate_string_uuid(_string):  # generates a uuid based on a string

    _uuid = uuid.UUID(bytes=_string.bytes)

    return _uuid


def generate_highlight(_code):

    _formatter = HtmlFormatter(style='default', linenos=False, noclasses=True)

    temp01 = highlight(_code, PythonLexer(), _formatter)

    return temp01


def markdown_converter(_string):
    markdown = mistune.Markdown()
    temp01 = markdown(_string).__str__()

    return temp01


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
    plain = ''
    style = ''
    meta = ''
    title = ''

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
            return 'failed to send mail! Exception: ' + e.args.__str__() + 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)

    def sendhtml(self):
        _object = GoogleMail()
        _object.sender = self.sender
        _object.to = self.to
        _object.subject = self.subject
        _object.content = self.content
        _object._login = self.login
        _object._password = self.password
        _object.plain = self.plain

        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # ssl connection
            server_ssl.ehlo()

            server_ssl.login(_object._login, _object._password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = _object.subject
            msg['From'] = _object.sender
            msg['To'] = _object.to

            # Create the body of the message (a plain-text and an HTML version).
            text = _object.plain
            html = """\
            <html>
              <head></head>
              <body>
                    %s
              </body>
            </html>
            """ % _object.content

            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            msg.attach(part1)
            msg.attach(part2)

            server_ssl.sendmail(_object.sender, _object.to, msg.as_string())

            server_ssl.quit()

            return 'sent mail successfully!'

        except Exception as e:
            return 'failed to send mail! Exception: ' + e.args.__str__() + 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)

    def sendcustomhtml(self):
        _object = GoogleMail()
        _object.sender = self.sender
        _object.to = self.to
        _object.subject = self.subject
        _object.content = self.content
        _object._login = self.login
        _object._password = self.password
        _object.plain = self.plain
        _object.style = self.style
        _object.meta = self.meta
        _object.title = self.title

        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # ssl connection
            server_ssl.ehlo()

            server_ssl.login(_object._login, _object._password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = _object.subject
            msg['From'] = _object.sender
            msg['To'] = _object.to

            # Create the body of the message (a plain-text and an HTML version).
            text = _object.plain
            html = """\
            <html>
              <head>
              %s
              
              %s
              
              %s
              </head>
              <body>
                    %s
              </body>
            </html>
            """ % (_object.title, _object.meta, _object.style, _object.content)

            # Record the MIME types of both parts - text/plain and text/html.
            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            # Attach parts into message container.
            # According to RFC 2046, the last part of a multipart message, in this case
            # the HTML message, is best and preferred.
            msg.attach(part1)
            msg.attach(part2)

            server_ssl.sendmail(_object.sender, _object.to, msg.as_string())

            server_ssl.quit()

            return 'sent mail successfully!'

        except Exception as e:
            return 'failed to send mail! Exception: ' + e.args.__str__() + 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)


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


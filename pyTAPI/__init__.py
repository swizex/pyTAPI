__all__ = ['pyTAPI']
name = "pyTAPI"

from .pyTAPI import AESEncryption
from .pyTAPI import MysqlConnector
from .pyTAPI import GoogleMail
from .pyTAPI import encrypt_data
from .pyTAPI import decrypt_data
from .pyTAPI import generate_key
from .pyTAPI import generate_hash
from .pyTAPI import generate_uuid
from .pyTAPI import generate_string_uuid
from .pyTAPI import generate_highlight
from .pyTAPI import markdown_converter
from .pyTAPI import Tostring

AESEncryption = AESEncryption()
MysqlConnector = MysqlConnector()
GoogleMail = GoogleMail()


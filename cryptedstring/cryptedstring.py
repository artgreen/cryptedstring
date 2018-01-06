from cryptography.fernet import Fernet
import json
import base64


class CryptedString:
    '''Simple class to manage encrypted strings'''

    def __init__(self, key_file_name):
        '''Initialize self and read key from key file. Key file is a JSON file with one key called
        amazingly enough "key". The key should be an UTF-8 string as prepared from Fernet.generate_key().

        The idea is that this key file will be OS protected and not world readable.  Doing otherwise would
        be pretty daft.
        '''
        self.encoding = "utf-8"
        self.key_file_name = key_file_name

        with open(self.key_file_name) as key_file:
            self.key = json.load(key_file)['key']
        try:
            base64.decodebytes(bytes(self.key, self.encoding))
        except Exception:
            raise ValueError("Invalid key format")

    def decrypt(self, cipher_text):
        '''Decrypt a string previously encrypted with Fernet.encrypt().
        Only feed decrypt a string and not a byte stream.
        Returns the plain text for the input cipher text.'''
        f = Fernet(bytes(self.key, self.encoding))
        return f.decrypt(bytes(cipher_text, self.encoding)).decode(self.encoding)

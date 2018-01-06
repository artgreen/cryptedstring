import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cryptedstring import cryptedstring
from unittest import TestCase

cipher_text = "gAAAAABaT_lnh9zEKZ_m53TTQx-O8-j4fEJg_ksv76gohUDgtH_-ga6VZydOOsF4e0Bj4GroNozofdwyOCD9KrWXVbUZ-Q3XqA=="
cipher_text_bytes = b"gAAAAABaT_lnh9zEKZ_m53TTQx-O8-j4fEJg_ksv76gohUDgtH_-ga6VZydOOsF4e0Bj4GroNozofdwyOCD9KrWXVbUZ-Q3XqA=="
plain_text = 'this is a test'


class TestDatacenter(TestCase):
    def test_create(self):
        cstring = cryptedstring.CryptedString('test-key.json')
        self.assertEqual(plain_text, cstring.decrypt(cipher_text))
        self.assertNotEqual('blahblahblahblah', cstring.decrypt(cipher_text))

    def test_create_invalid(self):
        self.assertRaises(FileNotFoundError, cryptedstring.CryptedString, 'missing.json')

    def test_bad_key(self):
        self.assertRaises(ValueError, cryptedstring.CryptedString, 'test-key-bad.json')

    def test_bad_text(self):
        cstring = cryptedstring.CryptedString('test-key.json')
        self.assertRaises(TypeError, cstring.decrypt, cipher_text_bytes)

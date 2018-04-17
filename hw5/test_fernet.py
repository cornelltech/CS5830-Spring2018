from fernet import Fernet
import pytest
import base64
import os

class TestFernet:
    def test_Functionality(self):
        key = Fernet.generate_key()
        fernet = Fernet(key)

        # decrypt(encrypt(msg)) == msg
        for i in xrange(20):
            msg = os.urandom(6)
            assert fernet.decrypt(fernet.encrypt(msg)) == msg

if __name__ == "__main__":
    a = TestFernet()
    a.test_Functionality()

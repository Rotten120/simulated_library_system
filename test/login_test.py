from test import *
from pages.login import Login

class LoginTest(unittest.TestCase):
    def test_valid_login(self):
        inp = ("Zedric", "secret")
        output = "Successfully logged as " + inp[0]
        self.assertEqual(Login.logic(inp), (output, 1))

    def test_invalid_username(self):
        inp = ("Zeds", "secret")
        output = "Username does not exist"
        self.assertEqual(Login.logic(inp), (output, 0))
        
    def test_invalid_password(self):
        inp = ("Zedric", "hehe")
        output = "Password is incorrect"
        self.assertEqual(Login.logic(inp), (output, 0))

if __name__ == "__main__":
    main.libsys_init()
    unittest.main()

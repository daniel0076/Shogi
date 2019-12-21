from django.test import TestCase

from Shogi_app.UserInfoManager import UserInfoManagerSingleton
from Shogi_app.models import UserAccount, UserSettings

class TestUserInfoManager(TestCase):
    def setUp(self):
        record = UserAccount(username = 'test', password = 'testtest')
        record.save()
        pass

    def test_login_suc(self):
        ret = UserInfoManagerSingleton.login({"username": 'test', "password": 'testtest'})
        self.assertEqual(ret, {"type": "[Auth] Login Response", "content": {"status": True, "userId": 1}})

    def test_login_fail(self):
        ret = UserInfoManagerSingleton.login({"username": 'test', "password": 'testtesttest'})
        self.assertEqual(ret, {"type": "[Auth] Login Response", "content": {"status": False, "userId": -1}})

    def test_reg_suc(self):
        ret = UserInfoManagerSingleton.register({"username": 'test2', "password": 'testtest'})
        self.assertEqual(ret, {"type": "[Auth] Register Response", "content": {"status": True, "errorMsg": ""}})

    def test_reg_fail(self):
        ret = UserInfoManagerSingleton.register({"username": 'test', "password": 'testtest'})
        self.assertEqual(ret, {"type": "[Auth] Register Response", "content": {"status": False, "errorMsg": "Username already be used"}})

    def test_online(self):
        UserInfoManagerSingleton.update_online(1, True) 
        self.assertEqual(UserInfoManagerSingleton.is_online(1), True)
        UserInfoManagerSingleton.update_online(1, False) 
        self.assertEqual(UserInfoManagerSingleton.is_online(1), False)

    def test_ingame(self):
        UserInfoManagerSingleton.update_ingame(1, True) 
        self.assertEqual(UserInfoManagerSingleton.is_ingame(1), True)
        UserInfoManagerSingleton.update_ingame(1, False) 
        self.assertEqual(UserInfoManagerSingleton.is_ingame(1), False)

    def test_settimg(self):
        self.assertEqual(UserInfoManagerSingleton.get_settings(1), {'content': {}, 'type': '[Settings]'})
        UserInfoManagerSingleton.update_settings(1, {"test": 9876})
        self.assertEqual(UserInfoManagerSingleton.get_settings(1), {'type': '[Settings]', 'content': {"test": 9876}})

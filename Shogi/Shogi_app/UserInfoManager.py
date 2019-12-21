import json
import threading
import time

from Shogi_app.models import UserAccount, UserSettings
from django.db.models import Q
from django.core import serializers

MAXUSER = 100

class UserInfoManager:
    def __init__(self):
        self.online_status = [False] * MAXUSER
        self.ingame_status = [False] * MAXUSER

    def login(self, data):
        r = UserAccount.objects.filter(username = data['username'], password = data['password'])
        if len(r) >= 1:
            user_id = json.loads(serializers.serialize('json', r))[0]['pk']
            if not self.is_online(user_id):
                self.update_online(user_id, True)
                return {"type": "[Auth] Login Response",
                        "content": {"status": True, "userId": user_id}}

        return {"type": "[Auth] Login Response",
                "content": {"status": False, "userId": -1}}

    def register(self, data):
        r = UserAccount.objects.filter(username = data['username'])
        if len(r) >= 1:
            return {"type": "[Auth] Register Response",
                    "content": {"status": False,    
                                "errorMsg": "Username already be used"}}
        record = UserAccount(username = data['username'], password = data['password'])
        record.save()
        return {"type": "[Auth] Register Response",
                "content": {"status": True, "errorMsg": ""}}

    def is_online(self, i):
        if i > MAXUSER or i < 0:
            return False
        else:
            return self.online_status[i]

    def update_online(self, i, status):
        if i > MAXUSER or i < 0:
            return
        else:
            self.online_status[i] = status

    def is_ingame(self, i):
        if i > MAXUSER or i < 0:
            return False
        else:
            return self.ingame_status[i]

    def update_ingame(self, i, status):
        if i > MAXUSER or i < 0:
            return
        else:
            self.ingame_status[i] = status

    def load_settings(self, user_id):
        r = UserSettings.objects.filter(userId = user_id)
        if (len(r) >= 1):
            return json.loads(r.values()[0]['settings'])
        else:
            return {}

    def save_settings(self, user_id, data):
        r = UserSettings.objects.filter(userId = user_id)
        if(len(r) <= 1):
            record = UserSettings(userId = user_id, settings = json.dumps(data))
            record.save()
        else:
            UserSettings.objects.filter(userId = user_id).update(settings = json.dumps(data))

    def get_settings(self, user_id):
        return {"type": "[Settings]", "content": self.load_settings(user_id)}

    def update_settings(self, user_id, data):
        data_pre = self.load_settings(user_id)
        data_pre.update(data)
        self.save_settings(user_id, data_pre)
        
UserInfoManagerSingleton = UserInfoManager()

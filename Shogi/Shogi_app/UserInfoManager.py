import json
import threading
import time

from Shogi_app.models import UserAccount
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
                return {"status": True, "userId": user_id}
                self.update_online(user_id, True)

        return {"status": False, "userId": -1}

    def register(self, data):
        r = UserAccount.objects.filter(username = data['username'])
        if len(r) >= 1:
            return {"status": False, "errorMsg": "username already be used"}
        record = UserAccount(username = data['username'], password = data['password'])
        record.save()
        return {"status": True, "errorMsg": ""}

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

    # TODO: setting

UserInfoManagerSingleton = UserInfoManager()

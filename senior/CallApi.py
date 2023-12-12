import json
import requests
from operator import itemgetter

def GuardianLogin(id, password):
    # return True, "850263"

    url = "http://141.164.44.219:3000/auth/guardian"
    data = {
        "id": id,
        "password": password
    }

    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        # print(response_data)

        if response.status_code == 201:
            if response_data["isLogin"]:
                return True, response_data
            else:
                return False, "아이디/비밀번호를 확인해주세요"
        else:
            return False, "서버 연결 오류"

    except requests.Timeout:
        return False, "요청 시간 초과"
    except requests.RequestException as e:
        return False, "아이디/비밀번호를 확인해주세요"

def SeniorLogin(id):
    url = "http://141.164.44.219:3000/auth/senior"
    data = {
        "id": id
    }

    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        # print(response_data)

        if response.status_code == 201:
            if response_data["isLogin"]:
                return True, response_data
            else:
                return False, "아이디를 확인해주세요"
        else:
            return False, "서버 연결 오류"

    except requests.Timeout:
        return False, "요청 시간 초과"
    except requests.RequestException as e:
        return False, "아이디를 확인해주세요"

def GetTask(id):
    url = "http://141.164.44.219:3000/task/" + str(id)

    try:
        response = requests.get(url)

        if response.status_code == 201:
            response_data = response.json()
            response_data = sorted(response_data, key=itemgetter("datetime"))
            # print(response_data)

            return response_data
        else:
            return False

    except requests.Timeout:
        return False
    except requests.RequestException as e:
        return False

def UpdateTask(taskInfo):
    url = "http://141.164.44.219:3000/task"
    # print(taskInfo)

    try:
        response = requests.put(url, json=taskInfo)

        if response.status_code == 201:
            print("task update success")

    except requests.Timeout:
        print(requests.RequestException)
        return False
    except requests.RequestException as e:
        print(requests.RequestException)
        return False

def AddTask(taskInfo):
    url = "http://141.164.44.219:3000/task"
    # print(taskInfo)

    try:
        response = requests.post(url, json=taskInfo)

        if response.status_code == 201:
            print("task add success")

    except requests.Timeout:
        print(requests.RequestException)
        return False
    except requests.RequestException as e:
        print(requests.RequestException)
        return False

def DeleteTask(taskInfo):
    url = "http://141.164.44.219:3000/task"
    # print(taskInfo)

    try:
        response = requests.delete(url, json=taskInfo)

        if response.status_code == 201:
            print("task delete success")

    except requests.Timeout:
        print(requests.RequestException)
        return False
    except requests.RequestException as e:
        print(requests.RequestException)
        return False

def GetQuiz(id):
    url = "http://141.164.44.219:3000/quiz/" + str(id)

    try:
        response = requests.get(url)

        if response.status_code == 201:
            response_data = response.json()
            # response_data = sorted(response_data, key=itemgetter("datetime"))
            # print(response_data)

            return response_data
        else:
            return False

    except requests.Timeout:
        return False
    except requests.RequestException as e:
        return False

def SendDm(dmInfo):
    url = "http://141.164.44.219:3000/notice/send"
    # print(dmInfo)

    try:
        response = requests.post(url, json=dmInfo)

        if response.status_code == 201:
            print("msg send success")

    except requests.Timeout:
        print(requests.RequestException)
        return False
    except requests.RequestException as e:
        print(requests.RequestException)
        return False

def GetDm(id):
    url = "http://141.164.44.219:3000/notice/receive/" + str(id)

    try:
        response = requests.get(url)
        response_data = response.json()

        if response.status_code == 201:
            if response_data["isSuccess"]:
                return response_data
            else:
                return False
        else:
            return False

    except requests.Timeout:
        return False
    except requests.RequestException as e:
        return False


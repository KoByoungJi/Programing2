import json
import requests

def GuardianLogin(id, password):
    url = "http://141.164.44.219:3000/auth/guardian"
    data = {
        "id": id,
        "password": password
    }

    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        print(response_data)

        if response.status_code == 201:
            return True, response_data["seniorName"]
        else:
            return False, None

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
        print(response_data)

        if response.status_code == 201:
            return True, response_data["seniorName"]
        else:
            return False, None

    except requests.Timeout:
        return False, "요청 시간 초과"
    except requests.RequestException as e:
        return False, "아이디를 확인해주세요"

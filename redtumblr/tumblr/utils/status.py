import requests


def get_is_blocked(url):
    response = requests.get(url)

    if "warning.or.kr" in response.text:
        return True
    return False


def get_is_deleted(url):
    response = requests.get(url)

    if response.status_code == 404:
        return True
    return False

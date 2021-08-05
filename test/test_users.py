import requests

TEST_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Skiing and playing tennis",
    "active": 1
}
URL = "http://127.0.0.1:5000/users"


def test_user_creation():
    out = requests.post(URL, json=TEST_USER)
    if out.status_code == 201:
        print(out.json())
    else:
        print("Something is WRONG :(")


def test_user_deactivate():
    out = requests.delete("%s/2" % URL)
    if out.status_code == 200:
        print(out.json())
    else:
        print("Something is WRONG while trying to DEACTIVATE")


if __name__ == "__main__":
    test_user_creation()
    test_user_deactivate()

# only for testing

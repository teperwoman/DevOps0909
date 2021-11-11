import requests


def test_get(url_to_test):
    response = requests.get(f"http://{url_to_test}/whatismyname")
    actual = response.text
    expected = "mazda, citroen, chevrolet"
    assert expected == actual


def test_post(url_to_test):
    response = requests.post(f"http://{url_to_test}/whatismyname")
    actual = response.text
    expected = "saved new car"
    assert expected == actual



test_get("localhost:5001")
test_post("localhost:5001")


test_get("localhost:5001")
test_post("localhost:5001")
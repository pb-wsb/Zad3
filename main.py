import requests


BASE_URL = "https://swapi.dev/api/"

ppl_list = [1, 2, 3000]

for p in ppl_list:
    resp = requests.get(f"{BASE_URL}people/{p}/")
    if resp.status_code == 200:
        data = resp.json()
        print(data.keys())
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

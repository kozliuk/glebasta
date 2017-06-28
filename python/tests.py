import json
import urllib3

HOST = "http://qainterview.cogniance.com"
candidate_id = None


def test_add_new_candidate_without_json_header_using_urllib3():
    http = urllib3.PoolManager()
    data = {
        "name": "Glebasta_without_header",
        "position": "Intern"
    }
    data = json.dumps(data).encode()
    request = http.request("POST", "%s/candidates" % HOST, body=data)
    assert request.status == 201, "Not returns 201"


def test_add_new_candidate_with_json_header_using_urllib3():
    http = urllib3.PoolManager()
    data = {
        "name": "Gleb",
        "position": "Intern"
    }
    data = json.dumps(data).encode()
    headers = {
        "Content-Type": "application/json"
    }
    request = http.request("POST", "%s/candidates" % HOST, body=data, headers=headers)
    assert request.status == 201, "Not returns 201(Candidate not added)"


def test_successful_adding_candidate_using_urllib3():
    global candidate_id
    found = False
    http = urllib3.PoolManager()
    request = http.request("GET", "%s/candidates" % HOST)
    data = json.loads(request.data.decode())
    for candidate in data["candidates"]:
        if candidate["name"] == "Gleb" and candidate["position"] == "Intern":
            found = True
            candidate_id = candidate["id"]
    assert found, "Cant find candidate"


def test_get_list_all_candidates_using_urllib3():
    http = urllib3.PoolManager()
    request = http.request("GET", "%s/candidates" % HOST)
    assert request.status == 200, "Not returns 200"
    try:
        print(json.loads(request.data.decode()))
    except ValueError:
        assert False, "It's not the json"
    assert json.loads(request.data.decode()) != {}, "Empty json data"


def test_delete_candidate_using_urllib3():
    global candidate_id
    http = urllib3.PoolManager()
    request = http.request("DELETE", "%s/candidates/%s" % (HOST, candidate_id))
    assert request.status == 200, "Cant delete candidate"


def test_successful_delete_candidate_using_urllib3():
    global candidate_id
    found = False
    http = urllib3.PoolManager()
    request = http.request("GET", "%s/candidates" % HOST)
    data = json.loads(request.data.decode())
    for candidate in data["candidates"]:
        if candidate["id"] == candidate_id:
            found = True
    assert not found, "Candidate not deleted!"


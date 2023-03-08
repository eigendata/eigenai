import json
from typing import Any, Dict

import urllib3


def post(
    url: str = "http://localhost:8080/",
    headers: Dict[str, str] = {"Content-Type": "application/json"},
    body: Dict[str, Any] = {},
    data: Dict[str, Any] = {},
):
    """"""
    encoded_body = json.dumps(body)
    http = urllib3.PoolManager()
    # {'Content-Type': 'application/json'}
    r = http.request("POST", url, headers=headers, body=encoded_body, data=data)

    return r.read()


def get(url: str = "http://localhost:8080/", headers: Dict[str, str] = {"Content-Type": "application/json"}):
    http = urllib3.PoolManager()
    r = http.request("GET", url, headers=headers)
    return r.read()

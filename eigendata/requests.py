import json
from typing import Any, Dict
from urllib import request


def post(
    url: str = "http://localhost:8080/",
    headers: Dict[str, str] = {"Content-Type": "application/json"},
    body: Dict[str, Any] = {},
    data: Dict[str, Any] = {},
):
    """"""
    data = json.dumps(body)

    # Convert to String
    data = str(data)

    # Convert string to byte
    data = data.encode("utf-8")

    # Post Method is invoked if data != None
    req = request.Request(url, data=data, headers=headers, method="POST")

    # Response
    resp = request.urlopen(req)

    return resp


def get(url: str = "http://localhost:8080/", headers: Dict[str, str] = {"Content-Type": "application/json"}):
    # Post Method is invoked if data != None
    req = request.Request(url, headers=headers, method="GET")

    # Response
    resp = request.urlopen(req)
    return resp

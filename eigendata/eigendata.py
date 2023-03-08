from typing import Optional

from eigendata.exceptions import raise_not_implemeneted
from eigendata.requests import post


class Eigendata:
    def __init__(self, api_token: str, api_url: Optional[str] = "b.eigendata.ai") -> None:
        self.token = api_token
        self.api_url = api_url

    def authenticate(self, username: str, password: str):
        auth_url = f"{self.api_url}/token"
        form_data = {"username": username, "password": password}
        res = post(auth_url, data=form_data)
        self.token = res.json()["access_token"]

    def generate_rules(self, data):
        gen_rules_url = f"{self.api_url}/generate_rules"
        headers = {"Content-Type": "application/json", "Authentication": f"Bearer {self.token}"}
        body = {"data": data}
        post(gen_rules_url, headers=headers, body=body)

    def predict(self, *args, **kwargs):
        raise_not_implemeneted()

    def upload_rule(self, *args, **kwargs):
        raise_not_implemeneted()

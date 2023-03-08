from eigendata.exceptions import raise_not_implemeneted


class Eigendata:
    def __init__(self, api_token: str) -> None:
        self.token = api_token

    def authenticate(self, *args, **kwargs):
        raise_not_implemeneted()

    def generate_rules(self, *args, **kwargs):
        raise_not_implemeneted()

    def predict(self, *args, **kwargs):
        raise_not_implemeneted()

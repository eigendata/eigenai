import pytest

from eigenai import RulesEngine


def test_train():
    engine = RulesEngine(api_token="garbage")
    with pytest.raises(NotImplementedError):
        engine.upload_rule()

import pytest

from eigendata import RulesEngine


def test_train():
    engine = RulesEngine(api_token="garbage")
    with pytest.raises(NotImplementedError):
        engine.list_models()

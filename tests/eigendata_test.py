import pytest

from eigendata import Eigendata


def test_train():
    model = Eigendata(api_token="garbage")
    with pytest.raises(NotImplementedError):
        model.generate_rules()

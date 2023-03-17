import os
from typing import Any, List, Optional

import numpy as np
import pandas as pd
from requests import post

from eigendata.exceptions import raise_missing_argument, raise_not_implemented
from eigendata.schemas import (
    Data,
    Prediction,
    PredictRequest,
    RuleEvalRequest,
    Rules,
    decode_data,
    encode_data,
)


class RulesEngine:
    def __init__(self, api_token: str, api_url: Optional[str] = "b.eigendata.ai") -> None:
        self.token = os.getenv("EIGEN_API_TOKEN", api_token)
        self.api_url = api_url
        self.dataset: pd.DataFrame = None
        self.data: Data = None
        self.model_id: int = None

    def _load_data(self, path: Optional[str], data: Optional[pd.DataFrame]):
        if data is not None:
            self.dataset = data
        elif path is not None:
            self.dataset = pd.read_csv(path)
        else:
            raise_missing_argument()

    def train(
        self,
        name: str,
        data_path: Optional[str],
        data: Optional[pd.DataFrame],
        target: str,
        features: Optional[List[str]],
        split: Optional[float],
        balance: Optional[float],
        complexity: Optional[int],
    ) -> int:
        """
        Returns the trained model id. Sets this model as default for the RulesEngine class.

        Parameters
        ----------
        name : str
            Name identifier for the model..
        data_path : str
            Path to dataset (CSV). Required unless `data` argument is provided.
        data : pd.DataFrame, Optional
            pandas DataFrame object containing the dataset.
        target : str
            Name of the Target column.
        split : float, Optional
            Which percentage of the dataset to be used for testing. > 0 and < 1.
        balance : float, Optional
            Value between 0 and 1 that balances the dataset classes during training sampling.
        complexity : int, Optional
            the higher this value the more complex the rules we can generate. Caps at 32.


        Returns
        -------
        model_id : int
            Trained model id for future use. This gets set as default use within the class instance.
        """
        train_url = f"{self.api_url}/train"
        headers = {"Content-Type": "application/json", "Authentication": f"Bearer {self.token}"}
        self._load_data(data_path, data)

        data = Data(
            name=name,
            dataset=encode_data(self.dataset),
            target=target,
            features=features,
            balance=balance,
            split=split,
            max_depth=complexity,
        )

        self.data = data

        response = post(train_url, headers=headers, data=data)
        return response.json()["model_id"]

    def authenticate(self, username: str, password: str):
        auth_url = f"{self.api_url}/token"
        form_data = {"username": username, "password": password}
        res = post(auth_url, data=form_data)
        self.token = res.json()["access_token"]

    def get_rules(self, model_id: Optional[int]) -> Rules:
        gen_rules_url = f"{self.api_url}/rules/gen"
        headers = {"Content-Type": "application/json", "Authentication": f"Bearer {self.token}"}
        data = self.data
        data["model_id"] = model_id or self.model_id
        res = post(gen_rules_url, headers=headers, data=self.data)
        res = res.json()
        rules = Rules(rule_set=decode_data(res["rule_set"]), importance=decode_data(res["importance"]))
        return rules

    def list_models(self) -> Any:
        raise_not_implemented()
        # list_models = f"{self.api_url}/models"
        # headers = {"Content-Type": "application/json", "Authentication": f"Bearer {self.token}"}
        # res = get(list_models, headers=headers)
        # models = res.json()
        # print(models)
        # return models

    def predict(self, datapoint: np.array, model_id: Optional[int]) -> Prediction:
        predict_url = f"{self.api_url}/predict"
        req = PredictRequest(datapoint=encode_data(datapoint), model_id=model_id or self.model_id)
        headers = {"Content-Type": "application/json", "Authentication": f"Bearer {self.token}"}
        res = post(predict_url, headers=headers, data=req)
        prediction = Prediction(datapoint=datapoint, result=res.json()["result"])
        return prediction

    def eval_rule(self, datapoint: pd.DataFrame, raw_rule: Optional[str], rule_id: Optional[int]) -> Prediction:
        eval_url = f"{self.api_url}/rules/eval"
        req = RuleEvalRequest(datapoint=encode_data(datapoint), raw_rule=raw_rule, rule_id=rule_id)
        headers = {"Content-Type": "application/json", "Authentication": f"Bearer {self.token}"}
        res = post(eval_url, headers=headers, data=req)
        prediction = Prediction(datapoint=datapoint, result=res.json()["result"])
        return prediction

    def upload_rule(self, *args, **kwargs):
        raise_not_implemented()


# rules.rules # me da el dataframe con lass reglas y metricas
# rules.importance # lista de tuplas ('feaure', score), (featr...)

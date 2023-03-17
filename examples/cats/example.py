import os

import numpy as np

from eigendata import Prediction, Rules, RulesEngine

engine = RulesEngine(api_token="<API_TOKEN_HERE>", api_url="https://octopus-app-qgvx4.ondigitalocean.app")

data_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
model_id = engine.train(
    name="example_model",
    data_path=data_path,
    target="target",
    features=["feature_01", "feature_02", "feature_03", "feature_05", "feature_06", "feature_11"],
)
print(model_id)

rules: Rules = engine.get_rules()
print(rules.rule_set)
print("feature importance:\n", rules.importance)

cat_datapoint = [
    0,
    0,
    -2,
    1,
    0,
    0,
    107,
    1.151481805088348,
    0.9049742849954245,
    -1.8388540737938648,
    1.363566175353061,
    1.5422151378158702,
    0.9459542014288947,
    -0.5832193364414454,
    -0.5757993264106427,
    -0.27076728248422527,
    -1.7414841581528044,
    -0.5661930322768176,
    -0.8865517154684772,
    2.087181550139055,
]
datapoint = np.array([cat_datapoint], dtype=np.float32)

prediction: Prediction = engine.predict(datapoint=datapoint)

import os

import pandas as pd

from eigenrules import Prediction, Rules, RulesEngine

# set the api token as an ENV var under EIGEN_API_TOKEN or pass it as an arg;
# alternativelly call engine.authenticate(username, password)
engine = RulesEngine(api_token="<your api token>")

data_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
model_id = engine.train(
    name="example_cat_model",
    data_path=data_path,
    target="target",
    features=["feature_01", "feature_02", "feature_03", "feature_05", "feature_06", "feature_11"],
    control_class="cat_1",
)
print("model ID: ", model_id, "\n\n")

models = engine.list_models()

print("Model List\n", models, "\n\n")

rules: Rules = engine.get_rules()
print("rules set: \n", rules.rule_set, "\n\n")
print("feature importance: \n", rules.importance, "\n\n")

cat_data_columns = [
    "feature_01",
    "feature_02",
    "feature_03",
    "feature_04",
    "feature_05",
    "feature_06",
    "feature_07",
    "feature_08",
    "feature_09",
    "feature_10",
    "feature_11",
    "feature_12",
    "feature_13",
    "feature_14",
    "feature_15",
    "feature_16",
    "feature_17",
    "feature_18",
    "feature_19",
    "feature_20",
]

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
datapoint = pd.DataFrame(cat_datapoint, columns=cat_data_columns)

prediction: Prediction = engine.predict(datapoint=datapoint)

print("prediction result: ", prediction.result)
print("prediction confidence: ", prediction.confidence)

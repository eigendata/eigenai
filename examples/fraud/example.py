import os

import pandas as pd

from eigendata import Prediction, Rules, RulesEngine

# set the api token as an ENV var under EIGEN_API_TOKEN or pass it as an arg;
# alternativelly call engine.authenticate(username, password)
engine = RulesEngine(api_token="<your api token>")

data_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
model_id = engine.train(
    name="example_fraud_model",
    data_path=data_path,
    target="is_fraud",
    features=["amount", "amount_ratio", "orders_qty", "order_type", "product_risk", "seconds_from_order"],
    control_class=0,
)
print("model ID: ", model_id, "\n\n")

models = engine.list_models()

print("Model List\n", models, "\n\n")

rules: Rules = engine.get_rules()
print("rules set: \n", rules.rule_set, "\n\n")
print("feature importance: \n", rules.importance, "\n\n")

# in a dict each key is a column with a list of values under it
user_data = {
    "amount": [886],
    "amount_ratio": [0.635851365592393],
    "seconds_from_login": [1614],
    "user_level": ["premium"],
    "orders_qty": [15],
    "order_type": ["restaurant"],
    "user_age": [46],
    "transaction_type": ["debit"],
    "product_risk": [0.6276506990427705],
    "seconds_from_order": [393],
}
datapoint = pd.DataFrame.from_dict(user_data)

prediction: Prediction = engine.predict(datapoint=datapoint)

print("prediction result: ", prediction.result)
print("prediction probabilities: ", prediction.probabilities)

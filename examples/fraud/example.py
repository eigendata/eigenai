import os

import numpy as np

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

user_datapoint = [886, 0.635851365592393, 1614, "premium", 15, "restaurant", 46, "debit", 0.6276506990427705, 393]
datapoint = np.array([user_datapoint], dtype=np.float32)

prediction: Prediction = engine.predict(datapoint=datapoint)

print("prediction result: ", prediction.result)

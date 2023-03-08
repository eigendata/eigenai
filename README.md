# eigendata
Powered by [eigendata.ai](https://eigendata.ai)

# installation

`pip install eigendata`

or

`poetry add eigendata`

# usage

```python
from eigendata import Eigendata

engine = Eigendata("<API Token>")


DATASET_PATH = "maybe_an_S3_addr_or_csv_filepath"
features = ["columns", "in", "my", "dataset", "I", "want", "to", "use"]
target = "target_col"

rules = engine.generate_rules(name="fraud_detection", data=DATASET_PATH, features=features, target=target)

print("top rule precision: ", rules[0].precision)

datapoint = {"a": 8, "b": "Max Müstermann"} # try to shape the datapoint to have same columns of the rest of the dataset
# run a prediction with highest precision rule by default
prediction = engine.predict(name="fraud_detection", data=datapoint)

print("is it fraud?")
print(f"{"Yes" if prediction["fraud"] == True else "No"}")

# run it with a rule you already had
my_old_rule = "I already have a rule in my system, can I use it?"
prediction = engine.predict(name="fraud_detection", data=datapoint, raw_rule=my_old_rule)

# store it for long term use
rule_id = engine.load_rule(my_old_rule)
prediction = engine.predict(name="fraud_detection", data=datapoint, rule_id=rule_id)
```

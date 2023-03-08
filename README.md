# eigendata
Powered by [eigendata.ai](https://eigendata.ai)

# installation

`pip install eigendata`

or

`poetry add eigendata`

# usage

```python
from eigendata import Eigendata

model = Eigendata("<API Token>")


DATASET_PATH = "maybe_an_S3_addr_or_csv_filepath"
features = ["columns", "in", "my", "dataset", "I", "want", "to", "use"]
target = "target_col"

model_precision = model.train(name="fraud_detection", data=DATASET_PATH, features=features, target=target)

print("trained model precision: ", model_precision)

datapoint = {"a": 8, "b": "Max Müstermann"} # try to shape the datapoint to have same columns of the rest of the dataset

prediction = model.predict(name="fraud_detection", data=datapoint)

print("is it fraud?")
print(f"{"Yes" if prediction["fraud"] == True else "No"}")
```

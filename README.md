# eigendata
Our public client to send requests to eigendata AI

# installation

`pip install eigendata`

or

`poetry add eigendata`

# usage

```python
import eigendata

eigendata.authenticate()

DATASET_PATH = "maybe_an_S3_addr_or_csv_filepath"
features = ["columns", "in", "my", "dataset", "I", "want", "to", "try"]
targets ["what", "do", "I", "want", "to", "predit"]

model_precision = eigendata.train(name="fraud_detection", data=DATASET_PATH, features=features, targets=targets)

print("trained model precision: ", model_precision)

datapoint = {"a": 8, "b": "Max Müstermann"} # try to shape the datapoint to have same columns of the rest of the dataset

prediction = eigendata.predit(model="fraud", data=datapoint)

print("is it fraud?")
print(f"{"Yes" if prediction["fraud"] == True else "No"}")
```

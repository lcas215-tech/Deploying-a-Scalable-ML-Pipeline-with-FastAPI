
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from ml.data import process_data
from ml.model import compute_model_metrics

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_preprocessing():
    """
    # tests preprocessing steps from function process_data
    """
    # Your code here
    data={"age":[30,35],
          "workclass":["state",'private'],
          "salary":["<=50K",">50K"]
          }
    df = pd.DataFrame(data)
    X,y,encoder,lb= process_data(
        df,categorical_features=["workclass"],
        label="salary",
        training=True
    )
    assert X.shape[0]==2
    assert len(y) == 2
    assert encoder is not None
    assert lb is not None




# TODO: implement the second test. Change the function name and input as needed
def test_mlmodel():
    """
    # verifies Random Forest as ML Model
    """

    X = np.array([[0,1],[1,1],[0,1],[1,0]])
    y = np.array([0,0,1,1])

    model = train_model(X,y)

    assert isinstance(model,RandomForestClassifier)




# TODO: implement the third test. Change the function name and input as needed
def test_value():
    """
    # compute model metrics returns expected value
    """
    p,r,f = compute_model_metrics([1,0,1],[0,0,1])
    assert round(p,2)==1.00




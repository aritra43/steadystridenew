import numpy as np
import pandas as pd

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.calibration import CalibratedClassifierCV
from sklearn.utils import resample


import numpy as np
import pandas as pd

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the saved model and scaler
loaded_model = pickle.load(open('static/models/parkinsons_model.pkl', 'rb'))
loaded_scaler = pickle.load(open('static/models/scaler.pkl', 'rb'))

# Function to take user input and make a prediction
def predict_parkinsons(kwargs):
    print("Enter the following details:")
    # tremor = int(input("Tremor (1 for Yes, 0 for No): "))
    # slowness = int(input("Slowness (1 for Yes, 0 for No): "))
    # rigidity = int(input("Rigidity (1 for Yes, 0 for No): "))
    # loss_of_smell = int(input("Loss of Smell (1 for Yes, 0 for No): "))
    # family_history = int(input("Family History (1 for Yes, 0 for No): "))
    # num_ancestors = int(input("Number of Ancestors with Parkinson's: "))
    # male_ancestors = int(input("Male Ancestors with Parkinson's (1 for Yes, 0 for No): "))
    # past_head_injury = int(input("Past Severe Head Injury (1 for Yes, 0 for No): "))

    # Combine inputs into a single array for prediction
    # input_features = np.array([[tremor, slowness, rigidity, loss_of_smell, family_history, num_ancestors, male_ancestors, past_head_injury]])
    input_features = np.array([[kwargs[key] for key in ["tremor", "slowness", "rigidity", "loss_of_smell", "family_history", "num_ancestors", "male_ancestors", "past_head_injury"]]])

    # Scale inputs using the saved scaler
    scaled_input = loaded_scaler.transform(input_features)

    # Predict using the model
    prediction = loaded_model.predict(scaled_input)
    probability = loaded_model.predict_proba(scaled_input)
    
    print(f"{prediction=} {probability=}")
    
    resultant_dict = {}
    
    if prediction[0] == 1:
        print(f"The model predicts that the person has Parkinson's disease with a probability of {probability[0][1]:.2f}.")
        resultant_dict["has_parkinson"] = 1
        resultant_dict["confidence"] = float(round(probability[0][1], 3))
    else:
        resultant_dict["has_parkinson"] = 0
        resultant_dict["confidence"] = float(round(probability[0][0], 3))
        print(f"The model predicts that the person does not have Parkinson's disease with a probability of {probability[0][0]:.2f}.")
    
    # return True if prediction[0] == 1 else False
    return resultant_dict


# Run the prediction function
# predict_parkinsons()

if __name__ == "__main__":
    kwargs = {
        "tremor" : 1,
        "slowness" : 1,
        "rigidity" : 1,
        "loss_of_smell" : 1,
        "family_history" : 1,
        "num_ancestors" : 1,
        "male_ancestors" : 1,
        "past_head_injury" : 1,
    }
    
    # kwargs = {
    #     "tremor" : 0,
    #     "slowness" : 0,
    #     "rigidity" : 0,
    #     "loss_of_smell" : 0,
    #     "family_history" : 0,
    #     "num_ancestors" : 0,
    #     "male_ancestors" : 0,
    #     "past_head_injury" : 0,
    # }

    print(predict_parkinsons(kwargs))
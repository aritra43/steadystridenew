import os, sys

root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
print(f"{root_folder=}")
sys.path.insert(0, root_folder)

import csv
import pandas as pd
from src.utils.constants import INPUT_PARAMETERS, PREDICTIONS_CSV

# Function to retrieve cached values from the CSV
# def predict_parkinsons(input_args):
#     with open(PREDICTIONS_CSV, mode="r") as file:
#         reader = csv.DictReader(file)
#         # Find the matching row
#         for row in reader:
#             if all(int(row[arg]) == input_args[arg] for arg in INPUT_PARAMETERS):
#                 return {
#                     "has_parkinson": int(row["has_parkinson"]),
#                     "confidence": float(row["confidence"])
#                 }
#     return None  # Return None if no match is found
# Load the CSV file into a pandas DataFrame
# df = pd.read_csv(PREDICTIONS_CSV)

# # Optimized function using pandas
# def predict_parkinsons(input_args):
#     """
#     Retrieve cached predictions using pandas for faster lookups.

#     :param input_args: A dictionary of input parameters.
#     :return: A dictionary with output parameters ("has_parkinson" and "confidence").
#     """

#     # Filter rows matching the input arguments
#     query = " & ".join([f"{key} == {value}" for key, value in input_args.items()])
#     match = df.query(query)

#     if not match.empty:
#         row = match.iloc[0]  # Take the first matching row
#         return {
#             "has_parkinson": int(row["has_parkinson"]),
#             "confidence": float(row["confidence"]),
#         }

#     raise ValueError("Input combination not found in cached predictions.")


import pandas as pd

# Preload the CSV into a dictionary for O(1) lookups
def preload_predictions(csv_path):
    df = pd.read_csv(csv_path)
    # Create a dictionary where the key is a tuple of input values
    predictions_dict = {
        tuple(row[INPUT_PARAMETERS]): {
            "has_parkinson": row["has_parkinson"],
            "confidence": row["confidence"],
        }
        for _, row in df.iterrows()
    }
    return predictions_dict

# Global variable to store preloaded predictions
predictions_cache = preload_predictions(PREDICTIONS_CSV)

def predict_parkinsons(input_args):
    """
    Retrieve cached predictions using a dictionary for O(1) lookups.

    :param input_args: A dictionary of input parameters.
    :return: A dictionary with output parameters ("has_parkinson" and "confidence").
    """
    key = tuple(input_args[param] for param in INPUT_PARAMETERS)
    if key in predictions_cache:
        return predictions_cache[key]
    else:
        raise ValueError("Input combination not found in cached predictions.")

# Example usage
result = predict_parkinsons({
    "tremor": 1,
    "slowness": 1,
    "rigidity": 1,
    "loss_of_smell": 1,
    "family_history": 1,
    "num_ancestors": 5,
    "male_ancestors": 2,
    "past_head_injury": 1,
})
print(result)


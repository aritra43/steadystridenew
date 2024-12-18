import os, sys

root_folder = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
print(f"{root_folder=}")
sys.path.insert(0, root_folder)

from src.utils.constants import INPUT_PARAMETERS, PREDICTIONS_CSV, OUTPUT_PARAMETERS
from src.infer_model import predict_parkinsons
import csv
from itertools import product

# Generate all possible combinations of inputs
# combinations = list(product([0, 1], repeat=len(INPUT_PARAMETERS)))

# Generate combinations for binary inputs and integer ranges
input_ranges = [
    [0, 1],  # tremor
    [0, 1],  # slowness
    [0, 1],  # rigidity
    [0, 1],  # loss_of_smell
    [0, 1],  # family_history
    range(0, 6),  # num_ancestors
    range(0, 6),  # male_ancestors
    [0, 1],  # past_head_injury
]
combinations = product(*input_ranges)

# Write to CSV
with open(PREDICTIONS_CSV, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(INPUT_PARAMETERS + OUTPUT_PARAMETERS)

    # Write each combination and prediction result
    for combo in combinations:
        kwargs = dict(zip(INPUT_PARAMETERS, combo))
        prediction = predict_parkinsons(kwargs)
        writer.writerow(list(combo) + [prediction[k] for k in OUTPUT_PARAMETERS])


"""
"tremor", "slowness", "rigidity", "loss_of_smell", "family_history", "num_ancestors", "male_ancestors", "past_head_injury"

I've got these 8 INPUT_PARAMETERS, which can take up the values 1 or 0, create all possible input combinations for the same.

I've got another function called predict_parkinsons(kwargs) which inputs a dictionary with keys as above and values as 0 and 1.

This function returns a dict -> 2 values in a dict "has_parkinson" : 1 or 0, and "confidence" = float,

Create a csv with headers "tremor", "slowness", "rigidity", "loss_of_smell", "family_history", "num_ancestors", "male_ancestors", "past_head_injury", "has_parkinson", "confidence"

Save it to a csv (using python's internal csv writer).

Once done, make a function return_cached_values_from_csv which replicates predict_parkinsons behaviour -> takes the input args and gives the "has_parkinson" : 1 or 0, and "confidence" = float, BUT NOW from the csv.
The requirement now has slightly changed : Range of following 2 integers has increased, please adjust for the same::

num_ancestors : 0-5,
male_ancestors : 0-5,

Constants are:

PREDICTIONS_CSV = "data/parkinsons_predictions.csv"
INPUT_PARAMETERS = ["tremor", "slowness", "rigidity", "loss_of_smell", "family_history", "num_ancestors", "male_ancestors", "past_head_injury"]
OUTPUT_PARAMETERS = ["has_parkinson", "confidence"]
"""
import requests

def make_request():
    # url = "https://2086-103-23-29-121.ngrok-free.app/predict"
    url = "https://parkinsonsih.onrender.com/predict/"

    headers = {
        "ngrok-skip-browser-warning": "true"  # Add this header with any value
    }

    payload = {
        "kwargs": {
            "tremor": 1,
            "slowness": 1,
            "rigidity": 1,
            "loss_of_smell": 1,
            "family_history": 1,
            "num_ancestors": 1,
            "male_ancestors": 1,
            "past_head_injury": 1,
        }
    }  # Example payload

    try:
        response = requests.post(url, json=payload, headers=headers)  # Include headers
        if response.status_code == 200:
            print("Response:", response.json())
        else:
            print("Error:", response.status_code, response.text)
    except requests.RequestException as e:
        print("Request failed:", e)

# Run the function
make_request()

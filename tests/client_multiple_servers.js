// const fetch = require('node-fetch'); // Uncomment if using Node.js without native fetch support

async function makeRequest(
    tremor,
    slowness,
    rigidity,
    loss_of_smell,
    family_history,
    num_ancestors,
    male_ancestors,
    past_head_injury
) {
    const urls = [
        "https://6174-103-23-29-122.ngrok-free.app/predict",
        "https://2086-103-23-29-121.ngrok-free.app/predict",
        "http://localhost:10000/predict/",
        "https://parkinsonsih.onrender.com/predict/",
        // Add more URLs here as needed
    ];

    const payload = {
        kwargs: {
            tremor: tremor,
            slowness: slowness,
            rigidity: rigidity,
            loss_of_smell: loss_of_smell,
            family_history: family_history,
            num_ancestors: num_ancestors,
            male_ancestors: male_ancestors,
            past_head_injury: past_head_injury,
        },
    };

    for (const url of urls) {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "ngrok-skip-browser-warning": "true", // Add this header with any value
                },
                body: JSON.stringify(payload),
            });

            if (response.ok) {
                const data = await response.json();
                console.log("Response from", url, ":", data);
                return data; // Return the response data if the request is successful
            } else {
                console.error("Error from", url, ":", response.status, await response.text());
            }
        } catch (error) {
            console.error("Fetch failed for", url, ":", error);
        }
    }

    console.error("All servers failed. Unable to complete the request.");
    return null; // Return null or handle the failure case as needed
}

// Sample call to the function
makeRequest(1, 1, 1, 1, 1, 1, 1, 1);


// {/* <script src="client.js"></script> */}
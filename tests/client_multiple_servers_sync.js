// const fetch = require("node-fetch"); // Use this in Node.js
const deasync = require("deasync");

function makeRequestSync(
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
        "http://localhost:10000/predict/",
        "https://parkinsonsih.onrender.com/predict/",
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

    let result = null;
    let done = false;

    for (const url of urls) {
        try {
            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "ngrok-skip-browser-warning": "true",
                },
                body: JSON.stringify(payload),
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(
                            `Error from ${url}: ${response.status} ${response.statusText}`
                        );
                    }
                    return response.json();
                })
                .then((data) => {
                    console.log("Response from", url, ":", data);
                    result = data;
                    done = true;
                })
                .catch((error) => {
                    console.error("Fetch failed for", url, ":", error);
                    done = true;
                });

            // Wait for the asynchronous code to finish
            while (!done) {
                deasync.sleep(100); // Polling interval
            }

            if (result) break; // Exit loop if a successful result is obtained
        } catch (error) {
            console.error("Error during request:", error);
        }
    }

    if (!result) {
        console.error("All servers failed. Unable to complete the request.");
    }
    return result; // Return result or null if all attempts fail
}

// Sample call to the function
const result = makeRequestSync(1, 1, 1, 1, 1, 1, 1, 1);
console.log("Final Result:", result);

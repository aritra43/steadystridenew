import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from src.infer_model import predict_parkinsons
from src.infer_model_fast import predict_parkinsons 

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to allow specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the request model
class PredictionRequest(BaseModel):
    kwargs: dict  # Accept keyword arguments as a dictionary

@app.post("/predict/")
async def predict(data: PredictionRequest):
    try:
        # Pass the keyword arguments to the prediction function
        result = predict_parkinsons(data.kwargs)
        return {"success": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")



if __name__ == "__main__":
    # PORT = 8095
    PORT = int(os.getenv("PORT", "10000"))
    uvicorn.run("main:app", port=PORT, host="0.0.0.0")
    # uvicorn main:app --host 0.0.0.0 --port $PORT

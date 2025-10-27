from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Define the input data model
class LeadData(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Load the model
with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

# Create FastAPI app
app = FastAPI()

@app.post("/predict")
def predict_lead_conversion(lead: LeadData):
    # Convert to dictionary for the model
    lead_dict = lead.dict()
    
    # Make prediction
    probability = pipeline.predict_proba([lead_dict])[0][1]
    
    # Convert numpy types to native Python types for JSON serialization
    probability_float = float(probability)
    convert_bool = bool(probability > 0.5)
    
    return {
        "probability": round(probability_float, 3),
        "convert": convert_bool
    }

@app.get("/")
def read_root():
    return {"message": "Lead Scoring API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}
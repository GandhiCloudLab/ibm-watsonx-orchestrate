from fastapi import FastAPI, HTTPException, Depends

import argparse
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

# ---------- Models ----------

# Request model
class RequestModel(BaseModel):
    source_city: str
    destination_city: str

class ResponseModel(BaseModel):
    msg: str
    city: str
    news: str

# ---------- App Setup ----------

app = FastAPI(
    title="News Alerts API",
    description="API to get news alerts for a route",
    version="1.0.0"
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

news_alerts_data = ["", "Heavy rains", "Political protest", "Religious festivals","Transport strikes"]

# Define routes and their possible intermediate cities
routes = {
    ("Chennai", "Bangalore"): ["Vellore", "Krishnagiri", "Hosur"],
    ("Mumbai", "Pune"): ["Lonavala", "Khandala"],
    ("Delhi", "Agra"): ["Faridabad", "Mathura"],
    ("Delhi", "Bangalore"): ["Nandid", "Nagpur", "Solapur"],
    ("Hyderabad", "Vizag"): ["Vijayawada", "Rajahmundry", "Eluru"],
    ("Kolkata", "Bhubaneswar"): ["Kharagpur", "Balasore", "Cuttack"]
}

def get_random_in_between_city(source, destination):
    # Find the matching route tuple in any order
    for (src, dest), cities in routes.items():
        if (src == source and dest == destination) or (src == destination and dest == source):
            return random.choice(cities)
    return None  # If route not found

# ---------- API Endpoint ----------

@app.get("/")
def home():
    return {"message": "Welcome to the  News Alerts API!"}

@app.get("/news", response_model=ResponseModel)
def get_news(request: RequestModel):
    """
    Given a route (source and destination),
    fetch related news updates that may affect travel.
    """

    # Mocked news list — replace this later with actual data
    route_city = get_random_in_between_city(request.source_city, request.destination_city)
    news_alert = random.choice(news_alerts_data)

    response = {
        "msg": f"Fetched news for route from {request.source_city} to {request.destination_city}",
        "city": route_city, 
        "news": news_alert
    }

    return response

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data/stock_market_data.json", "r") as file:
    data = json.load(file)

@app.get("/api/table")
async def get_data():
    return(data)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
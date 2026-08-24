import uvicorn
import traceback
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from pathlib import Path

from backend.main import run_trip_planner_agent

app = FastAPI(
        title="Trip Planner AI Agent",
        description="Travel Planner Multi-Agent App",
        version= "1.0.0"
    )

class TravelRequest(BaseModel):
    message: str
    thread_id: str | None

@app.get("/")
def home():
    return {
        'message': 'App is running properly',
        "status": 200
    }

@app.post('/travel')
def ask_query(input: TravelRequest):
    try:
        user_message= input.message.strip()
        # thread_id = input.thread_id.strip()

        if not user_message:
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        result = run_trip_planner_agent(user_query=user_message, thread_id=None)

        return JSONResponse(
            content={
                "success": True,
                "thread_id": result["thread_id"],
                "final_result": result["final_result"],
                "flight_result": result["flight_result"],
                "hotel_result": result["hotel_result"],
                "itineary_result": result["itineary_result"],
                "travellers": result["travellers"],
            }
        )

    except Exception as e:
        print("ERROR: ", e)
        traceback.print_exc()

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": str(e)
            }
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
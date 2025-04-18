# app.py

from fastapi import FastAPI
import api  # Import the FastAPI app from api.py

# Initialize FastAPI app (already defined in api.py)
app = api.app

if __name__ == "__main__":
    # This part is for running locally with Uvicorn if needed (though uvicorn will run it via `uvicorn app:app`)
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

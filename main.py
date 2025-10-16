from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import logging
import json
from datetime import datetime, timezone
from dotenv import load_dotenv
import os
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Custom JSON Response with pretty printing
class PrettyJSONResponse(JSONResponse):
    def render(self, content) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
            separators=(", ", ": "),
        ).encode("utf-8")

# Initialize FastAPI app
app = FastAPI(
    title="Backend Wizards - Stage 0",
    description="Dynamic Profile Endpoint with Cat Facts",
    version="1.0.0",
    default_response_class=PrettyJSONResponse  # Pretty JSON by default
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration from environment variables
USER_EMAIL = os.getenv("USER_EMAIL", "developer@example.com")
USER_NAME = os.getenv("USER_NAME", "Developer Name")
USER_STACK = os.getenv("USER_STACK", "Python/FastAPI")
CAT_FACTS_API_URL = "https://catfact.ninja/fact"
API_TIMEOUT = 10

async def fetch_cat_fact() -> str:
    """Fetch a random cat fact from the Cat Facts API."""
    try:
        async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
            logger.info(f"Fetching cat fact from {CAT_FACTS_API_URL}")
            response = await client.get(CAT_FACTS_API_URL)
            response.raise_for_status()
            
            data = response.json()
            cat_fact = data.get("fact", "")
            
            if not cat_fact:
                logger.warning("Empty cat fact received from API")
                return "Cats are amazing creatures!"
            
            logger.info("Successfully fetched cat fact")
            return cat_fact
            
    except httpx.TimeoutException:
        logger.error("Timeout while fetching cat fact")
        raise HTTPException(
            status_code=503,
            detail="Cat Facts API is currently unavailable (timeout)"
        )
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error while fetching cat fact: {e}")
        raise HTTPException(
            status_code=503,
            detail=f"Cat Facts API returned an error: {e.response.status_code}"
        )
    except Exception as e:
        logger.error(f"Unexpected error while fetching cat fact: {e}")
        raise HTTPException(
            status_code=503,
            detail="Unable to fetch cat fact at this time"
        )

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Backend Wizards Stage 0 API",
        "endpoints": {
            "/me": "Get developer profile with dynamic cat fact",
            "/health": "Health check endpoint"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/me")
async def get_profile() -> Dict[str, Any]:
    """Get developer profile with a dynamic cat fact."""
    try:
        cat_fact = await fetch_cat_fact()
        current_timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        
        response_data = {
            "status": "success",
            "user": {
                "email": USER_EMAIL,
                "name": USER_NAME,
                "stack": USER_STACK
            },
            "timestamp": current_timestamp,
            "fact": cat_fact
        }
        
        logger.info(f"Successfully generated profile response for {USER_EMAIL}")
        return response_data
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_profile: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred"
        )


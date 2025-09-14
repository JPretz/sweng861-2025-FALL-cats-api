# Cat Facts Bonus API

## Introduction
The Cat Facts Bonus API is a **FastAPI backend application** that fetches, stores, and manages cat facts.  
It demonstrates the use of:

- FastAPI for API endpoints
- SQLAlchemy for database management
- Pydantic for data validation
- API key-based authorization for secure operations
- Rate limiting and caching
- Swagger UI for interactive API testing

The backend allows users to fetch cat facts from an external API, store them in a local database, and perform CRUD operations on the stored facts.

-----------------------------------------------------------

## Project Structure
catfacts_bonus/
├─ main.py
├─ crud.py
├─ models.py
├─ schemas.py
├─ database.py
├─ requirements.txt
├─ README.md
├─ screenshots/
│ ├─ fetch_endpoint.png
│ ├─ swagger_docs.png
│ └─ demo_recording.mp4
└─ project_documentation/
├─ CatFacts_Project_Proposal.docx
└─ CatFacts_Design.pdf

-------------------------------------------------------------

## Project Description

This project:

- Fetches cat facts from [`catfact.ninja`](https://catfact.ninja/)  
- Stores cat facts in a local SQLite database via SQLAlchemy  
- Supports CRUD operations (Create, Read, Update, Delete)  
- Implements rate limiting to prevent abuse (5 requests per minute per IP)  
- Implements caching with FastAPI Cache (responses cached for 60 seconds)  
- Secures certain endpoints with API key authentication  

------------------------------------------------------------------------------

## Steps to Build the Backend

1. **Setup Project Environment**
   - Create a virtual environment and install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy httpx fastapi-cache2 slowapi
   
2. Database Setup:
  . Used SQLAlchemy with SQLite for simplicity.
  . Defined a CatFact model with id and fact columns.

3. Create Pydantic Schemas:
  . CatFactCreateSchema – for creating a fact
  . CatFactSchema – for responses (includes id)

4. Implement CRUD Functions
  . crud.py contains:
    catfact_exists
    create_catfact
    get_catfacts
    get_catfact
    update_catfact
    delete_catfact
   
5. Build API Endpoints:
  . / – Root endpoint with welcome message
  . /fetch/ – Fetch cat facts from external API, store unique facts, return IDs and facts
  . /catfacts/ – CRUD endpoints with API key authorization for create/update/delete

6. Add Security:
  . API key-based authorization using FastAPI's HTTPBearer scheme
  . Rate limiting using slowapi (5 requests/minute)
  . Caching with fastapi-cache2

7. Test API
Interactive testing using Swagger UI:
http://127.0.0.1:8000/docs

--------------------------------------------


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

How to Run it:
1. Activate your virtual environment:
   # Windows
       venv\Scripts\activate
   # macOS/Linux
       venv/bin/activate
2. Run the FastAPI server:
       uvicorn main:app --reload

3. Access the API:
   Swagger UI: http://127.0.0.1:8000/docs
   Root endpoint: http://127.0.0.1:8000/
   
   ----------------------------------------------
API Testing with Swagger:

1. Fetch Cat Facts /fetch/

   . Set count query parameter to fetch multiple facts.
   . Returns unique facts stored in the database along with their IDs.

2. CRUD Operations /catfacts/

   . API key required (mysecretkey123) for POST, PUT, DELETE.
   . GET endpoints do not require authentication.
   . Use Swagger UI for interactive testing.

   ---------------------------------------------
   ## Screenshots

![Authentication Test] https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/01_authentication_test.png
![POST Auth] https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/02_post_auth.png

![GET /fetch/ Auth](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/03_get_fetch_auth.png)
![GET /fetch/ Response](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/04_get_fetch_response.png)
![GET /catfacts/ IDs](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/05_get_catfacts_ids.png)
![GET /catfacts/{id}](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/06_get_catfact_id.png)
![GET invalid fact_id](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/07_get_catfact_invalid.png)
![GET /catfacts/ Auth](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/08_get_facts_auth.png)
![POST catfacts return ID](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/09_post_catfact_return.png)
![POST catfacts Test](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/10_post_catfact_test.png)
![PUT tested ID](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/11_put_tested_id.png)
![PUT Testing](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/12_put_testing.png)
![PUT with Auth](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/13_put_with_auth.png)
![DELETE Fact](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/14_delete_fact.png)
![DELETE with Auth](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/15_delete_with_auth.png)
![DELETE Auth](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/16_delete_auth.png)
![Test Rate Limits](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/17_test_rate_limits.png)
![Cache Miss Test](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/18_test_cache_miss.png)
![Verify GET after Delete](https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/19_verify_get_after_delete.png)

--------------------------------------------------

## Demo Video

<video width="600" controls>
  <source src="https://raw.githubusercontent.com/JohnPretz/CatFactsBonus/main/screenshots/20_demo.mkv" type="video/mp4">
  Your browser does not support the video tag.
</video>


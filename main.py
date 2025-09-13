from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from sqlalchemy.orm import Session
from typing import List
import httpx

import crud, models
from database import SessionLocal, engine
from schemas import CatFactCreateSchema, CatFactSchema

# --------------------
# Database Setup
# --------------------
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------
# App Setup
# --------------------
app = FastAPI(title="Cat Facts Bonus API")

# Rate limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return HTTPException(status_code=429, detail="Rate limit exceeded")

# Auth
bearer_scheme = HTTPBearer()
API_KEY = "mysecretkey123"

def authorize(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )

# Cache init
@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())

# --------------------
# Endpoints
# --------------------

@app.get("/fetch/")
@cache(expire=60)
@limiter.limit("5/minute")
async def fetch_catfacts(request: Request, count: int = 10, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://catfact.ninja/facts?limit={count}")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch cat facts")
    data = response.json().get("data", [])
    added_count = 0
    for item in data:
        fact_text = item.get("fact")
        if fact_text:
            crud.create_catfact(db, CatFactCreateSchema(fact=fact_text))
            added_count += 1
    return {"message": f"{added_count} unique cat facts added successfully!"}

@app.get("/catfacts/", response_model=List[CatFactSchema])
@cache(expire=60)
@limiter.limit("5/minute")
async def read_catfacts(request: Request, db: Session = Depends(get_db)):
    return crud.get_catfacts(db)

@app.get("/catfacts/{fact_id}", response_model=CatFactSchema)
@cache(expire=60)
@limiter.limit("5/minute")
async def read_catfact(request: Request, fact_id: int, db: Session = Depends(get_db)):
    db_fact = crud.get_catfact(db, fact_id)
    if not db_fact:
        raise HTTPException(status_code=404, detail="Fact not found")
    return db_fact

@app.post("/catfacts/", response_model=CatFactSchema)
async def create_catfact(fact: CatFactCreateSchema, db: Session = Depends(get_db),
                         credentials: HTTPAuthorizationCredentials = Depends(authorize)):
    return crud.create_catfact(db, fact)

@app.put("/catfacts/{fact_id}", response_model=CatFactSchema)
async def update_catfact(fact_id: int, fact: CatFactCreateSchema, db: Session = Depends(get_db),
                         credentials: HTTPAuthorizationCredentials = Depends(authorize)):
    updated = crud.update_catfact(db, fact_id, fact)
    if not updated:
        raise HTTPException(status_code=404, detail="Fact not found")
    return updated

@app.delete("/catfacts/{fact_id}")
async def delete_catfact(fact_id: int, db: Session = Depends(get_db),
                         credentials: HTTPAuthorizationCredentials = Depends(authorize)):
    deleted = crud.delete_catfact(db, fact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Fact not found")
    return {"message": f"Fact {fact_id} deleted successfully."}

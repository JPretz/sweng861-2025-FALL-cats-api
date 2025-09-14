from sqlalchemy.orm import Session
from models import CatFact
from schemas import CatFactCreateSchema

# Check if a fact already exists
def catfact_exists(db: Session, fact_text: str) -> bool:
    return db.query(CatFact).filter(CatFact.fact == fact_text).first() is not None

# Create a new cat fact
def create_catfact(db: Session, fact: CatFactCreateSchema):
    db_fact = CatFact(fact=fact.fact)
    db.add(db_fact)
    db.commit()
    db.refresh(db_fact)
    return db_fact

# Get all cat facts
def get_catfacts(db: Session):
    return db.query(CatFact).all()

# Get a single cat fact by ID
def get_catfact(db: Session, fact_id: int):
    return db.query(CatFact).filter(CatFact.id == fact_id).first()

# Update a cat fact
def update_catfact(db: Session, fact_id: int, fact: CatFactCreateSchema):
    db_fact = db.query(CatFact).filter(CatFact.id == fact_id).first()
    if not db_fact:
        return None
    db_fact.fact = fact.fact
    db.commit()
    db.refresh(db_fact)
    return db_fact

# Delete a cat fact
def delete_catfact(db: Session, fact_id: int):
    db_fact = db.query(CatFact).filter(CatFact.id == fact_id).first()
    if not db_fact:
        return False
    db.delete(db_fact)
    db.commit()
    return True

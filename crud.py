from sqlalchemy.orm import Session
from models import CatFact
from schemas import CatFactCreateSchema

def get_catfacts(db: Session):
    return db.query(CatFact).all()

def get_catfact(db: Session, fact_id: int):
    return db.query(CatFact).filter(CatFact.id == fact_id).first()

def create_catfact(db: Session, catfact: CatFactCreateSchema):
    db_fact = CatFact(fact=catfact.fact)
    db.add(db_fact)
    db.commit()
    db.refresh(db_fact)
    return db_fact

def update_catfact(db: Session, fact_id: int, catfact: CatFactCreateSchema):
    db_fact = db.query(CatFact).filter(CatFact.id == fact_id).first()
    if not db_fact:
        return None
    db_fact.fact = catfact.fact
    db.commit()
    db.refresh(db_fact)
    return db_fact

def delete_catfact(db: Session, fact_id: int):
    db_fact = db.query(CatFact).filter(CatFact.id == fact_id).first()
    if not db_fact:
        return None
    db.delete(db_fact)
    db.commit()
    return True

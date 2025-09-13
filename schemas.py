from pydantic import BaseModel

class CatFactCreateSchema(BaseModel):
    fact: str

class CatFactSchema(CatFactCreateSchema):
    id: int

    class Config:
        from_attributes = True  


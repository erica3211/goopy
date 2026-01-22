from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    phone: str

class CustomerUpdate(BaseModel):
    name: str
    phone: str

class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        from_attributes = True
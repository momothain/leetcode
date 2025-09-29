from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4

app = FastAPI(title="Sales API")

class Sale(BaseModel):
    product_name: str = Field(..., min_length=1, max_length=50)
    price: float = Field(..., ge=0)
    time: datetime = Field(now = datetime.timezone.utc())
    id: str = Field(uuid4())

DB: dict[str, Sale] = {}

@app.get("/sales", response_model=List[Sale])
def get_sales(id: str):
    sale = DB.get(id)
    if not sale:
        raise HTTPException(status_code=404, detail="{id} not found")
    else:
        return sale

# def post
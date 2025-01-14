from datetime import datetime
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from typing import Optional

class Expense(BaseModel):
    id: Optional[int] = None
    description: str
    amount: Decimal
    category: str = "General"
    date: datetime = Field(default_factory=datetime.now)

    @validator('amount')
    def validate_amount(cls, v):
        if v <= 0:
            raise ValueError("Amount must be greater than 0")
        return v

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
            Decimal: lambda v: str(v)
        } 
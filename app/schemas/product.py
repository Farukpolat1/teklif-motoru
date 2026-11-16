from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=200)
    unit: str = Field(default="adet", max_length=20)
    price: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    stock_qty: int = Field(default=0, ge=0)


class ProductRead(ProductCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

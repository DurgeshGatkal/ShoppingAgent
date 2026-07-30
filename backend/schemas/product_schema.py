"""
product_schema.py

Pydantic schemas for data validation across API endpoints and DB operations.
"""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class SpecificationSchema(BaseModel):
    """Schema for technical specifications."""
    storage: Optional[str] = "-"
    ram: Optional[str] = "-"
    display: Optional[str] = "-"
    processor: Optional[str] = "-"
    camera: Optional[str] = "-"
    battery: Optional[str] = "-"
    color: Optional[str] = "-"

    model_config = ConfigDict(from_attributes=True)


class ProductBase(BaseModel):
    """Base schema for Product fields."""
    name: str
    brand: str
    platform: str
    price: float
    rating: float = 0.0
    reviews_count: int = 0
    category: str
    image_url: Optional[str] = None
    delivery_info: Optional[str] = "Standard Delivery"
    offers: Optional[str] = "No offers"
    description: Optional[str] = None
    url: Optional[str] = None


class ProductCreate(ProductBase):
    """Schema for creating a new product."""
    specification: Optional[SpecificationSchema] = None


class ProductResponse(ProductBase):
    """Schema for returning product details with ID and specification."""
    id: int
    score: Optional[float] = None
    specification: Optional[SpecificationSchema] = None

    model_config = ConfigDict(from_attributes=True)

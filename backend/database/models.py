"""
models.py

SQLAlchemy ORM models representing Product, Platform, and Specification tables.
"""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from .connection import Base


class Platform(Base):
    """Platform model representing e-commerce sites (Amazon, Flipkart, Croma, etc.)."""
    __tablename__ = "platforms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    website_url = Column(String(255), nullable=True)

    products = relationship("Product", back_populates="platform_rel")


class Product(Base):
    """Product entity table."""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    brand = Column(String(100), index=True, nullable=False)
    platform = Column(String(50), ForeignKey("platforms.name"), nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, default=0.0)
    reviews_count = Column(Integer, default=0)
    category = Column(String(50), index=True, nullable=False)
    image_url = Column(String(500), nullable=True)
    delivery_info = Column(String(100), default="Standard Delivery")
    offers = Column(String(255), default="No offers available")
    description = Column(Text, nullable=True)
    url = Column(String(500), nullable=True)

    platform_rel = relationship("Platform", back_populates="products")
    specification = relationship("Specification", back_populates="product", uselist=False, cascade="all, delete-orphan")


class Specification(Base):
    """Technical specifications table for hardware components."""
    __tablename__ = "specifications"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), unique=True, nullable=False)
    storage = Column(String(50), default="-")
    ram = Column(String(50), default="-")
    display = Column(String(100), default="-")
    processor = Column(String(100), default="-")
    camera = Column(String(100), default="-")
    battery = Column(String(50), default="-")
    color = Column(String(50), default="-")

    product = relationship("Product", back_populates="specification")

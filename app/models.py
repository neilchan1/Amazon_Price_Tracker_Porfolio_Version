"""SQLAlchemy models (Code snippet)

Key points:
- Prices stored as integer penny to avoid floating point issues.
- Relationships: Product -> PriceHistory
"""
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    url = Column(Text, unique=True, nullable=False)
    asin = Column(String(20), nullable=True, index=True)
    title = Column(Text, nullable=True)

    # Prices stored in *penny*
    last_price_penny = Column(Integer, nullable=True)
    target_price_penny = Column(Integer, nullable=True)
    currency = Column(String(10), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # lightweight relationship to show modelling intent
    # history = relationship("PriceHistory", back_populates="product", cascade="all, delete-orphan")

class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), index=True)
    checked_at = Column(DateTime, default=datetime.utcnow, index=True)
    price_penny = Column(Integer, nullable=False)
    currency = Column(String(10), nullable=False)

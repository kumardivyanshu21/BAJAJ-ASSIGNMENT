from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class Instrument(BaseModel):
    symbol: str
    exchange: str
    instrumentType: str
    lastTradedPrice: float

class OrderRequest(BaseModel):
    symbol: str
    quantity: int = Field(..., gt=0)
    type: Literal['BUY', 'SELL']
    style: Literal['MARKET', 'LIMIT']
    price: Optional[float] = None

class OrderResponse(OrderRequest):
    orderId: str
    status: str
    timestamp: datetime

class Trade(BaseModel):
    tradeId: str
    orderId: str
    symbol: str
    quantity: int
    price: float
    timestamp: datetime

class PortfolioPosition(BaseModel):
    symbol: str
    quantity: int
    averagePrice: float
    currentValue: float
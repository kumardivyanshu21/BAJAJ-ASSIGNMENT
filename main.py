from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4
from datetime import datetime
import models
from database import db

app = FastAPI(
    title="Bajaj Broking Trading SDK",
    description="A simulated backend for trading APIs",
    version="1.0.0"
)

@app.get("/api/v1/instruments", response_model=List[models.Instrument])
def get_instruments():
    return db.instruments

@app.post("/api/v1/orders", response_model=models.OrderResponse)
def place_order(order: models.OrderRequest):
    stock = next((item for item in db.instruments if item["symbol"] == order.symbol), None)
    if not stock:
        raise HTTPException(status_code=404, detail="Instrument not found")

    order_id = str(uuid4())
    current_time = datetime.now()
    
    execution_price = stock["lastTradedPrice"]
    status = "EXECUTED" 
    
    new_order = models.OrderResponse(
        orderId=order_id,
        status=status,
        timestamp=current_time,
        **order.dict()
    )
    
    db.orders[order_id] = new_order

    if status == "EXECUTED":
        trade_id = str(uuid4())
        new_trade = models.Trade(
            tradeId=trade_id,
            orderId=order_id,
            symbol=order.symbol,
            quantity=order.quantity,
            price=execution_price,
            timestamp=current_time
        )
        db.trades.append(new_trade)
        
        update_portfolio(order.symbol, order.quantity, order.type, execution_price)

    return new_order

def update_portfolio(symbol, qty, side, price):
    position = db.portfolio.get(symbol)

    if side == "BUY":
        if not position:
            db.portfolio[symbol] = {"quantity": qty, "averagePrice": price}
        else:
            total_cost = (position["quantity"] * position["averagePrice"]) + (qty * price)
            total_qty = position["quantity"] + qty
            position["quantity"] = total_qty
            position["averagePrice"] = total_cost / total_qty
            
    elif side == "SELL":
        if not position or position["quantity"] < qty:
            raise HTTPException(status_code=400, detail="Insufficient holdings to sell")
        
        position["quantity"] -= qty

@app.get("/api/v1/portfolio", response_model=List[models.PortfolioPosition])
def get_portfolio():
    portfolio_list = []
    
    for symbol, data in db.portfolio.items():
        if data["quantity"] > 0:
            stock = next((i for i in db.instruments if i["symbol"] == symbol), None)
            current_price = stock["lastTradedPrice"] if stock else 0
            
            position = models.PortfolioPosition(
                symbol=symbol,
                quantity=data["quantity"],
                averagePrice=round(data["averagePrice"], 2),
                currentValue=round(data["quantity"] * current_price, 2)
            )
            portfolio_list.append(position)
            
    return portfolio_list

@app.get("/api/v1/trades", response_model=List[models.Trade])
def get_trades():
    return db.trades
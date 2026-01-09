BAJAJ BROKING TRADING SDK ASSIGNMENT

OVERVIEW
This is a backend simulation for the trading system assignment using Python and FastAPI.
It handles instruments, orders, and portfolio management in memory.

REQUIREMENTS
- Python 3.x
- Libraries: fastapi, uvicorn

HOW TO INSTALL
1. Open your terminal in this folder.
2. Run command: pip install fastapi uvicorn

HOW TO RUN
Run this exact command in the terminal:
python -m uvicorn main:app --reload

HOW TO TEST
Once the server is running, open this link in your browser to see the API and test it:
http://127.0.0.1:8000/docs

NOTES
- Data is stored in memory (dictionaries) and will reset when you stop the server.
- Market orders are simulated to execute immediately.

- The portfolio automatically updates average price on new buy orders.
- to place order:
- {
  "symbol": "BAJAJ-AUTO",
  "quantity": 10,
  "type": "BUY",
  "style": "MARKET"
}

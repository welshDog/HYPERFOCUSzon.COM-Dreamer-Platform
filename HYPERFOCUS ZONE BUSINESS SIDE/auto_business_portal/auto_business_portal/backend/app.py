"""
app.py
------

FastAPI application serving the BROski auto–business portal system.
This backend provides a few core endpoints:

* ``/api/portals`` – Returns a JSON list of available portals discovered
  by ``portal_scanner.scan_portals``.  Each portal descriptor contains
  a user‑friendly name and relative path.
* ``/api/pay`` – Accepts a payment request and forwards it to
  ``RevenueAgent``.  In this demo the payment is always considered
  successful.
* ``/api/ask`` – Accepts a user question for the ``CustomerSuccessAgent``
  and returns a canned response.  In a real system this might be
  replaced with an AI chatbot or a ticketing system.

To run the development server, install FastAPI and an ASGI server like
uvicorn.  Example::

    pip install fastapi uvicorn
    uvicorn app:app --reload --port 8000

Once running, the API will be available at http://localhost:8000/api/portals

"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

from .portal_scanner import scan_portals
from .agents import RevenueAgent, CustomerSuccessAgent, AnalyticsAgent, SecurityAgent, MarketingAgent


app = FastAPI(title="BROski Auto–Business Backend")


class PaymentRequest(BaseModel):
    user_id: str
    amount: float
    method: str = 'stripe'


class AskRequest(BaseModel):
    user_id: str
    query: str


@app.get("/api/portals", response_model=List[Dict[str, Any]])
async def get_portals() -> List[Dict[str, Any]]:
    """Return a list of discovered portal descriptors."""
    portals = scan_portals()
    return portals


@app.post("/api/pay")
async def pay(request: PaymentRequest) -> Dict[str, Any]:
    """Process a payment via the revenue agent.

    This endpoint validates the user via the security agent before
    processing the payment.  It always returns a successful status
    in this demo but lays the groundwork for real fraud detection and
    billing integration.
    """
    security = SecurityAgent()
    revenue = RevenueAgent()
    analytics = AnalyticsAgent()

    if not security.validate_user(request.user_id):
        raise HTTPException(status_code=403, detail="User validation failed")

    # monitor the transaction before processing
    if not security.monitor_transaction(request.user_id, request.amount):
        raise HTTPException(status_code=403, detail="Transaction flagged as fraudulent")

    success = revenue.process_payment(request.user_id, request.amount, request.method)
    analytics.record_event('purchase', {'user_id': request.user_id, 'amount': request.amount})

    return {"status": "success" if success else "failed"}


@app.post("/api/ask")
async def ask(request: AskRequest) -> Dict[str, str]:
    """Handle a customer support query via the customer success agent."""
    success = CustomerSuccessAgent()
    answer = success.handle_query(request.user_id, request.query)
    AnalyticsAgent().record_event('support_query', {'user_id': request.user_id, 'query': request.query})
    return {"response": answer}


# You can extend this API with additional endpoints for marketing,
# analytics dashboards, or portal management.  See ``agents.py`` for
# stub implementations of the various agent types.
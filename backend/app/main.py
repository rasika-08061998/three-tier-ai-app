from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator

from .database import SessionLocal
from . import models, schemas
from .ai_service import generate_ai_response

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def health_check():
    return {"status": "running"}


@app.post("/chat")
def chat(request: schemas.MessageRequest, db: Session = Depends(get_db)):

    ai_reply = generate_ai_response(request.message)

    message = models.Message(
        user_input=request.message,
        ai_response=ai_reply
    )

    db.add(message)
    db.commit()

    return {"response": ai_reply}


# Prometheus metrics
Instrumentator().instrument(app).expose(app)
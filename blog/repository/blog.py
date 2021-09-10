from sqlalchemy.orm import Session
from ..models import Blog


def get_all(db: Session):
    return db.query(Blog).all()

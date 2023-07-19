import datetime

from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import models


"""
    ACCOUNT
"""


def signup_user(firstname: str, lastname: str, email: str, password: str, db: Session):
    db_user = models.Account(
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        'id': db_user.id,
        'firstname': firstname,
        'lastname': lastname,
        'email': email
    }


def check_email(email: str, db: Session):
    result = db.execute(select(models.Account).where(models.Account.email == email)).first()
    return result[0].id


def get_user(username: str, db: Session):
    result = db.execute(select(models.Account).where(models.Account.email == username)).first()
    return result[0]

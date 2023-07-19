import datetime

from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from fastapi import HTTPException

from db import models
from models import schemas


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
    return db_user.id


def check_email(email: str, db: Session):
    result = db.execute(select(models.Account).where(models.Account.email == email)).first()
    return result[0].id


def get_user(username: str, db: Session):
    result = db.execute(select(models.Account).where(models.Account.email == username)).first()
    return result[0]


"""
    POST
"""


def get_post(postId: int, db: Session):
    result = db.execute(select(models.Post).where(models.Post.id == postId)).first()
    return result[0]


def add_post(post: schemas.AddOrUpdatePost, accountId: int, db: Session):
    db_post = models.Post(
        title=post.title,
        content=post.content,
        owner=accountId,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(postId, post: schemas.AddOrUpdatePost, db: Session):
    db.query(models.Post).filter(models.Post.id == postId).update(
        {
            models.Post.title: post.title,
            models.Post.content: post.content
        }
    )
    db.commit()


def delete_post(postId: int, db: Session):
    db.query(models.Post).filter(models.Post.id == postId).delete()
    db.commit()

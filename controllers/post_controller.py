from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import schemas
from db.crud import get_post, add_post, update_post, delete_post, like_post, dislike_post


def post_get(postId: int, db: Session):
    try:
        return get_post(postId, db)
    except:
        raise HTTPException(status_code=404, detail='Post not found')


def post_add(post: schemas.AddOrUpdatePost, accountId: int, db: Session):
    return add_post(post, accountId, db)


def post_update(postId: int, post: schemas.AddOrUpdatePost, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
        if post['owner'] != accountId:
            raise HTTPException(status_code=403)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    update_post(postId, post, db)
    return get_post(postId, db)


def post_delete(postId: int, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
        if post['owner'] != accountId:
            raise HTTPException(status_code=403)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    delete_post(postId, db)


def post_like(postId: int, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
        if post['owner'] == accountId:
            raise HTTPException(status_code=403)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    if like_post(post['likes'], postId, db):
        post['likes'] += 1
        return post


def post_dislike(postId: int, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
        if post['owner'] == accountId:
            raise HTTPException(status_code=403)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    if like_post(post['dislikes'], postId, db):
        post['dislikes'] += 1
        return post

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
        posts = get_post(postId, db)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    if posts.owner != accountId:
        raise HTTPException(status_code=403)
    update_post(postId, post, db)
    return get_post(postId, db)


def post_delete(postId: int, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    if post.owner != accountId:
        raise HTTPException(status_code=403)
    delete_post(postId, db)


def post_like(postId: int, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    if post.owner == accountId:
        raise HTTPException(status_code=403, detail='You can`t like your posts')
    like_post(post.likes, postId, db)
    return get_post(postId, db)


def post_dislike(postId: int, accountId: int, db: Session):
    try:
        post = get_post(postId, db)
    except:
        raise HTTPException(status_code=404, detail='Post not found')
    if post.owner == accountId:
        raise HTTPException(status_code=403, detail='You can`t dislike your posts')
    dislike_post(post.dislikes, postId, db)
    return get_post(postId, db)

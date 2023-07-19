from fastapi import routing, Depends
from sqlalchemy.orm import Session

from db.db import get_db
from controllers.reg_controller import get_current_account
from db import models
from models import schemas
from controllers.post_controller import post_get, post_add, post_delete, post_update


router = routing.APIRouter()


@router.get('/posts/{postId}', tags=['animal'])
async def get_post(postId: int, db: Session = Depends(get_db),
                   account: models.Account | None = Depends(get_current_account)):
    return post_get(postId, db)


@router.post('/posts', tags=['animal'], status_code=201)
async def add_post(post: schemas.AddOrUpdatePost, user: models.Account = Depends(get_current_account),
                   db: Session = Depends(get_db)):
    return post_add(post, user.id, db)


@router.put('/posts/{postId}', tags=['animal'])
async def update_post(postId: int, post: schemas.AddOrUpdatePost, user: models.Account = Depends(get_current_account),
                      db: Session = Depends(get_db)):
    return post_update(postId, post, user.id, db)


@router.delete('/posts/{postId}', tags=['animal'])
async def delete_post(postId: int, user: models.Account = Depends(get_current_account),
                      db: Session = Depends(get_db)):
    return post_delete(postId, user.id, db)

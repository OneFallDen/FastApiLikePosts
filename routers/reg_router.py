from fastapi import routing, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic

from db.db import get_db
from auth.auth import security_for_reg
from controllers.reg_controller import reg_user, get_current_account
from db import models


router = routing.APIRouter()


@router.post('/registration', tags=['registration'], status_code=201)
async def registration_user(user: models.Account, db: Session = Depends(get_db),
                            account: HTTPBasic | None = Depends(security_for_reg)):
    if account:
        raise HTTPException(status_code=403)
    return reg_user(user.firstName, user.lastName, user.email, user.password, db)

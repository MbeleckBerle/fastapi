from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from .. import schemas
from ..repository import user


router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):

    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):

    return user.show(id, db)


# @router.post("/", response_model=schemas.ShowUser)
# def create_user(request: schemas.User, db: Session = Depends(database.get_db)):

#     new_user = models.User(
#         name=request.name,
#         email=request.email,
#         password=hashing.Hash.bcrypt(request.password),
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# @router.get("/{id}", response_model=schemas.ShowUser)
# def get_user(id: int, db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"User with the id {id} is not found",
#         )

#     return user

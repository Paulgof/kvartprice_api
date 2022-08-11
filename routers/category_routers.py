from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import category_crud
from dependencies import get_db
from schemas import category_schemas

router = APIRouter()


@router.get('/categories/toilet_types/', response_model=list[category_schemas.ToiletType], tags=['categories'])
def read_toilet_types(db: Session = Depends(get_db)):
    return category_crud.get_toilet_types(db)


@router.get('/categories/repair_types/', response_model=list[category_schemas.RepairType], tags=['categories'])
def read_repair_types(db: Session = Depends(get_db)):
    return category_crud.get_repair_types(db)


@router.get('/categories/balcony_types/', response_model=list[category_schemas.BalconyType], tags=['categories'])
def read_balcony_types(db: Session = Depends(get_db)):
    return category_crud.get_balcony_types(db)


@router.get('/categories/lift_types/', response_model=list[category_schemas.LiftType], tags=['categories'])
def read_lift_types(db: Session = Depends(get_db)):
    return category_crud.get_lift_types(db)


@router.get('/categories/house_types/', response_model=list[category_schemas.HouseType], tags=['categories'])
def read_house_types(db: Session = Depends(get_db)):
    return category_crud.get_house_types(db)

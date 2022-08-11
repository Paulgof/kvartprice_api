from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from crud import place_crud
from dependencies import get_db
from schemas import place_schemas

router = APIRouter()


@router.post('/cities/', response_model=place_schemas.City, tags=['places'])
def create_city(city: place_schemas.CityCreate, db: Session = Depends(get_db)):
    db_city = place_crud.get_city_by_name(db, city.name_en)
    if db_city:
        raise HTTPException(status_code=400, detail='City already exists')

    return place_crud.create_city(db, city)


@router.get('/cities/', response_model=list[place_schemas.City], tags=['places'])
def read_cities(db: Session = Depends(get_db)):
    return place_crud.get_cities(db)


@router.get('/cities/{city_id}', response_model=place_schemas.City, tags=['places'])
def read_city(city_id: int, db: Session = Depends(get_db)):
    db_city = place_crud.get_city(db, city_id)
    if not db_city:
        raise HTTPException(status_code=404, detail='City not found')

    return db_city


@router.get('/cities/{city_id}/districts/', response_model=list[place_schemas.District], tags=['places'])
def read_districts(city_id: int, db: Session = Depends(get_db)):
    db_city = place_crud.get_city(db, city_id)
    if not db_city:
        raise HTTPException(status_code=404, detail='City not found')

    return db_city.districts


@router.post('/cities/{city_id}/districts/', response_model=place_schemas.District, tags=['places'])
def create_district(city_id: int, db: Session = Depends(get_db)):
    pass


@router.get('/districts/{district_id}', response_model=place_schemas.District, tags=['places'])
def read_district(district_id: int, db: Session = Depends(get_db)):
    db_district = place_crud.get_district(db, district_id)
    if not db_district:
        raise HTTPException(status_code=404, detail='District not found')

    return db_district


@router.get(
    '/districts/{district_id}/microdistricts/',
    response_model=list[place_schemas.Microdistrict],
    tags=['places'],
)
def read_microdistricts(district_id: int, db: Session = Depends(get_db)):
    db_district = place_crud.get_district(db, district_id)
    if not db_district:
        raise HTTPException(status_code=404, detail='District not found')

    return db_district.microdistricts


@router.post('/districts/{district_id}/microdistricts/', response_model=place_schemas.Microdistrict, tags=['places'])
def create_microdistricts(district_id: int, db: Session = Depends(get_db)):
    pass


@router.get('/microdistricts/{microdistrict_id}', response_model=place_schemas.Microdistrict, tags=['places'])
def read_microdistrict(microdistrict_id: int, db: Session = Depends(get_db)):
    db_microdistrict = place_crud.get_microdistrict(db, microdistrict_id)
    if not db_microdistrict:
        raise HTTPException(status_code=404, detail='Microdistrict not found')

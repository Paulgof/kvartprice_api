from sqlalchemy.orm import Session

from models import place_models
from schemas import place_schemas


def get_city(db: Session, city_id: int):
    return db.query(place_models.City).filter(place_models.City.city_id == city_id).first()


def get_city_by_name(db: Session, city_name: str):
    return db.query(place_models.City).filter(place_models.City.name_en == city_name).first()


def get_cities(db: Session):
    return db.query(place_models.City).all()


def create_city(db: Session, city: place_schemas.CityCreate):
    db_city = place_models.City(name_en=city.name_en, name_ru=city.name_ru, city_code=city.city_code)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


def get_district(db: Session, district_id: int):
    return db.query(place_models.District).filter(place_models.District.district_id == district_id).first()


def get_district_by_name(db: Session, district_name: str):
    return db.query(place_models.District).filter(place_models.District.name == district_name).first()


def get_districts(db: Session, city_id: int):
    return db.query(place_models.District).filter(place_models.District.city_id == city_id).all()


def create_city_district(db: Session, district: place_schemas.DistrictCreate, city_id: int):
    db_district = place_models.District(**district.dict(), city_id=city_id)
    db.add(db_district)
    db.commit()
    db.refresh(db_district)
    return db_district


def get_microdistrict(db: Session, microdistrict_id: int):
    return db.query(place_models.Microdistrict)\
        .filter(place_models.Microdistrict.microdistrict_id == microdistrict_id).first()


def get_microdistrict_by_name(db: Session, microdistrict_name: str):
    return db.query(place_models.Microdistrict).filter(place_models.Microdistrict.name == microdistrict_name).first()


def get_microdistricts(db: Session, district_id: int):
    return db.query(place_models.Microdistrict).filter(place_models.Microdistrict.district_id == district_id).all()


def create_microdistrict(db: Session, microdistrict: place_schemas.MicrodistrictCreate, district_id: int):
    db_microdistrict = place_models.Microdistrict(**microdistrict.dict(), district_id=district_id)
    db.add(db_microdistrict)
    db.commit()
    db.refresh(db_microdistrict)
    return db_microdistrict

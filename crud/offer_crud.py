from sqlalchemy.orm import Session

from crud import place_crud, category_crud
from models import offer_models
from schemas import offer_schemas
from schemas.place_schemas import CityCreate, DistrictCreate, MicrodistrictCreate
from schemas.category_schemas import ToiletTypeBase, RepairTypeBase, BalconyTypeBase, LiftTypeBase, HouseTypeBase
from schemas.offer_schemas import Statistics


def get_offer(db: Session, offer_id: int):
    return db.query(offer_models.Offer).filter(offer_models.Offer.offer_id == offer_id).first()


def get_offers_by_city(db: Session, city_id: int):
    return db.query(offer_models.Offer).filter(offer_models.Offer.city == city_id).all()


def get_offers_statistics(db: Session, city_id: int):
    city_offers = db.query(offer_models.Offer).filter(offer_models.Offer.city == city_id).all()
    count = 0
    microdistricts = {}
    summator = 0
    for offer in city_offers:
        count += 1
        old_value = microdistricts.setdefault(offer.microdistrict, 0)
        microdistricts[offer.microdistrict] += old_value + 1
        summator += offer.price / offer.square

    if 1 in microdistricts:
        microdistricts.pop(1)

    top_microdistrict_id = list(sorted(microdistricts, key=lambda x: microdistricts[x]))[-1]
    top_microdistrict = place_crud.get_microdistrict(db, top_microdistrict_id)
    return Statistics(offers_count=count, mean_price=summator/count, popular_microdistrict=top_microdistrict.name)


def create_offer(db: Session, offer: offer_schemas.OfferCreate):
    city = place_crud.get_city_by_name(db, offer.city)
    if not city:
        city = place_crud.create_city(db, CityCreate(name_en=offer.city, name_ru=offer.city, city_code=100))

    district = place_crud.get_district_by_name(db, offer.district)
    if not district:
        district = place_crud.create_city_district(db, DistrictCreate(name=offer.district), city.city_id)

    microdistrict = place_crud.get_microdistrict_by_name(db, offer.microdistrict)
    if not microdistrict:
        microdistrict = place_crud.create_microdistrict(
            db,
            MicrodistrictCreate(name=offer.microdistrict),
            district.district_id
        )

    toilet_type = category_crud.get_toilet_type_by_name(db, offer.toilet)
    if not toilet_type:
        toilet_type = category_crud.create_toilet_type(db, ToiletTypeBase(name=offer.toilet))

    balcony_type = category_crud.get_balcony_type_by_name(db, offer.balcony)
    if not balcony_type:
        balcony_type = category_crud.create_balcony_type(db, BalconyTypeBase(name=offer.balcony))

    repair_type = category_crud.get_repair_type_by_name(db, offer.repair)
    if not repair_type:
        repair_type = category_crud.create_repair_type(db, RepairTypeBase(name=offer.repair))

    lifts_type = category_crud.get_lift_type_by_name(db, offer.lifts)
    if not lifts_type:
        lifts_type = category_crud.create_lift_type(db, LiftTypeBase(name=offer.lifts))

    house_type = category_crud.get_house_type_by_name(db, offer.house_type)
    if not house_type:
        house_type = category_crud.create_house_type(db, HouseTypeBase(name=offer.house_type))

    flush_data = offer.dict()
    flush_data['city'] = city.city_id
    flush_data['district'] = district.district_id
    flush_data['microdistrict'] = microdistrict.microdistrict_id
    if 'microdistrict_2' in flush_data:
        flush_data['neighborhood'] = flush_data.pop('microdistrict_2')

    if 'residental_complex' in flush_data:
        flush_data['residential_complex'] = flush_data.pop('residental_complex')

    flush_data.pop('toilet')
    flush_data['toilet_type'] = toilet_type.toilet_type_id
    flush_data.pop('balcony')
    flush_data['balcony_type'] = balcony_type.balcony_type_id
    flush_data.pop('repair')
    flush_data['repair_type'] = repair_type.repair_type_id
    flush_data.pop('lifts')
    flush_data['lifts_type'] = lifts_type.lift_type_id
    flush_data.pop('house_type')
    flush_data['house_type'] = house_type.house_type_id

    db_offer = offer_models.Offer(**flush_data)
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

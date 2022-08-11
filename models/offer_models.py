from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text

from database import Base


class Offer(Base):
    __tablename__ = 'offers'

    offer_id = Column(Integer, primary_key=True, index=True)

    ext_site_id = Column(Integer, unique=True, index=True)
    ext_site_link = Column(String, unique=True)
    ext_offer_views = Column(Integer)

    price = Column(Integer)
    rooms = Column(Integer)
    square = Column(Float)
    live_square = Column(Float)
    kitchen = Column(Float)
    floor = Column(Integer)
    total_floors = Column(Integer)

    city = Column(Integer, ForeignKey('cities.city_id'))
    district = Column(Integer, ForeignKey('districts.district_id'))
    microdistrict = Column(Integer, ForeignKey('microdistricts.microdistrict_id'))
    neighborhood = Column(String)  # microdistrict_2
    residential_complex = Column(String)
    street = Column(String)
    flat_number = Column(String)

    description = Column(Text)
    flat_type = Column(String)
    toilet_type = Column(ForeignKey('toilet_types.toilet_type_id'))
    balcony_type = Column(ForeignKey('balcony_types.balcony_type_id'))
    repair_type = Column(ForeignKey('repair_types.repair_type_id'))
    house_type = Column(ForeignKey('house_types.house_type_id'))
    lifts_type = Column(ForeignKey('lift_types.lift_type_id'))
    ceiling = Column(String)
    house_year = Column(Integer)
    window_view = Column(String)
    parking = Column(String)
    gas = Column(String)

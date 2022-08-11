from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True, index=True)
    city_code = Column(Integer, unique=True)
    name_en = Column(String, index=True)
    name_ru = Column(String)

    districts = relationship('District', back_populates='city')


class District(Base):
    __tablename__ = 'districts'

    district_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))

    city = relationship('City', back_populates='districts')
    microdistricts = relationship('Microdistrict', back_populates='district')


class Microdistrict(Base):
    __tablename__ = 'microdistricts'

    microdistrict_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    district_id = Column(Integer, ForeignKey('districts.district_id'))

    district = relationship('District', back_populates='microdistricts')

from sqlalchemy import Column, Integer, String

from database import Base


class ToiletType(Base):
    __tablename__ = 'toilet_types'

    toilet_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class BalconyType(Base):
    __tablename__ = 'balcony_types'

    balcony_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class LiftType(Base):
    __tablename__ = 'lift_types'

    lift_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class RepairType(Base):
    __tablename__ = 'repair_types'

    repair_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class HouseType(Base):
    __tablename__ = 'house_types'

    house_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

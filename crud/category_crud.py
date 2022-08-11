from sqlalchemy.orm import Session

from models import category_models as m
from schemas import category_schemas as s


def get_toilet_types(db: Session):
    return db.query(m.ToiletType).all()


def get_toilet_type(db: Session, toilet_type_id: int):
    return db.query(m.ToiletType).filter(m.ToiletType.toilet_type_id == toilet_type_id).first()


def get_toilet_type_by_name(db: Session, name: str):
    return db.query(m.ToiletType).filter(m.ToiletType.name == name).first()


def create_toilet_type(db: Session, toilet_type: s.ToiletTypeBase):
    db_toilet_type = m.ToiletType(name=toilet_type.name)
    db.add(db_toilet_type)
    db.commit()
    db.refresh(db_toilet_type)
    return db_toilet_type


def get_balcony_types(db: Session):
    return db.query(m.BalconyType).all()


def get_balcony_type(db: Session, balcony_type_id: int):
    return db.query(m.BalconyType).filter(m.BalconyType.balcony_type_id == balcony_type_id).first()


def get_balcony_type_by_name(db: Session, name: str):
    return db.query(m.BalconyType).filter(m.BalconyType.name == name).first()


def create_balcony_type(db: Session, balcony_type: s.BalconyTypeBase):
    db_balcony_type = m.BalconyType(name=balcony_type.name)
    db.add(db_balcony_type)
    db.commit()
    db.refresh(db_balcony_type)
    return db_balcony_type


def get_lift_types(db: Session):
    return db.query(m.LiftType).all()


def get_lift_type(db: Session, lift_type_id: int):
    return db.query(m.LiftType).filter(m.LiftType.lift_type_id == lift_type_id).first()


def get_lift_type_by_name(db: Session, name: str):
    return db.query(m.LiftType).filter(m.LiftType.name == name).first()


def create_lift_type(db: Session, lift_type: s.LiftTypeBase):
    db_lift_type = m.LiftType(name=lift_type.name)
    db.add(db_lift_type)
    db.commit()
    db.refresh(db_lift_type)
    return db_lift_type


def get_repair_types(db: Session):
    return db.query(m.RepairType).all()


def get_repair_type(db: Session, repair_type_id: int):
    return db.query(m.RepairType).filter(m.RepairType.repair_type_id == repair_type_id).first()


def get_repair_type_by_name(db: Session, name: str):
    return db.query(m.RepairType).filter(m.RepairType.name == name).first()


def create_repair_type(db: Session, repair_type: s.RepairTypeBase):
    db_repair_type = m.RepairType(name=repair_type.name)
    db.add(db_repair_type)
    db.commit()
    db.refresh(db_repair_type)
    return db_repair_type


def get_house_types(db: Session):
    return db.query(m.HouseType).all()


def get_house_type(db: Session, house_type_id: int):
    return db.query(m.HouseType).filter(m.HouseType.house_type_id == house_type_id).first()


def get_house_type_by_name(db: Session, name: str):
    return db.query(m.HouseType).filter(m.HouseType.name == name).first()


def create_house_type(db: Session, house_type: s.HouseTypeBase):
    db_house_type = m.HouseType(name=house_type.name)
    db.add(db_house_type)
    db.commit()
    db.refresh(db_house_type)
    return db_house_type

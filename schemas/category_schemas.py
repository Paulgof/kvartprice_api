from pydantic import BaseModel


class ToiletTypeBase(BaseModel):
    name: str


class ToiletType(ToiletTypeBase):
    toilet_type_id: int

    class Config:
        orm_mode = True


class BalconyTypeBase(BaseModel):
    name: str


class BalconyType(BalconyTypeBase):
    balcony_type_id: int

    class Config:
        orm_mode = True


class RepairTypeBase(BaseModel):
    name: str


class RepairType(RepairTypeBase):
    repair_type_id: int

    class Config:
        orm_mode = True


class LiftTypeBase(BaseModel):
    name: str


class LiftType(LiftTypeBase):
    lift_type_id: int

    class Config:
        orm_mode = True


class HouseTypeBase(BaseModel):
    name: str


class HouseType(HouseTypeBase):
    house_type_id: int

    class Config:
        orm_mode = True

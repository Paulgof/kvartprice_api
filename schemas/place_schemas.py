from pydantic import BaseModel

class MicrodistrictBase(BaseModel):
    name: str

class MicrodistrictCreate(MicrodistrictBase):
    pass

class Microdistrict(MicrodistrictBase):
    microdistrict_id: int
    district_id: int

    class Config:
        orm_mode = True


class DistrictBase(BaseModel):
    name: str

class DistrictCreate(DistrictBase):
    pass

class District(DistrictBase):
    district_id: int
    city_id: int
    microdistricts: list[Microdistrict] = []

    class Config:
        orm_mode = True

class CityBase(BaseModel):
    name_en: str
    name_ru: str
    city_code: int

class CityCreate(CityBase):
    pass

class City(CityBase):
    city_id: int
    districts: list[District] = []

    class Config:
        orm_mode = True

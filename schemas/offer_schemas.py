from pydantic import BaseModel


class Statistics(BaseModel):
    offers_count: int
    mean_price: int
    popular_microdistrict: str


class OfferToPredict(BaseModel):
    rooms: int
    square: float
    floor: int
    total_floors: int
    district: str
    microdistrict: str
    toilet: str
    balcony: str
    repair: str
    house_type: str
    lifts: str


class PredictResult(BaseModel):
    prediction: int


class OfferCreate(BaseModel):
    ext_site_id: int
    ext_site_link: str
    ext_offer_views: int

    price: int
    rooms: int
    square: float
    live_square: float
    kitchen: float
    floor: int
    total_floors: int

    city: str
    district: str
    microdistrict: str
    neighborhood: str
    residential_complex: str
    street: str
    flat_number: str

    description: str
    flat_type: str
    toilet: str
    balcony: str
    repair: str
    house_type: str
    lifts: str
    ceiling: str
    house_year: int
    window_view: str
    parking: str
    gas: str


class Offer(BaseModel):
    offer_id: int

    ext_site_id: int
    ext_site_link: str
    ext_offer_views: int

    price: int
    rooms: int
    square: float
    live_square: float
    kitchen: float
    floor: int
    total_floors: int

    city: int
    district: int
    microdistrict: int
    neighborhood: str
    residential_complex: str
    street: str
    flat_number: str

    description: str
    flat_type: str
    toilet_type: int
    balcony_type: int
    repair_type: int
    house_type: int
    lifts_type: int
    ceiling: str
    house_year: int
    window_view: str
    parking: str
    gas: str

    class Config:
        orm_mode = True

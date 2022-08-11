from fastapi import Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from crud import offer_crud, place_crud
from database import engine
from dependencies import get_db
from models import place_models, category_models, offer_models
from nn.predict import predict
from routers import place_routers, category_routers
from schemas import offer_schemas

place_models.Base.metadata.create_all(bind=engine)
category_models.Base.metadata.create_all(bind=engine)
offer_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(category_routers.router)
app.include_router(place_routers.router)


@app.post('/offers/', response_model=offer_schemas.Offer, tags=['offers'])
def create_offer(offer: offer_schemas.OfferCreate, db: Session = Depends(get_db)):
    return offer_crud.create_offer(db, offer)


@app.get('/offers/statistics/', response_model=offer_schemas.Statistics, tags=['offers'])
def get_statistics(city_id: int, db: Session = Depends(get_db)):
    return offer_crud.get_offers_statistics(db, city_id)


@app.post('/offers/predict', response_model=offer_schemas.PredictResult, tags=['offers'])
def get_predictions(city_id: int, offer: offer_schemas.OfferToPredict, db: Session = Depends(get_db)):
    city_name = place_crud.get_city(db, city_id).name_en
    return offer_schemas.PredictResult(prediction=predict(offer, city_name))

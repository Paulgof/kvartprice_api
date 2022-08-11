import pandas as pd
import joblib
from tensorflow import keras

from schemas.offer_schemas import OfferToPredict


def predict(offer: OfferToPredict, city_name: str):
    model = keras.models.load_model(f'nn/models/{city_name}/nn.h5')
    transformer = joblib.load(f'nn/models/{city_name}/transformer.joblib')

    df = pd.DataFrame({
        'Price': [1],
        'Rooms': [offer.rooms],
        'Square': [offer.square],
        'Floor': [offer.floor],
        'Total Floors': [offer.total_floors],
        'District': [offer.district],
        'Microdistrict': [offer.microdistrict],
        'Toilet': [offer.toilet],
        'Balcony': [offer.balcony],
        'Repair': [offer.repair],
        'House Type': [offer.house_type],
        'Lifts': [offer.lifts]
    })
    df = transformer.transform(df)
    pred = model.predict(df.A[:, 1:])
    pred_price = int(pred.flatten()[0]) // 100000 * 100000

    return pred_price

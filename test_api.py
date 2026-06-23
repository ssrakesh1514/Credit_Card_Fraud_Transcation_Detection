import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_predict():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "Unnamed_0":1,
            "cc_num":123456,
            "amt":500,
            "zip":10001,
            "lat":40,
            "long":-80,
            "city_pop":100000,
            "unix_time":1371816865,
            "merch_lat":40.5,
            "merch_long":-80.2,
            "hour":14,
            "day":23,
            "month":6
        }
    )

    assert response.status_code == 200
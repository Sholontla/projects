import os
import re
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from binance.cm_futures import CMFutures
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#from config import api_key, secret
from uitils import *

from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# dir = directory=str(Path(BASE_DIR, 'static'))
#templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'static')))


app = FastAPI(
    title = "Test Biance Service ....",
    description = "Binance Futures",
    version = "v0.1",
)       
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")
templates = Jinja2Templates(directory="static")

@app.get('/')
async def main(request: Request):
    return templates.TemplateResponse("code/app/static/index.html", {"request": request})

@app.get('/binance/test/connection/{key}/{secret}')
def auth_get_all_blog_users(key: str, secret: str):
    cm_futures_client = CMFutures(key=key, secret=secret)
    return cm_futures_client.account()

@app.get('/binance/account/{api_key}/{secret}')
async def binance_account(api_key: str, secret: str):
    client = RequestClient(api_key=api_key, secret_key=secret)
    result = client.get_account_information()
    capital, asset_1, asset_2 = Get_Capital(result, "USDT")
    return  capital, asset_1, asset_2

# @app.get('/binance/candle')
# async def binance_candle(request: Request):
#     client = RequestClient(api_key=api_key, secret=secret)
#     candels = client.get_candlestick_data(symbol="BTCUSDT", interval="1m", limit=10)
#     return candels

# @app.get('/binance/filter/market')
# async def binance_account():
#     client = RequestClient(api_key=api_key, secret_key=secret)
#     result = client.get_exchange_information()
#     minQty, stepSize, maxQtz = Get_Exchange_filters(r= Calculate_max_Decimal_Qty(stepSize)esult, "ADAUSDT")
#     maxDecimal 
#     return  maxDecimal

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    uvicorn.run("main:app", host = "0.0.0.0", port = port, debug=False)
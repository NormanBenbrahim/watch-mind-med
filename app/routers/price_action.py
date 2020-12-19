from fastapi import APIRouter
from datetime import datetime, timedelta
from pytz import timezone 
from yfinance import Ticker 

# initiate the router
router = APIRouter()

# collect timestamps
time_now = datetime.now(timezone('EST'))
time_yesterday = time_now - timedelta(days=1)

# convert to string timestamps 
timestamp_now = time_now.strftime('%Y-%m-%d')
timestamp_yesterday = time_yesterday.strftime('%Y-%m-%d')


@router.get('/price_action')
async def price_action(price_limit: float):
    # get the mmed ticker
    mmed = Ticker("MMED.NE")
    
    # get current price
    prices_every_5_min = mmed.history(start=timestamp_yesterday, end=timestamp_now, interval="5m")

    # collect the last element which is the current price
    current_prices = prices_every_5_min.tail(1)

    # get the close price
    close_price = current_prices['Close'][0]

    # check that the close price isn't higher then the price_limit
    if close_price > price_limit:
        return {"message": "it's ok", "current price": close_price}
    else:
        return {"message": "aw hell...", "current price": close_price}
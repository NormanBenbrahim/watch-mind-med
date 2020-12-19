from fastapi import FastAPI
import uvicorn
import logging
import requests
import json
from routers import health_check, price_action

# base api:
# https://github.com/hjkelly/fastapi-budget/tree/master/app

# formatter for logging
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')

# start api
app = FastAPI()

# root
@app.get("/")
async def root():
    return {200: "Successfully connected to API, visit /docs to view all routes"}

# include other routes
app.include_router(health_check.router)
app.include_router(price_action.router)

if __name__ == '__main__':
    uvicorn.run(app, debug=True, host="0.0.0.0", port=8000)
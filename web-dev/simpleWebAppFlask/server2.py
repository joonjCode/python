from fastapi import FastAPI
from scarpe import run as scrape_runner
app = FastAPI()

@app.get('/')
def hello_world():
    return {'hello':'world'}


@app.get('/box-office-scraper')
def hello_world():
    scrape_runner()
    return {'hello':'Done'}
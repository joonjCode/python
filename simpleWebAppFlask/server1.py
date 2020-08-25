from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world. This is Flask'

@app.route('/abc', methods=['GET'])
def abc():
    return 'Hello, world. This is Flask'

@app.route('/box-office-scraper', methods=['POST'])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {'data':[1,2,3]}
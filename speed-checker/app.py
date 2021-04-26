import speedtest
from datetime import datetime
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import requests

import time

st = speedtest.Speedtest()


time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
start_time = time.time()
downspeed = round((round(st.download()) / 1048576), 2)
upspeed = round((round(st.upload()) / 1048576), 2)
ping = st.results.ping
print(f'time : {time_now}, download : {downspeed}, upspeed : {upspeed}, ping : {ping}')
print(f'Took {time.time() - start_time} to run ')




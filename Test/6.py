import pywebio
from pywebio.input import *
from pywebio.output import *

import time

def set_now_ts(set_value):
    set_value(int(time.time()))

ts = input('Timestamp', type=NUMBER, action=('Now', set_now_ts))
from datetime import date,timedelta
def select_date(set_value):
    with popup('Select Date'):
        put_buttons(['Today'], onclick=[lambda: set_value(date.today(), 'Today')])
        put_buttons(['Yesterday'], onclick=[lambda: set_value(date.today() - timedelta(days=1), 'Yesterday')])

d = input('Date', action=('Select', select_date), readonly=True)
put_text(type(d), d)
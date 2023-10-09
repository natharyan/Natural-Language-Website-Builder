from pywebio.input import *
from pywebio.output import *

def btn_click(btn_val):
    put_text("You click %s button" % btn_val)

put_buttons(['A', 'B', 'C'], onclick=btn_click)  # a group of buttons

put_button("Click me", onclick=lambda: put_button("Click",onclick=lambda: toast("Clicked")))  # single button
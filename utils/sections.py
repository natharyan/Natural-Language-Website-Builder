from pywebio.input import *
from pywebio.output import *
from pywebio import config
import sys
sys.path.append('utils/')
from style import style

# probably delete

sections = ["header","body","footer"]

config(css_file=style)

@use_scope('command_box',clear=True)
def command_box(text):
    print(style)
    command = input(help_text=text,type=TEXT)
    return command

@use_scope('header')
def header(*args):
    heading, subheading = args
    with use_scope('nav',clear=True):
        put_buttons([
        dict(label=i, value=i, color='success')
        for i in ['header']
        ], onclick=lambda b: scroll_to(b), link_style=True)
    put_html(f"""
    <div class="page-header" style="text-align: center;">
        <h1>{heading}</h1>
        <p class="lead">{subheading}</p>
    </div>""")

nav = ['header']
@use_scope('body')
def body(*args):
    #section, content
    #nav.append(section)
    with use_scope('nav',clear=True):
        put_buttons([
        dict(label=i, value=i, color='primary')
        for i in nav
        ], onclick=lambda b: scroll_to({b}), link_style=True)
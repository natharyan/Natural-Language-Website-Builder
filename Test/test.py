from pywebio import start_server,config
from pywebio.output import *

config(theme='dark')

def main():
    # home = 'home'
    tabs = [
        {'title': 'Home', 'content': put_scope('home')},
        {'title': 'About', 'content': put_text('the content for the about page')}
    ]
    put_tabs(tabs)
    # put_tabs([
    #     {'title':'Home','content':put_scope(home)},
    #     {'title':'About','content':'content for the about page'}
    # ])
    with use_scope('home'):
        put_text('text added later')

if __name__ == '__main__':
    start_server(main, debug=True, port=8000)
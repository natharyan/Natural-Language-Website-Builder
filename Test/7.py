from pywebio import start_server, config
from pywebio.input import *
from pywebio.output import *

@config(css_style=style, theme='dark',title='Title',)
def main():
    put_text('start')
    put_button('Click', onclick=lambda: toast('Clicked'),color='success')
    info = input_group("User Info",[
        input('Input your name', name='name'),
        input('Input your age', name='age', type=NUMBER)
    ])
    put_text(info['name'],info['age'],position=1)

if __name__ == '__main__':
    start_server(main,debug=True,port=8000)
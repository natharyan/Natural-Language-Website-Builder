from pywebio.input import *

# string
age = input("How old are you", type=NUMBER)

# string
password = input("Input password", type=PASSWORD)

# Drop-down selection - string
gift = select('Which gift you want?', ['keyboard', 'ipad'])

# Checkbox - list
agree = checkbox("User Term", options=['I agree to terms and conditions'])

# Single choice - list
answer = radio("Choose one", options=['A', 'B', 'C', 'D'])

# Multi-line text input - string
text = textarea('Text Area', rows=3, placeholder='Some text')

# File Upload - file - dict - image data
img = file_upload("Select a image:", accept="image/*")
from pywebio.output import *
import csv
# for different types of subcontents within keymaps and other functions

def make_tableList(file):
    if not file.endswith(".csv"):
        file += ".csv"
    table_data = []
    with open('./utils/files/'+file,'r',newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            table_data.append(row)
    return table_data

def makeimage(file):
    split = file.split('/')
    name = split[0]
    if len(split) != 1:
        dim_x = 'x' if 'x' in split[1] else 'X'
        dimensions = split[1].split(dim_x)
    else:
        dimensions = '500','500'
    img = open('./utils/img/'+split[0],'rb').read()
    print('./utils/img/'+split[0],dimensions[0],dimensions[1])
    return img,dimensions[0],dimensions[1]


def get_section(text):
    sections = ["header","body","footer"]
    return min(sections,key=lambda s: text.index(s) if s in text else float('inf'))

# content placement and style
function_map = {"title": [put_text,'text-align:center;font-size: 3em'], "description": [put_text,'text-align:center;'], "text": [put_text,''],"table":[put_table,make_tableList,'width:100%'],"image":[put_image,makeimage,'display:block;margin:auto']}

function_types = {"display":["title","description","text"],"dim":["image"],"extract":["table"]}
subsections_dict = {"title":['title','heading','main heading'],
                "description":['description','subheading','info','details','overview','explanation','summary'],
                "text":['text','paragraph','sentence','sentences'],
                "table":['table','matrix','grid','spreadsheet','file','sheet'],
                "image":["image","picture","graphic","photo","photograph","visual","illustration","drawing","chart","figure","artwork","snapshot"]
                }
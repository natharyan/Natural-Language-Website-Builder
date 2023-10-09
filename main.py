from pywebio.input import *
from pywebio.output import *
from pywebio import start_server, config
from utils.style import style, tabs_style
from utils.sections import *
from utils.prompts import prompts
from utils.keymap import get_section, function_map, function_types, make_tableList
from random import randint
from utils.nlp import nlp
import json


def makeSections():
    for i in ["header","body","footer"]:
        with use_scope(i):
            pass

def loadwebapp(webapp_builderList):
    json_string = json.dumps({"list":webapp_builderList})
    with open('your_webappbuilder.json','w') as json_file:
        json_file.write(json_string)

def makewebapp(webapp_builderList):
    makeSections()
    #section, tag, function_pyweb, content
    for webelem in webapp_builderList:
        with use_scope(webelem[0]):
            if webelem[1] in function_types['display']:
                function_map[webelem[1]][0](webelem[3]).style(function_map[webelem[1]][1])
            elif webelem[1] in function_types['dim']:
                function_map[webelem[1]][0](function_map[webelem[1]][1](webelem[3])[0],width=function_map[webelem[1]][1](webelem[3])[1],height=function_map[webelem[1]][1](webelem[3])[2]).style(function_map[webelem[1]][2])
            else:
                function_map[webelem[1]][0](function_map[webelem[1]][1](webelem[3])).style(function_map[webelem[1]][2])

# put your title and description here:
config(title='Dynamic WebApp Builder',description='build websites by typing english',theme='dark',css_style=style)

def main():
    makeSections()
    webapp_builderList = []
    with open('your_webappbuilder.json','r') as json_file:
        json_data = json.load(json_file)
    webapp_builderList = json_data["list"]
    print(webapp_builderList,type(webapp_builderList))
    makewebapp(webapp_builderList)
    while True:
        i = randint(0,len(prompts)-1)
        key = input(help_text="Hint: "+prompts[i],type=TEXT)
        if key in ['end','exit']:
            loadwebapp(webapp_builderList)
            break
        elif key in ['restart','clear']:
            clear()
            loadwebapp([])
            continue
        print("key:",key)
        section = get_section(key)
        print(f"section: {section}")
        key = key.replace(section,'',1)
        # dictionary matching type of content with content
        richContent_dict = nlp(key)
        try:
            if len(richContent_dict) != 0:
                print("retrieved dictionary:",richContent_dict)
                with use_scope(section):
                    for i in richContent_dict:
                        if i in function_types['display']:
                            function_map[i][0](richContent_dict[i][1:-1]).style(function_map[i][1])
                            webapp_builderList += [[section,i,function_map[i][0].__name__,richContent_dict[i][1:-1]]]
                        elif i in function_types['dim']:
                            function_map[i][0](function_map[i][1](richContent_dict[i][1:-1])[0],width=function_map[i][1](richContent_dict[i][1:-1])[1],height=function_map[i][1](richContent_dict[i][1:-1])[2]).style(function_map[i][2])
                            webapp_builderList += [[section,i,function_map[i][0].__name__,richContent_dict[i][1:-1]]]
                        else:
                            function_map[i][0](function_map[i][1](richContent_dict[i][1:-1])).style(function_map[i][2])
                            webapp_builderList += [[section,i,function_map[i][0].__name__,richContent_dict[i][1:-1]]]
            else:
                toast('Error1: please change your prompt and try again')
        except Exception as e:
            toast(f'Error2: {e}')
            print(f'Error2: {e}')

    
if __name__ == '__main__':
    start_server(main,remote_access=True,debug=True)
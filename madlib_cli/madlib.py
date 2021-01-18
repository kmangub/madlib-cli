print("""
*****************************************************************
**                                                             ** 
**   Hello and welcome! We will ask you to type in specific    **
**                 names, words, and numbers.                  **
**      Once you type your results, please press enter.        **
**      Read carefully or else it will not work correctly!     **
**                                                             **
*****************************************************************
""")

import re

def read_template(x):
    with open(x) as text:
        madlib = text.read()
        return madlib

def parse_template(txt):
    new = tuple(re.findall(r"\{([A-Za-z0-9_'\s1-]+)\}", txt, re.IGNORECASE))
    length = len(new)
    for i in range(0, length):
        if( i == 0 ):
            print(i)
            new_txt = txt.replace(new[i],"")
        else:
            new_txt = new_txt.replace(new[i],"")
    return new_txt, new

def user_prompt(words):
    print('Please enter in the specified word for the prompts')
    responses = []
    for word in words:
        responses.append(input(f'Please enter {word}'))
    return (responses)

def merge(strip, res):
    length = len(res)
    for i in range(0, length):
        if(i == 0):
            story = strip.replace('{}', res[i],1)
        else:
            story = story.replace('{}', res[i],1)
    return story

def game():
    stripped, prompts = parse_template(read_template('assets/madlib.txt'))

    res = user_prompt(prompts)
    fout = open("assets/libstory.txt", 'w')
    fout.write(merge(stripped, res))

    fout.close()
    print(merge(stripped, res))

game()

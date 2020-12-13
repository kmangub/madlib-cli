import re

# adjective1 = input('Please enter an adjective ')
# adjective2 = input('Please enter another adjective ')
# first_name1 = input('Please enter your first name ')
# past_tense_verb = input('Enter a past tense verb ')
# first_name2 = input("Please enter a friend's first name ")
# adjective3 = input('Enter an adjective ')
# adjective4 = input('Enter another adjective ')
# noun1 = input('Enter a plural noun ')
# animal1 = input('Enter a large animal ')
# animal2 = input('Enter a small animal ')
# girl_name = input("Enter a Girl's Name ")
# adjective5 = input('Enter yet another adjective ')
# noun2 = input('Enter a plural noun ')
# adjective6 = input('Sorry to ask you but could you give another adjective ')
# noun3 = input('Enter a plural noun ')
# number1 = input('Choose a number between 1 and 50 ')
# number2 = input('Choose another number ')
# noun4 = input('Enter a plural noun ')
# number3 = input('Choose another number ')
# noun5 = input('Enter a plural noun ')


# with open ('../assets/madlib.txt', 'r') as madlib:
#     word = madlib.read()

#     word = word.replace('{Adjective}', adjective1, 1)
#     word = word.replace('{Adjective}', adjective2, 1)
#     word = word.replace('{A First Name}', first_name1, 1)
#     word = word.replace('{Past Tense Verb}', past_tense_verb)
#     word = word.replace('{A First Name}', first_name2, 1)
#     word = word.replace('{Adjective}', adjective3, 1)
#     word = word.replace('{Adjective}', adjective4, 1)        
#     word = word.replace('{Plural Noun}', noun1, 1)
#     word = word.replace('{Large Animal}', animal1)    
#     word = word.replace('{Small Animal}', animal2)
#     word = word.replace("{A Girl's Name}", girl_name)
#     word = word.replace('{Adjective}', adjective5, 1)
#     word = word.replace('{Plural Noun}', noun2, 1)
#     word = word.replace('{Adjective}', adjective6, 1)
#     word = word.replace('{Plural Noun}', noun3, 1)
#     word = word.replace('{Number 1-50}', number1)
#     word = word.replace("{First Name's}", f"{first_name2}'s")
#     word = word.replace('{Number}', number2, 1)
#     word = word.replace('{Plural Noun}', noun4, 1)
#     word = word.replace('{Number}', number3, 1)
#     word = word.replace('{Plural Noun}', noun5, 1)


#     print(word)

def read_template(x):
    with open(x) as text:
        text_read = text.read()
        return text_read

def parse_template(txt):
    result = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", txt))
    new_txt = txt.replace(result[0], "")
    new_txt = new_txt.replace(result[2], "")
    return(new_txt, result)

def merge(one, two):
    new_str = one.format(two[0], two[1], two[2])
    print(new_str)
    return new_str




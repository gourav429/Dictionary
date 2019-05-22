import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn =  input('Did you mean %s instead? Enter Y if yes, or N if No ' %get_close_matches(word,data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'N' or yn =='n':
            return 'The word doesnn\'t exist. Please double check it.'
        else:
            return 'We didn\'t understand your query'
    else:
        print('This word doesn\'t exist please double check it')

word = input("Enter Word: ")

output = translate(word)

if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)


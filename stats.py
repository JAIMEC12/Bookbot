def count_words(text):
    return len(text.split()) #DIVIDE THE TEXT IN A LIST OF WORDS SEPARATEB BY SPACE. 
#LATER WE USE LEN IN ORDER TO KNOW THE SIZE OF THE LIST, THEREFORE, THE QUANTITY OF THE WORDS IN THE TEXt


def sort_on(dict):
    return dict["num"] #RETURN THE VALUE OF THE NUM KEY, THE NUMBER BECAUSE THE LIST WILL BE SORTED BY NUMBER OF TIMES THE CHARACTER APPEARED FROM THE GREATEST TO THE LEAST


#FUNCTION TO CREATE A SORTED LIST OF DICTIONARIES WITH TWO KEYS, CHAR AND NUM
def sort_dictionary(dictionary):
    new_list = []
    new_dictionary = {}
    for k in dictionary:
        #HERE WE ARE CREATING A DICTIONARY WHICH LATER WILL BE STORED IN THE LIST AND RESET
        new_dictionary["char"]= k #NOW THE KEY OF THE PREVIOUS DICTIONARY WILL BE THE VALUE OF THE KEY CHAR
        new_dictionary["num"]= dictionary[k] #THE SAME, BUT NOW WITH ITS VALUE WHICH WILL BE PAIRED WITH THE KEY NUM IN THE NEW DICTIONARY 
        new_list.append(new_dictionary)
        new_dictionary={}
    new_list.sort(reverse=True, key=sort_on) #LIST SORTED
    return new_list 

#FUNCTION TO CREATE A DICTIONARY TO STORE THE CHARACTERS AND THEIR TOTAL TIMES
def count_characters(text):
    empty_dictiony={} 
    for character in text:
        if character.lower() not in empty_dictiony:
            empty_dictiony[character.lower()] = 1
        else:
            empty_dictiony[character.lower()] = empty_dictiony[character.lower()] + 1
    return sort_dictionary(empty_dictiony) #RETURN A SORTED LIST WHICH HAS THE VALUES PREVIOUSLY STORED IN A SINGLE DICTIONARY WITH ONE KEY


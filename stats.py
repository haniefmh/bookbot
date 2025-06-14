def count_words(book_text):
    list_text = book_text.split()
    return(len(list_text))

def count_characters(book_text):
    dict_character = {}

    for character in book_text.lower():
        if character.isalpha():
            if character not in dict_character:
                dict_character[character] = 1
            else:
                dict_character[character] += 1
    
    return dict_character

def sort_char(dict_char):
    new_list = []
    for key in dict_char:
        char_obj = {"char": key, "num": dict_char[key]}
        new_list.append(char_obj)

    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict["num"]
def get_text_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
    
def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_characters(text):
    dict_chars = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in dict_chars:
                dict_chars[char] += 1
            else:
                dict_chars[char] = 1
    return dict_chars

def sort_by_count(dict_chars):
    dict_list = []
    for char, count in dict_chars.items():
        dict_list.append({
            'char': char,
            'count': count
        })
    dict_list.sort(key=lambda x: x['count'], reverse=True)
    return dict_list
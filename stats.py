def get_num_words(text):
    num_of_words = len(text.split())
    return num_of_words


def get_num_characters(text):
    text = text.lower()

    num_of_chracters = {}

    for char in text:
        if char in num_of_chracters:
            num_of_chracters[char] += 1
        else:
            num_of_chracters[char] = 1

    return num_of_chracters

def sort_dict(char_dict):
    list = []
    for key in char_dict:
        tempdict = {"char": key, "num":char_dict[key]}
        list.append(tempdict)

    sorted_list = sorted(list, key=lambda item: item['num'], reverse=True)
    
    return sorted_list
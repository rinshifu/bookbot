#def count():
#    with open("books/frankenstein.txt") as f:
#        book_contents = f.read()
#        total_words = len(book_contents.split())
#        print(total_words)

#count()

def book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    characters = {}
    lower_case_characters = text.lower()
    for i in lower_case_characters:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
    return(characters)

def sort_on(dict):
    return dict["count"]

def sort_only_alphabet(character):
    only_alphabet_list = []
    for char, count in character.items():
        char_data = {"char": char, "count": count}
        if char.isalpha():
            only_alphabet_list.append(char_data)
    return only_alphabet_list 

def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    final_count = character_count(text)
#   print(final_count)

    char_list = sort_only_alphabet(final_count)
    char_list.sort(reverse=True, key=sort_on)
    print(char_list)
main()
def main():
    path = "books/frankenstein.txt"
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(get_text(path))} words found in the document")
    counted_chars = count_chars(get_text(path))
    list_of_chars = []
    for key, cont in counted_chars.items():
        if key.isalpha():
            list_of_chars.append(key)

    for i in sorted(list_of_chars):
        print(f"The '{i}' character was found {counted_chars[i]} times")


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = len(text.split())
    return words

def count_chars(text):
    list_of_chars = {}
    for i in text:
        lowered = i.lower()
        if lowered in list_of_chars:
            list_of_chars[lowered] += 1
        else:
            list_of_chars[lowered] = 1
    return list_of_chars


main()

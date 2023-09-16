def main():
    word_counter()
    letter_counter(lazy_function()) 

def file_printer():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        print(file_contents)

def word_counter():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        print(len(file_contents))

def letter_counter(yyy):
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read().lower()
        for i in yyy:
            number = file_contents.count(i)
            print(f"The letter '{i}' character was found {number} times")

def lazy_function():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read().lower()
        letters = []
        for i in file_contents:
            if (i.isalpha()) and (i not in letters):
                letters.append(i)

    return letters


if __name__ == '__main__':
    main()
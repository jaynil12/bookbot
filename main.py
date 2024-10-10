def main():
    with open("books/frankenstein.txt") as file:
        contents = file.read()
        words = contents.split()
        count_list = count_char(contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document"+ "\n")
        
        for char, count in count_list:
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")
        
def count_char(content: str) -> int:
    content = content.lower()
    count_dict = {}
    for i in range(len(content)):
        char = content[i]
        if char.isalpha():
            count_dict[char] = 1 + count_dict.get(char, 0)
    countChar = list(count_dict.items())
    countChar.sort(reverse=True, key=lambda x: x[1])
    return countChar


main()

from collections import Counter
import os

def punctuation_removal(read_file):
    pun = (".", ",", '"')
    for y in pun:
        read_file = read_file.replace(y, "")
    return read_file

enter_name = input("Enter name of the file:")

path = "D:\pythonProject\Hillel_07_2022.git\lesson_12\Homework"
dirs = os.listdir(path)
if enter_name in dirs:
    with open(enter_name, "r") as file:
        read_file = file.read()
        print(read_file)

    allowed_options = "[read_last_10_lines/read_first_10_lines/read_all_file/find_longest_word/lines_number/words_frequency/exit]"

    while True:
        ask_to_user = input(f"What to do with the file?{allowed_options}:")

        if ask_to_user == "read_last_10_lines":
            with open(enter_name, "r") as file:
                lines = file.readlines()
                print(lines[-10:])

        elif ask_to_user == "read_first_10_lines":
            with open(enter_name, "r") as file:
                lines = file.readlines()
                print(lines[:10])

        elif ask_to_user == "read_all_file":
            with open(enter_name, "r") as file:
                read_file = file.read()
                print(read_file)

        elif ask_to_user == "find_longest_word":
            with open(enter_name, "r") as file:
                read_file = file.read()

                new_file = punctuation_removal(read_file)

                longest_word = max(new_file.split(), key=len)
                print(f"The longest word is: {longest_word}")

        elif ask_to_user == "lines_number":
            with open(enter_name, "r") as file:
                lines = file.readlines()
                print(len(lines))

        elif ask_to_user == "words_frequency":
            with open(enter_name, "r") as file:
                read_file = file.read()

                new_file = punctuation_removal(read_file)

                words_frequency = Counter(new_file.split())
                print(words_frequency)

        elif ask_to_user == "exit":
            print("Exiting...")
            break

        else:
            print(f"Please use allowed options! {allowed_options}")

else:
    print("File does not exist")
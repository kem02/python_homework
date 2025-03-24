# Task 1
def hello():
    return "Hello!"

# print(hello())



# Task 2
def greet(name):
    return f"Hello, {name}!"

# print(greet("John"))



# Task 3
def calc(a, b, operator="multiply"):
    try:
        match operator:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return int(a / b)
            case "power":
                return a**b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


# print(calc(2, 0, "divide"))


# Task 4
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."


# print(data_type_conversion("hello", "float"))



# Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        match average:
            case _ if average >= 90:
                return "A"
            case _ if 80 <= average <= 89:
                return "B"
            case _ if 70 <= average <= 79:
                return "C"
            case _ if 60 <= average <= 69:
                return "D"
            case _ if average < 60:
                return "F"
    except TypeError:
        return "Invalid data was provided."
    # print(average)


# print(grade(90, 70, 80))


# Task 6
def repeat(string, count):
    result = ""
    for i in range(count):
        result += f"{string}"
    return result


# print(repeat("up,", 4))



# Task 7
def student_scores(position, **kwargs):
    match position:
        case "best":
            highest_score = max(kwargs.values())
            for key, value in kwargs.items():
                if value == highest_score:
                    return key

            # 2nd Solution:
            # highest_score = int()
            # student = ''
            # for key, value in kwargs.items():

            #     if value > highest:
            #         highest_score = value
            #         student = key
            # return student

        case "mean":
            return sum(kwargs.values()) / len(kwargs)


# print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))



# Task 8
def titleize(text):

    split_text = text.split()

    for i, word in enumerate(split_text):
        if (
            i == 0
            or i == len(split_text) - 1
            or (word not in ["a", "on", "an", "the", "of", "and", "is", "in"])
        ):
            split_text[i] = word.capitalize()

    return " ".join(split_text)

    # 2nd Solution:
    # for i , word in enumerate(split_text):
    #     if i == 0:
    #         split_text[i] = word.capitalize()
    #     if 0 < i < len(split_text) - 1:
    #         if word in ["a", "on", "an", "the", "of", "and", "is", "in"]:
    #             continue
    #     if i == len(split_text) - 1:
    #         split_text[i] = word.capitalize()
    #     split_text[i] = word.capitalize()
    # return ' '.join(split_text)


# print(titleize("welcome gderger the jungle"))



# Task 9
def hangman(secret, guess):

    secret_list = list(secret)
    guess_list = list(guess)
    new_list = []

    for word in secret_list:
        if word in guess_list:
            new_list.append(word)
        else:
            new_list.append("_")

    # 2nd Solution:
    # for i , secret_letter in enumerate(secret_list):
    #     found_letter = '_'
    #     for j, guess_letter in enumerate(guess_list):
    #         if guess_letter == secret_letter:
    #             print(f"I found a letter {guess_letter} at index:{i}. {secret_letter} ")
    #             found_letter = guess_letter

    #     secret_list[i] = found_letter

    return "".join(new_list)


# print(hangman("difficulty", "ic"))



# Task 10
# This function can also take jumbled gibberish like pig_latin("dryfhq") and it will still check the word.
def pig_latin(sentence):

    sentence_split = sentence.split()
    new_list = []
    vowels = "aeiou"

    # Helper function
    def find_first_vowel(word_list, vowels):
        for i, letter in enumerate(word_list):
            if letter in vowels:
                return i
        return len(word_list)

    # Loop through list list of word/s
    for word in sentence_split:
        word_list = list(word)

        # If first letter starts with a vowel, add "ay" ending
        if word_list[0] in vowels:
            add_ending = word + "ay"
            new_list.append(add_ending)
        else:
            vowel_index = int()
            # Checks to see if there is a letter "q" in the current word iteration.
            # If not then search for the first occurance of a vowel in the current word iteration
            if "q" in word_list:
                q_index = word_list.index("q")
                # Checks to see if there is a "u" letter after the "q" and that it's within range of word_list length.
                # If there is then get the index of the letter next to "qu" as this needs to be moved together to the end of the current word.

                if (q_index + 1 < len(word_list) - 1) and word_list[q_index + 1] == "u":
                    vowel_index = q_index + 2
                # If only letter "q" if found, the continue searching for the index of first occurance of a vowel in the current word iteration.
                else:
                    vowel_index = find_first_vowel(word_list, vowels)

            # If only letter "q" is found, then search for the index of first occurance of a vowel.
            else:
                vowel_index = find_first_vowel(word_list, vowels)

            # Once we have the index of the first occuring vowel, we divide it into two lists, add the first half to the end of the second half,
            # then add a "ay" at the end of the list.

            first_letters = word_list[0:vowel_index]
            remainder_letters = word_list[vowel_index:]
            remainder_letters.extend(first_letters)
            remainder_letters.append("ay")
            new_list.append("".join(remainder_letters))

    # Finally we join the list together to form the word/sentence.
    return " ".join(new_list)


# print(pig_latin("the quick brown fox"))

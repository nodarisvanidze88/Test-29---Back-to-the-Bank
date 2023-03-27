import random as rd                                                                     # import random modul

def textToMoney(txt):                                                                   # function which checks the text, returns money value or stop value
    a = txt.lower().strip().split()                                                         # format text and split to list by words
    b = list(txt.lower().strip())                                                           # format text and split to list by characters
    if a[0] == "hello":                                                                     # check if first word is "Hello"
        return 0
    elif b[0] == "h":                                                                       # check if first character is "h"
        return 20
    elif a[0] != "hello" and b[0] != "h" and a[0] != "stop":                                # check both upper cases and exclude stop case
        return 100
    elif a[0] == "stop":                                                                    # initiate loop stop
        return "stop"

def main():
    input("Hi ")                                                                             # just first hi
    money = 0                                                                                # initiate money counter
    answers = [                                                                              # create question list
            "What did you say? ",
            "I think you told hello, but you always can stop it. ",
            "Do you need money? ",
            "Congratulation you got a money, just say stop. ",
            "Are you OK? I don't think so, do you whant stop it? just say stop. ",
            "How can I help you? "
            ]
    x = len(answers)-1                                                                       # get question list length
    while True:                                                                              # initiate infinity loop
        randNumber = rd.randint(0, x)                                                        # get random question number
        text = input(answers[randNumber])                                                    # ask with rendom question
        value = textToMoney(text)                                                            # get mony increase value or initiate stop
        if value != "stop":                                                                  # check if there is not stop
            money = money + value                                                            # sum money
            print("$ " + str(money))                                                         # print sum money value
        elif value == "stop":                                                                # check stop value
            print("You are good guy")                                                        # give last message
            break                                                                            # stop infinity loop

if __name__ == "__main__":
    main()

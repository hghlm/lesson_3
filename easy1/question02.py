def ends_with_exclamation(string):
    # length = len(string)
    
    # if string[length-1] == "!":
    #     print('True')
    # else:
    #     print('False')
    if string.endswith("!"):
        print('True')
    else:
        print('False')
    
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

ends_with_exclamation(str1)
ends_with_exclamation(str2)
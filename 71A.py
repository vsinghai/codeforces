def too_long():
    lines = int(input())
    
    for i in range(lines):
        word = str(input())
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[len(word)-1])
        else:
            print(word)
    

too_long()

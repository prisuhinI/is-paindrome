def is_palindrome():
    text = input('Write the word you want to check: ')
    if len(text) % 2 == 0:
        if text[:int(len(text) / 2)] == text[int(len(text) / 2): ]:
            print('Is palindrome')
        else:
            print('Is not palindrome')
    else:
        center = int(len(text) - 1.5)
        if text[:center - 1] == text[center:]:
            print('Is palindrome')
        else:
            print('Is not palindrome')
        
    
is_palindrome()
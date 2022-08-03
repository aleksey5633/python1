count_letter = ['python', 'c++', 'c', 'scala', 'java']
symb = []
for word in count_letter:
    for letter in word:
        if letter == 'c':
            letter += letter
            symb.append(letter)
            
print('summa s: ', len(symb))
import re 
#This code create an acronym for the word you entered.
i = 1 
while i<2:

    print('What is the acronym? Please enter the sentence ')
    acro = input('Please type the sentence')
    acro = re.sub(r'[.,;?!]', '', acro)#first i need clean the string using re function 
    words = re.split(r'\s', acro) #now divided by words
    character = ''

    for word in words:
        if word:  # check if the word is not empty
            character += word[0]
            #

    print("This is the acroym for you sentence:",character.upper())  

    print("Do you want to do another sentence?" )
    aux = int(input("Press 1: Yes,  2: No"))#if you want to do another word 

    if aux >=2: 
        i=3
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    print(names_list)
    names_list_final = []
    for name in names_list:
        new_name = name.strip(",\n")
        names_list_final.append(new_name)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names_list_final:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def create_letter(name,template:str):
    letter = template
    letter = letter.replace("[name]",name)
    return letter

with open("Day 23\\Mail Merge Project Start\\Input\\Names\\invited_names.txt",'r') as names:
    invited_names = names.readlines()

with open("Day 23\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt",'r') as letter:
    template = letter.read()

for name in invited_names:
    name = name.strip()
    letter = create_letter(name,template)
    with open(f'Day 23\\Mail Merge Project Start\Output\\ReadyToSend\\{name}.txt','w') as file:
        file.write(letter)



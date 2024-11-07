#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"Day24_FilesDirectoriesPaths\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    invited_names = [name.strip("\n") for name in names.readlines()]
    # print(invited_names)

for name in invited_names:
    with open(r"Day24_FilesDirectoriesPaths\Mail Merge Project Start\Input\Letters\starting_letter.txt") as template:
        base_letter = template.read().replace("[name]",name)
        with open(r"Day24_FilesDirectoriesPaths\Mail Merge Project Start\Output\ReadyToSend\{subject}_invitation.txt".format(subject=name),mode="w") as invitation_letter:
            invitation_letter.write(base_letter)
    print(f"{name}'s invitation letter DONE")

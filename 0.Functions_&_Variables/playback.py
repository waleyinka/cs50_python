# PLAYBACK SPEED

# In a file called playback.py, implement a program in Python that prompts the user for input and
# then outputs that same input, replacing each space with ()... three periods).

text = input("Enter a sample text")
rep_text = text.replace(" " , "...")
print(rep_text)
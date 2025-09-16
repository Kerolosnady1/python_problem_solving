# Find The Missing Character:

get_character = str(input("Put Your Characters alphabetical Here: ").strip().lower())

alphabetical = "abcdefghijklmnopqrstuvwxyz"

missed_characters = None

for character in range(0, len(alphabetical)):

    if  get_character[character] != alphabetical[character]:
        missed_characters += alphabetical[character]

    elif get_character[character] == alphabetical[character]:
        pass

    else:
        


if missed_characters == 0:
    print("No Missed Characters.")

else:
    print(f"Your Missed Characters Are: {missed_characters}")


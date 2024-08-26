with open("Demo.txt", "r") as file:
    Content_lower = file.read()
content_lower = Content_lower.lower()

Character = {}
for character in content_lower:
    if character in Character:
        Character[character] += 1
    else:
        Character[character] = 1
for character, count in Character.items():
    print(f"{character} comes {count} times in Demo.txt file.")
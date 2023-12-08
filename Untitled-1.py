with open("D:\TEXT.txt", mode="rt", ) as file:
    text = file.read()

lines = text.split("\n")
line_counter = 0  

for line in lines:
    line_counter += 1  
    words = line.split()
    print(f"У рядку № {line_counter} {len(words)} слів та {len(line)} символів")
#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
for ascii_code in range(65, 91):
   
    filename = chr(ascii_code) + '.txt'
    
    with open(filename, 'w') as file:
        file.write(f"{filename}.")


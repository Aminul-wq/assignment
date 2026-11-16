with open ("info.txt" , "w") as file:
    file.write("Name: sohag \n")
    file.write("Age:20 \n")
    
with open("info.txt" , "r") as con:
    content = con.read()
    print(content)
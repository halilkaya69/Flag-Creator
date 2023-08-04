#step3
width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)
print(("#"*int(width/2)+"-"*int(width/2)+"\n")*int(height/2)+("-"*width+"\n")*int(height/2))

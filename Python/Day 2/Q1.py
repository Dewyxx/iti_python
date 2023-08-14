List=[]
String=input("Enter your sentence:" )
char=input("Enter your character to locate: ")
for i, ch in enumerate(String):
    if ch==char:
     List.append(i)
print(List)

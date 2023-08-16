import pandas as pd

def readfile(path, option="text"):
    if option == "text":
        with open(path, 'r') as file:
            return file.read()
    elif option == "excel":
        return pd.read_excel(path)
    

def writefile(path, content, option="text"):
    if option == "text":
        with open(path, 'w') as file:
            file.write(content)
    elif option == "excel":
        content.to_excel(path, index=False)
   




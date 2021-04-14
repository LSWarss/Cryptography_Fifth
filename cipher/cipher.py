import re


def cipher_text(path):
    f = open(path)
    text_string = f.read()
    chunksArray = [text_string[i: i + 200] for i in range(0, len(text_string), 200)]
    for i in range(len(chunksArray)): 
        if(i % 2 == 0): 
            chunksArray[i] = transposition_row(chunksArray[i])
        
    return chunksArray

def transposition_row(row : str): 
    assert type(row) == str
    return row[::-1]
    
    

def decipher_text(path):
    pass
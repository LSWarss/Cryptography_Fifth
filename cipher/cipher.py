import re
import random

def cipher_text(path):
    f = open(path)
    text_string = f.read()
    chunksArray = [text_string[i: i + 200] for i in range(0, len(text_string), 200)]
    for i in range(len(chunksArray)): 
        if(i % 2 == 0): 
            chunksArray[i] = transposition_row(chunksArray[i])
        if(i % 3 == 0):
            chunksArray[i] = transposition_column(chunksArray[i],3)
    
    print(  )
    return chunksArray

def transposition_row(row : str): 
    assert type(row) == str
    return row[::-1]

def transposition_column(row: str,transpostion_steps: int):
    assert type(row) == str
    column_number = random.randint(0, len(row))
    return row.replace(row[column_number], row[column_number+transpostion_steps]).replace(row[column_number+transpostion_steps], row[column_number]) if column_number + transpostion_steps < len(row) else row
    
    

def decipher_text(path):
    pass
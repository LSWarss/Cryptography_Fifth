import re
import random
import string
  
# A list containing all characters
all_letters= string.ascii_letters


def cipher_text(path,key):

    dict1 = {}

    """ 
    create a dictionary to store the substitution 
    for the given alphabet in the plain text 
    based on the key
    """
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i+key)%len(all_letters)]


    f = open(path)
    text_string = f.read()
    text_string = text_string.replace(" ", "")
    cipher_txt=[]
    # loop to generate ciphertext
    for char in text_string:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp =char
            cipher_txt.append(temp)
            
    cipher_txt= "".join(cipher_txt)

    chunksArray = [text_string[i: i + 200] for i in range(0, len(cipher_txt), 200)]
    for i in range(len(chunksArray)): 
        if(i % 2 == 0): 
            chunksArray[i] = transposition_row(chunksArray[i])
        if(i % 3 == 0):
            chunksArray[i] = transposition_column(chunksArray[i],3)
    
    save_ciphered_to_file(path,key,chunksArray)
    return chunksArray

def decipher_text(path,key):
    dict2 = {}     
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i-key)%(len(all_letters))]
        
    # loop to recover plain text
    decrypt_txt = []

    f = open(path)
    text_string = f.read()
    decipher_text = []
    
    for char in text_string:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)
    
    chunksArray = [text_string[i: i + 200] for i in range(0, len(decipher_text), 200)]
    for i in range(len(chunksArray)): 
        if(i % 2 == 0): 
            chunksArray[i] = transposition_row(chunksArray[i])
        if(i % 3 == 0):
            chunksArray[i] = detranspostion_column(chunksArray[i],3)

    return chunksArray

def save_ciphered_to_file(path,key, array):
    f=open(f'{path[:-4]}_ciphered_{key}.txt', 'w')
    for ele in array:
        f.write(ele+'\n')
    f.close()

def transposition_row(row : str): 
    assert type(row) == str
    return row[::-1]

def transposition_column(row: str,transpostion_steps: int):
    assert type(row) == str
    column_number = random.randint(0, len(row))
    return row.replace(row[column_number], row[column_number+transpostion_steps]).replace(row[column_number+transpostion_steps], row[column_number]) if column_number + transpostion_steps < len(row) else row

def detranspostion_column(row: str, transpostion_steps : int):
    assert type(row) == str
    column_number = random.randint(0, len(row))
    return row.replace(row[column_number+transpostion_steps],row[column_number]).replace( row[column_number],row[column_number+transpostion_steps]) if column_number + transpostion_steps < len(row) else row

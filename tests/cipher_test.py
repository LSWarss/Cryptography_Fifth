from cipher.cipher import cipher_text, transposition_row, transposition_column

test_string = "LAMPA"

def test_transpositon_row():
    assert transposition_row(test_string) == "APMAL"

def test_transposition_column():
    assert transposition_column(test_string,3)

def test_cipher():
    textArray = cipher_text("cipher_testing.txt", 4)
    assert isinstance(textArray, list)
    text = " ".join(str(x) for x in textArray)
    assert isinstance(text, str)
    assert open("cipher_testing_ciphered_4.txt")
    
    
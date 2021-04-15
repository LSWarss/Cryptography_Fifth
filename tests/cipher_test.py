from cipher.cipher import cipher_text, transposition_row, transposition_column

test_string = "LAMPA"

def test_transpositon_row():
    assert transposition_row(test_string) == "APMAL"

def test_transposition_column():
    assert transposition_column(test_string,3)
from cipher.cipher import cipher_text, transposition_row

test_string = "LAMPA"

def test_transpositon_row():
    assert transposition_row(test_string) == "APMAL"


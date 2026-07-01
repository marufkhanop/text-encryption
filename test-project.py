from project import generate_key, encrypt, dicrypt, original_siq

def test_generate_key():
    key = generate_key()
    assert len(key) == len(original_siq)

def test_encrypt():
    # A simple reversed key layout for testing matching logic
    test_key = original_siq[::-1]
    assert encrypt("a", test_key) == test_key[0]
    assert encrypt("$", test_key) == "$"

def test_dicrypt():
    test_key = original_siq[::-1]
    assert dicrypt(test_key[0], test_key) == "a"
    assert dicrypt("$", test_key) == "$"
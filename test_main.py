from main import clean_data

def test_clean_logic():
    sample_data = [{"name": " test USER ", "email": "TEST@sample.com"}]
    result = clean_data(sample_data)

    #Verificaciones (Assertions)
    assert result[0]["name"] == "Test user"
    assert result[0]["email"] == "test@sample.com"
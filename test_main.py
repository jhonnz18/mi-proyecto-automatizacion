from main import clean_data

def test_clean_logic():
    # Datos de prueba con espacios y mayúsculas desordenadas
    sample_data = [{"name": " test USER ", "email": "TEST@sample.com"}]
    result = clean_data(sample_data)

    # Verificaciones usando .iloc para acceder a las celdas de Pandas
    # "test USER" debe convertirse en "Test User" por el .title()
    assert result.iloc[0]["name"] == "Test User"
    assert result.iloc[0]["email"] == "test@sample.com"
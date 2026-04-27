import pandas as pd

def clean_data(data):
    """Limpia nombres y correos electrónicos usando Pandas."""
    df = pd.DataFrame(data)
    
    # Corregido: Usamos .str.strip() con punto, no con guion
    df['email'] = df['email'].str.strip().str.lower()
    df['name'] = df['name'].str.strip().str.title()
    
    return df

if __name__ == "__main__":
    raw_data = [
        {'name': '  Jhonnier zambrano  ', 'email': ' jhonnierzambrano@gmail.com '},
        {'name': '  danilo polo  ', 'email': ' danilopolo@epam.com '}
    ]
    
    cleaned_data = clean_data(raw_data)
    print("Datos limpios:\n", cleaned_data)
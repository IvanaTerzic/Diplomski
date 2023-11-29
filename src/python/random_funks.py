import sys
sys.path.append('../')
from modules import * 
from paths import *
from columns import *

""" color_function - takes dicitonary(which includes category as key and list of values for some category), df_pca dataframe which includes PCA components as columns and names of polutants in index  
 RETURN - pandas DataFrame with new column """

def color_function(dict_,df_pca):
    finish=[]
    keys = dict_.keys()

    for item in df_pca.index:
        for key in keys:
            if item in dict_[key]:
                finish.append(key)
    
    df_pca['col']=finish
    return df_pca


"""
extract_numeric_value - takes a string and searches for the first numeric value (either an integer or a float) within that string.

Parameters:
- text: A string from which the numeric value is to be extracted.

Returns:
- float: The first found numeric value within the provided string.
- None: If no numeric value is found in the provided string.

Notes:
- The function uses a regular expression to identify numeric values which can be integers or floats (e.g., "123", "456.78").
- If multiple numeric values are found, only the first one is returned.
"""
def extract_numeric_value(text):
    
    if pd.isna(text):  # Provjera za NaN vrijednosti
        return None
    pattern = r'(\d+(?:\.\d+)?)'  
    matches = re.findall(pattern, str(text))
    if matches:
        return float(matches[0])
    else:
        return None
    
    
def process_dataframe(df):
    """
    Obrada DataFrame objekta za pretvaranje tekstualnih ćelija u numeričke vrijednosti i uklanjanje kolona sa svim NaN vrijednostima.

    Parametri:
    - df: DataFrame koji želite obraditi.

    Povratna vrijednost:
    - new_df: Novi DataFrame sa numeričkim vrijednostima i uklonjenim kolonama koje su imale sve NaN vrijednosti.

    Napomene:
    - Funkcija koristi 'extract_numeric_value' za izvlačenje numeričkih vrijednosti iz tekstualnih ćelija.
    - Funkcija se primjenjuje samo na kolonama od treće pa nadalje (indeksirano od 2).
    """
    
    # Primjenjuje extract_numeric_value na svaku ćeliju u DataFrame-u, ali samo za kolone od treće nadalje
    new_df = df.iloc[:, 2:].applymap(extract_numeric_value)
    
    # Pretvara kolone u numeričke vrijednosti i uklanja kolone koje imaju sve NaN vrijednosti
    new_df = new_df.apply(pd.to_numeric, errors='coerce')
    new_df.dropna(axis=1, how='all', inplace=True)
    
    return new_df




def plot_boxplot(data, start_col_index, end_col_index=None, id_var_column='LOKACIJA'):
    """
    Funkcija za stvaranje boxplota iz odabranih kolona DataFrame-a.

    Parametri:
    - data: Ulazni DataFrame koji sadrži podatke.
    - start_col_index: Indeks početne kolone za vizualizaciju.
    - end_col_index: Indeks krajnje kolone za vizualizaciju (opcionalno).
    - id_var_column: Naziv kolone koja se koristi kao identifikator (default je 'LOKACIJA').

    Povratna vrijednost:
    - Nema povratne vrijednosti. Funkcija direktno prikazuje boxplot.
    """
    
    # Filtrira kolone iz ulaznog DataFrame-a koristeći iloc
    filtered_data = data.iloc[:, start_col_index:end_col_index]
    
    # Dodaje kolone za identifikaciju, u ovom slučaju 'LOKACIJA' i 'RIJEKA'
    filtered_data[id_var_column] = data[id_var_column]
    filtered_data['RIJEKA'] = data['RIJEKA']
    
    # Pretvara DataFrame u 'long' format koristeći funkciju `melt`
    df_melted = filtered_data.melt(id_vars=[id_var_column, 'RIJEKA'], var_name='Spoj', value_name='Koncentracija')
    
    # Kreira boxplot koristeći Plotly Express, sa dodatnim podacima o 'LOKACIJI' i 'RIJECI' kao hover informacijama
    fig = px.box(df_melted, x='Spoj', y='Koncentracija', hover_data=[id_var_column, 'RIJEKA'])
    
    # Postavlja dimenzije grafika (u pikselima)
    fig.update_layout(width=1000, height=400)
    
    # Prikazuje boxplot
    fig.show()



    

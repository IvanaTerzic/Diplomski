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
- String: If no numeric value is found in the provided string.

Notes:
- The function uses a regular expression to identify numeric values which can be integers or floats (e.g., "123", "456.78").
- If multiple numeric values are found, only the first one is returned.
"""

def extract_numeric_value(text):
    if pd.isna(text):  # Provjera za NaN vrijednosti
        return text
    pattern = r'(\d+(?:\.\d+)?)'  # Uzorak za pronalazak brojeva
    matches = re.findall(pattern, str(text))
    if matches:
        return float(matches[0])
    else:
        return text  # Vraća izvorni string ako nema broja

def extract_numeric_from_df(df):
    return df.apply(lambda x: x.map(extract_numeric_value))

    
    
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
    
def plot_boxplot_toks(data, start_col_index, end_col_index=None, id_var_column='LOKACIJA'):
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
    df_melted = filtered_data.melt(id_vars=[id_var_column, 'RIJEKA'], var_name='Spoj', value_name='TU_sed')
    
    # Kreira boxplot koristeći Plotly Express, sa dodatnim podacima o 'LOKACIJI' i 'RIJECI' kao hover informacijama
    fig = px.box(df_melted, x='Spoj', y='TU_sed', hover_data=[id_var_column, 'RIJEKA'])
    
    # Postavlja dimenzije grafika (u pikselima)
    fig.update_layout(width=1000, height=400)
    
    # Prikazuje boxplot
    fig.show()


def zamijeni_nazive_molekula(report_df):
    # Definiranje zamjena
    zamjene = {
        'Molecule 1': 'Flu', 'Molecule 2': 'Pir', 'Molecule 3': 'BaA', 'Molecule 4': 'Kri', 
        'Molecule 5': 'BjF', 'Molecule 6': 'BbF', 'Molecule 7': 'BkF', 'Molecule 8': 'BaP',
        'Molecule 9': 'DahA', 'Molecule 10': 'BghiP', 'Molecule 11': 'IP', 'Molecule 12': 'HCB', 
        'Molecule 13': 'α-HCH', 'Molecule 14': 'β-HCH', 'Molecule 15': 'γ-HCH',
        'Molecule 16': 'DDE', 'Molecule 17': 'DDD', 'Molecule 18': 'DDT', 'Molecule 19': 'PCB-28', 
        'Molecule 20': 'PCB-52', 'Molecule 21': 'PCB-101', 'Molecule 22': 'PCB-118',
        'Molecule 23': 'PCB-153', 'Molecule 24': 'PCB-138', 'Molecule 25': 'PCB-180', 
        'Molecule 26': 'PCB-74', 'Molecule 27': 'PCB-60', 'Molecule 28': 'PCB-123',
        'Molecule 29': 'PCB-114', 'Molecule 30': 'PCB-105', 'Molecule 31': 'PCB-167', 
        'Molecule 32': 'PCB-156', 'Molecule 33': 'PCB-157', 'Molecule 34': 'PCB-170',
        'Molecule 35': 'PCB-189'
    }

    # Provjera postojanja i zamjena identifikatora za 'Id'
    if 'Id' in report_df.columns:
        report_df['Id'] = report_df['Id'].replace(zamjene)

    # Provjera postojanja i zamjena identifikatora za 'tId'
    if 'tId' in report_df.columns:
        report_df['tId'] = report_df['tId'].replace(zamjene)
    
    return report_df

def dodaj_nazive_lokacija_i_rijeka(data, index_lokacija, index_rijeka):
    naziv_lokacije = data['LOKACIJA'].iloc[index_lokacija]
    naziv_rijeka = data['RIJEKA'].iloc[index_rijeka]
    return f"{naziv_lokacije} - {naziv_rijeka}"



def racunaj_TU_sed(data, report, report_logP, lc50_column_index):
    
    kols=PAH_kol+OCP_kol+PCB_kol
    
    # Korak 1: Izračunaj Koc
    logP=report_logP['logP_median'].values
    log_Koc = 1.03 * logP - 0.61
    Koc = np.power(10, log_Koc)

    # Korak 2: Izračunaj Kp
    TOC = data['TOC(%)'] / 100
    Kp = np.outer(Koc, TOC)

    # Korak 3: Učitaj LC50 vrijednosti
    LC50 = report.iloc[:, lc50_column_index].values
    LC50_expanded = LC50[:, np.newaxis]
    LC50_broadcasted = np.tile(LC50_expanded, (1, len(TOC)))

    # Korak 4: Izračunaj TU
    konc_array = data.loc[:, kols].values
    TU_sed = konc_array / (Kp.T * LC50_broadcasted.T * 10**6)
              
    return TU_sed



def racunaj_TU_site_log10(data, report, report_logP, lc50_column_index):
    
    kols=PAH_kol+OCP_kol+PCB_kol
    
    # Korak 1: Izračunaj Koc
    logP=report_logP['logP_median'].values
    log_Koc = 1.03 * logP - 0.61
    Koc = np.power(10, log_Koc)

    # Korak 2: Izračunaj Kp
    TOC = data['TOC(%)'] / 100
    Kp = np.outer(Koc, TOC)

    # Korak 3: Učitaj LC50 vrijednosti
    LC50 = report.iloc[:, lc50_column_index].values
    LC50_expanded = LC50[:, np.newaxis]
    LC50_broadcasted = np.tile(LC50_expanded, (1, len(TOC)))

    # Korak 4: Izračunaj TU
    konc_array = data.loc[:, kols].values
    TU_sed = konc_array / (Kp.T * LC50_broadcasted.T * 10**6)

    # Korak 5: Izračunaj TU_site_log10
    TU_sed_sum = np.sum(TU_sed, axis=1)
    TU_site_log10 = np.log10(TU_sed_sum)
        
    return TU_site_log10




    

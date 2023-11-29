import sys
sys.path.append('../../src')
from paths import *
from modules import *
from columns import *

"""map_f-Uzima dva DataFrame jedan se odnosi na report iz VEGA-QSAR, a drugi se odnosi na promatrane tvari/molekule i lokacije
output funkcije je heatmap

VAŽNO data i report bez NaN vrijednosti
"""

def map_f(data,report):
    
    TU=[]
    final_kol=PAH_kol+OCP_kol+PCB_kol
    
    for i in range(data.shape[0]):
        #ovo se da bolje napraviti da nade LC50_model te ukoliko postoji želja za vise 
        LC50_array = report.iloc[:,-1].values
        konc_array = data.loc[[i],final_kol].values
        rezultat = konc_array/LC50_array
        rezultat=rezultat.sum()
        TU.append(rezultat)
        
    data['TU']=TU

    # Stvorite praznu mapu
    mapa = folium.Map(location=[data['LAT'].mean(), data['LON'].mean()], zoom_start=10)

    # Pripremite podatke za HeatMap
    heat_data = [[row['LAT'], row['LON'], row['TU']] for index, row in data.iterrows()]

    # Dodajte HeatMap na kartu
    HeatMap(heat_data).add_to(mapa)

    for index, row in data.iterrows():
        lat = row['LAT']
        lon = row['LON']
        naziv_postaje = row['LOKACIJA']
        TU = round(row['TU'], 3)
        rijeka = row['RIJEKA']
        
        # Generirajte tekst za popup
        popup_text = f"<b>Rijeka:</b> {rijeka}<br><b>Naziv postaje:</b> {naziv_postaje}<br><b>TU:</b> {TU}"
            
        # Dodajte točku na kartu kao CircleMarker s popup tekstom
        folium.CircleMarker(location=[lat, lon], radius=3, color='blue', fill=True, fill_color='blue', popup=popup_text).add_to(mapa)

    # Prikazuje mapu
    mapa.save('../../data/ivana_karta_TU.html')
    
    return mapa
    
    


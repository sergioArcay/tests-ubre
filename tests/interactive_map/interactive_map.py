import folium,json
import pandas as pd

prov_geo = 'spain-provunces.json'
prov_occ = 'ocupados.csv'
'''
occ = pd.read_csv(prov_occ,converters={'Prov':str})
'''
m = folium.Map([41,1], zoom_start=6, )
'''
m.choropleth (
    geo_str=open(prov_geo).read(),
    data=occ,
    columns=['Prov', 'Occ'],
    key_on='feature.properties.cod_prov',
    fill_color='BuPu', fill_opacity=0.9, line_opacity=0.5,
    legend_name='Ocupados (miles de personas)'
)
'''
m.save('map_occ.html')
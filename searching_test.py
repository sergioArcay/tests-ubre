#from OSMPythonTools.api import Api
from OSMPythonTools.nominatim import Nominatim
nominatim = Nominatim()
from places import municipios
busqueda = input("Cadena de busqueda: ")
data = nominatim.query(busqueda).toJSON()

print(data)

print();print("MATCHES: " + str(len(data)));print()
for place in range(len(data)):
    print(str(data[place]["osm_type"]) + " - " + str(data[place]["osm_id"]))
    print(data[place]["display_name"])
    print()
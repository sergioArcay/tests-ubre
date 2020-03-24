from OSMPythonTools.nominatim import Nominatim

import random
import math

from places import establecimientos

class Usuario:

    def __init__(self, origen):
        self.__origen = origen
        self.__solicitudes = []

    def get_solicitudes(self):
        return self.__solicitudes

    def create_solicitud(self):
        if not self.__solicitudes:
            new_origen = self.__origen
        else:
            new_origen= self.__solicitudes[-1]["destino"]

        new_destino = random_destino(self.__origen)

        new_solicitud = {
            "origen" : new_origen,
            "destino" : new_destino
        }
        self.__solicitudes.append(new_solicitud)


def random_destino(origen):
    nominatim = Nominatim()
    establecimiento = establecimientos[random.randint(0,len(establecimientos)-1)]
    data = nominatim.query(str(establecimiento) + " " + "redondela" + " galicia").toJSON() # TODO cambiar "redondela" por municipio de origen
    destino = {"latitud": data[0]["lat"], "longitud": data[0]["lon"]}
    print("[Usuario random_destino] " + "establecimiento: " + str(establecimiento) + " , en Redondela , name: " + str(data[0]["display_name"]))
    #print(origen)
    return destino
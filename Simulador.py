import openrouteservice as ors
import mplleaflet as mplleaflet

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

import random

from Usuario import Usuario
from places import municipios
from places import establecimientos

class Simulador:

    def __init__(self, usuarios=None):
        self.__usuarios = []

    def create_usuarios(self, cantidad): # origen -> random(municipio)
        print("[Sim - create_usuarios] creando usuarios")
        for i in range (cantidad):
            ind = random.randint(0,len(municipios)-1)
            new_municipio_origen = list(municipios)[ind]
            # TODO establecer en punto al azar dentro del municipio
            new_usuario = Usuario(municipios[new_municipio_origen])
            print(municipios[new_municipio_origen])
            self.__usuarios.append(new_usuario)
            print("\t[Sim - create_usuarios] Usuario " + str(i) + " creado en " + str(new_municipio_origen))
        print()

    def create_una_solicitud_por_usuario(self):
        for usuario in self.__usuarios:
            usuario.create_solicitud()

    def imprimir_solicitudes(self):
        plt.figure(figsize=(8, 6))
        fig = plt.figure()
        for usuario in self.__usuarios:
            for solicitud in usuario.get_solicitudes():
                latitud_origen = solicitud["origen"]["latitud"]
                longitud_origen = solicitud["origen"]["longitud"]
                latitud_destino = solicitud["destino"]["latitud"]
                longitud_destino = solicitud["destino"]["longitud"]
                coordinates = [ [longitud_origen,latitud_origen], [longitud_destino,latitud_destino] ]
                self.create_route(coordinates)
        mplleaflet.show(fig=fig)

    def create_route(self, coordinates):
        ors_client = ors.Client(key='5b3ce3597851110001cf6248f3b059537e424e639a05afc159c35d77')
        route = ors_client.directions(
            coordinates=coordinates,
            profile='driving-car',
            format='geojson'
        )
        print ("[create_route] " + str(coordinates))
        route_points = route['features'][0]['geometry']['coordinates']
        plt.plot(route_points[0][0], route_points[0][1], 'ro', markersize=16) # Marca en punto de origen
        plt.plot(route_points[-1][0], route_points[-1][1], 'go', markersize=16) # Marca en punto de destino
        route_points.append(route_points[-1]) # Para que no haya problemas al final del siguiente for
        for p in range(len(route_points)-1): # Linea de union entre cada par de puntos consecutivos
            col=(1,0,0) # TODO cambiar el color para cada usuario
            trayectoria = mlines.Line2D([route_points[p+1][0], route_points[p][0]], [route_points[p+1][1], route_points[p][1]], color=col, linewidth=4)
            plt.gca().add_line(trayectoria)

simulador = Simulador()
simulador.create_usuarios(2)
simulador.create_una_solicitud_por_usuario()
simulador.imprimir_solicitudes()
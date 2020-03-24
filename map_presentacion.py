from OSMPythonTools.nominatim import Nominatim
import openrouteservice as ors
import mplleaflet as mplleaflet
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

nominatim = Nominatim()

def create_route(coordinates): # coordinates = [ [Lo,lo] , [Ld,ld] ]
    ors_client = ors.Client(key='5b3ce3597851110001cf6248f3b059537e424e639a05afc159c35d77')
    route = ors_client.directions(
        coordinates=coordinates,
        profile='driving-car',
        format='geojson'
    )
    route_points = route['features'][0]['geometry']['coordinates']
    return route_points

def draw_point(coordinates, color="green", marker='o', size=16, alpha=1):
    plt.plot(float(coordinates[0]), float(coordinates[1]), color=color, marker=marker, markersize=size, alpha=alpha) # Marca en punto escogido

def draw_route(route_points, color=(1,0,0), alpha=1):
    route_points.append(route_points[-1]) # Para que no haya problemas al final del siguiente for
    for p in range(len(route_points)-1): # Linea de union entre cada par de puntos consecutivos
        trayectoria = mlines.Line2D([route_points[p+1][0], route_points[p][0]], [route_points[p+1][1], route_points[p][1]], color=color, linewidth=4, alpha=alpha)
        plt.gca().add_line(trayectoria)

def search_for_point(search):
    global nominatim
    data = nominatim.query(search).toJSON()

    print(data)

    print();print("MATCHES: " + str(len(data)));print()
    for place in range(len(data)):
        print(str(data[place]["lon"]) + ", " + str(data[place]["lat"]))
        print(data[place]["display_name"])
        print()
    return [data[0]["lon"], data[0]["lat"]]

plt.figure(figsize=(8, 6))
fig = plt.figure()

Ao = search_for_point("fornelos de montes")
Ad = search_for_point("estacion redondela galicia")
Bo = search_for_point("a ermida borben galicia")
Bd = search_for_point("42.2760627, -8.6158682")

AoAd_route = create_route( [Ao, Ad] )
AoBo_route = create_route( [Ao, Bo] )
BoAd_route = create_route( [Bo, Ad] )
AdBd_route = create_route( [Ad, Bd] )

draw_point(Ao,      color="green", marker="o", alpha=1)
draw_point(Ad,      color="green", marker="s", alpha=1)

draw_point(Bo,      color="blue", marker="o", alpha=1)
draw_point(Bd,      color="blue", marker="s", alpha=1)

draw_route(AoAd_route, color=(1,0,1),  alpha=0)
draw_route(AoBo_route, color=(1,0,1),  alpha=1)
draw_route(BoAd_route, color=(1,0,1),  alpha=1)
draw_route(AdBd_route, color=(1,0,0),  alpha=0)

mplleaflet.show(fig=fig)
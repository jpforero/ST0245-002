import matplotlib.pyplot as plt
import pandas as pd
from shapely import wkt
import networkx as nx
import pydeck as pdk

#Profe intentamos hacer el codigo para las 3 rutas pero hay un problema que dibuja unicamente una, igual ahi dejo comentado lo demas
#___________________________________________________________________________________________________________________________________



# Recoge los datos de las calles con su riesgo de acoso
edges = pd.read_csv('https://raw.githubusercontent.com/jpforero/ST0245-002/master/codigo/calles_de_medellin_con_acoso.csv', sep=';')
myfile = pd.read_csv('https://raw.githubusercontent.com/jpforero/ST0245-002/master/codigo/calles_de_medellin_con_acoso.csv', sep=';')
listaAcoso = nx.from_pandas_edgelist(myfile,source='length', target='harassmentRisk', edge_attr=True)
myfile['harassmentRisk'].fillna(myfile['harassmentRisk'].mean(), inplace = True)
#print(myfile['length'], end="\n\n")
#print(myfile['harassmentRisk'], end="\n\n")
myfile['length'] *= myfile['harassmentRisk']
edges['length']=myfile['length']
#print(edges)

listaCalles = nx.from_pandas_edgelist(edges, source='origin', target='destination', edge_attr='length')
edges['geometry'] = edges['geometry'].apply(wkt.loads)
"""
# Recoge los datos de las calles con su riesgo de acoso de long y harass
edgesL = pd.read_csv('https://raw.githubusercontent.com/jpforero/ST0245-002/master/codigo/calles_de_medellin_con_acoso.csv', sep=';')
listaCallesL = nx.from_pandas_edgelist(edgesL, source='origin', target='destination', edge_attr='length')

edgesH = pd.read_csv('https://raw.githubusercontent.com/jpforero/ST0245-002/master/codigo/calles_de_medellin_con_acoso.csv', sep=';')
listaCallesH = nx.from_pandas_edgelist(edgesH, source='origin', target='destination', edge_attr='harassmentRisk')
edgesH['harassmentRisk'].fillna(edgesH['harassmentRisk'].mean(), inplace = True)

#_________________________________________________________________________________
"""

# Implementación con dijkstra para encontrar la ruta más corta

a = input('Ingrese la coordenada del origen >>> ')
b = input('Ingrese la coordenada del destino >>> ')
shortest_route = nx.dijkstra_path(listaCalles, source=a, target=b, weight='length')
"""
# Implementación con dijkstra para encontrar la ruta más corta de long y harass
shortest_routeL = nx.dijkstra_path(listaCallesL, source=a, target=b, weight='length')
shortest_routeH = nx.dijkstra_path(listaCallesH, source=a, target=b, weight='length')
print(shortest_route)
print(shortest_routeL)
print(shortest_routeH)
#_____________________________________________________
"""
#Pasar de String a Float

dataframe=pd.DataFrame(shortest_route,columns=['calles'])
dataframe['longitud']=dataframe['calles'].map(lambda x:x.split(',')[0])
dataframe['latitud']=dataframe['calles'].map(lambda x:x.split(',')[1])
del(dataframe['calles'])
dataframe=dataframe.replace('\(|\)','',regex=True).astype(float)
"""
#Pasar de String a Float de long y harass
dataframeL=pd.DataFrame(shortest_routeL,columns=['calles'])
dataframeL['longitud']=dataframeL['calles'].map(lambda x:x.split(',')[0])
dataframeL['latitud']=dataframeL['calles'].map(lambda x:x.split(',')[1])
del(dataframeL['calles'])
dataframeL=dataframeL.replace('\(|\)','',regex=True).astype(float)

dataframeH=pd.DataFrame(shortest_routeH,columns=['calles'])
dataframeH['longitud']=dataframeH['calles'].map(lambda x:x.split(',')[0])
dataframeH['latitud']=dataframeH['calles'].map(lambda x:x.split(',')[1])
del(dataframeH['calles'])
dataframeH=dataframeH.replace('\(|\)','',regex=True).astype(float)

#______________________________________________________________________
"""
#Enlistado
Listac=list(zip(dataframe.longitud,dataframe.latitud))
Matrizcalles=[Listac]
color=["#9D33FF"]
rutaLista=list(zip(Matrizcalles,color))
"""
#Enlistado de long y harass
ListaL=list(zip(dataframeL.longitud,dataframe.latitud))
MatrizcallesL=[ListaL]
color1=["#FFFFFF"]
rutaListaL=list(zip(Matrizcalles,color1))

ListaH=list(zip(dataframeH.longitud,dataframe.latitud))
MatrizcallesH=[ListaH]
color2=["#FA3CC3"]
rutaListaH=list(zip(Matrizcalles,color2))
#____________________________________________
"""
#Dataframe de la ruta

ruta=pd.DataFrame(rutaLista,columns=['Ruta','color'])
"""
#Dataframe de la ruta long y harass
rutaL=pd.DataFrame(rutaListaL,columns=['Ruta','color'])
rutaH=pd.DataFrame(rutaListaH,columns=['Ruta','color'])
#_______________________________________________________
"""
#doc de PathLayer
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


ruta["color"] = ruta["color"].apply(hex_to_rgb)


view_state = pdk.ViewState(latitude=6.217 , longitude=-75.567, zoom=10)

layer = pdk.Layer(
    type="PathLayer",
    data=ruta,
    pickable=True,
    get_color="color",
    width_scale=2,
    width_min_pixels=2,
    get_path="Ruta",
    get_width=5,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"})
r.to_html("path_layer.html")

#________________________________________________________
"""
rutaL["color"] = rutaL["color"].apply(hex_to_rgb)



layerL = pdk.Layer(
    type="PathLayer",
    data=rutaL,
    pickable=True,
    get_color="color",
    width_scale=2,
    width_min_pixels=2,
    get_path="Ruta",
    get_width=5,
)

L = pdk.Deck(layers=[layerL], initial_view_state=view_state, tooltip={"text": "{name}"})
L.to_html("path_layer.html")
#___________________________________________________________________________________________
rutaH["color"] = rutaH["color"].apply(hex_to_rgb)


"""
"""
layerH = pdk.Layer(
    type="PathLayer",
    data=rutaH,
    pickable=True,
    get_color="color",
    width_scale=2,
    width_min_pixels=2,
    get_path="Ruta",
    get_width=5,
)

H = pdk.Deck(layers=[layerH], initial_view_state=view_state, tooltip={"text": "{name}"})
H.to_html("path_layer.html")"""


from vector import *

class Object(object):
    
    def __init__(self, filename):

        self.lines = []

        with open(filename) as f: #Abriendo el archivo .obj.
            lines = f.read().splitlines() #Se leen las líneas, se hacen split y se guardan en la variable global lines.

        self.faces = [] #Lista para las caras del obj.
        self.vertices = [] #Lista para los vértices del obj.
        self.vts = [] #Lista para los vértices de textura del obj.
        
        for line in lines:

            if not line or line.startswith("#"): #Si hay una línea vacía o una línea que tenga #, se salta. 
                continue

            
            prefix, value = line.split(' ', 1) #Se hace split de la línea en dos partes, el prefijo y el valor.

            if prefix == 'v': #Si el prefijo es v, se agrega el valor a la lista de vértices.
                self.vertices.append(
                    list(
                        map(
                            float, value.strip().split(' ') #Se quitan los strings inválidos y los espacios. Luego se convierten a float.
                        )
                    )
                )                
                #print(vertices) #Debuggeo.
            if prefix == 'f': #Si el prefijo es f, se agrega el valor a la lista de caras.
                try: 
                    self.faces.append(
                        [
                            list(
                                map(int, face.strip().split('/') #Se quita el / y se convierte a entero.
                                )
                            ) 
                            for face in value.strip().split(' ') #Se quita el espacio.
                        ]
                    )
                except: #Aquí se quitan las caras que tienen doble /.
                    self.faces.append(
                        [
                            list(
                                map(int, face.strip().split('//') #Se quita el / y se convierte a entero.
                                )
                            ) 
                            for face in value.strip().split(' ') #Se quita el espacio.
                        ]
                    )

            if prefix == 'vt': #Si el prefijo es vt, se agrega el valor a la lista de vértices de textura.
                self.vts.append(
                    list(
                        map(
                            float, value.strip().split(' ') #Se quitan los strings inválidos y los espacios. Luego se convierten a float.
                        )
                    )
                )

#Función que transforma los vértices de la estructura de la imagen.
    def transform_vertex(self, vertex, scale, translate): 
        
      
        return V3(
                (vertex[0] * scale[0]) + translate[0], #X.
                (vertex[1] * scale[1]) + translate[1], #Y.
                (vertex[2] * scale[2]) + translate[2] #Z.
            )
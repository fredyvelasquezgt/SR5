from utilidades import *

class Texture: #Clase para la textura.
        
    def lectura(self, path): #Archivo que sirve para leer la textura.
        with open(path, 'rb') as image:
            image.seek(10) #Saltando algunos bytes. Estas sumas se pueden quitar y dejarlo como un número.
            header_size = struct.unpack("=l", image.read(4))[0] #El l es formato nativo.
            image.seek(18) #Saltando algunos bytes.
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size) #Quitando el header.
            self.pixels = [] #Lista de pixeles.
            for y in range(self.height):
                self.pixels.append([]) #Añadiendo una fila de pixeles.
                for x in range(self.width):
                    #Se lee de 1 en 1, porque el color usa 3 bytes.
                    b = ord(image.read(1)) #Leyendo el byte de b.
                    g = ord(image.read(1)) #Leyendo el byte de g.
                    r = ord(image.read(1)) #Leyendo el byte de r.

                    self.pixels[y].append(
                        color(r/255, g/255, b/255)
                    ) #Añadiendo el color a la lista de pixeles.


    def get_color(self, tx, ty): #Función que recibe dos coordenadas y que de el color en las coordenadas.
        
        x = int(tx * self.width) #Redondeando el valor de x.
        y = int(ty * self.height) #Redondeando el valor de y.

        return self.pixels[y][x] #Se devuelve el color de un pixel con una intensidad.

    def get_color_with_intensity(self, tx, ty, intensity): #Obteniendo el color con su intensidad.
        
        x = int(tx * self.width) #Redondeando el valor de x.
        y = int(ty * self.height) #Redondeando el valor de y.
        
       
        b = int(self.pixels[y][x][0] * intensity) #Obteniendo el valor de b.
        g = int(self.pixels[y][x][1] * intensity) #Obteniendo el valor de g.
        r = int(self.pixels[y][x][2] * intensity) #Obteniendo el valor de r.

        return color(r/255, g/255, b/255) #Se devuelve el color de un pixel con una intensidad.
    
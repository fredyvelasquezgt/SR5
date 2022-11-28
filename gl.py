
from Render import * 
from utilidades import *
from vector import *
from Obj import *
from textures import *

c1 = Render() 
c2 = Texture() 

def glInit(): 

    pass

def glCreateWindow(width, height): 
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)

    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Creando las dimensiones de la pantalla.

            c1.width = width #Ancho de la pantalla.
            c1.height = height #Alto de la pantalla.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.

    colorV = color(0.4, 0.8, 0.08) #Creando el color del viewport.

    #Verificando que las dimensiones del viewport sean múltiplos de 4.
    if width % 4 == 1 and height % 4 == 1:
        
        c1.colorViewPort = colorV #Se manda a hacer el color del viewport.

        c1.View(x, y, width, height) #Se manda a hacer el viewport.
    else: 
        print("Error")


def glClear(): #Se usará para que llene el mapa de bits con un solo color.   
    

    

    c1.framebuffer = [
                    [c1.colorFondo for x in range(c1.width)] #Llenando el framebuffer con el color que se le pasó en glClearColor.
                      for y in range(c1.height)
                    ] #Llenando el framebuffer con el color que se le pasó en glClearColor.

    c1.zBuffer = [
                    [-9999 for x in range(c1.width)] #Llenando el zBuffer con un valor muy pequeño.
                    for y in range(c1.height)
                ] #Llenando el zBuffer con un valor muy pequeño.
    
   

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
        
    #Verificando que los códigos de los colores no sean negativos.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1: #Verificando que los códigos de los colores no sean mayores a 255.
        print("Error")
    else: #Si todo está bien, entonces se crea el framebuffer con el color que se le pasa.
        
        
        colorPantalla = color(r, g, b) #Creando el color de la pantalla.
        
        c1.colorFondo = colorPantalla #Se manda a hacer el color de la pantalla.

       

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    
    if 0 < x < c1.width and 0 < y < c1.height: #Verificando que las coordenadas estén dentro del viewport.
        c1.Vertex(x, y) #Se manda a hacer el punto.

#Función que crea una línea entre dos puntos. Esta tiene que estar en el rango de 0 a 1.
def glLine(v1, v2):


    #Redondeo para que no haya problemas con los decimales.
    x0 = round(v1.x)
    y0 = round(v1.y)
    x1 = round(v2.x)
    y1 = round(v2.y)



    #Prueba.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

   


    steep = dy > dx #Verificando si la línea es vertical o horizontal.

    if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    
    if x0 > x1: #Si el punto 1 está a la derecha del punto 2, entonces se cambia el orden de los puntos.
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Calculando los nuevos cambios.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    offset = 0 #Offset de la línea.
    threshold = dx #Umbral de la línea.	
    y = y0 #Coordenada y de la línea.

    

    #Dibujando la línea.
    for x in range(x0, x1 + 1):
        
        offset += dy * 2 #Cambiando el offset.
        if offset >= threshold: #Si el offset es mayor o igual al umbral, entonces se cambia la coordenada y.
            y += 1 if y0 < y1 else -1
            threshold += 2 * dx

           
        if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
            #print("Coordenadas: ", x, y)
            glVertex(y, x)
        else: #Si la línea es horizontal, entonces se cambia el orden de los puntos.
           
            glVertex(x, y)


def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    
    #Convertir el valor de 0 a 1 de 0 a 255 y luego llamar al color.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1:
        print("Error")
    else:
        
        #print("Color antes de ser cambiado: ", c1.colorP)
        Color = color(r, g, b) #Se manda a hacer el color con las utilidades y se setea el color.
        #print("Color en gl: ", Color)
        c1.colorP = Color #Se setea el color del punto.

#Este método recibe ahora dos paths. Uno es para el obj y el otro es para el bmp.
def modelo(path1, path2, scale, translate): #Método para cargar un modelo 3D.
    
    r = Object(path1) #Llamando al método Object del archivo Obj.py.

    if path2: 
        #Método para hacer el ejemplo de Dennis.
        c2.lectura(path2) #Abriendo el bmp de la textura y procesando sus pixeles.

        c1.tpath = path2 #Se setea la textura.

        #print("Path de la textura: ", c1.tpath) #Debuggeo.

    #print("Textura: ", c1.tpath) #Debuggeo.

    #Recorriendo las caras del objeto y dibujando las líneas en el framebuffer.
    for face in r.faces: 
        #print(face) #Debuggeo.
        
        if len(face) == 4: #Validando que la cara tenga 4 vértices.
            
            if c1.tpath: #Si hay una textura, entonces se dibuja la cara con textura.
            
                #El array de caras es bidimensional en este código.
                f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                f2 = face[1][0] - 1 #Agarrando el índice 0.
                f3 = face[2][0] - 1 #Agarrando el índice 1.
                f4 = face[3][0] - 1 #Agarrando el índice 2.

                #Transformando los vértices.
                v1 = r.transform_vertex(r.vertices[f1], scale, translate)
                v2 = r.transform_vertex(r.vertices[f2], scale, translate)
                v3 = r.transform_vertex(r.vertices[f3], scale, translate)
                v4 = r.transform_vertex(r.vertices[f4], scale, translate)

                ft1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                ft2 = face[1][1] - 1 #Agarrando el índice 0.
                ft3 = face[2][1] - 1 #Agarrando el índice 1.
                ft4 = face[3][1] - 1 #Agarrando el índice 2.
                
                
                #Obteniendo los vértices de texuras.
                vt1 = V3(*r.vts[ft1])

                vt2 = V3(*r.vts[ft2])

                vt3 = V3(*r.vts[ft3])

                vt4 = V3(*r.vts[ft4])

             

                #Primer triángulo.

                #Vértices normales.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v2)
                c1.vertex_buffer_obj.append(v3)

                #Vértices de textura.
                c1.vertex_buffer_obj.append(vt1)
                c1.vertex_buffer_obj.append(vt2)
                c1.vertex_buffer_obj.append(vt3)

                #Segundo triángulo.
                
                #Vértices normales.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v3)
                c1.vertex_buffer_obj.append(v4)

                #Vértices de textura.
                c1.vertex_buffer_obj.append(vt1)
                c1.vertex_buffer_obj.append(vt3)
                c1.vertex_buffer_obj.append(vt4)


            
            else: #Si no hay textura, entonces se dibuja la cara sin textura.
                #El array de caras es bidimensional en este código.
                f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                f2 = face[1][0] - 1 #Agarrando el índice 0.
                f3 = face[2][0] - 1 #Agarrando el índice 1.
                f4 = face[3][0] - 1 #Agarrando el índice 2.

                #Transformando los vértices.
                v1 = r.transform_vertex(r.vertices[f1], scale, translate)
                v2 = r.transform_vertex(r.vertices[f2], scale, translate)
                v3 = r.transform_vertex(r.vertices[f3], scale, translate)
                v4 = r.transform_vertex(r.vertices[f4], scale, translate)

                #print("Cara: ", f1, f2, f3, f4)

                #Guardando los vértices.

                #Primer triángulo.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v2)
                c1.vertex_buffer_obj.append(v3)

                #Segundo triángulo.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v3)
                c1.vertex_buffer_obj.append(v4)
                


        elif len(face) == 3: #Validando que la cara tenga 3 vértices.
            
            if c1.tpath: #Si el path2 no está vacío, entonces se dibuja el triángulo.
                
                #El array de caras es bidimensional en este código.
                f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                f2 = face[1][0] - 1 #Agarrando el índice 0.
                f3 = face[2][0] - 1 #Agarrando el índice 1.
                #f4 = face[3][0] - 1 #Agarrando el índice 2.

                #Transformando los vértices.
                v1 = r.transform_vertex(r.vertices[f1], scale, translate)
                v2 = r.transform_vertex(r.vertices[f2], scale, translate)
                v3 = r.transform_vertex(r.vertices[f3], scale, translate)
                #v4 = r.transform_vertex(r.vertices[f4], scale, translate)
                
                #Jalando las caras de las texturas.

                ft1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                ft2 = face[1][1] - 1 #Agarrando el índice 0.
                ft3 = face[2][1] - 1 #Agarrando el índice 1.
                #f4 = face[3][0] - 1 #Agarrando el índice 2.

                #print(r.vertices[f1], scale, translate)

                #Obteniendo los vértices de texuras.
                vt1 = V3(*r.vts[ft1])

                vt2 = V3(*r.vts[ft2])

                vt3 = V3(*r.vts[ft3])

                #print("Cara: ", f1, f2, f3)
                #print(v1, v2, v3)

                #colr = color(1, 0, 0) #Color para el triángulo.

                #print("Textura: ", c1.tpath) #Debuggeo.

                #Guardando los vértices.

                #Vértices normales.
                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v2)
                c1.vertex_buffer_obj.append(v3)

                #Vértices de textura.
                c1.vertex_buffer_obj.append(vt1)
                c1.vertex_buffer_obj.append(vt2)
                c1.vertex_buffer_obj.append(vt3)

            else: #Si el path2 está vacío, entonces se dibuja el triángulo.
                
                #El array de caras es bidimensional en este código.
                f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
                f2 = face[1][0] - 1 #Agarrando el índice 0.
                f3 = face[2][0] - 1 #Agarrando el índice 1.


                #Transformando los vértices.
                v1 = r.transform_vertex(r.vertices[f1], scale, translate)
                v2 = r.transform_vertex(r.vertices[f2], scale, translate)
                v3 = r.transform_vertex(r.vertices[f3], scale, translate)

                c1.vertex_buffer_obj.append(v1)
                c1.vertex_buffer_obj.append(v2)
                c1.vertex_buffer_obj.append(v3)

#Mëtodo para dibujar el triángulo.
def dibujar(poligono, col):
    c1.active_vertex = iter(c1.vertex_buffer_obj)

    if poligono == "triangle":
        try: 
            while True:
                triangle(col)
        except StopIteration:
            print("Dibujado exitoso.")


def cross(V1, V2): #Producto cruz entre dos vectores, pero con return de V3.

    return V3(
        V1.y * V2.z - V1.z * V2.y,
        V1.z * V2.x - V1.x * V2.z,
        V1.x * V2.y - V1.y * V2.x
    )

def bounding_box(A, B, C): #Función que calcula el bounding box de un triángulo.

    coords = [(A.x, A.y), (B.x, B.y), (C.x, C.y)] #Se guardan las coordenadas de los puntos.

    #Se calculan las coordenadas mínimas y máximas.
    xmin = 99999
    xmax = -99999
    ymin = 99999
    ymax = -99999


    for (x, y) in coords: #Se recorren las coordenadas.

        if x < xmin: #Si la coordenada x es menor que la mínima, se setea la mínima.
            xmin = x
        if x > xmax: #Si la coordenada x es mayor que la máxima, se setea la máxima.
            xmax = x
        if y < ymin: #Si la coordenada y es menor que la mínima, se setea la mínima.
            ymin = y
        if y > ymax: #Si la coordenada y es mayor que la máxima, se setea la máxima.
            ymax = y

    #print("Coordenadas: ", x, y)

    return V3(xmin, ymin), V3(xmax, ymax) #Se retornan las coordenadas mínimas y máximas.


    #return V3(xmin, xmax), V3(ymin, ymax) #Retornando los valores mínimos y máximos de x y y.

def baricentrico(A, B, C, P):

    cx, cy, cz = V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y)
                    

    #print("¨Producto cruz: ", V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y))

    #print("Valor de cz: ", cz)

    if cz == 0: #Si el valor de cz es 0, entonces el punto no está en el plano.
        u, v = -1, -1
        w = -1

        return (u, v, w)
    else: #Si el valor de cz es diferente de 0, entonces el punto está en el plano.

        u = cx/cz
        v = cy/cz
        w = 1 - (u + v)

        return (u, v, w)

def triangle(col): #Función que dibuja un triángulo.

    A = next(c1.active_vertex)
    B = next(c1.active_vertex)
    C = next(c1.active_vertex)

    if c1.tpath: #Si el path2 no está vacío, entonces se dibuja el triángulo con textura.
        tA = next(c1.active_vertex)
        tB = next(c1.active_vertex)
        tC = next(c1.active_vertex)
        #print(tA, tB, tC)

    

    L = V3(0, 0, 1) #Vector de la luz.

    #Calculando la normal.
    N = cross((B - A), (C - A)) #Se calcula la normal.

    #print("Normal: ", N) #Se imprime la normal.

    i = (L.normalice() @ N.normalice()) * 5 #Se calcula el producto punto. Esto es para la intensidad del color.


    if i < 0: #Si i es menor a 1, entonces el punto está opuesto a la luz.
        i = abs(i) #Se le saca el valor absoluto a i.
        #print(i) #Se imprime i.
    if i > 1: #Si i es mayor a 1, entonces el punto está en la misma dirección que la luz.
        i = 1 #Se le asigna el valor de 1 a i.
    
    #print("Producto punto: ", i)

    c1.colorP = color(
        col[0] * i, 
        col[1] * i, 
        col[2] * i
        ) #Se setea el color del punto en escala de grises.

    


    #Calculando los mínimos y máximos de los puntos.
    min, max = bounding_box(A, B, C) #Se calculan los mínimos y máximos de los puntos.

    

    #Redondeando los mínimos y máximos para poderlos meter a los for-loops.
    min.round()
    max.round()


    for x in range(min.x, max.x + 1):
        for y in range(min.y, max.y + 1):
            w, u, v = baricentrico(A, B, C, V3(x, y)) #Se calcula el baricéntrico.

            if u < 0 or v < 0 or w < 0: #Si el baricéntrico es mayor o igual a 0, entonces se dibuja el punto.
                #print("Punto: ", x, y)
                continue
            
           

            z = A.z * w + B.z * v + C.z * u #Se calcula la z.
            

            if (c1.zBuffer[x][y] < z):
                c1.zBuffer[x][y] = z #Se setea la z.
                
                if c1.tpath: #Si el path2 no está vacío, entonces se dibuja el triángulo con textura.
                    tx = tA.x * v + tB.x * w + tC.x * u #Se calcula la x de la textura.
                    ty = tA.y * v + tB.y * w + tC.y * u #Se calcula la y de la textura.
                    c1.colorP = c2.get_color_with_intensity(tx, ty, i) #Se setea el color del punto con textura.

                    #print(c1.colorP)
                glVertex(x, y) #Se dibuja el punto.
            #glVertex(x, y) #Se dibuja el punto.


def zBuffer(): 
    
    #Copiar el zBuffer al zBufferE.
    c1.zBufferE = c1.zBuffer.copy() #Copiar el zBuffer al zBufferE.

    #Recorriendo el zBufferE. Si hay un -9999, entonces se cambia por un 0.
    for i in range(c1.height):
        for j in range(c1.width):
            if c1.zBufferE[i][j] == -9999: #Si el zBufferE tiene un -9999, entonces se cambia por un 0.
                c1.zBufferE[i][j] = color(0, 0, 0)
            elif c1.zBufferE[i][j] < 0: #Si el zBufferE tiene un valor menor a 0, entonces se cambia por un 0.
                c1.zBufferE[i][j] = color(0, 0, 0)
            elif c1.zBufferE[i][j] > 1 and c1.zBufferE[i][j] < 255: #Si el zBufferE tiene un valor mayor a 1, pero menor a 255, entonces dividir el número entre 255.
                c1.zBufferE[i][j] = color(int(c1.zBufferE[i][j] / 255), int(c1.zBufferE[i][j] / 255), int(c1.zBufferE[i][j] / 255))
                #print(c1.zBufferE[i][j])
            elif c1.zBufferE[i][j] > 255: #Si hay un valor mayor a 255, entonces se cambia por un 1.
                c1.zBufferE[i][j] = color(1, 1, 1)
            else: #Si hay algún color sesgado entre 0 y 1, entonces se pintan.
                c1.zBufferE[i][j] = color(int(c1.zBufferE[i][j]), int(c1.zBufferE[i][j]), int(c1.zBufferE[i][j]))


def texturas(path1, path2, col): #Método para dibujar las texturas.

    
    r = Object(path1) #Llamando al método Object del archivo Obj.py.

    #Método para hacer el ejemplo de Dennis.
    c2.lectura(path2) #Abriendo el bmp de la textura y procesando sus pixeles.

    c1.framebuffer = c2.pixels #Se setea el framebuffer con la textura.

    print(c1.colorFondo)

    #Recorriendo las caras del objeto y dibujando las líneas en el framebuffer.
    for face in r.faces: 
        #print(face) #Debuggeo.
        
        if len(face) == 4: #Validando que la cara tenga 4 vértices.
            #El array de caras es bidimensional en este código.
            f1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][1] - 1 #Agarrando el índice 0.
            f3 = face[2][1] - 1 #Agarrando el índice 1.
            f4 = face[3][1] - 1 #Agarrando el índice 2.

            #Transformando los vértices.
            vt1 = V3(
                r.vts[f1][0] * c2.width,
                r.vts[f1][1] * c2.height
            )

            vt2 = V3(
                r.vts[f2][0] * c2.width,
                r.vts[f2][1] * c2.height
            )

            vt3 = V3(
                r.vts[f3][0] * c2.width,
                r.vts[f3][1] * c2.height
            )

            vt4 = V3(
                r.vts[f4][0] * c2.width,
                r.vts[f4][1] * c2.height
            )

            #print("Cara: ", f1, f2, f3, f4)

            # #Dibujando los triangulos.
            # triangle(vt1, vt2, vt4)
            # triangle(vt2, vt3, vt4)

            # #Dibujando triángulos con líneas por el momento.
            glLine(vt1, vt2)
            glLine(vt2, vt3)
            glLine(vt3, vt1)
            
            # #Dibujar triángulos con líneas y el vértice 4.
            glLine(vt2, vt3)
            glLine(vt3, vt4)
            glLine(vt4, vt2)


        elif len(face) == 3: #Validando que la cara tenga 3 vértices.
            
            f1 = face[0][1] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][1] - 1 #Agarrando el índice 0.
            f3 = face[2][1] - 1 #Agarrando el índice 1.
            #f4 = face[3][0] - 1 #Agarrando el índice 2.

            #print(r.vts[f1]) #Debuggeo.

            #print(r.vertices[f1], scale, translate)

            #Transformando los vértices.
            #Obteniendo los vértices del tamaño de la escala y la translación.
            vt1 = V3(
                r.vts[f1][0] * c2.width,
                r.vts[f1][1] * c2.height
            )

            vt2 = V3(
                r.vts[f2][0] * c2.width,
                r.vts[f2][1] * c2.height
            )

            vt3 = V3(
                r.vts[f3][0] * c2.width,
                r.vts[f3][1] * c2.height
            )
            
          

            # #Pintando un triángulo por ahora.
            glLine(vt1, vt2)
            glLine(vt2, vt3)
            glLine(vt3, vt1)
            

            #triangle(vt1, vt2, vt3, col1) #Llamando al método triangle para dibujar un triángulo.

def glFinish(): #Función que escribe el archivo de imagen resultante.

   c1.write() #Escribiendo el archivo.
   #c1.write2() #Escribiendo el archivo con el zBuffer.



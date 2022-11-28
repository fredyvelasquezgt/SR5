
from fnmatch import translate
from gl import * 
from textures import * 

def main():
    
    glCreateWindow(1024, 1024) #Creando la ventana para los bb8's. 
    glClearColor(1, 1, 1) #Color del fondo.
    glClear() 
  
    col1 = (0.6, 0.1, 0.9) #Otro color.

    scale = (200, 200, 250) #Escala para los bb8's.
    translate = (512, 300, 0) #Traslación para los bb8's.
    
    modelo("./droids.obj", "./droids.bmp", scale, translate) #Llamando al método modelo para dibujar el modelo 3D.
    dibujar("triangle", col1) #Llamando al método dibujar para dibujar el modelo 3D.

   
    
    glFinish() 

main()
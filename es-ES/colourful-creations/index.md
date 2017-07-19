---
title: Creaciones coloridas
description: Crea tus propios colores personalizados y úsalos para crear un póster colorido. 
notes: "Colourful Creations - notes.md"
layout: project
new: true
---

# Introducción { .intro}

En este proyecto crearás un diccionario de colores que convierta códigos de colores difíciles de recordar en nombres sencillos.  

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/41a99e668b?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/colourful-finished.png">
</div>

# Paso 1: Uso de códigos de colores hexagonales { .activity}

## Lista de comprobación de actividades { .check}

La tortuga de Python tiene colores predefinidos tales como 'red' y 'white', sin embargo, también puedes usar códigos de colores hexagonales (es posible que ya hayas visto este tipo de códigos en el curso sobre HTML y CSS). 

+ Abre el Trinket de la plantilla Python en blanco: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. 

+ Añade el siguiente código de configuración para usar la tortuga:

    ![screenshot](images/colourful-setup.png)
    
    Ten en cuenta que has usado un color con nombre: 'white'.
    
+ La tortuga posee una lista de nombres de colores que puedes usar, sin embargo, seguramente en cierta ocasiones desearás seleccionar tus propios colores. La tortuga también te permite usar códigos de colores hexadecimales. 

  Abre <a href="http://jumpto.cc/colour-picker" target="_blank">jumpto.cc/colour-picker</a> y selecciona el color que desees. Encuentra su código hexadecimal (que comienza con una '#'), como por ejemplo '#A7E30E'.  
  
+ Copia el código hexadecimal, incluyendo la almohadilla marcándolo y, a continuación, haciendo clic derecho y seleccionando Copiar o usando Ctrl-C. 
  
+ A continuación, cambia la línea del código que establece el color de la pantalla para usar tu color. Por ejemplo:

   ![screenshot](images/colourful-background.png)
   
   Puedes usar clic derecho y Pegar o  Ctrl-V para pegar el código hexadecimal en el trinket. 
  
+ Selecciona otro código de color hexadecimal y úsalo para crear texto a color:

   ![screenshot](images/colourful-write.png)
   
   No tienes que usar la fuente 'Arial', puedes usar 'Verdana', 'Times' o 'Courier'.
   
   El tamaño de la fuente es '40'. Intenta cambiarlo.  
   
+ Prueba con otros colores hasta que encuentres dos que verdaderamente te gusten juntos. 


## Guarda tu proyecto {.save}

# Paso 2: Un diccionario de colores{ .activity}

## Lista de comprobación de actividades { .check}
 
Usar códigos de color hexagonales es muy flexible, pero también son difíciles de recordar. 

Como probablemente sepas, un diccionario te permite buscar palabras y consultar su significado. En Python, un diccionario es todavía más flexible. Te permite buscar un valor para cualquier 'key' del diccionario.

Creemos un diccionario que convierta nombres de colores (claves) en códigos hexadecimales (valores).

+ El diccionario debe estar entre llaves. 

  Crea un diccionario vacío denominado `colours`:

   ![screenshot](images/colourful-dict.png)
   
+ Selecciona nombres interesantes para tus colores y edita la línea `colours = {} ` para añadir sus entradas en el diccionario. 

  Aquí tienes un ejemplo del diccionario de colores:

   ![screenshot](images/colourful-colours.png)
   
   Los dos puntos `:` separan las claves (nombres de color) del valor (código hexagonal). Necesitarás una coma `,` entre cada pareja clave:valor del diccionario. 

+ Ahora ya no necesitas recordar los códigos hexadecimales, simplemente búscalos en el diccionario. 

  Adapta el siguiente código para usar tus nombres de color:
  
  ![screenshot](images/colourful-entries.png)
  
  La clave debe situarse dentro de los corchetes '[]', después del nombre del diccionario. 
  
+ Ahora puedes actualizar tu código para busca colores en el diccionario:

  ![screenshot](images/colourful-use.png)
  
  
+ Prueba tu código para asegurarte de que el texto se visualiza correctamente. 

## Guarda tu proyecto {.save}

## Reto: ¡Más colores! {.challenge}

¿Puedes añadir más colores al diccionario y probarlos? Usa <a href="http://jumpto.cc/colour-picker" target="_blank">jumpto.cc/colour-picker</a> para encontrar más colores. 

No te olvides de darles nombres fantásticos. 

Aquí tienes un código de ejemplo que te recordará cómo usar la tortuga:

![screenshot](images/colourful-challenge1.png)


## Guarda tu proyecto {.save}

## Reto: Crea un póster

Los diseñadores a menudo crean paletas de colores para temáticas concretas como, por ejemplo, el desierto o el espacio. 

¿Puedes crear un nuevo proyecto Python que use un diccionario para una paleta de colores temática? Puedes elegir el otoño, el bosque, el mar, las Navidades, los helados, los colores de tu equipo favorito o cualquier otra temática. 

Crea un póster usando tu diccionario de paleta de colores.

También puedes usar otros comandos tortuga como `forward`, `right`, `left`, `penup` y `pendown`. 

¿Eres capaz de añadir un contorno a tu póster?

Otros comandos tortuga útiles:

+ `circle(50)` dibuja el contorno de un círculo con un radio de 50.
+ `dot(100)` dibuja un círculo relleno con un diámetro de 100. 
  
A continuación tienes un ejemplo:

![screenshot](images/colourful-finished.png)

## Guarda tu proyecto {.save}



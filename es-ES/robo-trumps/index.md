---
title: Cartas robóticas
description: Crea una base de datos de robots, ¡y juega a Cartas robóticas con un amigo!
notes: "Robo-Trumps - notes.md"
layout: project
new: true
---

# Introducción { .intro}

En este proyecto leerás datos de un archivo para crear cartas robóticas. A continuación, podrás jugar a Cartas robóticas con un amigo.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/9ccc368bd5?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/robotrumps-finished.png">
</div>


# Paso 1: Lee los datos del robot desde un archivo { .activity}

A menudo resulta útil leer la información desde un archivo. A continuación, podrás cambiar los datos del archivo sin tener que cambiar tu código. 

## Lista de comprobación de actividades { .check}

+ Abre este trinket: <a href="http://jumpto.cc/trumps-go" target="_blank">jumpto.cc/trumps-go</a>. 

+ To proyecto de inicio incluye un archivo `cards.txt` con datos sobre los robots. 

  Haz clic en `cards.txt` para ver los datos:

  ![screenshot](images/robotrumps-cards.png)

  Cada línea posee datos de un robot. Los elementos están separados por comas. 

  Cada línea contiene la siguiente información:

  nombre, valoración de inteligencia, duración de la batería, nombre del archivo de imagen


+ Leeamos los datos del archivo de modo que puedas usarlos. 

  El primer paso es abrir el archivo `cards.txt` en tu script:
  
  ![screenshot](images/robotrumps-open.png)
  
+ A continuación, lee los datos del archivo:

  ![screenshot](images/robotrumps-read.png)
  
+ Debes cerrar siempre los archivos cuando no los estés usando:

  ![screenshot](images/robotrumps-close.png)

+ Esto nos da el archivo como una cadena. Necesitarás despiezarla en datos individuales. 

  En primer lugar, puedes dividir el archivo en una lista de líneas:

  ![screenshot](images/robotrumps-lines.png)
  
  Mira detenidamente en la salida. Hay tres elementos en la lista, cada uno es una línea del archivo. 
  
+ A continuación, podrás ciclar sobre dichas líneas de una en una

  ![screenshot](images/robotrumps-loop.png)
  
+ En lugar de imprimir las líneas, léelas en variables:

  ![screenshot](images/robotrumps-variables.png)
  
+ Debes ser capaz de usar estos datos posteriormente para buscar los valores de un robot concreto. Usemos el nombre del robot como clave de un diccionario. 

  Añade un diccionario `robots`:

  ![screenshot](images/robotrumps-dict.png)
  
+ A continuación, añadamos una entrada al diccionario de robots para cada robot. 

  El nombre de la clave y el valor son una lista de datos para dicho robot. 

  Añade el código marcado:
 
  ![screenshot](images/robotrumps-data.png)
  
  Puedes eliminar `print robots` una vez hayas probado tu script. 


# Paso 2: Visualiza los datos { .activity}

Ahora podrás visualizar los datos del robot de modo mucho más interesante. 

Visualicemos una carta robótica con una imagen y datos sobre su inteligencia y utilidad. 

Cuando hayas completado este paso, serás capaz de visualizar robots de este modo:

![screenshot](images/robotrumps-example.png)


## Lista de comprobación de actividades { .check}

+ Pregunta al usuario qué robot desea ver:

  ![screenshot](images/robotrumps-choose.png)
  
+ Si el robot está en el diccionario, busca sus datos:

  ![screenshot](images/robotrumps-if.png)
  
  Prueba tu código introduciendo el nombre del robot.

  
+ Si robot no existe, recibirás un error.

  ![screenshot](images/robotrumps-else.png)
  
 Prueba tu código introduciendo el nombre de un robot que no esté en el diccionario.

+ A continuación, usa la tortuga Python para visualizar los datos del robot. 

  Importa la biblioteca de tortuga en la parte superior de tu script y configura la pantalla y la tortuga:

  ![screenshot](images/robotrumps-turtle.png)

+ A continuación, añade el código para que la tortuga imprima el nombre del robot:

  ![screenshot](images/robotrumps-name.png)
  
+ Intenta cambiar la variable `style` hasta que estés satisfecho con el texto. 
  
  En lugar de `Arial`, prueba: `Courier`, `Times` o `Verdana`. 
  
  Cambia `14` a otro número distinto para cambiar el tamaño de la fuente. 
  
  Puedes cambiar `bold` a `normal` o `italic`. 
  
+ Guarda la lista de estadísticas del robot en una variable en lugar de imprimirlas:

  ![screenshot](images/robotrumps-stats.png)
  
+ Ahora puedes acceder a las estadísticas del robot como elementos de una lista:

  + `stats[0]` es la inteligencia
  + `stats[1]` es la batería
  + `stats[2]` es el nombre de la imagen
  
  Añade un código para visualizar las estadísticas de inteligencia y batería:
  
  ![screenshot](images/robotrumps-stats-2.png)
   
  
+ ¡Vaya! Las estadísticas están superpuestas. Necesitarás añadir un código para mover la tortuga:

   ![screenshot](images/robotrumps-stats-3.png)

+ Por último, añadamos la imagen del robot para completar la visualización. 

  Necesitarás añadir una línea para registrar la imagen cuando leas los datos de `cards.txt`:
  
  ![screenshot](images/robotrumps-register.png)
     
+ Añade un código para colocar y marcar la imagen:

  ![screenshot](images/robotrumps-image.png)
  
+ Prueba el código introduciendo un robot y, a continuación otro. ¡Verás que se muestran uno encima del otro!

  Antes de visualizar un robot, debes borrar la pantalla: 

  ![screenshot](images/robotrumps-clear.png)

## Guarda tu proyecto {.save}

## Reto: Añadir más robots { .challenge}

¿Puedes añadir datos de más robots en `cards.txt`? 

Haz clic sobre el botón de imágenes para ver las imágenes de los robots que puedes usar. 

Debes decidir cuánta batería e inteligencia tienen.

![screenshot](images/robotrumps-yellow.png)


## Guarda tu proyecto {.save}

## Reto: Añadir más estadísticas a los robots {.challenge}
¿Se te ocurren más estadísticas que puedas añadir a los robots? Puedes añadir `speed` o `usefulness` o cualquier otra idea que se te ocurra. 

Necesitarás:

+ Añadir datos al archivo para cada nueva categoría 
+ Añadir la nueva categoría al código que lee los datos
+ Escribir una nueva categoría al visualizar una carta

Incluso podrás añadir un color y mostrar las estadísticas para los robots con sus propios colores. 

Sugerencia: Usa `color('red')` para cambiar el texto de la tortuga al color rojo antes de escribir. 

Ejemplo: 

![screenshot](images/robotrumps-jet.png) 


## Guarda tu proyecto {.save}

# Paso 3: Visualiza un robot aleatorio { .activity}

Añadamos un código de modo que obtengas un robot aleatorio cuando escribas Aleatorio en lugar del nombre de un robot.

## Lista de comprobación de actividades { .check}

+ Primero, necesitarás importar la función de selección desde el módulo aleatorio:

  ![screenshot](images/robotrumps-random.png)
  
+ Podrás usar `choice` para seleccionar un nombre de robot aleatorio desde la lista de claves del diccionario del robot. 

  ![screenshot](images/robotrumps-choice.png)
  

## Guarda tu proyecto {.save}

## Reto: Juega a Cartas robóticas con un amigo {.challenge}
Comparte tu proyecto con un amigo y jugar a Cartas robóticas. ¡Usar el mismo proyecto para que la partida sea justa! El jugador uno solicita un robot aleatorio y, a continuación selecciona una categoría. A continuación, el jugador 2 solicitará un robot aleatorio y tú comprobarás quién tiene la mayor puntuación de la categoría seleccionada. A continuación, cambiar. 

El juego es mejor si ambos jugadores juegan con la misma baraja. Comparte un enlace al proyecto de tu trinket con un amigo de modo que podáis jugar con la misma baraja. 

![screenshot](images/robotrumps-play.png)

## Guarda tu proyecto {.save}

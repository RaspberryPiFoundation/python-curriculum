# 06—Tre på rad

På tide med et nytt spill! I dag skal vi lage tre på rad, hvor spillerne etter tur merker med ruter med X eller O inntil en av spillerne får tre på rad.

## Steg 1: Tegne rutenettet

Vi vil tegne fire linjer, i et #-mønster, som dette:

```
_|_|_
_|_|_
 | | 
```

Vi kunne brukt skilpadde-kommandoer for å tegne rutenettet, men i dag skal vi i stedet lære å bruke Tk-lerretet til tegning.

1. Åpne IDLE, lag en ny fil og lagre den som 'xox.py'

2. Skriv følgende kode

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    mainloop()
    ```

3. Lagre og kjør programmet ditt. Du vil se et rutenett tegnet på skjermen!

### Lerretet

Vi lager et 600 ganger 600-piksler vindu med kommandoen `c = Canvas(main, width=600, height=600)`. For datamaskinen ser dette slik ut:

```
    0       200      400      600   ...
   0+--------+--------+--------+-----> bortover
    |
    |
    |
    |
 200|        A        B
    |
    |
    |
    |
 400|        C        D
    |
    |
    |
    |
 600|
    |
 ...|
    V
  nedover
```

Her er punkt `A` ved 200 bortover, 200 nedover. Punkt `B` er ved 400 bortover, 200 nedover. Punkt `C` er ved 200 bortover, 400 nedover. Til slutt er punkt `D` ved 400 bortover, 400 nedover.

Hver av kodelinjene `c.create_line(bortover1, nedover1, bortover2, nedover2)` tegner en linje på skjermen, hvor de fire tallene beskriver hvor linjer starter og slutter. For eksempel, om vi vil tegne en linje fra `A` til `D` kan vi bruke `c.create_line(200, 200, 400, 400)`.

```
     0       200      400      600   ...
   0 +--------A--------B--------+-----> bortover
     |
     |
     |
     |
 200 M                          O
     |
     |
     |
     |
 400 N                          P
     |
     |
     |
     |
 600 |        C        D
     |
 ... |
     V
   nedover
```

Med de nye punktene i denne figuren vil vi tegne linjer fra A til C, B til D, M til O og N til P.  

```python
c.create_line(200, 0, 200, 600) # A til C
c.create_line(400, 0, 400, 600) # B til D

c.create_line(0, 200, 600, 200) # M til O
c.create_line(0, 400, 600, 400) # N til P

```

Når vi koder kaller vi ofte bortover for `x`, mens nedover ofte kalles `y`. Dette rutenettet ligner ganske mye på koordinatene du kanskje har lært om i mattetimen. Forskjellen er at her begynner vi i øvre venstre hjørne.

## Step 2: Drawing a O

1. In the same file, let's add a new function to draw when you click the mouse!

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    def click(event):
        c.create_oval(200,200,400,400)

    c.bind("<Button-1>", click)

    mainloop()
    ```

2. Run your code, and click on the grid, what happens?

   You should see a circle in the centre of the grid.

3. Let's edit the code, so it will draw where you click

    For this we'll need to take the mouse position, and work out which grid square it is in, and change the `click` function

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    def click(event):
        across = int(c.canvasx(event.x)/200)
        down = int(c.canvasy(event.y)/200)

        c.create_oval(
                across*200,down*200,
                (across+1)*200,(down+1)*200
        )

    c.bind("<Button-1>", click)

    mainloop()
    ```

    `int(c.canvasx(event.x)/200)` takes the mouse position `event.x`, turns it into the canvas position, `c.canvas(event.x)` and then divides it by 200, and rounds it down, so we get a number 0, 1 or 2 to tell us how far across the mouse is.

4. Run the code, click in the grid squares, each one should fill in with a circle!

    The code `c.create_oval(across*200,down*200,(across+1)*200,(down+1)*200)` turns 'Along 1, Down 2' into positions on the grid, like Along 200, Down 400. 

## Step 3: Drawing an X

1. In the same file, let's add some code to draw an X, then an O, then an X, ...

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    shape = "O"

    def click(event):
        global shape
        across = int(c.canvasx(event.x)/200)
        down = int(c.canvasy(event.y)/200)

        if shape == "O":
            c.create_oval(
                across*200,down*200,
                (across+1)*200,(down+1)*200
            )
            shape = "X"
        else:
            c.create_line(
                across*200, down*200,
                (across+1)*200, (down+1)*200
            )
            c.create_line(
                across*200, (down+1)*200,
                (across+1)*200, down*200
            )
            shape = "O"

    c.bind("<Button-1>", click)

    mainloop()
    ```
2. Run your program, try click on a grid, it should draw a O, click elsewhere it should draw an X

    We've used a new feature of python, `global` to let us change the variable `shape` in the function `click`.
    If you change variables defined outside of a function, then you have to use `global`. 

3. What happens if you click on the same square twice? 

    This is because our code doesn't keep track of what has been drawn, or where players have moved. We will have write some more code to fix this.

## Step 4: Keeping track

To stop players playing the same move twice, we'll have to keep track of the moves they make. To do this we'll introduce a list called `grid`

1. In the same file, 

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    shape = "O"
    grid = [
        "0", "1", "2", 
        "3", "4", "5",
        "6", "7", "8", 
    ]

    def click(event):
        global shape, grid
        across = int(c.canvasx(event.x)/200)
        down = int(c.canvasy(event.y)/200)

        square = across + (down*3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if shape == "O":
            c.create_oval(
                cross*200,down*200,
                (across+1)*200,(down+1)*200
            )
            grid[square] = "O"
            shape = "X"
        else:
            c.create_line(
                across*200, down*200,
                (across+1)*200, (down+1)*200
            )
            c.create_line(
                across*200, (down+1)*200,
                (across+1)*200, down*200
            )
            grid[square] = "X"
            shape = "O"

    c.bind("<Button-1>", click)

    mainloop()
    ```
2. Run your program, and try and click in the same square twice? What happens?

## Step 5: Finding a winner

Now we have got the game working, we need to find a winner!

1. In the same file, we're going to introduce a new function `winner`, and call it to check if the game has been won
    
    The completed code looks like this!

    ```python
    from tkinter import *

    main = Tk()

    c = Canvas(main, width=600, height=600)
    c.pack()

    c.create_line(200, 0, 200, 600)
    c.create_line(400, 0, 400, 600)

    c.create_line(0, 200, 600, 200)
    c.create_line(0, 400, 600, 400)

    shape = "O"
    grid = [
        "0", "1", "2", 
        "3", "4", "5",
        "6", "7", "8", 
    ]
        

    def click(event):
        global shape, grid
        across = int(c.canvasx(event.x)/200)
        down = int(c.canvasy(event.y)/200)

        square = across + (down*3)

        if grid[square] == "X" or grid[square] == "O":
            return

        if winner():
            return

        if shape == "O":
            c.create_oval(
                across*200,down*200,
                (across+1)*200,(down+1)*200
            )
            grid[square] = "O"
            shape = "X"
        else:
            c.create_line(
                across*200, down*200,
                (across+1)*200, (down+1)*200
            )
            c.create_line(
                across*200, (down+1)*200,
                (across+1)*200, down*200
            )
            grid[square] = "X"
            shape = "O"

    def winner():
        for across in range(3):
            row = across*3
            line = grid[row] + grid[row+1] + grid[row+2]
            if line == "XXX" or line == "OOO":
                return True
            
        for down in range(3):
            line = grid[down] + grid[down+3] + grid[down+6]
            if line == "XXX" or line == "OOO":
                return True

        line = grid[0]+grid[4]+grid[8]

        if line == "XXX" or line == "OOO":
                return True

        line = grid[2]+grid[4]+grid[6]
            
        if line == "XXX" or line == "OOO":
                return True

            
    c.bind("<Button-1>", click)

    mainloop()
    ```
2. Try playing the game and winning, can you make any more moves?

    We have four checks in `winner`

    1. Check each row for three X's or  O's

    2. Check each column for three X's or O's

    3. Check the diagonal from left to right 

    4. Check the diagonal from right to left.

## Step 6:

You're all done! Why not change the code to draw different shapes! 

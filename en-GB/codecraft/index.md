---
title: CodeCraft
description: Design and code improvements to a 2D version of Minecraft.
notes: "CodeCraft - notes.md"
layout: project
---

# Introduction { .intro}

In this project, you’ll design and code improvements to a 2D version of Minecraft.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/9ac3995d69?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/craft-finished.png">
</div>

# Step 1: Playing the game { .activity}

## Activity Checklist { .check}

+ Open this trinket: <a href="http://jumpto.cc/codecraft-go" target="_blank">jumpto.cc/codecraft-go</a>. If you're reading this online, you can also use the embedded version of this trinket below.

<div class="trinket">
<iframe src="https://trinket.io/embed/python/fdd32064f8?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

+ Use the WASD keys to move your player around the world, which is full of different resources (dirt, grass and water).

    ![screenshot](images/craft-move.png)

+ You can press the spacebar to collect resources. Pick up a few of each type of resource, and you'll see them added to your inventory.

    ![screenshot](images/craft-pickup.png)

+ Press the number keys (1 to 3) to place a resource on the map. For example, press 3 to place some water on the map. This will only work if you have some water in your inventory.

    ![screenshot](images/craft-place-water.png)

+ You can craft an item by pressing the key displayed in the menu. Crafting means combining items you already have in your inventory to create new ones. Try pressing the 'r' key to craft a new brick (as long as you have 2 dirt and 1 water in your inventory).

    ![screenshot](images/craft-craft-brick.png)

+ You can then press they '4' key to place your crafted bricks.

    ![screenshot](images/craft-place-brick.png)

## Save Your Project {.save}

## Challenge: Build your world {.challenge}
Can you build a house, with a garden and a swimming pool? What else can you create?

![screenshot](images/craft-build-example.png)

## Save Your Project {.save}

# Step 2: Customising your game { .activity}

Let’s modify some variables to change how your game works.

+ Click the `variables.py` file to see some variables that can be changed.

    ![screenshot](images/craft-variables.png)

+ Change the value of your `BACKGROUNDCOLOUR` variable, and click 'Run' to see the change to your game.

    ![screenshot](images/craft-background.png)

+ The variable `MAXTILES` is the amount of each resource that can be held in your inventory. Change this variable if you want to store more (or less) than 20 of each resource.

    ![screenshot](images/craft-maxtiles.png)

## Challenge: Change your world size { .challenge}
Can you change the values of your `MAPWIDTH` and `MAPHEIGHT` variables to change the size of the world?

![screenshot](images/craft-mapsize.png)

## Save Your Project {.save}

# Step 3: Creating a new wood resource { .activity}

Let's create a new wood resource. To do this, you'll need to add to some variables in your `variables.py` file.

+ First, you need to give your new resource a number. You'll then be able to use the word `WOOD` in your code instead of the number 4.

    ![screenshot](images/craft-wood-const.png)

+ You should add your new `WOOD` resource to your list of `resources`.

    ![screenshot](images/craft-wood-resources.png)

+ You should also give your resource a name, which will be displayed in the inventory.

    ![screenshot](images/craft-wood-name.png)

    Notice the comma `,` at the end of the line above.

+ Your resource will also need an image. The project already includes an image called `wood.png`, which you should add to the `textures` dictionary.

    ![screenshot](images/craft-wood-texture.png)

+ Add the number of your resource that should be in your `inventory` to start with.

    ![screenshot](images/craft-wood-inventory.png)

+ Finally, add the key that you'll press to place wood in the world. 

    ![screenshot](images/craft-wood-placekey.png)

+ Run your project to test it. You'll see that you now have a new 'wood' resource in your inventory.

    ![screenshot](images/craft-wood-test.png)

+ There's no wood in your world! To fix this, click on your `main.py` file and find the function called `generateRandomWorld()`.

    ![screenshot](images/craft-wood-random1.png)    

    This code generates a random number between 0 and 10, and uses the number to decide which resource to place:

    + 1 or 2 = water
    + 3 or 4 = grass
    + anything else = DIRT

+ Add this code to add wood to your world whenever the `randomNumber` is 5.

    ![screenshot](images/craft-wood-random2.png)

+ Test your project again. This time, you should see some wood appear in your world.

    ![screenshot](images/craft-wood-test2.png)

## Challenge: Creating sand { .challenge}
Can you add a `SAND` resource to your game? You can use the steps above to help you.

![screenshot](images/craft-sand.png)

The project already includes a `sand.png` image, but you can create and upload your own if you prefer.

![screenshot](images/craft-upload.png)

## Save Your Project {.save}

# Step 4: Crafting planks from wood { .activity}

Let's create a new plank resource that be crafted from wood.

+ First, add a new `PLANK` variable to your game.

    ![screenshot](images/craft-plank-const.png)

+ Add a new `PLANK` variable to your game.

    ![screenshot](images/craft-plank-resources.png)

+ Name the resource `'plank'`.

    ![screenshot](images/craft-plank-names.png)

+ Give your `PLANK` resource an image. The project already contains a `plank.png` image, but you can create your own if you prefer.

    ![screenshot](images/craft-plank-textures.png)

+ Add planks to your inventory.

    ![screenshot](images/craft-plank-inventory.png)

+ Set a key for placing planks.

    ![screenshot](images/craft-plank-placekeys.png)

+ As this resource can be crafted, you need to create a crafting rule, which is that a plank can be made from 3 wood tiles. Add this code to the `crafting` dictionary. 

    ![screenshot](images/craft-plank-crafting.png)

+ Finally, you need to set a key for crafting new planks.

    ![screenshot](images/craft-plank-craftkeys.png)

+ To test your new plank resource, gather up a few wood tiles and then craft some planks from your wood. You can then place your new planks in your world.

    ![screenshot](images/craft-plank-test.png)

## Save Your Project {.save}

## Challenge: Crafting glass from sand { .challenge}
Can you create a new glass resource, that can be crafted from sand? You can follow the steps above to help you.

![screenshot](images/craft-glass.png)

The project already contains a `glass.png` image that you can use, or you can create your own image if you prefer.

## Save Your Project {.save}

## Challenge: Create more resources { .challenge}
Can you add more resources and crafting rules to your game?

## Save Your Project {.save}
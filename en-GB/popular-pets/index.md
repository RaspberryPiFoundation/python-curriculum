---
title: Popular Pets
description: Create pie charts and bar graphs from data using the PyGal library. 
notes: "Popular Pets - notes.md"
layout: project
new: true
---

# Introduction { .intro}

In this project you create pie charts and bar graphs from data that you collect from members of your Code Club.  

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/70d24d92b8?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/pets-finished.png">
</div>


# Step 1: Create a Pie Chart { .activity}

Pie Charts are are useful way of showing data. Let's do a survey of favourite pets in your Code Club and then present the data as a Pie Chart. 

## Activity Checklist { .check}

+ Ask your volunteer to help organise a survey. You could record the results on a computer connected to a projector or a whiteboard that everyone can see. 

  Write a list of pets and make sure everyone's favourite is included. 
  
  Then get everyone to vote for their favourite by putting their hand up when it gets called out. Only one vote each!
  
  For example:
  
  ![screenshot](images/pets-favourite.png)

+ Create a new Python trinket <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. If you're reading this online, you can also use the embedded version of this trinket below.

<div class="trinket">
<iframe src="https://trinket.io/embed/python/33e5c3b81b?start=result" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
</div>

+ Let's create a pie chart to show the results of your survey. You'll be using the PyGal library to do some of the hard work.

  First import the Pygal library:

  ![screenshot](images/pets-pygal.png)


+ Now let's create a Pie chart and display (render) it:

  ![screenshot](images/pets-pie.png)
  
  Don't worry, it gets more interesting when you add data!


+ Let's add in the data for one of the pets. Use the data that you collected.

  ![screenshot](images/pets-add.png)
  
  There's only one piece of data so it takes up the whole pie chart. 

+ Now add the rest of the data in the same way. 

  For example:
  
  ![screenshot](images/pets-add-all.png)
  
+ And to finish off your chart, add a title:

  ![screenshot](images/pets-title.png)
  

## Save Your Project {.save}

## Challenge: Create your own bar chart {.challenge}

You can create bar charts in a similar way. Just use `barchart = pygal.Bar()` to create a new barchart and then add data and render in the same way as for a chart. 

Collect data from your Code Club members to create your own bar graph. 

Make sure that you choose a topic that everyone will know about and is suitable for the children in your class. You could try: favourite sports or ice cream flavours. You could find out which month children's birthday's are in or how they get to school (walk, cycle, car, bus.)You could pick a yes/no question such as 'Do you play Minecraft?'.  

Don't ask questions that give personal data such as where people live. Ask your volunteer if you're not sure. 

Examples:

![screenshot](images/pets-bar.png)
 
![screenshot](images/pets-pn-bar.png)
  

# Step 2: Read data from a file { .activity}

It's useful to be able to store data in a file rather than having to including it in your code. 

## Activity Checklist { .check}

+ Add a new file to your project and call it `pets.txt`:

  ![screenshot](images/pets-file.png)

+ Now add data to the file. You can use the favourite pets data that you collected or the example data. 

  ![screenshot](images/pets-data.png)
  
+ Switch back to `main.py` and comment out the lines that render (display) charts and graphs:

  ![screenshot](images/pets-comment.png)

+ Now let's read the data from the file. 

  ![screenshot](images/pets-read.png)
  
  The for loop will loop over the lines in the file, `splitlines()` removes the newline character from the end of the line as you don't want that. 
  
+ Each line needs to be separated into a label and a value:
  
  ![screenshot](images/pets-split.png)
  
  This will split the line at the spaces so don't include spaces in the labels. (You can add support for spaces in labels later.)
  
+ You might get an error like this:

  ![screenshot](images/pets-split.png)
  
  This happens if you have an empty line at the end of your file. 
  
  You can fix the error only getting the label and value if the line isn't empty:
  
  ![screenshot](images/pets-split.png)
  
+ Now let's add the label and value to a new Pie Chart and render it:

  ![screenshot](images/pets-pie2.png)
  
  Note that add expects the value to be a number,  `int(value)` turns the value from a string into an integer.
  
  If you wanted to use decimals such as 3.5 (floating point numbers) you could use `float(value)` instead. 
  
  
## Save Your Project {.save}

## Challenge: Create a bar chart from a file {.challenge}

Can you create a bar chart from the data you collected in the earlier challenge? You'll need to create a new .txt file. 

![screenshot](images/pets-pn.png)

 Tip: If you want to have spaces in the labels then use `line.split(': ')` and add colons to your data file, e.g. 'Red Admiral: 6'
 
 ![screenshot](images/pets-butterflies.png)
 
 
## Challenge: More charts and graphs! {.challenge}

Can you create a pie chart and a bar chart from the same file? You can either use the data you collected earlier or collect some new data. 

## Save Your Project {.save}

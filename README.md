# Accuknox-Interview-Question
Here's my submission on accuknox interview question 

## Problem statement 1: (Python Language)

A restaurant keeps a log of (eater_id, foodmenu_id) for all the diners. The eater_id
is a unique number for every diner and foodmenu_id is unique for every food item
served on the menu.

Write a program that reads this log file and returns the top 3
menu items consumed. If you find an eater_id with the same foodmenu_id more
than once then show an error.

> Tip: Find the ocuurance of food items ordered and raise error if duplicay found in food items. 

## Solution:

Using json to track food menu and eater id and check occurance, if occurance occur more than one time then raising error.

## Problem statement 2: 

Fix: Change the globle variable list children because it's access by all node and have to init in initilazise function to access it for each node.

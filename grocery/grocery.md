## Grocery List

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called `grocery.py`, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

## Hints
- Note that you can detect when the user has inputted control-d by catching an [EOFError](https://docs.python.org/3/library/exceptions.html#EOFError) with code like:
```python
try:
    item = input()
except EOFError:
    ...
```
- Odds are you’ll want to store your grocery list as a dict.
- Note that a dict comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), among them get, and supports operations like:
```
d[key]
```
and
wherein `d` is a `dict` and `key` is a `str`.

- Be sure to avoid or catch any [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError).
- Note that you can sort a dictionary’s keys alphabetically by passing that dictionary as an argument to [sorted](https://docs.python.org/3/library/functions.html#sorted).


## Demo
```
$ python grocery.py                                                             
apple                                                                           
banana                                                                          
banana                                                                          
ice cream

1 APPLE                                                                         
2 BANANA                                                                        
1 ICE CREAM                                                                     
$ python grocery.py                                                             
lettuce                                                                         
tomato                                                                          
tomato                                                                          
carrot                                                                          
tomato

1 CARROT                                                                        
1 LETTUCE                                                                       
3 TOMATO                                                                        
$
```

## Before You Begin

From your root directory run
```
mkdir grocery
```
to make a folder called grocery in your codespace.
Then execute
```
cd grocery
```
to change directories into that folder.
You can now execute:
```
code grocery.py
```
to make a file called `grocery.py` where you’ll write your program.


## How to Test
Here’s how to test your code manually:

Run your program with `python grocery.py`. Type `mango` and press Enter, then type `strawberry` and press Enter, followed by control-d. Your program should output:
```
1 MANGO
1 STRAWBERRY
```
Run your program with `python grocery.py`. Type `milk` and press Enter, then type `milk` again and press Enter, followed by control-d. Your program should output:
```
2 MILK
```
Run your program with `python grocery.py`. Type `tortilla` and press Enter, then type `sweet potato` and press Enter, followed by control-d. Your program should output:
```
1 SWEET POTATO
1 TORTILLA
```

## Check50
```
check50 cs50/problems/2022/python/grocery --local
```
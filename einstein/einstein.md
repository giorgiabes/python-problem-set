## Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert [Einstein](https://en.wikipedia.org/wiki/Albert_Einstein) et al. Essentially, the formula means that mass and energy are equivalent.

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

## Hints
- Recall that `input` returns a `str`, per [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that `int` can convert a `str` to an `int`, per [docs.python.org/3/library/functions.html#int](https://docs.python.org/3/library/functions.html#int).
- Recall that Python comes with several built-in functions, per [docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

## Demo
```
$ python einstein.py                                                            
m: 50                                                                           
E: 4500000000000000000                                                          
$
```

<img src="../gifs/einstein.gif" alt="demo">

## Hot to Test
Here’s how to test your code manually:

- Run your program with `python einstein.py`. Type `1` and press Enter. Your program should output:
```
90000000000000000
```
- Run your program with `python einstein.py`. Type `14` and press Enter. Your program should output:
```
1260000000000000000
```
- Run your program with `python einstein.py`. Type `50` and press Enter. Your program should output
```
4500000000000000000
```

## Check50
```
check50 cs50/problems/2022/python/einstein --local
```
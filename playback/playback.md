## Playback Speed
Some people have a habit of ~~lecturing~~ speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).

## Hints
- Recall that input returns a str, per [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that a str comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).


## Demo
```
$ python playback.py
This is Python.
This...is...Python.
$
```

## How to Test
Here’s how to test your code manually:

- Run your program with `python playback.py`. Type `This is Python` and press Enter. Your program should output:
```
This...is...Python
```
- Run your program with `python playback.py`. Type `This is our module on functions` and press Enter. Your program should output:
```
This...is...our...module...on...functions
```
- Run your program with `python playback.py`. Type `Let's implement a function called hello` and press Enter. Your program should output:
```
Let's...implement...a...function...called...hello
```

## Check50
```
check50 cs50/problems/2022/python/playback --local
```
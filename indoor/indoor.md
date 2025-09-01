## Indoor Voice
WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`.

## Hints
- Recall that `input` returns a `str`, per [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Demo
```
$ python indoor.py                                                              
HELLO, WORLD                                                                    
hello, world                                                                    
$
```

<img src="demo.gif" alt="demo">

<video controls width="720" preload="metadata" poster="thumb.png">
  <source src="demo.mp4" type="video/mp4" />
  Sorry—your browser can’t play this video. 
  <a href="demo.mp4">Download MP4</a>.
</video>


## How to Test
- Run your program with `python indoor.py`. Type `HELLO` and press Enter. Your program should output `hello`.
- Run your program with `python indoor.py`. Type THIS IS PYTHON3 and press Enter. Your program should output this is python3.
- Run your program with `python indoor.py`. Type 42 and press Enter. Your program should output 42.

## Check50
```
check50 cs50/problems/2022/python/indoor --local
```
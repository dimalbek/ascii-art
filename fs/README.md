## ascii-art-fs

### Objectives

You must follow the same [instructions](../README.md) as in the first subject but the second argument must be the name of the template. I know some templates may be hard to read, just do not obsess about it.

### Instructions

- Your project must be written in **Python**.
- You can see all about the **banners** [here](../).
- The usage must respect this format `python3 main.py [STRING] [BANNER]`, any other formats must return the following usage message:

```console
Usage: python3 main.py [STRING] [BANNER]

EX: python3 main.py something standard
```

If there are other `ascii-art` optional projects implemented, the program should accept other correctly formatted `[OPTION]` and/or `[BANNER]`.  
Additionally, the program must still be able to run with a single `[STRING]` argument.

### Usage

```console
$ python3 main.py "hello" standard | cat -e
 _              _   _          $
| |            | | | |         $
| |__     ___  | | | |   ___   $
|  _ \   / _ \ | | | |  / _ \  $
| | | | |  __/ | | | | | (_) | $
|_| |_|  \___| |_| |_|  \___/  $
                               $
                               $
$ python3 main.py "Hello There!" shadow | cat -e
                                                                                         $
_|    _|          _| _|                _|_|_|_|_| _|                                  _| $
_|    _|   _|_|   _| _|   _|_|             _|     _|_|_|     _|_|   _|  _|_|   _|_|   _| $
_|_|_|_| _|_|_|_| _| _| _|    _|           _|     _|    _| _|_|_|_| _|_|     _|_|_|_| _| $
_|    _| _|       _| _| _|    _|           _|     _|    _| _|       _|       _|          $
_|    _|   _|_|_| _| _|   _|_|             _|     _|    _|   _|_|_| _|         _|_|_| _| $
                                                                                         $
                                                                                         $
$ python3 main.py "Hello There!" thinkertoy | cat -e
                                                $
o  o     o o           o-O-o o                o $
|  |     | |             |   |                | $
O--O o-o | | o-o         |   O--o o-o o-o o-o o $
|  | |-' | | | |         |   |  | |-' |   |-'   $
o  o o-o o o o-o         o   o  o o-o o   o-o O $
                                                $
                                                $
```

### Allowed packages

- Only the [standard Python](https://docs.python.org/3/library/) packages are allowed.

This project will help you learn about :

- The Python file system(**fs**) API
- Data manipulation

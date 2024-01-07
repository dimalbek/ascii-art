## ascii-art-output

### Objectives

- You must follow the same [instructions](../README.md) as in the first subject **while** writing the result into a file.

The file must be named by using the flag `--output=<fileName.txt>`, in which `--output` is the flag and `<fileName.txt>` is the file name which will contain the output.

- The flag must have exactly the same format as above, any other formats must return the following usage message:

```console
Usage: python3 main.py [OPTION] [STRING] [BANNER]

EX: python3 main.py --output=<fileName.txt> something standard
```

If there are other `ascii-art` optional projects implemented, the program should accept other correctly formatted `[OPTION]` and/or `[BANNER]`.  
Additionally, the program must still be able to run with a single `[STRING]` argument.

### Instructions

- Your project must be written in **Python**.

### Usage

```console
$ python3 main.py --output=banner.txt "hello" standard
$ cat -e banner.txt
 _              _   _          $
| |            | | | |         $
| |__     ___  | | | |   ___   $
|  _ \   / _ \ | | | |  / _ \  $
| | | | |  __/ | | | | | (_) | $
|_| |_|  \___| |_| |_|  \___/  $
                               $
                               $
$
$ python3 main.py --output=banner.txt "Hello There!" shadow
$ cat -e banner.txt
                                                                                         $
_|    _|          _| _|                _|_|_|_|_| _|                                  _| $
_|    _|   _|_|   _| _|   _|_|             _|     _|_|_|     _|_|   _|  _|_|   _|_|   _| $
_|_|_|_| _|_|_|_| _| _| _|    _|           _|     _|    _| _|_|_|_| _|_|     _|_|_|_| _| $
_|    _| _|       _| _| _|    _|           _|     _|    _| _|       _|       _|          $
_|    _|   _|_|_| _| _|   _|_|             _|     _|    _|   _|_|_| _|         _|_|_| _| $
                                                                                         $
                                                                                         $
$
```

### Allowed packages

- Only the [standard Python](https://docs.python.org/3/library/) packages are allowed

This project will help you learn about :

- The Python file system(**fs**) API
- Data manipulation

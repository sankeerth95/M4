# M4 compiler

M4 is a 32 bit compiler producing 32 bit assembly code on the linux platorm(It outputs elf32 binaries). The assembly code emission is mostly handled by python.

It can also run in REPL mode. It is developed with the intent of making a simple language with expressible semantics used for quick prototyping. 

Construct:
    - uses tagged datatypes and pointers
    - pure integers and chars only, floating point support to be eventually included.
    - 

Dependencies: 
    - gcc compiler(any frickin version)
    - python 3.53 or later.


Currently needs development of the parser, understands only intermediate representation of code for now.



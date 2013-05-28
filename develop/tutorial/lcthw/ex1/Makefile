# set the compiler to use
CC=gcc
# set the compile option
CFLAGS=-Wall -g -c

all: ex1

ex1: ex1.o
	$(CC) ex1.o -o ex1

ex1.o: ex1.c
	$(CC) $(CFLAGS) ex1.c -o ex1.o

clean:
	rm -f ex1
	rm -f ex1.o

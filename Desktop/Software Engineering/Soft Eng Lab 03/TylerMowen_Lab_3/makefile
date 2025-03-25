# This is a omment line
CC=g++
# CFLAGS will be the options passed to the ompiler.
CFLAGS= -Wall
OBJECTS = main.o isEven.o isOdd.o
all: prog

prog: $(OBJECTS)
	$(CC) $(OBJECTS) -o prog

main.o: main.c
	$(CC) $(CFLAGS) -c main.c

isEven.o: isEven.c
	$(CC) $(CFLAGS) -c isEven.c

isOdd.o: isOdd.c
	$(CC) $(CFLAGS) -c isOdd.c

clean:
	rm -rf *.o 
CC = g++
CFLAGS = -std=gnu++11 -g 
WARNS = -w

LIBS := -lm -pthread
LIBS_OPENGL := `pkg-config --cflags --libs x11 xi gl glu` -lglut

all: lab4


.PHONY: lab4
lab4:
	$(CC) $(CFLAGS) $(WARNS) -o $@ $@.cpp $(LIBS) $(LIBS_OPENGL) 


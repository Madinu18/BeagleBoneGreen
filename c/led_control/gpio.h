#ifndef __GPIO_H_
#define __GPIO_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

#define OUT "out"
#define IN "in"

#define HIGH 1
#define LOW 0

typedef unsigned char UINT8;
typedef unsigned int UINT16;
typedef unsigned long UINT32;

extern int gpio_set_dir(UINT8 pin, const char *dir);
extern int digital_write(UINT8 pin, int value);
extern int digital_read(UINT8 pin);

#endif
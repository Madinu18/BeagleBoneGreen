#include <stdio.h>

#include "gpio.h"

#define LOOP 1

#define BTN_PIN 44

int main()
{
    while (1)
    {
        printf("Pin State : ");

        if(digital_read(BTN_PIN)){
            printf("HIGH\n");
        }
        else printf("LOW\n");

        sleep(1);

        if (!LOOP){
            return 1;
        }
    }
}
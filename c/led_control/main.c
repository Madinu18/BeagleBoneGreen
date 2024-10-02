#include <stdio.h>

#include "gpio.h"

#define LOOP 0

#define LED_RED 69
#define LED_GREEN 68
#define LED_BLUE 45

int led_blink(int pin)
{
    gpio_set_dir(pin, OUT);
    digital_write(pin, HIGH);

    sleep(1);

    digital_write(pin, LOW);

    printf("Success\n");
}

int main()
{
    while (1)
    {
        led_blink(LED_RED);
        led_blink(LED_GREEN);
        led_blink(LED_BLUE);
        if (!LOOP){
            return 1;
        }
    }
}
#include "gpio.h"


#define GPIO_PATH "/sys/class/gpio/"

int gpio_set_dir(UINT8 pin, const char *dir){
    char path[64];
    int fd;

    snprintf(path, sizeof(path), GPIO_PATH "gpio%d/direction",pin);
    fd = open(path, O_WRONLY);
    if (fd < 0){
        perror("Failed to open gpio direction for writing");
        return -1;
    }
    if (write(fd, dir, strlen(dir)) < 0) {
        perror("Failed to set direction");
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}

int digital_write(UINT8 pin, int value){
    char path[64];
    int fd;

    snprintf(path, sizeof(path), GPIO_PATH "gpio%d/value",pin);
    fd = open(path, O_WRONLY);
    if (fd < 0){
        perror("Failed to open gpio direction for writing");
        return -1;
    }

    if (value == 0) {
        if (write(fd, "0", 1) < 0) {
            perror("Failed to write value");
            close(fd);
            return -1;
        }
    } else {
        if (write(fd, "1", 1) < 0){
            perror("failed to write value");
            close(fd);
            return  -1;
        }
    }

    close(fd);
    return 0;
}

int digital_read(UINT8 pin){
    char path[64];
    char value_str[3];
    int fd;

    snprintf(path, sizeof(path), GPIO_PATH "gpio%d/value", pin);
    fd = open(path, O_RDONLY);
    if (fd < 0){
        perror("Failed to open gpio value for reading");
        return -1;
    }

    if (read(fd, value_str, 3) < 0){
        perror("Failed to read value");
        close(fd);
        return -1;
    }

    close(fd);
    return atoi(value_str);
}
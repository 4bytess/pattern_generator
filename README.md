# PATTERN GENERATOR

This is a python3 script that automates the genereation of unique patterns and calculates offsets. It is designed for buffer overflow exploitation.

## USAGE

### Parameters:

> `-m <mode>` Specify the mode
> `-v <value>` Specify the value

### Examples:

> `pattern.py -m generate -v 100` Generates 100 bytes of unique pattern:

![image](https://github.com/user-attachments/assets/0eaf9a98-4b94-481c-92ee-ebb1ecc323c7)
> `pattern.py -m offset -v b14b15b1` Calculates the offset between the start of the pattern and the value:

![image](https://github.com/user-attachments/assets/cbe182a9-421b-474f-80aa-c3ede6bdf868)
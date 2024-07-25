# PATTERN GENERATOR

This is a python3 script that automates the genereation of unique patterns and calculates offsets. It is designed for buffer overflow exploitation.

## USAGE

Parameters:

> `-m <mode>` Specify the mode
> `-v <value>` Specify the value

Examples:

> `pattern.py -m generate -v 500` Generates 500 bytes of unique pattern:

![image](https://github.com/user-attachments/assets/fdb0f582-98b2-4f44-a746-007af4557657)
> `pattern.py -m offset -v b14b15b1` Calculates the offset between the start of the pattern and this value:

![image](https://github.com/user-attachments/assets/cbe182a9-421b-474f-80aa-c3ede6bdf868)
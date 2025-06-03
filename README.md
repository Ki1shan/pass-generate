# Password Generator Tools

This project contains two Python-based tools that generate strong, meaningful passwords from personal information like name, DOB, city, nickname, and PIN. These tools focus on both "memorability" and "security", using different generation techniques.

----------------

## Tools Overview

| Tool            | Behavior                                                      | Output Type     |
|-----------------|-----------------------------------------------------------------|------------------|
| `pass.py`       | Generates the **same password** every time for the same input | Consistent / Repeatable |
| `random-pass.py`| Generates a **different password** each time using the same input | Randomized / Unique |

------------------

##  Requirements

- Python 3.x  
- Uses only built-in modules:
  - `random`
  - `string`

-------------------

## Input Fields for Both Tools
You’ll be prompted to enter:
   1. Name
   2. Date of Birth (format: DD/MM/YYYY)
   3. Address / City
   4. Nickname
   5. PIN Code

--------------------

## How They Work
1. pass.py – Consistent Password Generator
   Extracts:
        First 2 letters of Name
        Last 2 of Nickname
        First 3 of Address
        Last 4 of DOB
        Last 2 of PIN

    Adds:
        1 random digit
        1 symbol
Slightly randomizes capitalization
Output is the same every time for the same input
------
2. random-pass.py – Randomized Password Generator
    Extracts same elements as above

    Randomly:
    Shuffles parts
    Adds 2 digits and 2 symbols
    Applies random upper/lower casing
    Output changes every time, even with the same input

--------------------

## Output(for example)
Enter your name: Rahul ||
Enter your DOB (DD/MM/YYYY): 15/08/2000 ||
Enter your address/city: Delhi ||
Enter your nickname: Rocky ||
Enter your PIN code: 110001 ||

 pass.py → RocyDel2000@9 ||
 random-pass.py → DeK@20R9yl (randomly changes every time)

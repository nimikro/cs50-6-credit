# cs50-6-credit - Summary
This is a command line application developed in Python that will validate a credit card number, as well as it's flag using Hans Peter Luhn's algorithm. This is an exercise for Harvard's CS50 online course.

# Table of contents
1. [Credit](#Credit)
2. [Luhn’s Algorithm](#Luhn’s-Algorithm)
3. [About this program](#About-this-program)
4. [Usage](#Usage)

# Credit
The implemented program determines whether a provided credit card number is valid according to Luhn’s algorithm.
```
$ python credit.py
Number: 378282246310005
AMEX
```
# Luhn’s Algorithm
So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
Add the sum to the sum of the digits that weren’t multiplied by 2.
If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.

For the sake of discussion, let’s first underline every other digit, starting with the number’s second-to-last digit:

4003600000000014

Okay, let’s multiply each of the underlined digits by 2:

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

That gives us:

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

Now let’s add those products’ digits (i.e., not the products themselves) together:

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

Yup, the last digit in that sum (20) is a 0, so David’s card is legit!

So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s write a program.

# About this program
Credit.py is a program that prompts the user for a credit card number and then reports whether it is a valid American Express, MasterCard, or Visa card number, per the definitions of each’s format herein. This program uses a command line interface and was made only using Python. This program is one of week 6's exercises of Harvard's CS50 online course.

# Usage
You will need Python to run this application.

After cloning this repository and installing Python3, enter the project's folder through the command line and type the following to run the program:

`python3 credit.py`

The application will request a number, where you should input the credit card number to be tested. Although this is a simple application that will not store this number anywhere, always be careful with sensitive information. [Here](https://developer.paypal.com/docs/payflow/payflow-pro/payflow-pro-testing/) are some fictional credit card numbers Paypal recommend using for tests.
```
Number: <type a credit card number>
```
The application will return if the inputed number is a Visa, Mastercard, Amex or invalid, a la the below:
```
$ python3 credit.py
Number: 4003600000000014
VISA
```
The application will reject non-numeric inputs, asking again until receive a valid input or pressing Ctrl+C.

Also, consider the below representative of how the program behaves when passed a valid credit card number (sans hyphens), but also during non valid inputs.
```
$ ./credit
Number: 4003600000000014
VISA
```

```
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

```
$ ./credit
Number: 6176292929
INVALID
```

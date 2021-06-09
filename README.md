# Application of Matrix in Cryptography
- I created this project just to practice my coding skills in python

## Overview
- This is a simple application based on python with a simple UI created with Tkinter module in python.
- Python version: 3.8.5
- Numpy version: 1.20.3
- Tkinter version: 8.6.9

## What can you do this App ?
- You encode a message with a matrix key of your choice.
    - The app will give you set of numbers(encoded message) equivalent to the message you want to encode and can only be decoded by the matrix key you provided.
- You can decode a set of numbers (encoded message) with the matrix key that was used to encode the message.
    - The app will give you the message (in alphabet letters) equivalent to the set of numbers (encoded message) decoded by the matrix key you entered.
## How does it Work ?
### When encoding:
- Divide the message into group of (dimension of key matrix).
- Assign each character of the message its corresponding ASCII code.
- Convert each group of numbers into a 1 by (dimension of key matrix) matrices.
- Multiply each matrix by the matrix key.
- Example (TODO)

### When decoding:
- Divide the message into group of (dimension of key matrix).
- Convert each group of numbers into a 1 by (dimension of key matrix) matrices.
- Multiply each matrix by the inverse of matrix key.
- Example (TODO)



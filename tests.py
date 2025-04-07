#!/bin/env python
"""
Xchel's logic challenges module
"""
import functools

def decrypt_finder(string: str) -> tuple[int, int]:
    """
    Challenge that checks an input test with decryption methods.

    The first lines are a single word which will be searched for in the message.
    The last message is the message to decrypt.

    Args:
        string (str): String containing words to search and message to decrypt.

    Returns:
        tuple: Tuple containing the number of words found and the value of decode.
    """
    def decrypt_message(message: str, shift: int) -> str:
        """
        Decrypts a message with the shift value.

        Args:
            message (str): Message to decrypt.
            shift (int): Shift value for decryption.

        Returns:
            str: Decrypted message
        """
        return ''.join(list(map(lambda char: chr((ord(char)%32 + shift)%27 +
                                                 (64 if (ord(char)%32 + shift)%27 else 32)),
                                message)))

    words = list(map(lambda word: word.strip(), string.strip().upper().split('\n')))
    message = words.pop(-1)
    result = (0, -1)
    for shift in range(27):
        decrypted_message = decrypt_message(message, shift)
        count = functools.reduce(lambda total, word: total + int(word.strip() in decrypted_message),
                                 words, int())
        if count > result[0]:
            result = (count, shift)
    return result

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

def matrix_parity(matrix: str) -> str:
    """
    Challenge that checks if a matrix's rows and columns all sum an even number.

    The incoming string will be the matrix to check

    Args:
        matrix (str): String containing matrix to check.

    Returns:
        str: OK for pass, Change (int, int) for only one error, Corrupt for other cases.
    """
    matrix = list(map(lambda row: row.strip().split(), matrix.strip().split('\n')))
    row_sum = list(map(lambda row: row.count('1')%2, matrix))
    column_sum = list(map(lambda column: column.count('1')%2, zip(*matrix)))
    print(matrix)
    print(row_sum)
    print(column_sum)
    if sum(row_sum) + sum(column_sum) == 0:
        return "OK"
    if sum(row_sum) == sum(column_sum) == 1:
        return f"Change ({column_sum.index(1) + 1}, {row_sum.index(1) + 1})"
    return "Corrupt"

primes = [2, 3]
def factor_list(number: int) -> list[int]:
    """
    Challenge that returns a number's factors in a list.

    Args:
        number (int): Number to get factors from.

    Returns:
        list[int]: List of factors in a number.
    """
    result = []
    sign = -1 if number < 0 else 1
    number *= sign
    for prime in primes:
        while number%prime == 0:
            number //= prime
            result.append(prime)
    factor = prime + 2
    while number != 1:
        for prime in primes:
            if factor%prime == 0:
                break
        else:
            primes.append(factor)
            while number%factor == 0:
                number //= factor
                result.append(factor)
        factor += 2

    result[0] *= sign
    return result

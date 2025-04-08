#!/bin/env python
"""
Xchel's logic challenges testing module
"""
import pytest
from challenges import decrypt_finder, matrix_parity, factor_list, top_routes

decrypt_data = (
(
    """
    HELLO
    BYE
    ASDDSD FVSCS AS
    """,
    (0, -1)
    ),
(
    """
    HELLO
    BYE
    IFMMP CZF CSAX
    """,
    (2, 26)
    ),
(
    """
    HELLO
    BYE
    THE
    THIS
    IFMMP CZF SGD SGHR
    """,
    (2, 1)
    ),
(
    """
    HELLO
    BYE
    THE
    THIS
    IFMMPCZFUIFUIJT
    """,
    (4, 26)
    ),
)

matrix_data = (
(
    """
    1 1 1 1
    0 0 0 0
    1 1 1 1
    0 0 0 0
    """,
    "OK"
    ),
(
    """
    1 0 1 0
    0 1 0 1
    1 0 1 0
    0 1 0 1
    """,
    "OK"
    ),
(
    """
    1 0 1 0
    0 1 0 1
    1 1 1 0
    0 1 0 1
    """,
    "Change (2, 3)"
    ),
(
    """
    1 0 1 0
    0 1 1 1
    1 1 1 0
    0 1 0 1
    """,
    "Corrupt"
    ),
)

factor_data = (
        (2, [2]),
        (3, [3]),
        (-6, [-2, 3]),
        (-10, [-2, 5]),
        (18, [2, 3, 3]),
        (28, [2, 2, 7]),
        (32, [2, 2, 2, 2, 2]),
        (36, [2, 2, 3, 3]),
        (-73, [-73]),
        (-210, [-2, 3, 5, 7]),
        (-2849, [-7, 11, 37]),
        )

routes_data = (
(
    """
    example.1. A 123.123.123.1
    example.2. AAAA 1fba:1::f
    example.3. CTYPE trash
    example.4. CTYPE example.3.
    example.5. CTYPE example.1.
    example.6. CTYPE example.7.
    example.7. CTYPE example.8.
    example.8. CTYPE example.2.
    example.9. CTYPE example.10.
    example.10. CTYPE example.11.
    example.11. CTYPE example.0.
    """,
    '\n'.join("""1fba:1::f-4
    123.123.123.1-2
    """.split())
    ),
)

@pytest.mark.parametrize("string, expected", decrypt_data)
def test_decrypt_finder(string, expected):
    """
    Function that tests decrypt_finder using previously expected results.
    """
    assert decrypt_finder(string) == expected

@pytest.mark.parametrize("matrix, expected", matrix_data)
def test_matrix_parity(matrix, expected):
    """
    Function that tests matrix_parity using previously expected results.
    """
    assert matrix_parity(matrix) == expected

@pytest.mark.parametrize("number, expected", factor_data)
def test_factor_list(number, expected):
    """
    Function that tests factor_list using previously expected results.
    """
    assert factor_list(number) == expected

@pytest.mark.parametrize("string, expected", routes_data)
def test_top_routes(string, expected):
    """
    Function that tests top_routes using previously expected results.
    """
    assert top_routes(string) == expected

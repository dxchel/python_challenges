#!/bin/env python
"""
Xchel's logic challenges testing module
"""
import pytest
from tests import decrypt_finder, matrix_parity

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

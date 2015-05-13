from Executor import fivePrint, sixPrint

__author__ = 'rob'

import pytest

def test_five():
    print("NIEE!")
    assert fivePrint() == 5
def test_six():
    print("DUPA!")
    assert sixPrint() == 9
__author__ = 'rob'

import pytest

def test_five():
    print("NIEE!")
    from Executor import fivePrint
    return fivePrint() == 5
def test_six():
    print("DUPA!")
    from Executor import sixPrint
    return sixPrint() == 9
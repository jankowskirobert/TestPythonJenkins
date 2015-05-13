__author__ = 'rob'
import Executor
import pytest

def test_five():
    print("NIEE!")
    return Executor.fivePrint() == 5
def test_six():
    print("DUPA!")
    return Executor.sixPrint() == 9
__author__ = 'rob'
import Executor
import pytest

def test_five():
    return Executor.fivePrint() == 5
def test_six():
    return Executor.sixPrint() == 9
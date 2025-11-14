from byterun.interpreter.vm import Interpreter
import pytest

def test_stack():
     empty_stack = Interpreter()
     assert len(empty_stack.stack)== 0

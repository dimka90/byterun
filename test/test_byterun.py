from byterun.evm.vm import Interpreter
def test_interpreter_instance():
     empty_stack = Interpreter()
     assert len(empty_stack.stack)== 0
     assert isinstance(empty_stack ,Interpreter)



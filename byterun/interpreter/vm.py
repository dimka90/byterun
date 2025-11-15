
from  byterun.exception.errors import EmptyStackError, StackUnderflowError
from byterun.types.opcode import Opcode
from byterun.types.models import Program, Instruction
class Interpreter:
    def __init__(self):
        self.stack = []
    def load(self, data: int) ->  None:
        self.stack.append(data)
    
    def print(self) -> None:
        if len(self.stack) == 0:
            raise EmptyStackError("Nothing to print")
        result = self.stack.pop()
        print(f'Result: {result}')
     
    def add(self) -> None:
        if len(self.stack)< 2:
            raise StackUnderflowError
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)
    
    def run(self, program: Program) ->None:
        instructions = program.instructions
        args = program.numbers
        for _, instruction in enumerate(instructions):
            to_dict = instruction.model_dump()
            if to_dict['opcode'] == Opcode.LOAD:
                index = to_dict["index"]
                number_to_store = args[index]
                self.load(number_to_store)
            elif to_dict["opcode"] == Opcode.ADD:
                self.add()
            elif to_dict["opcode"] == Opcode.PRINT:
                self.print()


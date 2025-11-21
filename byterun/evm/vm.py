
from  byterun.exception.errors import EmptyStackError, StackUnderflowError
from byterun.types.opcode import Opcode
from byterun.types.models import Program
from typing import List, Dict


class Interpreter:
    def __init__(self):
        self.stack: List = []
        self.environment: Dict = {}

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

    def pop(self) -> int:
        return self.stack.pop()
    
    def load_name(self, to_dict, var_names):
        index = to_dict["index"]
        key = var_names[index]
        value_to_stack = self.environment[key]
        self.load(value_to_stack)

    def store_name(self,to_dict, var_names):
        value = self.pop()
        index = to_dict["index"]
        key = var_names[index]
        self.environment[key] = value
        
    def run(self, program: Program) ->None:
        instructions = program.instructions
        args = program.numbers
        var_names = program.var_names
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

            elif to_dict["opcode"] == Opcode.LOAD_NAME:
                self.load_name(to_dict, var_names)
            
            elif to_dict["opcode"] == Opcode.STORE_NAME:
                self.store_name(to_dict, var_names)


opcode_map = {
    Opcode.ADD: Interpreter.add,
    Opcode.LOAD: Interpreter.load,
    Opcode.LOAD_NAME: Interpreter.load_name,
    Opcode.PRINT: Interpreter.print
}
print(opcode_map)
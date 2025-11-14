from pydantic import BaseModel, Field
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Dict
from  byterun.exception.errors import EmptyStackError

class Instruction(BaseModel):
    op: Literal["ADD", "LOAD", "PRINT"]
    value: Optional[int] = Field(default = None)

class Program(BaseModel):
    instructions: List[Instruction]
    numbers: List[int]
class Interpreter:
    def __init__(self):
        self.stack = []
    def load(self, data: int) ->  None:
        self.stack.append(data)
    
    def print(self) -> None:
        if len(self.stack) == 0:
            raise EmptyStackError
        result = self.stack.pop()
        print(f'Result: {result}')
     
    def add(self) -> None:
        if len(self.stack) == 0:
            raise EmptyStackError
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        total = first_num + second_num
        self.stack.append(total)
    
    def run(self, program: Program):
        instructions = program.instructions
        args = program.numbers

        for _, instruction in enumerate(instructions):
            to_dict = instruction.model_dump()
            if to_dict['op'] == "LOAD":
                self.load(args)
                




    #  def run_code(self, what_to_execute):
    #     instructions = what_to_execute["instructions"]
    #     numbers = what_to_execute["numbers"]
    #     for each_step in instructions:
    #         instruction, argument = each_step
    #         if instruction == "LOAD_VALUE":
    #             number = numbers[argument]
    #             self.LOAD_VALUE(number)
    #         elif instruction == "ADD_TWO_VALUES":
    #             self.ADD_TWO_VALUES()
    #         elif instruction == "PRINT_ANSWER":
    #             self.PRINT_ANSWER()
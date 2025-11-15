from pydantic import BaseModel, Field
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Dict
from  byterun.exception.errors import EmptyStackError

class Instruction(BaseModel):
    opcode: Literal["ADD", "LOAD", "PRINT"]
    index: Optional[int] = Field(default = None)

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
    
    def run(self, program: Program) ->None:
        instructions = program.instructions
        args = program.numbers
        for _, instruction in enumerate(instructions):
            to_dict = instruction.model_dump()
            if to_dict['opcode'] == "LOAD":
                index = to_dict["index"]
                number_to_store = args[index]
                self.load(number_to_store)
            if to_dict["opcode"] == "ADD":
                self.add()
            if to_dict["opcode"] == "PRINT":
                self.print()


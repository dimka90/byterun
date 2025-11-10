from pydantic import BaseModel
from dataclasses import dataclass, field
from typing import List
from exception.errors import EmptyStackError


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
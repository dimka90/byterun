from pydantic import BaseModel, Field
from typing import List, Optional
from byterun.types.opcode import Opcode

class Instruction(BaseModel):
    opcode: Opcode
    index: Optional[int] = Field(default = None)

class Program(BaseModel):
    instructions: List[Instruction]
    numbers: List[int]
    var_names: Optional[List[str]] = Field(default=None)

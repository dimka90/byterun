from pydantic import BaseModel, Field
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Dict
from byterun.types.opcode import Opcode
class Instruction(BaseModel):
    opcode: Opcode
    index: Optional[int] = Field(default = None)

class Program(BaseModel):
    instructions: List[Instruction]
    numbers: List[int]

from enum import Enum

class Opcode(str, Enum):
    LOAD = "LOAD"
    PRINT = "PRINT"
    ADD = "ADD"
from enum import Enum

class Opcode(str, Enum):
    LOAD = "LOAD"
    PRINT = "PRINT"
    ADD = "ADD"
    LOAD_NAME = "LOAD_NAME"
    STORE_NAME = "STORE_NAME"


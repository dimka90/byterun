from byterun.interpreter.vm import  Interpreter, Program
import sys
vm = Interpreter()
# raw = {
#     "instructions": [
#         {"opcode": "LOAD", "index": 0},
#         {"opcode": "LOAD", "index": 1},
#         {"opcode": "ADD"},
#         {"opcode": "PRINT"}
#     ],
#     "numbers": [7, 5]
# }
raw = {
    "instructions": [
        {"opcode": "LOAD", "index": 0},
        {"opcode": "LOAD", "index": 1},
        {"opcode": "ADD"},
        {"opcode": "LOAD", "index": 2},
        {"opcode": "ADD"},
        {"opcode": "PRINT"}
    ],
    "numbers": [7, 5, 8]
}
program = Program(**raw)
vm.run(program)

# print(vm.stack)
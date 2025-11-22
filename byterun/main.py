from byterun.evm.vm import  Interpreter, Program
from byterun.evm.memory import Memory
vm = Interpreter()
raw = {
    "instructions": [
        {"opcode": "LOAD", "index": 0},
        {"opcode": "STORE_NAME", "index": 0},
        {"opcode": "LOAD", "index": 1},
        {"opcode": "STORE_NAME", "index": 1},
        {"opcode": "LOAD_NAME", "index": 0},
        {"opcode": "LOAD_NAME", "index": 1},
        {"opcode": "ADD"},
        {"opcode": "PRINT"}
    ],
    "numbers": [10, 12],
    "var_names": ["a", "b"]
}
print("======================================")
memory = Memory()
memory.store(0, 30)
memory.store(0, 1)
memory.store(90, 1)
result = memory.load(0)
print("30", result)
result1 = memory.load(90)
print("90", result1)
print("======================================")
program = Program(**raw)
vm.run(program)
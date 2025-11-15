from byterun.interpreter.vm import  Interpreter, Program
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
program = Program(**raw)
vm.run(program)
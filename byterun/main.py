from byterun.interpreter.vm import  Interpreter, Program
import sys
vm = Interpreter()
vm.load(5)
vm.load(90)
print(vm.stack)
raw = {
    "instructions": [
        {"op": "LOAD", "arg": 0},
        {"op": "LOAD", "arg": 1},
        {"op": "ADD"},
        {"op": "PRINT"}
    ],
    "numbers": [7, 5]
}
print(sys.path)

program = Program(**raw)
vm.run(program)

print(vm.stack)
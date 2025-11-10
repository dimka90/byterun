from interpreter.vm import  Interpreter
vm = Interpreter()
vm.load(5)
vm.load(90)
vm.add()
vm.print()
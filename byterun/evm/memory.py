class Memory:
    """EVM Memory - Byte-addressable volatile memory"""
    def __init__(self):
        self.data = bytearray()

    def extend(self, offset, size)-> int:
        new_size = offset + size
        old_size = len(self.data)

        if new_size > old_size:
            seize_to_compute = new_size -old_size
            self.data.extend(b'\0x00' * seize_to_compute )
        return 0
    
    def store(self, offset: int, value: int) -> None:
        self.extend(offset, 32)
        self.data[offset:offset+ 32] = value.to_bytes(32, 'big')

    def load(self, offset: int) -> int:
        self.extend(offset, 32)
        value_to_return = self.data[offset:offset + 32]
        print(value_to_return)
        return int.from_bytes(value_to_return, 'big')
    
    def store8(self, offset: int, value: int) -> None:
        self.extend(offset, 1)
        self.data[offset: offset +1] = value & 0xFF
        

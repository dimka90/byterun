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
        self.extend(offset, value)
        self.data[offset:offset+ 32] = value.to_bytes(32, 'big')

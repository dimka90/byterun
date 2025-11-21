class Memory:
    """EVM Memory - Byte-addressable volatile memory"""
    def __init__(self):
        self.data = bytearray()

    def extend(self, offset, size):
        new_size = offset + size
        old_size = len(self.data)
        if new_size > old_size:
            seize_to_compute = new_size -old_size
            self.data.extend(b'\0x00' * seize_to_compute )
            print(self.data)
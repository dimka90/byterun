from .constants.constants import BYTE_SIZE, WORD_SIZE

class Memory:
    """EVM Memory - Byte-addressable volatile memory"""
    def __init__(self):
        self.data = bytearray()

    def extend(self, offset, size)-> int:
        """Expands memory to contain to store value"""
        new_size = offset + size
        old_size = len(self.data)

        if new_size > old_size:
            seize_to_compute = new_size -old_size
            self.data.extend(b'\x00' * seize_to_compute )
            
            return self._expansion_cost(old_size, new_size)
        return 0
    
    def store(self, offset: int, value: int) -> None:
        self.extend(offset, WORD_SIZE)
        self.data[offset:offset+ WORD_SIZE] = value.to_bytes(WORD_SIZE, 'big')

    def store8(self, offset: int, value: int) -> None:
        """write 8 bit to the memory"""
        self.extend(offset, BYTE_SIZE)
        self.data[offset] = value & 0xFF

    def load(self, offset: int) -> int:
        "Read value from the memory"
        self.extend(offset, WORD_SIZE)
        value_to_return = self.data[offset:offset + WORD_SIZE]
        return int.from_bytes(value_to_return, 'big')
    
    def size(self) -> int:
        "size of data"
        return len(self.data)
    
    def _expansion_cost(self, old_size: int, new_size: int) -> int:
        old_words = (old_size + 31) // WORD_SIZE
        new_words = (new_size + 31) // WORD_SIZE
        gas = (new_words - old_words ) * 3

        return gas
   


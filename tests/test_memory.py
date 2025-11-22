from byterun.evm.memory import Memory
from byterun.evm.constants.constants import BYTE_SIZE, WORD_SIZE
import pytest

@pytest.fixture
def memory():
    " Returns a fresh memomry instance"
    return Memory()

def test_empty_memory(memory):
    assert len(memory.data) == 0

def test_store(memory):
    memory.store(0, 10)
    assert len(memory.data) == WORD_SIZE
    assert memory.load(0) == 10

@pytest.mark.parametrize("offset, value", [(0,12), (12, 30), (32,0xFF)])
def test_store8_various_values(memory, offset, value):
    memory.store8(offset, value)
    assert memory.data[offset] == value
from byterun.evm.memory import Memory
from byterun.evm.constants.constants import BYTE_SIZE, WORD_SIZE
import pytest

@pytest.fixture
def memory():
    " Returns a fresh memomry instance"
    return Memory()
def test_data_len(memory):
    assert len(memory.data) == 0

def test_store(memory):
    memory.store(0, 10)
    assert len(memory.data) == WORD_SIZE
    assert memory.load(0) == 10

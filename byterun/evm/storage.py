from typing import Dict
class Storage:
    "Permanent Storage"
    def __init__(self):
        self.data: Dict[int, int] = {}
        self.original: Dict[int, int] = {}

    def load(self, key: int) ->int:
        """Load value from storage"""
        return self.data.get(key, 0)
    
    def store(self, key: int, value: int) -> int:
        pass


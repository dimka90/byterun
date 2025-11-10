from pydantic import BaseModel, Field
from dataclasses import dataclass
from typing import List

class Interpreter:
    def __init__(self):
        self.stack: List[int] = []
from typing import List, Dict

class Teacher:
    def __init__(self, id: str, subjects: List[str], availability: Dict[str, List[int]]):
        self.id = id
        self.subjects = subjects
        self.availability = availability

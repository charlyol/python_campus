from dataclasses import dataclass, field
from typing import List

from python_project.guardian import Guardian


@dataclass
class Player:
    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)

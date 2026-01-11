
from dataclasses import dataclass

@dataclass
class Team:
    id: int
    year: int
    team_code: str
    name: str
    salari: float

    def __str__(self):
        return f' {self.team_code} ({self.name})'

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return self.id == other.id

from typing import Sequence, NamedTuple

class Job(NamedTuple):
    """Tuple storing data about job - its ID and times needed to complete for each machine."""
    nr: int
    czas: Sequence[int]

    def __eq__(self, other):
        return self.nr == other.nr
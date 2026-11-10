# This is where I'm stuffing the class definition of the frog.
from enum import Enum
from typing import Generic, TypeVar

T = TypeVar("T")

class FrogState(Enum):
    ACTIVE = 1
    BURROWED = 2
    DEAD = 3


class RainFrog (Generic[T]):
    genome: T
    parent1: int | None
    parent2: int | None
    state: FrogState
    generation: int
    fitness: float | None
    identity: int
    
    def __init__(self,
                 genome: T,
                 identity: int,
                 generation: int = 0,
                 parent1: int | None = None,
                 parent2: int | None = None,) -> None:
        self.genome = genome
        self.parent1 = parent1
        self.parent2 = parent1
        self.state = FrogState.ACTIVE
        self.generation = generation
        self.fitness = None
        self.identity = idendity

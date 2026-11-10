# I am absolutely flabbergasted at generics
# Goal here is to like. Abstract the domain into a generic so that we can put ANY optimization problem
# into this bit. 

from typing import Generic, TypeVar
from collections.abc import Callable

T = TypeVar("T")
S = TypeVar("S")


class DomainExpansion(Generic[T], Generic[S]):
    Mutation: Callable[[T,T], T]
    Crossover: Callable[[T,T], T]
    GenomeGen: Callable[[],T]
    SearchSpace: S
    FitnessEval: Callable[[T],float]
    GenomeEval: Callable[[T], bool]
    def __init__(
            self,
            Mutation: Callable[[T, T], T],
            Crossover: Callable[[T, T], T],
            GenomeGen: Callable[[], T],
            SearchSpace: S,
            FitnessEval: Callable[[T], float],
            GenomeEval: Callable[[T], bool],
    ) -> None:
        self.Mutation = Mutation
        self.Crossover = Crossover
        self.GenomeGen = GenomeGen
        self.SearchSpace = SearchSpace
        self.FitnessEval = FitnessEval
        self.GenomeEval = GenomeEval



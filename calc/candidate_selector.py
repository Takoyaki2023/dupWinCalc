from abc import *
from typing import List
import random


class CandidateSelector(metaclass=ABCMeta):
    def __init__(self, active_user_count: int):
        self.active_user_count = active_user_count

    @abstractmethod
    def select_candidates(self, candidate_count: int) -> List[int]:
        pass


class SimpleCandidateSelector(CandidateSelector):
    def __init__(self, active_user_count: int):
        super().__init__(active_user_count)
        self.user_pool = range(self.active_user_count)

    def select_candidates(self, candidate_count: int) -> List[int]:
        return random.sample(self.user_pool, k=candidate_count)


class HeavyUserCandidateSelector(CandidateSelector):
    def __init__(self, active_user_count: int, heavy_user_count: int):
        super().__init__(active_user_count)
        self.heavy_user_count = heavy_user_count
        self.user_pool = range(heavy_user_count, active_user_count)

    # heavy user들은 매 이벤트 참여한다고 가정.
    def select_candidates(self, candidate_count: int) -> List[int]:
        candidates = [i for i in range(self.heavy_user_count)]

        extra_candidates = random.sample(self.user_pool, k=candidate_count - self.heavy_user_count)

        candidates.extend(extra_candidates)

        return candidates

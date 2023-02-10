from typing import List
from collections import Counter
import random
from .candidate_selector import CandidateSelector


class EventInfo:
    def __init__(self, prize_count: int, candidate_count: int):
        self.prize_count: int = prize_count
        self.candidate_count: int = candidate_count


class SimulatingResult:
    def __init__(self):
        self.dup_winning_counter: Counter = Counter()

    def add_single_person_result(self, won_count: int):
        self.dup_winning_counter[won_count] += 1


class EventResult:
    def __init__(self, won_users: List[int]):
        self.won_users = won_users


class DrawSimulator:
    def simulate_once(self, event_infos: List[EventInfo], selector: CandidateSelector) -> SimulatingResult:
        user_winning_counter: Counter = Counter()

        for event_info in event_infos:
            candidates: List[int] = selector.select_candidates(event_info.candidate_count)
            event_result = self.__draw(event_info, candidates)
            user_winning_counter.update(event_result.won_users)

        return self.__generate_simulating_result(user_winning_counter)

    def __generate_simulating_result(self, user_winning_counter: Counter) -> SimulatingResult:
        simulating_result = SimulatingResult()

        for winning_count in user_winning_counter:
            simulating_result.add_single_person_result(user_winning_counter[winning_count])

        return simulating_result

    def __draw(self, event_info: EventInfo, candidates: List[int]) -> EventResult:
        won_users: List[int] = random.sample(candidates, k=event_info.prize_count)
        return EventResult(won_users=won_users)

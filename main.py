from input_generator.static_generator import generate_with_static_values
from calc.calculator import *
from calc.candidate_selector import *

SIMPLE_SELECTOR_MODE = 1
HEAVY_USER_SELECTOR_MODE = 2


def simulate(mode: int, heavy_user_count: int = 82):
    active_user_count, event_infos = generate_with_static_values()
    simulator = DrawSimulator()

    trials = 1000
    total_dup_winning_counter = Counter()

    selector = None
    if mode == SIMPLE_SELECTOR_MODE:
        selector = SimpleCandidateSelector(active_user_count)
    else:
        selector = HeavyUserCandidateSelector(active_user_count, heavy_user_count)

    for i in range(trials):
        simulating_result = simulator.simulate_once(event_infos, selector)
        single_trial_dup_winning_counter = simulating_result.dup_winning_counter

        for winning_streak in range(2, 6):
            total_dup_winning_counter[winning_streak] += single_trial_dup_winning_counter[winning_streak]

    total_dup_count = sum(total_dup_winning_counter.values())
    print("dup winner per simulation is {0}\n".format(total_dup_count/1000))

    for winning_streak in range(2, 6):
        print("{0}-game streak winner per simulation is {1}".format(winning_streak,
                                                                    total_dup_winning_counter[winning_streak]/1000))


if __name__ == '__main__':
    simulate(HEAVY_USER_SELECTOR_MODE, 30)
    # simulate(SIMPLE_SELECTOR_MODE)

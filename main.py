from input_generator.static_generator import generate_with_static_values
from calc.calculator import *
from calc.candidate_selector import *

SIMPLE_SELECTOR_MODE = 1
HEAVY_USER_SELECTOR_MODE = 2


def simulate(mode: int, heavy_user_count: int = 82):
    active_user_count, event_infos = generate_with_static_values()
    simulator = DrawSimulator()

    trials = 1000
    five_win_streak_user_count = 0
    four_win_streak_user_count = 0
    dup_winner_count = 0

    selector = None
    if mode == SIMPLE_SELECTOR_MODE:
        selector = SimpleCandidateSelector(active_user_count)
    else:
        selector = HeavyUserCandidateSelector(active_user_count, heavy_user_count)

    for i in range(trials):
        simulating_result = simulator.simulate_once(event_infos, selector)
        dup_winning_counter = simulating_result.dup_winning_counter

        if dup_winning_counter[4] > 0:
            four_win_streak_user_count += 1

        if dup_winning_counter[5] > 0:
            five_win_streak_user_count += 1

        dup_winner_count += dup_winning_counter[2]
        dup_winner_count += dup_winning_counter[3]
        dup_winner_count += dup_winning_counter[4]
        dup_winner_count += dup_winning_counter[5]

    print("dup winner per simulation is {0}\n".format(dup_winner_count/1000))
    print("4-game streak winner per simulation is {0}\n".format(four_win_streak_user_count/1000))
    print("5-game streak winner per simulation is {0}\n".format(five_win_streak_user_count/1000))


if __name__ == '__main__':
    simulate(HEAVY_USER_SELECTOR_MODE, 20)
    # simulate(SIMPLE_SELECTOR_MODE)

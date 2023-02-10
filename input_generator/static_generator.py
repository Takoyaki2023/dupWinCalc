from typing import List, Tuple
from calc.calculator import EventInfo


def generate_with_static_values() -> Tuple[int, List[EventInfo]]:
    ## based on this posts https://gall.dcinside.com/mgallery/board/view/?id=mugimido&no=155597&s_type=search_subject_memo&s_keyword=.ED.99.95.EB.A5.A0&page=1

    event_info_lists = [
        [30, 861], [30, 334], [13, 313], [43, 1111], [15, 5923],
        [10, 2804], [3, 2539], [1, 2420], [50, 509], [20, 730],
        [20, 1947], [42, 1841], [24, 1728], [254, 3536], [23, 2500],
        [23, 1319], [23, 1954], [23, 1392], [30, 185], [23, 339],
        [23, 251], [23, 332], [30, 201], [23, 384], [28, 567],
        [50, 382], [23, 488], [23, 617]
    ]

    event_infos = []

    for event_info_tup in event_info_lists:
        event_infos.append(EventInfo(event_info_tup[0], event_info_tup[1]))

    active_user_count = 5923

    return active_user_count, event_infos

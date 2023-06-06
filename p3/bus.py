from re import fullmatch
import json




def bus_info(j_son):
    validation = {
        'bus_id': {'type': int, 're_pattern': r"\d+"},
        'stop_id': {'type': int, 're_pattern': r"\d+"},
        'stop_name': {'type': str, 're_pattern': r"[\w\s\.]+"},
        'next_stop': {'type': int, 're_pattern': r"\d+"},
        'stop_type': {'type': str, 're_pattern': r"[SOF]?"},
        'a_time': {'type': str, 're_pattern': r"\d{2}:\d{2}"}
    }

    err_lst = dict.fromkeys(validation, 0)

    routes = json.loads(j_son)

    for route in routes:
        for key, val in route.items():
            if not isinstance(val, validation[key]['type']) \
                    or fullmatch(validation[key]['re_pattern'], str(val)) is None:
                err_lst[key] += 1

    print(f"Type and required field validation: {sum(err_lst.values())} errors")
    for k, v in err_lst.items():
        print(f"{k}: {v}")
    for route in routes:
        for key, val in route.items():
            if not isinstance(val, validation[key]['type']) \
                    or fullmatch(validation[key]['re_pattern'], str(val)) is None:
                err_lst[key] += 1

    print(f"Type and required field validation: {sum(err_lst.values())} errors")
    for k, v in err_lst.items():
        print(f"{k}: {v}")

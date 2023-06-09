# ruff: noqa: E501
from datetime import datetime, timedelta
import sys


def main(start: str = "", goal_time: str = "", goal_duration: str = ""):
    def time_from_str(s: str):
        if s.find(":") != -1:
            pass
        else:
            match len(s):
                case 4:
                    s = f"{s[:2]}:{s[2:]}"
                case 3:
                    s = f"{s[0]}:{s[1:]}"
                case 2 | 1:
                    s = f"{s}:00"
        t = datetime.strptime(s, "%H:%M")
        return t

    if len(start) != "":
        start_time: datetime = time_from_str(start)
    else:
        start_time: datetime = time_from_str("Start time ► ")

    current_time = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M")
    delta = current_time - start_time

    s = f'{start_time.strftime("%H:%M")} - ({str(delta)[:-3]}) - {current_time.strftime("%H:%M")}'

    time_left = None
    if goal_time != "":
        goal_time_t = time_from_str(goal_time)
        time_left = goal_time_t - current_time
    elif goal_duration != "":
        goal_duration_t = time_from_str(goal_duration)
        goal_duration_t = timedelta(hours=goal_duration_t.hour, minutes=goal_duration_t.minute)
        time_left = goal_duration_t - delta
        goal_time_t= current_time + time_left

    if time_left is not None:
        s += f' - ({str(time_left)[:-3]}) - {goal_time_t.strftime("%H:%M")}'
        s += f'\nTotal: {str(delta+time_left)[:-3]}'
        
    return s


if __name__ == "__main__":
    print(main(*sys.argv[1:]))

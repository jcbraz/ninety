from datetime import datetime, timedelta
import re

time_pattern = re.compile(r"[01]?[0-9]\s?:\s?[0-5][0-9]")
sleep_hours_pattern = re.compile(r"[0-9]\s?(\.[0-9])?")


def recommended_bed_wakeup_time_based_on_hours_of_sleep():
    print("Enter Bed Time and hours of sleep required, separated by commas\n")
    print("Example: 22:30,8\n")

    user_input = input()
    user_input = user_input.strip().split(",")

    while (
        not time_pattern.match(user_input[0])
        or not sleep_hours_pattern.match(user_input[1])
    ):
        print("Invalid input. Try again\n")
        user_input = input()
        user_input = user_input.split(",")

    bed_time = datetime.strptime(user_input[0], "%H:%M")
    bed_datetime = datetime(2023, 1, 1, bed_time.hour, bed_time.minute)

    hours_of_sleep = float(user_input[1])

    num_of_cycles = hours_of_sleep // 1.5

    first_recommendation = bed_datetime + timedelta(minutes=90 * num_of_cycles)

    second_recommendation = first_recommendation + timedelta(minutes=90)

    print(
        f"Suggested Wakeup Time: {first_recommendation.strftime('%H:%M')} with {(first_recommendation - bed_datetime).total_seconds() / 3600.0} hours of sleep or {second_recommendation.strftime('%H:%M')} with {((second_recommendation - bed_datetime).total_seconds() / 3600.0)}\n"
    )


def recommended_bed_wakeup_time_based_on_specific_wakeup_time():
    print("Enter Bed Time and Wakeup Time, separated by commas\n")
    print("Example: 22:30,6:30\n")

    user_input = input()
    user_input = user_input.split(",")

    while not time_pattern.match(user_input[0]) or not time_pattern.match(
        user_input[1]
    ):
        print("Invalid input. Try again\n")
        user_input = input()
        user_input = user_input.split(",")

    bed_time = datetime.strptime(user_input[0], "%H:%M")
    wakeup_time = datetime.strptime(user_input[1], "%H:%M")

    bed_datetime = datetime(2023, 1, 1, bed_time.hour, bed_time.minute)
    if wakeup_time.hour < bed_time.hour:
        wakeup_datetime = datetime(2023, 1, 2, wakeup_time.hour, wakeup_time.minute)
    else:
        wakeup_datetime = datetime(2023, 1, 1, wakeup_time.hour, wakeup_time.minute)

    sleep_time = (wakeup_datetime - bed_datetime).total_seconds() / 3600.0

    num_of_cycles = sleep_time // 1.5

    first_recommendation = bed_datetime + timedelta(minutes=90 * num_of_cycles)

    second_recommendation = first_recommendation + timedelta(minutes=90)

    print(
        f"Suggested WakeUp Time: {first_recommendation.strftime('%H:%M')} with {(first_recommendation - bed_datetime).total_seconds() / 3600.0} hours of sleep or {second_recommendation.strftime('%H:%M')} with {((second_recommendation - bed_datetime).total_seconds() / 3600.0)}\n"
    )

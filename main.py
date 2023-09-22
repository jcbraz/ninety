from datetime import datetime, timedelta


def recommended_bed_wakeup_time_based_on_hours_of_sleep():
    print("Enter Bed Time and hours of sleep required, separated by commas\n")
    print("Example: 22:30,8\n")

    user_input = input()
    user_input = user_input.split(",")

    bed_time = datetime.strptime(user_input[0], "%H:%M")
    bed_datetime = datetime(2023, 1, 1, bed_time.hour, bed_time.minute)

    hours_of_sleep = int(user_input[1])

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

    bed_time = datetime.strptime(user_input[0], "%H:%M")
    wakeup_time = datetime.strptime(user_input[1], "%H:%M")

    bed_datetime = datetime(2023, 1, 1, bed_time.hour, bed_time.minute)
    wakeup_datetime = datetime(2023, 1, 2, wakeup_time.hour, wakeup_time.minute)

    sleep_time = (wakeup_datetime - bed_datetime).total_seconds() / 3600.0

    num_of_cycles = sleep_time // 1.5

    first_recommendation = bed_datetime + timedelta(minutes=90 * num_of_cycles)

    second_recommendation = first_recommendation + timedelta(minutes=90)

    print(
        f"Suggested WakeUp Time: {first_recommendation.strftime('%H:%M')} with {(first_recommendation - bed_datetime).total_seconds() / 3600.0} hours of sleep or {second_recommendation.strftime('%H:%M')} with {((second_recommendation - bed_datetime).total_seconds() / 3600.0)}\n"
    )


def main():
    user_input = input(
        "Select an option:\n"
        "1 - Recommended Bed/Wakeup Time based on specific hours of sleep\n"
        "2 - Recommended Bed/Wakeup Time based on specific Wakeup Time\n"
    )

    while user_input not in ["1", "2"]:
        print("Invalid input\n")
        user_input = input(
            "Select an option:\n"
            "1 - Recommended Bed/Wakeup Time based on specific hours of sleep\n"
            "2 - Recommended Bed/Wakeup Time based on specific Wakeup Time\n"
        )

    if user_input == "1":
        recommended_bed_wakeup_time_based_on_hours_of_sleep()
    elif user_input == "2":
        recommended_bed_wakeup_time_based_on_specific_wakeup_time()
        pass


if __name__ == "__main__":
    main()

from recommendations import recommended_bed_wakeup_time_based_on_hours_of_sleep, recommended_bed_wakeup_time_based_on_specific_wakeup_time

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

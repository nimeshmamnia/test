def parse_time(time_str):
    # Parse time string to extract hours and minutes
    if ':' in time_str:
        time_parts = time_str.split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
    else:
        hours = int(time_str)
        minutes = 0
    return hours, minutes


def sum_timesheet(filename):
    total_hours = 0
    total_minutes = 0  # Initialize total minutes
    with open(filename, "r") as timesheet_file:
        # Read each line from the file
        for time_range in timesheet_file:
            check_in, check_out = time_range.split('-')
            check_in_hours, check_in_minutes = parse_time(check_in.strip())
            check_out_hours, check_out_minutes = parse_time(check_out.strip())

            # Calculate work hours for each time range
            work_hours = check_out_hours - check_in_hours
            work_minutes = check_out_minutes - check_in_minutes

            if work_minutes < 0:
                # Adjust for negative minutes (e.g., check-in 2:30, check-out 4)
                work_hours -= 1
                work_minutes += 60

        total_hours += work_hours
        total_minutes += work_minutes

    # Convert extra minutes to hours if needed
    total_hours += total_minutes // 60
    total_minutes %= 60

    return total_hours, total_minutes


filename = input("Enter text file with check in and check out times: ")
total_work_hours, total_work_minutes = sum_timesheet(filename)
print(f"Total work hours: {total_work_hours} hours and {total_work_minutes} minutes")

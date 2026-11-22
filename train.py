def find_seat_iterative(seats, target_seat):
    low = 0
    high = len(seats) - 1
    checks = 0

    while low <= high:
        checks += 1
        mid = (low + high) // 2
        current = seats[mid]

        if current["seat"] == target_seat:
            if current["is_free"]:
                return f"Seat {target_seat} is available! (Checks: {checks})"
            else:
                return f"Seat {target_seat} is already taken. (Checks: {checks})"
        
        elif current["seat"] < target_seat:
            low = mid + 1
        else:
            high = mid - 1

    return f"Seat {target_seat} does not exist on this train. (Checks: {checks})"

import sys


# Regular fcfs
def fcfs(requests, initial_position):
    # Set starting position
    current_position = initial_position
    # Initialize total head movements to 0
    total_head_movements = 0

    # Loop through requests
    for request in requests:
        # Calculate movement
        head_movement = abs(request - current_position)
        # Increment movement
        total_head_movements += head_movement
        # Move head position
        current_position = request

    return total_head_movements


# fcfs with rearranging input file
def optimized_fcfs(requests, initial_position):
    # Calculate distance from initial position to innermost and outermost request
    highest_difference = abs(initial_position - max(requests))
    lowest_difference = abs(initial_position - min(requests))
    # Sort requests ascending or descending depending on which difference is smaller
    if lowest_difference < highest_difference:
        requests.sort()
    else:
        requests.sort(reverse=True)

    # Use regular fcfs with the now rearranged list
    result = fcfs(requests, initial_position)

    return result


# SCAN
def SCAN(requests, initial_position):
    # Head movement direction (1 for moving towards outermost cylinder, -1 for moving towards innermost cylinder)
    direction = -1

    # Copy so that the original request list doesn't get emptied
    local_requests = requests.copy()

    # Initialize total head movements
    total_head_movements = 0

    # Set starting position
    current_position = initial_position

    # Run until all requests served
    while local_requests:
        # Check if current position has a request
        while current_position in local_requests:
            # Service the request
            local_requests.remove(current_position)

        # Update total head movements
        total_head_movements += 1

        # Check if head has reached an end
        if current_position == 0 or current_position == 4999:
            # Change direction
            direction *= -1

        # Move the head in the current direction
        current_position += direction

    # Decrement by 1 to account for the 1 increment at the very first run through the loop (iniial position)
    return total_head_movements - 1


# C SCAN
def C_SCAN(requests, initial_position):
    # Initialize total head movements
    total_head_movements = 0

    # Copy so that the original request list doesn't get emptied
    local_requests = requests.copy()

    # Set initial position
    current_position = initial_position

    # Run until all requests served
    while local_requests:
        # Check if current position has a request
        while current_position in local_requests:
            # Service the request
            local_requests.remove(current_position)

        # Update total head movements
        total_head_movements += 1

        # If head reaches innermost cylinder, move to outermost cylinder
        if current_position == 0:
            current_position = 4999
            total_head_movements += 4999

        # Move head
        current_position -= 1

    # Decrement by 1 for the same reason as SCAN
    return total_head_movements - 1


def main():
    # Check if arguments in cmd are correct
    if len(sys.argv) != 3:
        print("Usage: python program_name.py initial_position input_file")
        return

    # Get initial position and input file name from cmd arguments
    initial_position = int(sys.argv[1])
    input_file = sys.argv[2]

    # Read input file
    with open(input_file, 'r') as file:
        requests = [int(line.strip()) for line in file]

    # Calculate total head movements using FCFS
    total_head_movements_fcfs = fcfs(requests, initial_position)
    total_head_movements_scan = SCAN(requests, initial_position)
    total_head_movements_c_scan = C_SCAN(requests, initial_position)
    total_head_movements_optimized_fcfs = optimized_fcfs(requests, initial_position)

    # Output the result
    print("\nTotal head movements using FCFS:", total_head_movements_fcfs)
    print("Total head movements using optimized FCFS:", total_head_movements_optimized_fcfs)
    print("Total head movements using SCAN:", total_head_movements_scan)
    print("Total head movements using C SCAN:", total_head_movements_c_scan)


if __name__ == "__main__":
    main()

def selection_sort(arr):
    n = len(arr)
    step_count = 0  # Variable to track steps with changes

    # Traverse through all array elements
    for i in range(n):
        # Assume the current position has the minimum element
        min_index = i

        # Find the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # If the minimum element is not at the current position, swap it
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            step_count += 1  # Increment step count only if a swap happens
            print(f"Step {step_count}: {arr}")  # Print only after a swap

    return arr


# Taking user input for array
def take_input():
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    return arr


# Main function to execute the selection sort
if __name__ == "__main__":
    arr = take_input()
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

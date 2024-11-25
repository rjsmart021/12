# task one

def generate_squares(n):
    return [i**2 for i in range(1, n+1)]

# Example:
print(generate_squares(5))  # Output: [1, 4, 9, 16, 25]

# Time complexity: O(n)
# Space complexity: O(n)

# task two

def reverse_sublist(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# Example:
print(reverse_sublist([1, 2, 3, 4, 5], 1, 3))  # Output: [1, 4, 3, 2, 5] the sublist [2, 3, 4] is reversed

# Time complexity: O(n)
# Space complexity: O(n)

# task three

def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1

    # Append remaining elements of lst1 or lst2
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])

    return merged_list

# Example:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

# Time complexity: O(n + m)
# Space complexity: O(n + m)

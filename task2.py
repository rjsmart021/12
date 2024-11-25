# Task 1

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Create a copy of the first dictionary
    merged_dict.update(dict2)   # Update with the second dictionary
    return merged_dict

# Example:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}
# preserves the value of the second dictionary if the key is the same

# Time complexity: O(n + m)
# Space complexity: O(n + m)

# Task 2

def intersect_dictionaries(dict1, dict2):
    return {k: dict1[k] for k in dict1 if k in dict2}

# Example:
dict1 = {'a': 1, 'b': 2, 'd': 5}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(intersect_dictionaries(dict1, dict2))  # Output: {'b': 2, 'd': 5}

# Time complexity: O(n)
# Space complexity: O(k)

# Task 3

def count_word_frequencies(word_list):
    frequency_dict = {}
    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

# Example:
word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_word_frequencies(word_list))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# Time complexity: O(n)
# Space complexity: O(m)

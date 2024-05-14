def count_occurrences(string, char):
    count = 0
    for ch in string:
        if ch == char:
            count += 1
    return count

string = "helloooo world"
char = "o"
times = count_occurrences(string, char)
print(f"The character '{char}' occurs {times} times in the string.")

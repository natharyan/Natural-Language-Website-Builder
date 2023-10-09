def find_first_occurrence(strings, text):
    return min(strings, key=lambda string: text.index(string) if string in text else float('inf'))

list1 = ["apple", "banana", "cherry"]
text = "I like banana more than apple, but cherry is also good."

first_occurrence = find_first_occurrence(list1, text)
print("First occurring string:", first_occurrence)
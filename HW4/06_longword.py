def get_longest_word(s: str) -> str:
    return max(s.split(), key=len)

print(get_longest_word("Python is simple and effective!"))
print(get_longest_word("Any pythonista like namespaces a lot."))
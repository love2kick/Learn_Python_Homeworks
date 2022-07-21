def split_by_index(s: str, indexes: list[int]) -> list[str]:
    if indexes[-1] > len(s):
        return [s]
    else:
        return [s[i:j] for i, j in zip([0] + indexes, indexes + [len(s)])]

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))
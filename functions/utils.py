from collections import Counter

def most_frequent(lst):
    counter = Counter(s for s in lst if isinstance(s, str))
    if not counter:
        return []
    max_count = max(counter.values())
    return [s for s, count in counter.items() if count == max_count]

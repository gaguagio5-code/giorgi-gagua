score: list [tuple[str, int]] = [
    ("Alice", 45),
    ("Bob", 82),
    ("Charlie", 67),
    ("David", 38),
    ("Eve", 90),
    ("Frank", 55),
    ("Grace", 72)
]
filtered_scores = list(filter(lambda score: score[1] >= 50, score))
mapped_scores = boosted = list(map(lambda score: min(score[1] + 5, 100), filtered_scores))
print("Filtered Scores (>= 50):", filtered_scores)
print("Boosted Scores (with +5, max 100):", mapped_scores)  

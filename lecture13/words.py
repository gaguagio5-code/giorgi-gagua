words = ["python", "generator", "yield", "code", "ai", "developer"]

long_words = (p for p in words if len(p) > 4)
highlighted_words = (word.upper() for word in long_words)
for word in highlighted_words:
    print(word)
scores = [80]

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

scores.remove(45)

average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print(f"Average score: {average}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")

scores.sort()
print(f"Sorted scores: {scores}")

passed_scores = [score for score in scores if score >= 60]
print(f"Passed scores: {passed_scores}")
def above_hundred(score):
	if score >= 100:
		return True
	else: return False

scores = [96, 47, 113, 89, 100, 102]

print(len(list(filter(above_hundred, scores))))

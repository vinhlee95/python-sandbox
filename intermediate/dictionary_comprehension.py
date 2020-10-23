"""
Dictionary comprehension

🔑 Generator comprehension
- Beneficial when interating over a huge list
- Generator does not store the entire list in the memory => migitate MemoryError issue
- Much faster than normal list comprehension

📚
https://realpython.com/introduction-to-python-generators/#using-generators

"""
scores = [13, 23, 30, 41, 12, 12, 23]
# 🛠 Create a dictionary of player score
# {player1: 13, player2: 23...}
player_score = {f'Player {index}: {score}' for index, score in enumerate(scores)}
# print('Player scores are:', sorted(player_score))

# 🛠 Set comprehension
unique_scores = {scores for scores in scores}
# print(unique_scores)
# 🤔 But not sure why would we do that, if we could simply do:
# print(set(scores))

# 🛠 Generator comprehension
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
for num in gen_exp:
	print(num)

import timeit
list_comp = "[num for num in range(0, 10 ** 8)]"
# timeit.timeit(list_comp, number=1)
gen_comp = "(num for num in range(0, 10 ** 8))"
# timeit.timeit(gen_comp, number=1)
# timeit.timeit(gen_comp, number=10000000) # run the operation 10000000 times
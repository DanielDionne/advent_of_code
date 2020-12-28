# def solve:
# 	base case:
# 		no available allergens to pair with
# 		return list of unpaired ingredients
# 	for available pairs
# 		pair ingredient and allergen
# 		check validity - no food item that has the allergen lacks the ingredient
# 		solve
# 		un-pair

import re

def get_food_info(filename):
	result = []
	with open(filename, 'r') as f:
		for food_item in f.read().split('\n'):
			# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
			m = re.match(r'(.*) \(contains (.*)\)', food_item)
			ingredients = m.group(1).split(' ')
			allergens = m.group(2).split(', ')
			result.append((ingredients, allergens))
	return result

def check_validity(food_info, ingredient, allergen):
	# check that all food items that have the allergen also have the ingredient
	for f in food_info:
		if allergen in f[1] and ingredient not in f[0]:
			return False
	return True

def solve(food_info, ingredients, allergens, pairs):
	if len(allergens) == 0:
		return True
	for allergen in allergens:
		for ingredient in ingredients:
			if not check_validity(food_info, ingredient, allergen):
				continue
			pairs[allergen] = ingredient
			ingredients.remove(ingredient)
			allergens.remove(allergen)
			s = solve(food_info, ingredients, allergens, pairs)
			if s:
				return True
			pairs.pop(allergen)
			ingredients.append(ingredient)
			allergens.append(allergen)

def problem_1(food_info):
	# count how many times these ingredients appear
	s = 0
	for food_item in food_info:
		for ingredient in food_item[0]:
			s += ingredient in ingredients
	print(s)

def problem_2(food_info, pairs):
	print(",".join([pairs[i] for i in sorted(pairs.keys())]))

# food_info = get_food_info('21_test.txt')
food_info = get_food_info('21_input.txt')
ingredients = list(set([a for item in [f[0] for f in food_info] for a in item]))
allergens = list(set([a for item in [f[1] for f in food_info] for a in item]))

pairs = {}
solve(food_info, ingredients, allergens, pairs)

problem_1(food_info)
problem_2(food_info, pairs)

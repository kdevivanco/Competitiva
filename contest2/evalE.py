from itertools import permutations, product

def generate_all_expressions(numbers):
    operators = ['+', '-', '*', '/']
    expressions = []
    for nums in permutations(numbers):
        for ops in product(operators, repeat=3):
            expressions.append(f'(({nums[0]}{ops[0]}{nums[1]}){ops[1]}{nums[2]}){ops[2]}{nums[3]}')
            expressions.append(f'(({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]}))')
            expressions.append(f'({nums[0]}{ops[0]}({nums[1]}{ops[1]}{nums[2]})){ops[2]}{nums[3]}')
            expressions.append(f'({nums[0]}{ops[0]}{nums[1]}){ops[1]}({nums[2]}{ops[2]}{nums[3]})')
            expressions.append(f'{nums[0]}{ops[0]}(({nums[1]}{ops[1]}{nums[2]}){ops[2]}{nums[3]})')
    return expressions

def eval_expr(expr):
    try:
        result = eval(expr)
        if result == int(result) and result <= 24:
            return int(result)
    except ZeroDivisionError:
        pass
    return None

def max_value_24(cards):
    max_val = -1
    for expr in generate_all_expressions(cards):
        result = eval_expr(expr)
        if result is not None:
            max_val = max(max_val, result)
    return max_val


num_cases = int(input().strip())
results = []

for _ in range(num_cases):
    cards = [int(input().strip()) for _ in range(4)]
    results.append(max_value_24(cards))

for result in results:
    print(result)


# def main():
#     cases = [
#         [3, 3, 3, 3],
#         [1, 1, 1, 1],
#         [12, 5, 13, 1]
#     ]
    
#     results = []
#     for cards in cases:
#         results.append(max_value_24(cards))
    
#     for result in results:
#         print(result)

# if __name__ == "__main__":
#     main()

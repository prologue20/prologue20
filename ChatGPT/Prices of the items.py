# Prices of the items
price_saftvand = 6
price_kakao = 15
price_chokolade = 8

# The total amount spent
total_amount = 90

# Find all combinations of items that total 90 kr
solutions = []

# Try all possible numbers of saftvand, kakao, and chokolade
for saftvand_count in range(total_amount // price_saftvand + 1):
    for kakao_count in range(total_amount // price_kakao + 1):
        for chokolade_count in range(total_amount // price_chokolade + 1):
            total_cost = (
                saftvand_count * price_saftvand
                + kakao_count * price_kakao
                + chokolade_count * price_chokolade
            )
            if total_cost == total_amount:
                solutions.append(
                    (saftvand_count, kakao_count, chokolade_count)
                )

# Print the solutions
print("Possible combinations (Saftvand, Kakao, Chokolade):")
for solution in solutions:
    print(solution)

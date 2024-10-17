def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count

    return result

amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))
# Виведе: {50: 2, 10: 1, 2: 1, 1: 1}


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізація мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    # Словник для збереження комбінацій монет для кожної суми
    coin_count = [{} for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_count[i] = coin_count[i - coin].copy()
                    if coin in coin_count[i]:
                        coin_count[i][coin] += 1
                    else:
                        coin_count[i][coin] = 1

    return coin_count[amount]

print("Динамічне програмування:", find_min_coins(amount))
# Виведе: {50: 2, 10: 1, 2: 1, 1: 1}

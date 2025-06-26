import random

def get_random_prize():
    wheel = [
        {'label': '🎁 ₹0.10 – 10 ₹', 'amount': 0.10, 'weight': 50},
        {'label': '🎁 ₹0.50 – 20 ₹', 'amount': 0.50, 'weight': 20},
        {'label': '🎁 ₹0.80 – 25 ₹', 'amount': 0.80, 'weight': 15},
        {'label': '🎁 ₹1.00 – 30 ₹', 'amount': 1.00, 'weight': 10},
        {'label': '🎁 ₹5.00 – 50 ₹', 'amount': 5.00, 'weight': 5},
    ]
    choices = [item for item in wheel for _ in range(item['weight'])]
    prize = random.choice(choices)
    return prize

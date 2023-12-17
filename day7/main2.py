from functools import cmp_to_key 

def parse_line(line: str):
    cards, bid = line.strip().split(" ")
    return cards, int(bid)

def get_card_counts(cards) -> dict[str, int]:
    counts = {}
    for c in cards:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

game_wins ={ "full-house": 5, "5row": 7, "4row": 6, "3row": 4, "double-pair": 3, "single-pair": 2, "no": 0}

def get_cards_score(cards):
    counts = get_card_counts(cards)
    jokers = counts["J"] if "J" in counts else 0
    max_key = max(counts, key=counts.get)
    maxi = counts[max_key]

    if len(counts) == 1:
        return 7

    #4 in a row or full house
    if len(counts) == 2:
        if maxi == 4:
            if jokers > 0:
                return game_wins["5row"]
            return game_wins["4row"]

        if jokers == 2:
            return game_wins["5row"] #4row or 5row
        elif jokers == 3:
            return game_wins["5row"]
        
        return game_wins["full-house"]
    
    #tris or two pair
    if len(counts) == 3:
        if maxi == 3:
            if max_key == "J":
                return game_wins["3row"]
            if jokers == 2:
                return game_wins["5row"]
            if jokers == 1:
                return game_wins["4row"]
            return game_wins["3row"]

        if "J" in counts and counts["J"] == 2:
            return game_wins["4row"]        
        if jokers > 0:
            return game_wins["full-house"]
        return game_wins["double-pair"]
    
    #one pair
    if len(counts) == 4:
        if jokers > 0:
            return game_wins["3row"]
        return game_wins["single-pair"]
    if jokers > 0:
        return game_wins["single-pair"]
    return game_wins["no"]

def compare_high_cards(card1, card2):
    for i, c1 in enumerate(card1):
        c2 = card2[i]
        if c1 == c2:
            continue
        if card_values[c1] > card_values[c2]:
            return 1
        else:
            return -1
    return -1

def compare_hands(hand1, hand2):
    cards1, cards2 = hand1[0], hand2[0]
    score1, score2 = get_cards_score(cards1), get_cards_score(cards2)
    print(f"{cards1}, {score1}")
    if score1 == score2:
        return compare_high_cards(cards1, cards2)
    elif score1 > score2:
        return 1
    return -1

card_types = ["A", "K","Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_values = {card_types[i]: len(card_types)-i  for i in range(len(card_types))}

hands: list[tuple[list[str], int]] = []

with open("./day7/data.txt") as f:
    lines = f.readlines()

for l in lines:
    cards, bid = parse_line(l)
    hands.append((cards, bid))

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

sum = 0

for i, (c, bid) in enumerate(sorted_hands):
    print(f"{c},{sorted(c, key=lambda x: card_values[x])}, {bid}")
    sum += bid * (i+1)
        
print(sum)
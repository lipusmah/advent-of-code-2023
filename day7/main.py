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

def get_cards_score(cards):
    counts = get_card_counts(cards)
    if len(counts) == 1:
        return 7
    
    if len(counts) == 2:
        for key in counts:
            if counts[key] == 4:
                return 6
        return 5

    if len(counts) == 3:
        for key in counts:
            if counts[key] == 3:
                return 4
        return 3
    
    if len(counts) == 4:
        return 2
    
    return 1

def compare_high_cards(card1, card2):
    for i, c1 in enumerate(card1):
        c2 = card2[i]
        if c1 == c2:
            continue
        if card_values[c1] > card_values[c2]:
            return 1
        else:
            return -1
    return 0

def compare_hands(hand1, hand2):
    cards1, cards2 = hand1[0], hand2[0]
    score1, score2 = get_cards_score(cards1), get_cards_score(cards2)
    if score1 == score2:
        return compare_high_cards(cards1, cards2)
    elif score1 > score2:
        return 1
    return -1

card_types = ["A", "K","Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values = {card_types[i]: len(card_types)-i  for i in range(len(card_types))}

hands: list[tuple[list[str], int]] = []


with open("./day7/data.txt") as f:
    lines = f.readlines()

for l in lines:
    cards, bid = parse_line(l)
    sorted_cards = sorted(cards, key=lambda x: card_values[x], reverse=True)
    hands.append((cards, bid))

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

sum = 0
with open("new.txt", "w") as fw:
    for i, (c, bid) in enumerate(sorted_hands):
        fw.write(str(cards)+"\n")
        sum += bid * (i+1)
        
print(sum)
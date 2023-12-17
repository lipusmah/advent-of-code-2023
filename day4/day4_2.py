import heapq

def parse_line(line: str):
    left, right = line.strip().split("|")
    game, nums = left.strip().split(":")
    nums = nums.strip().replace("  ", " ")
    right = right.strip().replace("  ", " ")

    my_nums = [int(n) for n in right.strip().split(" ")]
    nums = [int(n) for n in nums.strip().split(" ")]
    game = game.strip().split(" ")[-1]
    return int(game), set(nums), my_nums

def get_count(num_set, nums):
    i = 0
    for n in nums:
        if n in num_set:
           i += 1
    return i

def update_cards(cards, original_cards, game, count):
    for i in range(count):
        new_card = original_cards[game+i]
        heapq.heappush(cards, (new_card[0], new_card))
    return cards

with open("./day4/data.txt") as f:
    original_cards = [parse_line(line) for line in f.readlines()]
    cards = [(l[0], l) for l in original_cards]
    heapq.heapify(cards)
    c = 1
    total_count = len(cards)
    while len(cards) > 1:
        i, (game, num_set, nums) = heapq.heappop(cards)
        count = get_count(num_set, nums)
        total_count += count
        cards = update_cards(cards, original_cards, game, count)
        print(f"{c}, {count}, {len(cards)}, {total_count}")
        c += 1
       
    print(total_count)
import os

global_opponents = []
opponent_dict = {}
global_cards = []
card_dict = {}

for draft in os.listdir("drafts"):
    file = open('drafts\\%s' % str(draft), 'r')
    lines = []
    header_info = []
    player_info = []
    opponents = []
    cards = []

    for line in file:
        lines.append(line)

    for line in lines[:2]:
        header_info.append(line)

    for line in lines[2:11]:
        player_info.append(line.replace(' ', '').replace('\n', ''))

    for line in lines[12:]:
        if line[0:3] == '-->':
            cards.append(line[4:].strip('\n'))

    for player in player_info[1:]:
        if player[0:3] != '-->':
            opponents.append(player)

    global_opponents += opponents
    global_cards += cards

    for opp in global_opponents:
        if opp not in opponent_dict:
            opponent_dict[opp] = 1
        else:
            opponent_dict[opp] += 1

    for card in global_cards:
        if card not in card_dict:
            card_dict[card] = 1
        else:
            card_dict[card] += 1

sorted_opps = sorted(opponent_dict.items(), key=lambda x: x[1], reverse=True)
sorted_cards = sorted(card_dict.items(), key=lambda x: x[1], reverse=True)
cards_txt = open("cards.txt", "w")
opp_txt = open("opponents.txt", "w")

for opp in sorted_opps:
    opp_txt.write(opp[0] + ": " + str(opp[1]) + '\n')
for card in sorted_cards:
    cards_txt.write(card[0] + ": " + str(card[1]) + '\n')

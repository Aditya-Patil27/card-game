import random

#CARD NUMBER

I='GOLD'
II='SILVER'
III='BRONZE'

#CARD FACE
STAR_FACE=[
    "+-----------+",
    "|     *     |",
    "|    ***    |",
    "|   *****   |",
    "|    ***    |",
    "|     *     |",
    "+-----------+"
]
SKULL_FACE=[
    "+-----------+",
    "|    ---    |",
    "|  - 0 0 -  |",
    "|   _ ! _   |",
    "|    ###    |",
    "|           |",
    "+-----------+"  
]
QUESTION_FACE=[
    "+-----------+",
    "|           |",
    "|     ?     |",
    "|   ?   ?   |",
    "|     ?     |",
    "|           |",
    "+-----------+"
]
#FUNCTION TO SHUFFLE CARD NUMBER
def shuffle_card(card_number):
    if card_number == I:
        faces=[STAR_FACE,STAR_FACE,STAR_FACE,QUESTION_FACE,QUESTION_FACE,SKULL_FACE]
    elif card_number == II:
        faces=[STAR_FACE,STAR_FACE,QUESTION_FACE,QUESTION_FACE,SKULL_FACE,SKULL_FACE]
    else:
        faces=[STAR_FACE,QUESTION_FACE,QUESTION_FACE,SKULL_FACE,SKULL_FACE,SKULL_FACE]
    return random.choice(faces)

def play_turn(player_name):
    stars_collected=0
    skull_collected=0
    while True:
        cards=[shuffle_card(I),shuffle_card(II),shuffle_card(III)]
        for card in cards:
            print("\n".join(card))
            if card==STAR_FACE:
                stars_collected+=1
            elif card==SKULL_FACE:
                skull_collected+=1
        print("Stars collected:{stars_collected} Skull_collected:{skull_collected}")
        if skull_collected>=3:
             print(f"{player_name}loses all stars!")
             return 0
        shuffle_again=input("do you want to shuffle again?(Y/N)").strip().upper()
        if shuffle_again!='Y':
            return stars_collected
#MAIN GAME LOOP
def main():
    players=["RAM","SHYAM"]
    scores = {player:0 for player in players}
    winning_scores = 15
    
    while max(scores.values())<winning_scores:
        for player in players:
            print(f"\n{player}'s turn:")
            scores[player] +=play_turn(player)
            print(f"\n{player}'s score:{scores[player]}")
            if scores[player]>=winning_scores:
                break
    winner=max(scores,key=scores.get)
    print(f"\{winner}wins with{scores[winner]}points!")
if __name__ == "__main__":
     main()

            
        


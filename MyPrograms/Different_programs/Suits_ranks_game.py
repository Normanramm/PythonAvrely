suits = ['♥', '♦', '♣', '♠']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []
for suit in suits:
    for rank in ranks:
        deck.append([rank, suit])

# Перемешаем вручную — просто поменяем местами несколько карт
deck[0], deck[-1] = deck[-1], deck[0]
deck[1], deck[-2] = deck[-2], deck[1]


def draw_card_ascii(rank, suit):
    print("┌─────────┐")
    print("│", rank, "      │")
    print("│         │")
    print("│   ", suit, "   │")
    print("│         │")
    print("│      ", rank, "│")
    print("└─────────┘")


def draw_cards(num_cards):
    count = 0
    index = len(deck) - 1
    while count < num_cards and index >= 0:
        card = deck[index]
        draw_card_ascii(card[0], card[1])
        count = count + 1
        index = index - 1


def main():
    print("Добро пожаловать в игру 'Вытяни карту'!")
    print("В колоде", len(deck), "карт.")

    while True:
        user_input = input("Сколько карт вытянуть? (0 для выхода): ")

        if user_input == "0":
            break

        if user_input == "1":
            draw_cards(1)
        elif user_input == "2":
            draw_cards(2)
        elif user_input == "3":
            draw_cards(3)
        else:
            print("Введите число от 0 до 3")


if __name__ == "__main__":
    main()

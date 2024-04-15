class Player:
    def __init__(self):
        self.pos = 0
        self.money = 50
        self.grain = 0
        self.energy = 10
    def print_stats(self):
        print("Position: " + str(self.pos))
        print("Energy: " + str(self.energy))
        print("Grain: " + str(self.grain))
    def handle_travel(self):
        self.pos += 1
        self.energy -= 3
    def handle_eat(self):
        self.grain -= 1
        self.energy += 2

if __name__ == "__main__":
    hero = Player()
    # Buy grain
    print("You have $100! Please proceed to buy supplies.")
    n_grain = int(input("How much grain would you like to buy? "))
    hero.grain += n_grain
    hero.money -= 10 * n_grain
    user_command = ""
    while user_command != "quit":
        user_command = input("Enter your command: ")
        if user_command == "travel":
            hero.handle_travel()
        elif user_command == "travel":
            hero.handle_travel()
        elif user_command == "eat":
            hero.handle_eat()
        else:
            print("Invalid command. Please try again.")
            break
        hero.print_stats()
        if hero.pos == 5:
                print("Victory!")
                break
        if hero.energy < 0:
            print("You died.")
            break
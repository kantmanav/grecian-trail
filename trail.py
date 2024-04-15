from random import sample

global grain_cost
global water_cost
global grain_energy
global water_hydration
grain_cost = 10
water_cost = 10
grain_energy = 10
water_hydration = 10

global nutrition_store
nutrition_store = []


class Player:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.money = 100
        self.resources = [0] * len(nutrition_store)
        self.swords = 0
        self.arrows = 0
        self.pos = 0
        # 3 categories of health are energy, hydration, and injury (wounds) respectively.
        self.health = [100] * 3
        self.dead = False
        self.won = False
    
    def travel(self):
        self.pos += 1
        self.health[0] -= 10

    # Ingest an object of class Nutrition
    def ingest(self, idx):
        resource = nutrition_store[idx]
        for i in range(len(self.health)):
            self.health[i] += resource.gains[i]
        self.resources[idx] -= 1
    
    def rest(self):
        self.pos += 0
        self.health[0] += 10
        for idx in range(len(nutrition_store)):
            resource = nutrition_store[idx]
            print("You have %d units of %s." %(self.resources[idx], resource.name))
            if self.resources[idx] > 0:
                eat = input("Would you like to ingest a unit of %s? " %(resource.name))
                if eat.lower() == "yes":
                    self.ingest(idx)
    
    def print_stats(self):
        print("\n\n")
        print("---------------------------------------------")
        print("Name: " + self.name)
        print("Goal: " + str(len(self.path.nodes) - 1))
        print("Position: " + str(self.pos))
        print("Health: " + str(self.health))
        for idx in range(len(nutrition_store)):
            print("Units of %s: %d" %(nutrition_store[idx].name, self.resources[idx]))
        if self.dead:
            print(self.name + " died. :,(")
        elif self.won:
            print(self.name + " won!!!")

    def select_supplies(self):
        for idx in range(len(nutrition_store)):
            resource = nutrition_store[idx]
            print("One unit of %s costs %d and increases your health by %s" %(resource.name, resource.cost, resource.gains))
        print("You have $" + str(self.money))
        # Implement money limit to buying supplies.
        print("Please delineate the quantity of each item that you would like to buy.")
        for idx in range(len(nutrition_store)):
            resource = nutrition_store[idx]
            qty = float('inf')
            while self.money - qty * resource.cost < 0:
                qty = int(input("%s: " %resource.name))
            self.money -= qty * resource.cost
            self.resources[idx] += qty

    def handle_turn(self):
        move = input("Enter your move: ")
        if move == "travel":
            self.travel()
        elif move == "rest":
            self.rest()
        curr_node = self.path.nodes[self.pos]
        if sample(range(100), 1)[0] < curr_node.p_damage:
            print("Damage incurred!")
            for idx in range(len(self.health)):
                self.health[idx] -= curr_node.damage[idx]
        for idx in range(len(self.health)):
            if self.health[idx] < 0:
                self.dead = True
        if self.pos == len(self.path.nodes) - 1:
            self.won = True
        self.print_stats()

class Path:
    def __init__(self, nodes):
        self.nodes = nodes

class Node:
    def __init__(self, damage, p_damage):
        self.damage = damage
        self.p_damage = p_damage

class Damage:
    def __init__(self, losses):
        # list of size Player.health
        self.losses = losses

class Nutrition:
    def __init__(self, name, cost, gains):
        self.name = name
        self.cost = cost
        # list of size Player.health
        self.gains = gains

if __name__ == "__main__":
    path1 = Path([Node([20, 0, 0], 40), Node([0, 20, 0], 40), Node([0, 0, 20], 40)])
    water = Nutrition("water", 10, [10, 0, 0])
    food = Nutrition("grain", 10, [0, 10, 0])
    nutrition_store.append(water)
    nutrition_store.append(food)
    player1 = Player("Manav", path1)
    game_status = True
    player1.select_supplies()
    while game_status:
        player1.handle_turn()
        if player1.won:
            game_status = False
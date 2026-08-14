from enum import Enum
import time
import tkinter as tk
import os

class Resource(Enum):
    """Resource types for the game."""
    WOOD = 1
    FOOD = 2
    STEEL = 3
    MONEY = 4
    STONE = 5

class Building:
    """Class representing a building in the game."""
    def __init__(self, name, price, consumption_type=None, consumption_amount=0, production_type=None, production_amount=0, production_time=0):
        self.name = name
        self.price = price
        self.consumption_type = consumption_type
        self.consumption_amount = consumption_amount
        self.production_type = production_type
        self.production_amount = production_amount
        self.production_time = production_time


class Game:
    """Main game class to manage resources and game state."""
    def __init__(self):
        self.inventory = {resource: 0 for resource in Resource}
        self.running = True
        self.buildings = []

    def update_inventory(self, resource, amount):
        """Update the inventory for a given resource."""
        if resource in self.inventory:
            if self.inventory[resource] + amount < 0:
                pass
            else:
                self.inventory[resource] += amount
        else:
            self.inventory[resource] = amount
        
        #refresh the labels after updating the inventory
        wood_label.config(text=f"Holz: {self.inventory[Resource.WOOD]}")
        food_label.config(text=f"Essen: {self.inventory[Resource.FOOD]}")
        steel_label.config(text=f"Stahl: {self.inventory[Resource.STEEL]}")
        money_label.config(text=f"Geld: {self.inventory[Resource.MONEY]}")
        stone_label.config(text=f"Stein: {self.inventory[Resource.STONE]}")

    def build(self, building):
        """Attempt to build a building if enough resources are available."""
        if self.inventory[Resource.MONEY] >= building.price:
            self.update_inventory(Resource.MONEY, -building.price)
            self.buildings.append(building)
            # Additional logic for building construction can be added here
            woodmill_button.config(state=tk.DISABLED)  # Disable the build button after construction

        else:
            print("Nicht genug Geld zum Bauen!")
        
        


if __name__ == "__main__":
    #setup
    game = Game()
    
    #base game window
    root = tk.Tk()
    root.title("Plangeländespiel Verwaltung")
    root.geometry("800x600")
    timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
    timer_label.place(x=350, y=20)

    #resource labels
    money_label = tk.Label(root, text=f"Geld: {game.inventory[Resource.MONEY]}", font=("Helvetica", 16))
    money_label.place(x=60, y=100)
    wood_label = tk.Label(root, text=f"Holz: {game.inventory[Resource.WOOD]}", font=("Helvetica", 16))
    wood_label.place(x=210, y=100)
    food_label = tk.Label(root, text=f"Essen: {game.inventory[Resource.FOOD]}", font=("Helvetica", 16))
    food_label.place(x=360, y=100)
    steel_label = tk.Label(root, text=f"Stahl: {game.inventory[Resource.STEEL]}", font=("Helvetica", 16))
    steel_label.place(x=510, y=100)
    stone_label = tk.Label(root, text=f"Stein: {game.inventory[Resource.STONE]}", font=("Helvetica", 16))
    stone_label.place(x=660, y=100)
    
    button_add_money = tk.Button(root, text="+1", command=lambda: game.update_inventory(Resource.MONEY, 1))
    button_add_money.place(x=60, y=130)

    button_remove_money = tk.Button(root, text="-1", command=lambda: game.update_inventory(Resource.MONEY, -1))
    button_remove_money.place(x=100, y=130)

    button_add_ten_money = tk.Button(root, text="+10", command=lambda: game.update_inventory(Resource.MONEY, 10))
    button_add_ten_money.place(x=60, y=160)
    
    button_remove_ten_money = tk.Button(root, text="-10", command=lambda: game.update_inventory(Resource.MONEY, -10))
    button_remove_ten_money.place(x=100, y=160)

    #create buildings
    woodmill = Building("Holzfällerhütte", price=10, consumption_type=None, consumption_amount=0, production_type=Resource.WOOD, production_amount=1, production_time=10)
    quary = Building("Steinbruch", price=20, consumption_type=Resource.WOOD, consumption_amount=10, production_type=Resource.STONE, production_amount=1, production_time=10)
    mine = Building("Mine", price=30, consumption_type=Resource.STONE, consumption_amount=10, production_type=Resource.STEEL, production_amount=1, production_time=10)
    farm = Building("Bauernhof", price=40, consumption_type=Resource.WOOD, consumption_amount=10, production_type=Resource.FOOD, production_amount=1, production_time=10)
    office = Building("Bürogebäude", price=50, consumption_type=(Resource.FOOD,Resource.STEEL), consumption_amount=10, production_type=Resource.MONEY, production_amount=1, production_time=10)
    flats = Building("Wohnhaus", price=60, consumption_type=(Resource.FOOD,Resource.STONE), consumption_amount=10, production_type=Resource.MONEY, production_amount=0, production_time=0)
    park = Building("Park", price=70, consumption_type=None, consumption_amount=0, production_type=None, production_amount=0, production_time=0)

    #building labels and buttons
    woodmill_label = tk.Label(root, text=f"{woodmill.name} (Preis: {woodmill.price})", font=("Helvetica", 16))
    woodmill_label.place(x=60, y=200)
    woodmill_button = tk.Button(root, text="Bauen", command=lambda: game.build(woodmill))
    woodmill_button.place(x=60, y=230)

    

    start = time.time()

    def update_timer():
        elapsed_time = int(time.time()-start)
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        #entkommentieren, um fixes Ende festzusetzen
        #if elapsed_time >= 10:  
        #    on_closing()

        #calculate production for each building
        for building in game.buildings:
            if building.production_type and building.production_amount > 0:
                
                if elapsed_time % building.production_time == 0:
                    game.update_inventory(building.production_type, building.production_amount)

        root.after(1000, update_timer)  # schedule the next update in 1 second
    
    update_timer()

    def on_closing():
        with open("resources.txt", "w") as f:
            f.write("Vergangene Zeit: " + timer_label.cget("text") + "\n")
            for resource, amount in game.inventory.items():
                f.write(f"{resource.name}: {amount}\n")

        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()




    
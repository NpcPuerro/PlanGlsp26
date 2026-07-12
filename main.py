from enum import Enum
import time
import tkinter as tk

class Resource(Enum):
    """Resource types for the game."""
    WOOD = 1
    STONE = 2
    FOOD = 3
    STEEL = 4

class Game:
    """Main game class to manage resources and game state."""
    def __init__(self):
        self.inventory = {resource: 0 for resource in Resource}
        self.running = True

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
        stone_label.config(text=f"Stein: {self.inventory[Resource.STONE]}")
        food_label.config(text=f"Essen: {self.inventory[Resource.FOOD]}")
        steel_label.config(text=f"Stahl: {self.inventory[Resource.STEEL]}")



if __name__ == "__main__":
    #setup
    game = Game()

    
    root = tk.Tk()
    root.title("Plangeländespiel Verwaltung")
    root.geometry("800x600")
    timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
    timer_label.place(x=350, y=20)

    wood_label = tk.Label(root, text=f"Holz: {game.inventory[Resource.WOOD]}", font=("Helvetica", 16))
    wood_label.place(x=150, y=100)
    stone_label = tk.Label(root, text=f"Stein: {game.inventory[Resource.STONE]}", font=("Helvetica", 16))
    stone_label.place(x=300, y=100)
    food_label = tk.Label(root, text=f"Essen: {game.inventory[Resource.FOOD]}", font=("Helvetica", 16))
    food_label.place(x=450, y=100)
    steel_label = tk.Label(root, text=f"Stahl: {game.inventory[Resource.STEEL]}", font=("Helvetica", 16))
    steel_label.place(x=600, y=100)

    button_add_wood = tk.Button(root, text="+1", command=lambda: game.update_inventory(Resource.WOOD, 1))
    button_add_wood.place(x=150, y=130)
    button_add_stone = tk.Button(root, text="+1", command=lambda: game.update_inventory(Resource.STONE, 1))
    button_add_stone.place(x=300, y=130)
    button_add_food = tk.Button(root, text="+1", command=lambda: game.update_inventory(Resource.FOOD, 1))
    button_add_food.place(x=450, y=130)
    button_add_steel = tk.Button(root, text="+1", command=lambda: game.update_inventory(Resource.STEEL, 1))
    button_add_steel.place(x=600, y=130)

    button_remove_wood = tk.Button(root, text="-1", command=lambda: game.update_inventory(Resource.WOOD, -1))
    button_remove_wood.place(x=190, y=130)
    button_remove_stone = tk.Button(root, text="-1", command=lambda: game.update_inventory(Resource.STONE, -1))
    button_remove_stone.place(x=340, y=130)
    button_remove_food = tk.Button(root, text="-1", command=lambda: game.update_inventory(Resource.FOOD, -1))
    button_remove_food.place(x=490, y=130)
    button_remove_steel = tk.Button(root, text="-1", command=lambda: game.update_inventory(Resource.STEEL, -1))
    button_remove_steel.place(x=640, y=130)

    button_add_ten_wood = tk.Button(root, text="+10", command=lambda: game.update_inventory(Resource.WOOD, 10))
    button_add_ten_wood.place(x=150, y=160)
    button_add_ten_stone = tk.Button(root, text="+10", command=lambda: game.update_inventory(Resource.STONE, 10))
    button_add_ten_stone.place(x=300, y=160)
    button_add_ten_food = tk.Button(root, text="+10", command=lambda: game.update_inventory(Resource.FOOD, 10))
    button_add_ten_food.place(x=450, y=160)
    button_add_ten_steel = tk.Button(root, text="+10", command=lambda: game.update_inventory(Resource.STEEL, 10))
    button_add_ten_steel.place(x=600, y=160)

    button_remove_ten_wood = tk.Button(root, text="-10", command=lambda: game.update_inventory(Resource.WOOD, -10))
    button_remove_ten_wood.place(x=190, y=160)
    button_remove_ten_stone = tk.Button(root, text="-10", command=lambda: game.update_inventory(Resource.STONE, -10))
    button_remove_ten_stone.place(x=340, y=160)
    button_remove_ten_food = tk.Button(root, text="-10", command=lambda: game.update_inventory(Resource.FOOD, -10))
    button_remove_ten_food.place(x=490, y=160)
    button_remove_ten_steel = tk.Button(root, text="-10", command=lambda: game.update_inventory(Resource.STEEL, -10))
    button_remove_ten_steel.place(x=640, y=160)

    start = time.time()

    def update_timer():
        elapsed_time = int(time.time()-start)
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)  # schedule the next update in 1 second
    
    update_timer()
    
    root.mainloop()




    
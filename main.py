from enum import Enum
import time
import tkinter as tk

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

    def upgrade_consumption(self):
        """Upgrade the consumption amount of the building."""
        if game.inventory[Resource.MONEY] >= (7-self.consumption_amount)*5:
            game.update_inventory(Resource.MONEY, -(7-self.consumption_amount)*5)
            if self.consumption_amount > 0:
                self.consumption_amount -= 1
                match self.name:
                    case "Steinbruch":
                        quary_input_button.config(text=f"Verbrauch verringern ({(7-self.consumption_amount)*5}$)")
                        quary_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                    case "Mine":
                        mine_input_button.config(text=f"Verbrauch verringern ({(7-self.consumption_amount)*5}$)")
                        mine_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                    case "Bauernhof":
                        farm_input_button.config(text=f"Verbrauch verringern ({(7-self.consumption_amount)*5}$)")
                        farm_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                    case "Bürogebäude":
                        office_input_button.config(text=f"Verbrauch verringern ({(7-self.consumption_amount)*5}$)")
                        office_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                    case "Wohnhaus":
                        flats_input_button.config(text=f"Verbrauch verringern ({(7-self.consumption_amount)*5}$)")
                        flats_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
            if self.consumption_amount == 1:
                match self.name:
                    case "Steinbruch":
                        quary_input_button.config(state=tk.DISABLED)
                    case "Mine":
                        mine_input_button.config(state=tk.DISABLED)
                    case "Bauernhof":
                        farm_input_button.config(state=tk.DISABLED)
                    case "Bürogebäude":
                        office_input_button.config(state=tk.DISABLED)
                    case "Wohnhaus":
                        flats_input_button.config(state=tk.DISABLED)
        else:
            print("Nicht genug Geld zum Upgraden!")
            warn_label.place(x=200, y=60)  # show the warning label
            root.after(800, lambda: warn_label.place_forget())


    def upgrade_production(self):
        """Upgrade the production amount of the building."""
        if game.inventory[Resource.MONEY] >= int((1.5**(self.production_amount-1))*10):
            game.update_inventory(Resource.MONEY, -(int((1.5**(self.production_amount-1))*10)))
            self.production_amount += 1
            match self.name:
                case "Holzfällerhütte":
                    woodmill_output_button.config(text=f"Produktion erhöhen ({int((1.5**(self.production_amount-1))*10)}$)")
                    woodmill_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                case "Steinbruch":
                    quary_output_button.config(text=f"Produktion erhöhen ({int((1.5**(self.production_amount-1))*10)}$)")
                    quary_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                case "Mine":
                    mine_output_button.config(text=f"Produktion erhöhen ({int((1.5**(self.production_amount-1))*10)}$)")
                    mine_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                case "Bauernhof":
                    farm_output_button.config(text=f"Produktion erhöhen ({int((1.5**(self.production_amount-1))*10)}$)")
                    farm_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                case "Bürogebäude":
                    office_output_button.config(text=f"Produktion erhöhen ({int((1.5**(self.production_amount-1))*10)}$)")
                    office_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                case "Wohnhaus":
                    flats_output_button.config(text=f"Produktion erhöhen ({int((1.5**(self.production_amount-1))*10)}$)")
                    flats_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
        else:
            print("Nicht genug Geld zum Upgraden!")
            warn_label.place(x=200, y=60)  # show the warning label
            root.after(800, lambda: warn_label.place_forget())

    def upgrade_production_time(self):
        """Upgrade the production time of the building."""
        if game.inventory[Resource.MONEY] >= (7-self.production_time)*5:
            game.update_inventory(Resource.MONEY, -(7-self.production_time)*5)
            if self.production_time > 0:
                    self.production_time -= 1
                    match self.name:
                        case "Holzfällerhütte":
                            woodmill_time_button.config(text=f"Produktionszeit verringern ({(7-self.production_time)*5}$)")
                            woodmill_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                        case "Steinbruch":
                            quary_time_button.config(text=f"Produktionszeit verringern ({(7-self.production_time)*5}$)")
                            quary_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                        case "Mine":
                            mine_time_button.config(text=f"Produktionszeit verringern ({(7-self.production_time)*5}$)")
                            mine_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                        case "Bauernhof":
                            farm_time_button.config(text=f"Produktionszeit verringern ({(7-self.production_time)*5}$)")
                            farm_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                        case "Bürogebäude":
                            office_time_button.config(text=f"Produktionszeit verringern ({(7-self.production_time)*5}$)")
                            office_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
                        case "Wohnhaus":
                            flats_time_button.config(text=f"Produktionszeit verringern ({(7-self.production_time)*5}$)")
                            flats_label.config(text=f"{self.name}({self.consumption_amount}/{self.production_amount}/{self.production_time})")
            if self.production_time == 1:
                match self.name:
                    case "Holzfällerhütte":
                        woodmill_time_button.config(state=tk.DISABLED)
                    case "Steinbruch":
                        quary_time_button.config(state=tk.DISABLED)
                    case "Mine":
                        mine_time_button.config(state=tk.DISABLED)
                    case "Bauernhof":
                        farm_time_button.config(state=tk.DISABLED)
                    case "Bürogebäude":
                        office_time_button.config(state=tk.DISABLED)
                    case "Wohnhaus":
                        flats_time_button.config(state=tk.DISABLED)
        else:
            print("Nicht genug Geld zum Upgraden!")
            warn_label.place(x=200, y=60)  # show the warning label
            root.after(800, lambda: warn_label.place_forget())

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
            # Disable the build button after construction
            match building.name:
                case "Holzfällerhütte":
                    woodmill_button.config(state=tk.DISABLED)
                    woodmill_time_button.config(state=tk.NORMAL)
                    woodmill_output_button.config(state=tk.NORMAL)
                case "Steinbruch":
                    quary_button.config(state=tk.DISABLED)
                    quary_time_button.config(state=tk.NORMAL)
                    quary_output_button.config(state=tk.NORMAL)
                    quary_input_button.config(state=tk.NORMAL)
                case "Mine":
                    mine_button.config(state=tk.DISABLED)
                    mine_time_button.config(state=tk.NORMAL)
                    mine_output_button.config(state=tk.NORMAL)
                    mine_input_button.config(state=tk.NORMAL)
                case "Bauernhof":
                    farm_button.config(state=tk.DISABLED)
                    farm_time_button.config(state=tk.NORMAL)
                    farm_output_button.config(state=tk.NORMAL)
                    farm_input_button.config(state=tk.NORMAL)
                case "Bürogebäude":
                    office_button.config(state=tk.DISABLED)
                    office_time_button.config(state=tk.NORMAL)
                    office_output_button.config(state=tk.NORMAL)
                    office_input_button.config(state=tk.NORMAL)
                case "Wohnhaus":
                    flats_button.config(state=tk.DISABLED)
                    flats_time_button.config(state=tk.NORMAL)
                    flats_output_button.config(state=tk.NORMAL)
                    flats_input_button.config(state=tk.NORMAL)
                case "Park":
                    park_button.config(state=tk.DISABLED)


        else:
            print("Nicht genug Geld, um das zu bauen!")
            warn_label.place(x=200, y=60)  # show the warning label
            root.after(800, lambda: warn_label.place_forget())


if __name__ == "__main__":
    #setup
    game = Game()
    
    #base game window
    root = tk.Tk()
    root.title("Plangeländespiel Verwaltung")
    root.geometry("800x700")
    timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
    timer_label.place(x=350, y=20)

    warn_label = tk.Label(root, text="Warnung: Nicht genug Geld, um das zu kaufen!", font=("Helvetica", 12), fg="red")
    warn_label.place(x=200, y=60)
    warn_label.config(fg="red")
    warn_label.place_forget()  # initially hide the warning label


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
    quary = Building("Steinbruch", price=10, consumption_type=Resource.WOOD, consumption_amount=5, production_type=Resource.STONE, production_amount=1, production_time=10)
    mine = Building("Mine", price=10, consumption_type=Resource.STONE, consumption_amount=5, production_type=Resource.STEEL, production_amount=1, production_time=10)
    farm = Building("Bauernhof", price=10, consumption_type=Resource.WOOD, consumption_amount=5, production_type=Resource.FOOD, production_amount=1, production_time=10)
    office = Building("Bürogebäude", price=10, consumption_type=(Resource.FOOD,Resource.STEEL), consumption_amount=5, production_type=Resource.MONEY, production_amount=1, production_time=10)
    flats = Building("Wohnhaus", price=10, consumption_type=(Resource.FOOD,Resource.STONE), consumption_amount=5, production_type=Resource.MONEY, production_amount=1, production_time=10)
    park = Building("Park", price=100, consumption_type=None, consumption_amount=0, production_type=None, production_amount=0, production_time=100)

    #building labels and buttons
    woodmill_label = tk.Label(root, text=f"{woodmill.name}({woodmill.consumption_amount}/{woodmill.production_amount}/{woodmill.production_time})", font=("Helvetica", 16))
    woodmill_label.place(x=60, y=200)
    woodmill_button = tk.Button(root, text="Bauen (10$)", command=lambda: game.build(woodmill))
    woodmill_button.place(x=60, y=230)

    quary_label = tk.Label(root, text=f"{quary.name}({quary.consumption_amount}/{quary.production_amount}/{quary.production_time})", font=("Helvetica", 16))
    quary_label.place(x=60, y=270)
    quary_button = tk.Button(root, text="Bauen (10$)", command=lambda: game.build(quary))
    quary_button.place(x=60, y=300)

    mine_label = tk.Label(root, text=f"{mine.name}({mine.consumption_amount}/{mine.production_amount}/{mine.production_time})", font=("Helvetica", 16))
    mine_label.place(x=60, y=340)
    mine_button = tk.Button(root, text="Bauen (10$)", command=lambda: game.build(mine))
    mine_button.place(x=60, y=370)

    farm_label = tk.Label(root, text=f"{farm.name}({farm.consumption_amount}/{farm.production_amount}/{farm.production_time})", font=("Helvetica", 16))
    farm_label.place(x=60, y=410)
    farm_button = tk.Button(root, text="Bauen (10$)", command=lambda: game.build(farm))
    farm_button.place(x=60, y=440)

    office_label = tk.Label(root, text=f"{office.name}({office.consumption_amount}/{office.production_amount}/{office.production_time})", font=("Helvetica", 16))
    office_label.place(x=60, y=480)
    office_button = tk.Button(root, text="Bauen (10$)", command=lambda: game.build(office))
    office_button.place(x=60, y=510)

    flats_label = tk.Label(root, text=f"{flats.name}({flats.consumption_amount}/{flats.production_amount}/{flats.production_time})", font=("Helvetica", 16))
    flats_label.place(x=60, y=550)
    flats_button = tk.Button(root, text="Bauen (10$)", command=lambda: game.build(flats))
    flats_button.place(x=60, y=580)

    park_label = tk.Label(root, text=f"{park.name}", font=("Helvetica", 16))
    park_label.place(x=60, y=620)
    park_button = tk.Button(root, text="Bauen (100$)", command=lambda: game.build(park))
    park_button.place(x=60, y=650)

    #building upgrade labels and buttons

    #upgrade consumption buttons
    quary_input_button = tk.Button(root, text="Verbrauch verringern (10$)", command=lambda: quary.upgrade_consumption())
    quary_input_button.place(x=160, y=300)
    quary_input_button.config(state=tk.DISABLED)  # disable the button initially
    mine_input_button = tk.Button(root, text="Verbrauch verringern (10$)", command=lambda: mine.upgrade_consumption())
    mine_input_button.place(x=160, y=370)
    mine_input_button.config(state=tk.DISABLED)  # disable the button initially
    farm_input_button = tk.Button(root, text="Verbrauch verringern (10$)", command=lambda: farm.upgrade_consumption())
    farm_input_button.place(x=160, y=440)
    farm_input_button.config(state=tk.DISABLED)  # disable the button initially
    office_input_button = tk.Button(root, text="Verbrauch verringern (10$)", command=lambda: office.upgrade_consumption())
    office_input_button.place(x=160, y=510)
    office_input_button.config(state=tk.DISABLED)  # disable the button initially
    flats_input_button = tk.Button(root, text="Verbrauch verringern (10$)", command=lambda: flats.upgrade_consumption())
    flats_input_button.place(x=160, y=580)
    flats_input_button.config(state=tk.DISABLED)  # disable the button initially

    #upgrade_production_buttons
    woodmill_output_button = tk.Button(root, text="Produktion erhöhen (10$)", command=lambda: woodmill.upgrade_production())
    woodmill_output_button.place(x=360, y=230)
    woodmill_output_button.config(state=tk.DISABLED)  # disable the button initially
    quary_output_button = tk.Button(root, text="Produktion erhöhen (10$)", command=lambda: quary.upgrade_production())
    quary_output_button.place(x=360, y=300)
    quary_output_button.config(state=tk.DISABLED)  # disable the button initially
    mine_output_button = tk.Button(root, text="Produktion erhöhen (10$)", command=lambda: mine.upgrade_production())
    mine_output_button.place(x=360, y=370)
    mine_output_button.config(state=tk.DISABLED)  # disable the button initially
    farm_output_button = tk.Button(root, text="Produktion erhöhen (10$)", command=lambda: farm.upgrade_production())
    farm_output_button.place(x=360, y=440)
    farm_output_button.config(state=tk.DISABLED)  # disable the button initially
    office_output_button = tk.Button(root, text="Produktion erhöhen (10$)", command=lambda: office.upgrade_production())
    office_output_button.place(x=360, y=510)
    office_output_button.config(state=tk.DISABLED)  # disable the button initially
    flats_output_button = tk.Button(root, text="Produktion erhöhen (10$)", command=lambda: flats.upgrade_production())
    flats_output_button.place(x=360, y=580)
    flats_output_button.config(state=tk.DISABLED)  # disable the button initially

    #upgrade production time buttons
    woodmill_time_button = tk.Button(root, text="Produktionszeit verringern (10$)", command=lambda: woodmill.upgrade_production_time())
    woodmill_time_button.place(x=600, y=230)
    woodmill_time_button.config(state=tk.DISABLED)  # disable the button initially
    quary_time_button = tk.Button(root, text="Produktionszeit verringern (10$)", command=lambda: quary.upgrade_production_time())
    quary_time_button.place(x=600, y=300)
    quary_time_button.config(state=tk.DISABLED)  # disable the button initially
    mine_time_button = tk.Button(root, text="Produktionszeit verringern (10$)", command=lambda: mine.upgrade_production_time())
    mine_time_button.place(x=600, y=370)
    mine_time_button.config(state=tk.DISABLED)  # disable the button initially
    farm_time_button = tk.Button(root, text="Produktionszeit verringern (10$)", command=lambda: farm.upgrade_production_time())
    farm_time_button.place(x=600, y=440)
    farm_time_button.config(state=tk.DISABLED)  # disable the button initially
    office_time_button = tk.Button(root, text="Produktionszeit verringern (10$)", command=lambda: office.upgrade_production_time())
    office_time_button.place(x=600, y=510)
    office_time_button.config(state=tk.DISABLED)  # disable the button initially
    flats_time_button = tk.Button(root, text="Produktionszeit verringern (10$)", command=lambda: flats.upgrade_production_time())
    flats_time_button.place(x=600, y=580)
    flats_time_button.config(state=tk.DISABLED)  # disable the button initially

    start = time.time()

    def update_timer():
        elapsed_time = int(time.time()-start)
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        #entkommentieren, um fixes Ende festzusetzen
        if elapsed_time >= 3600:  
            on_closing()

        #calculate production for each building
        for building in game.buildings:
            if elapsed_time % building.production_time == 0:
                if building.production_type and building.production_amount > 0:
                    if building.consumption_type:
                        if isinstance(building.consumption_type, tuple):
                            if all(game.inventory[res] >= building.consumption_amount for res in building.consumption_type):
                                for res in building.consumption_type:
                                    game.update_inventory(res, -building.consumption_amount)
                                #add 1 to production ammount of wohnhaus if a park has been built
                                if building.name == "Wohnhaus" and any(b.name == "Park" for b in game.buildings):
                                    game.update_inventory(building.production_type, building.production_amount + 1)  # Double production for Wohnhaus
                                else:
                                    game.update_inventory(building.production_type, building.production_amount)
                        else:
                            if game.inventory[building.consumption_type] >= building.consumption_amount:
                                game.update_inventory(building.consumption_type, -building.consumption_amount)
                                game.update_inventory(building.production_type, building.production_amount)
                    else:
                        game.update_inventory(building.production_type, building.production_amount)

        root.after(1000, update_timer)  # schedule the next update in 1 second
    
    update_timer()

    def on_closing():
        with open("inventory.txt", "w") as f:
            f.write("Vergangene Zeit: " + timer_label.cget("text") + "\n")
            for resource, amount in game.inventory.items():
                f.write(f"{resource.name}: {amount}\n")
            for building in game.buildings:
                f.write(f"{building.name}: ({building.consumption_amount}/{building.production_amount}/{building.production_time})\n")

        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()
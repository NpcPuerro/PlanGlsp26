from enum import Enum
import time
import tkinter as tk

class Resource(Enum):
    """Resource types for the game."""
    WOOD = 1
    STONE = 2
    FOOD = 3
    STEEL = 4





if __name__ == "__main__":
    #setup
    inventory = {}
    for resource in Resource:
        inventory[resource] = 0
    running = True
    root = tk.Tk()
    root.title("Plangeländespiel Verwaltung")
    root.geometry("800x600")
    timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
    timer_label.pack(pady=20)

    
    start = time.time()
    #"render" loop
    #while running:
        #timer_label.config(text=str(int(time.time()-start)))
        #if time.time()-start > 10:  # run for 10 seconds
            #running = False
        #time.sleep(1)  # wait for 1 second before next update

    def update_timer():
        elapsed_time = int(time.time()-start)
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        root.after(1000, update_timer)  # schedule the next update in 1 second
    update_timer()
    root.mainloop()




    
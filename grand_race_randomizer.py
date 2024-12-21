import tkinter as tk
import random
import json
import os

# Relative path to JSON file in working directory
DATA_FILE = os.path.join(os.getcwd(), "item_lists.json")

root = tk.Tk()
root.title("Grand Race Randomizer")

list_names = [
    "Alpha GP", "Drift", "Hypercar", "Monster", "Motocross", 
    "Racing", "Rally", "Rally Raid", "Street Tier 1", "Street Tier 2"
]

item_lists = {
    "Alpha GP": ["Creators", "Ivory Tower", "KTM", "Proto", "Red Bull"],
    "Drift": ["Acura", "BMW", "Chevrolet", "Creators", "Dodge", "Ferrari", "Ford", "Forsberg Racing", "Hoonigan", "Koenigsegg", "Lamborghini", "Mazda", "Mitsubishi", "McLaren", "Nissan", "RUF", "Shelby", "Toyota"],
    "Hypercar": ["Bugatti", "Chevrolet", "Citreon", "Creators", "Ferrari", "Ford", "Jaguar", "Koenigsegg", "KTM", "Lamborghini", "Lotus", "Maserati", "Mercedes-Benz", "McLaren", "Nissan", "Noble", "Pagani", "Porsche", "Proto", "Renault", "Rimac", "Saleen", "Gordon Murray", "Ivory Tower", "Liberty Walk", "Zenvo", "Hyperion", "W Motors"],
    "Monster": ["Chevrolet", "DeLorean", "Dodge", "Ford", "Hummer", "Jeep", "Nissan", "Proto", "Volkswagen", "Abarth"],
    "Motocross": ["Kawasaki", "KTM", "Suzuki", "Yamaha"],
    "Racing": ["Acura", "Aston Martin", "Audi", "Bentley", "BMW", "Bugatti", "Cadillac", "Chevrolet", "Dodge", "Ducatti", "Ferrari", "Ford", "Forsberg Racing", "Hoonigan", "Kawasaki", "Koenigsegg", "KTM", "Lamborghini", "Maserati", "Mazda", "Mercedes-AMG", "Mercedes-Benz", "Mini", "McLaren", "Nissan", "Pagani", "Porsche", "Proto", "Renault", "Saleen", "Shelby", "Spyker", "Suzuki", "Yamaha", "Volkswagen", "Gordon Murray", "Alfa Romeo"],
    "Rally": ["Audi", "Cadillac", "Chevrolet", "Citreon", "Creators", "Dodge", "Ford", "Forsberg Racing", "Lotus", "Mini", "Mitsubishi", "Nissan", "Porsche", "Shelby", "Peugeot", "Renault", "Abarth", "Mazda", "Lancia"],
    "Rally Raid": ["Ariel", "BMW", "Cadillac", "Chevrolet", "Creators", "Dodge", "Ducatti", "Ford", "GMC", "Hummer", "Ivory Tower", "Jeep", "Kawasaki", "KTM", "Land Rover", "Mazda", "Mercedes-Benz", "Mini", "Nissan", "Peugeot", "Pontiac", "Porsche", "Proto", "RAM", "RUF", "Toyota", "Volkswagen"],
    "Street Tier 1": ["Audi", "BMW", "Bugatti", "Cadillac", "Chevrolet", "Chrysler", "DeLorean", "Dodge", "Ducatti", "Ferrari", "Ford", "Harley-Davidson", "Honda", "Hummer", "Indian", "Jaguar", "Jeep", "Kawasaki", "KTM", "Mazda", "Mercedes-Benz", "Mini", "Mitsubishi", "Nissan", "Plymouth", "Pontiac", "Porsche", "Proto", "Renault", "Shelby", "Volkswagen", "Land Rover", "Aston Martin", "Alfa Romeo", "Abarth", "Lancai", "Buick", "Hoonigan", "KRC Japan", "Maserati", "Toyota"],
    "Street Tier 2": ["Acura", "Ariel", "Aston Martin", "Audi", "Bentley", "BMW", "Chevrolet", "Chrysler", "Dodge", "Ducatti", "Ferrari", "Ford", "Forsberg Racing", "Honda", "Hoonigan", "Indian", "Infiniti", "Ivory Tower", "Jaguar", "Kawasaki", "KTM", "Lamborghini", "Liberty Walk", "Lotus", "Maserati", "Mazda", "Mercedes-AMG", "Mercedes-Benz", "Mitsubishi", "Nissan", "Porsche", "Pontiac", "Saleen", "Spyker", "Suzuki", "Toyota", "TVR", "Yamaha", "DeLorean", "Land Rover", "Alfa Romeo", "Ringbrothers"]
}

# Load lists from the JSON file if it exists
def load_lists():
    global item_lists
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            item_lists = json.load(f)

# Save lists to the JSON file
def save_lists():
    with open(DATA_FILE, 'w') as f:
        json.dump(item_lists, f, indent=4)

# Create a frame to organize the content
frame = tk.Frame(root)
frame.pack(pady=20)

# Function to update available lists in dropdowns
def update_dropdowns(*args):
    selected_lists = [dropdown_vars[i].get() for i in range(3)]
    for i, dropdown in enumerate(dropdowns):
        # Don't show duplicates in dropdown boxes
        available_lists = [list_name for list_name in list_names if list_name not in selected_lists or list_name == dropdown_vars[i].get()]
        
        # Update the dropdown menu with available options
        menu = dropdown["menu"]
        menu.delete(0, "end")  # Clear current options
        for option in available_lists:
            menu.add_command(label=option, command=tk._setit(dropdown_vars[i], option))

# Function to pick a random item from the selected list
def randomize_results():
    try:
        selected_lists = [dropdown_vars[i].get() for i in range(3)]
        if all(list_name in item_lists for list_name in selected_lists):
            random_items = [random.choice(item_lists[selected_list]) for selected_list in selected_lists]
            for i, label in enumerate(result_labels):
                label.config(text=f"{selected_lists[i]}: {random_items[i]}")
        else:
            for i, label in enumerate(result_labels):
                label.config(text="Error: List not found")
    except KeyError as e:
        print(f"KeyError: {e}")
        for i, label in enumerate(result_labels):
            label.config(text="Error: List not found")

# Function to reset the chosen lists and results
def reset_program():
    for var in dropdown_vars:
        var.set(list_names[0])
    for label in result_labels:
        label.config(text="")
    update_dropdowns()

# Function to open the Add Manufacturer window
def open_add_manufacturer_window():
    # Create a new window
    add_window = tk.Toplevel(root)
    add_window.title("Add Manufacturer")
    
    # Entry field for new item
    new_item_label = tk.Label(add_window, text="Type in the name of the car manufacturer you want to add, followed by \nchoosing whichever car group it belongs to, and then click the Add button:", font=('Arial', 14))
    new_item_label.pack(pady=10)
    new_item_entry = tk.Entry(add_window, font=('Arial', 14), width=20)
    new_item_entry.pack(pady=10)
    
    # Dropdown for selecting the list to add the item to
    list_select_var = tk.StringVar()
    list_select_var.set(list_names[0])
    list_select_dropdown = tk.OptionMenu(add_window, list_select_var, *list_names)
    list_select_dropdown.config(font=('Arial', 14), width=20)
    list_select_dropdown.pack(pady=10)
    
    # Function to handle adding the new manufacturer
    def add_manufacturer():
        new_item = new_item_entry.get()
        selected_list = list_select_var.get()
        
        # Check if the new item is not empty and not already in the selected list
        if new_item and new_item not in item_lists[selected_list]:
            item_lists[selected_list].append(new_item)
            new_item_entry.delete(0, 'end')
            update_dropdowns()
            save_lists()
            add_window.destroy()
    
    # Add a darken on hover option to the Add button
    normal_color = "SystemButtonFace"
    hover_color = "#d9d9d9"

    add_button = tk.Button(add_window, text="Add", font=('Arial', 14), width=20, command=add_manufacturer, bg=normal_color)
    add_button.pack(pady=20)
    apply_hover_effect(add_button, normal_color, hover_color)

dropdown_vars = []
dropdowns = []
font = ('Arial', 14)

for i in range(3):
    var = tk.StringVar()
    var.set(list_names[0])
    dropdown_vars.append(var)
    dropdown = tk.OptionMenu(frame, var, *list_names)
    dropdown.config(font=font, width=20)
    dropdown.grid(row=0, column=i, padx=10, pady=5)
    dropdowns.append(dropdown)
    var.trace("w", update_dropdowns)

# Helper function to apply hover effect
def apply_hover_effect(button, normal_color, hover_color):
    def on_enter(event):
        button.config(bg=hover_color)
    def on_leave(event):
        button.config(bg=normal_color)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

def apply_hover_effect(button, normal_color, hover_color):
    def on_enter(event):
        button.config(bg=hover_color)
    def on_leave(event):
        button.config(bg=normal_color)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Create buttons with hover effects and set consistent sizes
normal_color = "SystemButtonFace"
hover_color = "#d9d9d9"

button_font = ('Arial', 14)
button_width = 20         

add_button = tk.Button(frame, text="Add Manufacturer", font=button_font, width=button_width, command=open_add_manufacturer_window, bg=normal_color)
add_button.grid(row=1, column=0, pady=10)
apply_hover_effect(add_button, normal_color, hover_color)

randomize_button = tk.Button(frame, text="Randomize", font=button_font, width=button_width, command=randomize_results, bg=normal_color)
randomize_button.grid(row=1, column=1, pady=10)
apply_hover_effect(randomize_button, normal_color, hover_color)

reset_button = tk.Button(frame, text="Reset", font=button_font, width=button_width, command=reset_program, bg=normal_color)
reset_button.grid(row=1, column=2, pady=10)
apply_hover_effect(reset_button, normal_color, hover_color)

# Result labels
result_labels = []
for i in range(3):
    label = tk.Label(frame, text="", font=font, width=20, anchor="w")
    label.grid(row=2, column=i, padx=10, pady=1)
    result_labels.append(label)

credit_text = tk.Text(
    root,
    height=1,
    width=1,
    font=('Arial', 10),
    fg="gray",
    bg=root.cget("bg"),
    bd=0, 
    highlightthickness=0, 
    wrap="none" 
)
credit_text.pack(side="bottom", fill="x", pady=5)

static_text = "Made by Invis | "
credit_text.insert("1.0", static_text)

hyperlink_text = "GitHub"
start_index = f"1.{len(static_text)}"
end_index = f"1.{len(static_text) + len(hyperlink_text)}"
credit_text.insert("end", hyperlink_text)
credit_text.tag_add("hyperlink", start_index, end_index)
credit_text.tag_config("hyperlink", foreground="blue", underline=True)

def open_github(event):
    import webbrowser
    webbrowser.open("https://github.com/TheInvis/Grand-Race-Randomizer")

def on_hyperlink_enter(event):
    credit_text.config(cursor="hand2")

def on_hyperlink_leave(event):
    credit_text.config(cursor="") 

credit_text.tag_bind("hyperlink", "<Button-1>", open_github) 
credit_text.tag_bind("hyperlink", "<Enter>", on_hyperlink_enter)  
credit_text.tag_bind("hyperlink", "<Leave>", on_hyperlink_leave) 

credit_text.tag_config("center", justify="center")
credit_text.tag_add("center", "1.0", "end")

credit_text.config(state="disabled")

# Load lists and start the program
load_lists()
update_dropdowns()
root.mainloop()
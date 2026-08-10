"""
Description:
  Graphical user interface that displays select information about a
  user-specified Pokemon fetched from the PokeAPI

Usage:
  python poke_info_viewer.py
"""

from tkinter import Tk, ttk, messagebox

from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames
input = ttk.Frame(root)
input.grid(row=0, column=0, columnspan=2)

info = ttk.LabelFrame(root, text="Info")
info.grid(row=1, column=0, sticky="N", padx=(10, 5), pady=(5, 10))

stats = ttk.LabelFrame(root, text="Stats")
stats.grid(row=1, column=1, sticky="N", padx=(5, 10), pady=(5, 10))

# Populate the user input frame with widgets
input_lbl = ttk.Label(input, text="Pokemon Name:")
input_lbl.grid(row=0, column=0, padx=(10, 5), pady=10)

input_ent = ttk.Entry(input)
input_ent.grid(row=0, column=1, padx=5, pady=10)


def get_info():
    poke_name = input_ent.get().strip()
    if not poke_name:
        return

    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        height_val["text"] = f'{poke_info["height"]} dm'
        weight_val["text"] = f'{poke_info["weight"]} hg'

        # Build comma-separated list of type(s), no trailing comma
        types = [t["type"]["name"].capitalize() for t in poke_info["types"]]
        type_val["text"] = ", ".join(types)

        hp_bar["value"] = poke_info["stats"][0]["base_stat"]
        att_bar["value"] = poke_info["stats"][1]["base_stat"]
        def_bar["value"] = poke_info["stats"][2]["base_stat"]
        satt_bar["value"] = poke_info["stats"][3]["base_stat"]
        sdef_bar["value"] = poke_info["stats"][4]["base_stat"]
        speed_bar["value"] = poke_info["stats"][5]["base_stat"]
    else:
        messagebox.showerror(
            title="Error",
            message=f"Unable to fetch information for {poke_name.capitalize()} from the PokeAPI."
        )

    return


input_btn = ttk.Button(input, text="Get Info", command=get_info)
input_btn.grid(row=0, column=2, padx=(5, 10), pady=10)

# Populate the info frame
height_lbl = ttk.Label(info, text="Height:")
weight_lbl = ttk.Label(info, text="Weight:")
type_lbl = ttk.Label(info, text="Type:")
height_val = ttk.Label(info, width=20)
weight_val = ttk.Label(info, width=20)
type_val = ttk.Label(info, width=20)

height_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
weight_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
type_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=(5, 10))
height_val.grid(row=0, column=1, sticky="W", padx=(5, 10), pady=(10, 5))
weight_val.grid(row=1, column=1, sticky="W", padx=(5, 10), pady=5)
type_val.grid(row=2, column=1, sticky="W", padx=(5, 10), pady=(5, 10))

# Populate the stats frame
hp_lbl = ttk.Label(stats, text="HP:")
att_lbl = ttk.Label(stats, text="Attack:")
def_lbl = ttk.Label(stats, text="Defense:")
satt_lbl = ttk.Label(stats, text="Special Attack:")
sdef_lbl = ttk.Label(stats, text="Special Defense:")
speed_lbl = ttk.Label(stats, text="Speed:")

hp_lbl.grid(row=0, column=0, sticky="E", padx=(10, 5), pady=(10, 5))
att_lbl.grid(row=1, column=0, sticky="E", padx=(10, 5), pady=5)
def_lbl.grid(row=2, column=0, sticky="E", padx=(10, 5), pady=5)
satt_lbl.grid(row=3, column=0, sticky="E", padx=(10, 5), pady=5)
sdef_lbl.grid(row=4, column=0, sticky="E", padx=(10, 5), pady=5)
speed_lbl.grid(row=5, column=0, sticky="E", padx=(10, 5), pady=(5, 10))

MAX_STAT = 255
BAR_LENGTH = 200
hp_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
att_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
def_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
satt_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
sdef_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)
speed_bar = ttk.Progressbar(stats, maximum=MAX_STAT, length=BAR_LENGTH)

hp_bar.grid(row=0, column=1, padx=(5, 10), pady=(10, 5))
att_bar.grid(row=1, column=1, padx=(5, 10), pady=5)
def_bar.grid(row=2, column=1, padx=(5, 10), pady=5)
satt_bar.grid(row=3, column=1, padx=(5, 10), pady=5)
sdef_bar.grid(row=4, column=1, padx=(5, 10), pady=5)
speed_bar.grid(row=5, column=1, padx=(5, 10), pady=(5, 10))

# Create window
root.mainloop()
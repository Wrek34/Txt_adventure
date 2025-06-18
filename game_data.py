"""
Game Data for Retro Text Adventure
Contains all game content: rooms, items, and game world structure
"""

def initialize_game_world():
    """Create and return the initial game world data structure"""
    
    # Create the game world dictionary
    game_world = {
        "starting_room": "bedroom",
        "rooms": {},
        "items": {}
    }
    
    # Define items
    game_world["items"] = {
        "rusty_key": {
            "name": "Rusty Key",
            "description": "An old, rusty key. It looks like it might break if used too forcefully."
        },
        "flashlight": {
            "name": "Flashlight",
            "description": "A small flashlight with batteries. It provides a weak but useful beam of light."
        },
        "note": {
            "name": "Crumpled Note",
            "description": "A handwritten note that reads: 'The basement holds secrets. Look behind the shelves.'"
        },
        "old_book": {
            "name": "Ancient Book",
            "description": "A dusty tome bound in leather. The pages contain strange symbols and diagrams."
        },
        "silver_coin": {
            "name": "Silver Coin",
            "description": "A tarnished silver coin with unusual markings. It feels heavier than it should."
        },
        "strange_amulet": {
            "name": "Strange Amulet",
            "description": "An ornate amulet with a glowing blue stone in the center. It pulses with an inner light."
        },
        "crowbar": {
            "name": "Crowbar",
            "description": "A sturdy metal crowbar. Perfect for prying things open."
        },
        "old_photograph": {
            "name": "Old Photograph",
            "description": "A faded photograph showing a family standing in front of this house. The faces are eerily familiar."
        }
    }
    
    # Define rooms
    
    # Bedroom
    game_world["rooms"]["bedroom"] = {
        "name": "Bedroom",
        "description": "A small bedroom with peeling wallpaper. A bed sits in the corner, and dust covers most surfaces. Weak light filters through a dirty window.",
        "exits": {
            "north": "hallway"
        },
        "items": ["flashlight", "note"],
        "features": {
            "bed": {
                "description": "A simple bed with a worn mattress. The sheets are rumpled as if someone recently slept here."
            },
            "window": {
                "description": "The window is too dirty to see through clearly, but you can tell it's nighttime outside. The window seems to be stuck shut."
            }
        }
    }
    
    # Hallway
    game_world["rooms"]["hallway"] = {
        "name": "Hallway",
        "description": "A narrow hallway with faded photographs hanging on the walls. The floorboards creak under your feet.",
        "exits": {
            "south": "bedroom",
            "north": "living_room",
            "east": "bathroom",
            "west": "study"
        },
        "items": ["old_photograph"],
        "features": {
            "photographs": {
                "description": "The photographs show people you don't recognize, though they all seem to be from decades ago. One frame is empty."
            },
            "floorboards": {
                "description": "The wooden floorboards are worn and creaky. One board seems slightly loose."
            }
        },
        "item_uses": {
            "crowbar": {
                "message": "You pry up the loose floorboard with the crowbar. Underneath, you find a silver coin!",
                "adds_item": "silver_coin",
                "consumes_item": False
            }
        }
    }
    
    # Bathroom
    game_world["rooms"]["bathroom"] = {
        "name": "Bathroom",
        "description": "A small, dingy bathroom. The mirror above the sink is cracked, and the faucet drips steadily.",
        "exits": {
            "west": "hallway"
        },
        "items": [],
        "features": {
            "mirror": {
                "description": "The cracked mirror distorts your reflection in an unsettling way. Behind one of the cracks, you notice something shiny."
            },
            "sink": {
                "description": "An old porcelain sink with rust stains. The faucet drips continuously."
            },
            "bathtub": {
                "description": "A claw-foot bathtub with a grimy ring around the inside."
            }
        },
        "item_uses": {
            "crowbar": {
                "message": "You carefully pry at the cracked mirror with the crowbar. A piece falls away, revealing a rusty key hidden behind it!",
                "adds_item": "rusty_key",
                "consumes_item": False
            }
        }
    }
    
    # Study
    game_world["rooms"]["study"] = {
        "name": "Study",
        "description": "A small room lined with bookshelves. A wooden desk sits in the center, covered in papers.",
        "exits": {
            "east": "hallway"
        },
        "items": ["old_book"],
        "features": {
            "desk": {
                "description": "The desk is covered in papers with strange symbols and diagrams. Some of the ink seems fresh."
            },
            "bookshelves": {
                "description": "The bookshelves are filled with old, dusty books on various esoteric subjects."
            },
            "papers": {
                "description": "The papers contain notes about some kind of ritual. Many words are crossed out or illegible."
            }
        }
    }
    
    # Living Room
    game_world["rooms"]["living_room"] = {
        "name": "Living Room",
        "description": "A spacious room with worn furniture. A fireplace dominates one wall, and a large rug covers the center of the floor.",
        "exits": {
            "south": "hallway",
            "north": "kitchen",
            "west": "basement_door"
        },
        "items": [],
        "features": {
            "fireplace": {
                "description": "The fireplace contains cold ashes. Something metallic glints among the cinders."
            },
            "rug": {
                "description": "A large, ornate rug with an intricate pattern. It looks out of place in this otherwise modest house."
            },
            "furniture": {
                "description": "The furniture is old but was once high quality. The cushions are worn from years of use."
            }
        },
        "item_uses": {
            "flashlight": {
                "message": "You shine the flashlight into the fireplace. Among the ashes, you spot a crowbar!",
                "adds_item": "crowbar",
                "consumes_item": False
            }
        }
    }
    
    # Kitchen
    game_world["rooms"]["kitchen"] = {
        "name": "Kitchen",
        "description": "A dated kitchen with yellowed linoleum and old appliances. The air smells stale.",
        "exits": {
            "south": "living_room",
            "east": "back_door"
        },
        "items": [],
        "features": {
            "refrigerator": {
                "description": "The refrigerator is empty except for some moldy food items. It's not running."
            },
            "cabinets": {
                "description": "The cabinets contain dusty dishes and a few canned goods that expired years ago."
            },
            "sink": {
                "description": "The sink is dry. When you turn the faucet, nothing happens."
            }
        }
    }
    
    # Basement Door
    game_world["rooms"]["basement_door"] = {
        "name": "Basement Door",
        "description": "A heavy wooden door that leads to the basement. It's locked with a rusty padlock.",
        "exits": {
            "east": "living_room"
        },
        "locked_exits": {
            "down": {
                "description": "locked with a rusty padlock",
                "hint": "You need a key that fits the lock."
            }
        },
        "items": [],
        "features": {
            "door": {
                "description": "The door is solid wood with a rusty padlock securing it. There are scratch marks around the lock."
            },
            "padlock": {
                "description": "A rusty padlock that looks like it's seen better days. It needs a key."
            }
        },
        "item_uses": {
            "rusty_key": {
                "message": "You insert the rusty key into the padlock. With some effort, it turns and the lock opens!",
                "unlocks": "down",
                "consumes_item": False
            }
        }
    }
    
    # Basement
    game_world["rooms"]["basement"] = {
        "name": "Basement",
        "description": "A dark, damp basement with concrete walls. Old shelves line one wall, and there's a musty smell in the air.",
        "exits": {
            "up": "basement_door"
        },
        "items": [],
        "features": {
            "shelves": {
                "description": "Dusty shelves filled with old jars, tools, and boxes. They look like they could be moved."
            },
            "walls": {
                "description": "Concrete walls with water stains. In one corner, the wall seems different."
            },
            "floor": {
                "description": "The concrete floor is cracked in places. Dark stains mark the surface."
            }
        },
        "item_uses": {
            "crowbar": {
                "message": "You use the crowbar to move the heavy shelves. Behind them, you discover a hidden alcove containing a strange amulet!",
                "adds_item": "strange_amulet",
                "consumes_item": False
            }
        }
    }
    
    # Back Door
    game_world["rooms"]["back_door"] = {
        "name": "Back Door",
        "description": "A solid door that leads outside. It's locked and won't budge.",
        "exits": {
            "west": "kitchen"
        },
        "locked_exits": {
            "east": {
                "description": "locked and won't open",
                "hint": "It seems to be sealed by some supernatural force."
            }
        },
        "items": [],
        "features": {
            "door": {
                "description": "The door is solid wood with no visible lock, yet it won't open. Strange symbols are carved around the frame."
            },
            "symbols": {
                "description": "The symbols look similar to those in the ancient book you found. They seem to be part of some kind of seal."
            }
        },
        "item_uses": {
            "strange_amulet": {
                "message": "As you hold the amulet near the door, the symbols begin to glow. The door creaks open, revealing a path to freedom! You've escaped the mysterious house!",
                "unlocks": "east",
                "wins_game": True
            }
        }
    }
    
    # Add the basement exit to the basement door room
    game_world["rooms"]["basement_door"]["exits"]["down"] = "basement"
    
    return game_world
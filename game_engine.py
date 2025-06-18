"""
Game Engine for Retro Text Adventure
Handles game mechanics, command processing, and game state
"""

class GameEngine:
    """Main game engine class that processes commands and manages game state"""
    
    def __init__(self, game_world):
        """Initialize the game engine with the game world data"""
        self.game_world = game_world
        self.current_room = game_world["starting_room"]
        self.inventory = []
        self.is_running = True
        self.game_won = False
        self.visited_rooms = set()
    
    def process_command(self, command):
        """Process player commands and return the result"""
        # Split the command into words
        words = command.split()
        
        # Handle empty command
        if not words:
            return "Please enter a command."
        
        # Get the first word (the action)
        action = words[0]
        
        # Process different commands
        if action in ["quit", "exit"]:
            self.is_running = False
            return "Goodbye!"
            
        elif action == "help":
            return self._get_help()
            
        elif action in ["look", "examine"]:
            if len(words) > 1:
                target = " ".join(words[1:])
                return self._examine_object(target)
            else:
                return self._look_around()
                
        elif action in ["go", "move", "walk"]:
            if len(words) > 1:
                direction = words[1]
                return self._move(direction)
            else:
                return "Go where? Try 'go north', 'go south', etc."
                
        elif action in ["take", "get", "grab"]:
            if len(words) > 1:
                item = " ".join(words[1:])
                return self._take_item(item)
            else:
                return "Take what? Try 'take [item name]'."
                
        elif action in ["drop", "leave"]:
            if len(words) > 1:
                item = " ".join(words[1:])
                return self._drop_item(item)
            else:
                return "Drop what? Try 'drop [item name]'."
                
        elif action in ["inventory", "i"]:
            return self._show_inventory()
            
        elif action in ["use"]:
            if len(words) > 1:
                item = " ".join(words[1:])
                return self._use_item(item)
            else:
                return "Use what? Try 'use [item name]'."
        
        # Handle directional shortcuts
        elif action in ["north", "n", "south", "s", "east", "e", "west", "w", "up", "down"]:
            direction_map = {
                "n": "north", "s": "south", "e": "east", "w": "west",
                "north": "north", "south": "south", "east": "east", "west": "west",
                "up": "up", "down": "down"
            }
            return self._move(direction_map[action])
            
        else:
            return f"I don't understand '{command}'. Type 'help' for a list of commands."
    
    def _get_help(self):
        """Return help text with available commands"""
        help_text = """
Available commands:
- go [direction] - Move in a direction (north, south, east, west, up, down)
- look or examine [object] - Get details about your surroundings or a specific object
- take [item] - Pick up an item
- drop [item] - Drop an item from your inventory
- inventory or i - Show items you're carrying
- use [item] - Use an item in your inventory
- quit or exit - End the game
- help - Show this help text

You can also use shortcuts for directions: n, s, e, w
        """
        return help_text
    
    def _look_around(self):
        """Return description of the current room"""
        room = self.game_world["rooms"][self.current_room]
        
        # Mark room as visited
        self.visited_rooms.add(self.current_room)
        
        # Build the description
        description = f"\n{room['name']}\n"
        description += f"{'-' * len(room['name'])}\n"
        description += f"{room['description']}\n"
        
        # List available exits
        exits = []
        for direction, room_id in room["exits"].items():
            exits.append(direction)
        
        if exits:
            description += f"\nExits: {', '.join(exits)}\n"
        else:
            description += "\nThere are no obvious exits.\n"
        
        # List items in the room
        if room["items"]:
            description += "\nYou can see:\n"
            for item in room["items"]:
                description += f"- {self.game_world['items'][item]['name']}\n"
        
        return description
    
    def _examine_object(self, target):
        """Examine a specific object or item"""
        room = self.game_world["rooms"][self.current_room]
        
        # Check if the target is an item in the room
        for item_id in room["items"]:
            item = self.game_world["items"][item_id]
            if target.lower() == item["name"].lower():
                return item["description"]
        
        # Check if the target is an item in inventory
        for item_id in self.inventory:
            item = self.game_world["items"][item_id]
            if target.lower() == item["name"].lower():
                return item["description"]
        
        # Check if the target is a feature in the room
        if "features" in room:
            for feature_id, feature in room["features"].items():
                if target.lower() == feature_id.lower():
                    return feature["description"]
        
        return f"You don't see any {target} here."
    
    def _move(self, direction):
        """Move player in the specified direction"""
        room = self.game_world["rooms"][self.current_room]
        
        # Check if the direction is valid
        if direction in room["exits"]:
            # Check if the exit is locked
            if "locked_exits" in room and direction in room["locked_exits"]:
                lock_info = room["locked_exits"][direction]
                return f"The way {direction} is {lock_info['description']}. {lock_info['hint']}"
            
            # Move to the new room
            self.current_room = room["exits"][direction]
            return self._look_around()
        else:
            return f"You can't go {direction} from here."
    
    def _take_item(self, item_name):
        """Pick up an item from the current room"""
        room = self.game_world["rooms"][self.current_room]
        
        # Check if the item is in the room
        for item_id in room["items"]:
            item = self.game_world["items"][item_id]
            if item_name.lower() == item["name"].lower():
                if item.get("takeable", True):
                    # Remove from room and add to inventory
                    room["items"].remove(item_id)
                    self.inventory.append(item_id)
                    return f"You take the {item['name']}."
                else:
                    return f"You can't take the {item['name']}."
        
        return f"You don't see any {item_name} here."
    
    def _drop_item(self, item_name):
        """Drop an item from inventory into the current room"""
        room = self.game_world["rooms"][self.current_room]
        
        # Check if the item is in inventory
        for item_id in self.inventory:
            item = self.game_world["items"][item_id]
            if item_name.lower() == item["name"].lower():
                # Remove from inventory and add to room
                self.inventory.remove(item_id)
                room["items"].append(item_id)
                return f"You drop the {item['name']}."
        
        return f"You don't have a {item_name}."
    
    def _show_inventory(self):
        """Show the player's inventory"""
        if not self.inventory:
            return "Your inventory is empty."
        
        result = "You are carrying:\n"
        for item_id in self.inventory:
            item = self.game_world["items"][item_id]
            result += f"- {item['name']}\n"
        
        return result
    
    def _use_item(self, item_name):
        """Use an item from inventory"""
        # Check if the item is in inventory
        item_id_to_use = None
        for item_id in self.inventory:
            item = self.game_world["items"][item_id]
            if item_name.lower() == item["name"].lower():
                item_id_to_use = item_id
                break
        
        if not item_id_to_use:
            return f"You don't have a {item_name}."
        
        # Get the current room
        room = self.game_world["rooms"][self.current_room]
        
        # Check if the item has a special use in this room
        if "item_uses" in room and item_id_to_use in room["item_uses"]:
            use_result = room["item_uses"][item_id_to_use]
            
            # Handle unlocking exits
            if "unlocks" in use_result:
                direction = use_result["unlocks"]
                if "locked_exits" in room and direction in room["locked_exits"]:
                    del room["locked_exits"][direction]
            
            # Handle adding items
            if "adds_item" in use_result:
                room["items"].append(use_result["adds_item"])
            
            # Handle removing the used item if it's consumed
            if use_result.get("consumes_item", False):
                self.inventory.remove(item_id_to_use)
            
            # Handle winning the game
            if "wins_game" in use_result and use_result["wins_game"]:
                self.game_won = True
            
            return use_result["message"]
        
        # Generic use message if no special use is defined
        return f"You use the {item_name}, but nothing happens."
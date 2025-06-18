#!/usr/bin/env python3
"""
Retro Text Adventure Game
Main entry point for the game
"""
import time
from game_engine import GameEngine
from game_data import initialize_game_world

def display_intro():
    """Display the game introduction"""
    print("\n" + "=" * 60)
    print("RETRO TEXT ADVENTURE".center(60))
    print("=" * 60 + "\n")
    
    intro_text = """
    You wake up in a dimly lit room. Your head is pounding and you can't 
    remember how you got here. The air is musty and cold. You need to 
    find your way out and discover what happened to you...
    
    Type 'help' at any time to see available commands.
    """
    
    for line in intro_text.split('\n'):
        print(line.strip())
        time.sleep(0.5)  # Slow typing effect
    
    print("\n" + "=" * 60 + "\n")

def main():
    """Main game function"""
    display_intro()
    
    # Initialize game world and engine
    game_world = initialize_game_world()
    game = GameEngine(game_world)
    
    # Main game loop
    while game.is_running:
        command = input("\n> ").strip().lower()
        result = game.process_command(command)
        print(result)
        
        if game.game_won:
            print("\nCongratulations! You've completed the adventure!")
            break
            
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
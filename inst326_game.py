from random import choice
import sys
import re
import inst326_story
import story_events
 

def main():
    """Purpose of this is to be the engine in which our game actually executes
    Primary Author: Ryan
    Technique: regex
    """
    game = Game()
    player = Player(game)
    print("_" * 80)
    print("INSTRUCTIONS:\nQ = Terminate Session\nM = Show Manpower\nF = Show Food\nP = Show Power\nR = Show Reputation\nD = Show Decisions\nS = Show Achievements")
    print("_" * 80)
    user_input = input("Type the name of your character, followed by your class (ex: John, Rogue)\nOptions: Rogue, Knight, Wizard, Peasant: ")
    name_class = r"^(\w+)(?:[,\s]+(\w+))?$"
    result = re.match(name_class, user_input)
    if not result:
        print("Invalid format, defaulting to Player and Peasant")
        game.name = "Player"
        game.character_class = "Peasant"
    else:   
        game.name =  result.group(1)
        game.character_class = result.group(2)
        if game.character_class != None:
            player.assign_class(game.character_class)
        else:
            player.assign_class()
    print(f"Welcome {game.name}, you are playing as a {player.get_class()}. It is 1403 AD, and you are the leader of a small settlement.")
    print(f"You must make the best decisions you can for you and your town's inhabitants.")
    print("_" * 80)

    while True:
        
        scenario_selection(game, inst326_story.scenario_branches, player)
    
        player.assign_skills()
      
def get_input(game):
    """Handles player input for game loop
    
    Args:
        game (Game): The player object that stores character decisions and attributes
    Returns:
        player_input(str): Player's choice for story progression
	    None
    Side Effects:
        Prints out character stats
        Exits program if player_input == "Q"
        Requests player input

    Raises: 
        N/A
    """
    
    while True:
        player_input = input("\nWhat choice will you pick? ").upper().strip()
    
        if player_input == "Q":
           sys.exit("GAME TERMINATED")
        elif player_input == "M":
            game.check_manpower()
            return None
        elif player_input == "F":
            game.check_food()
            return None
        elif player_input == "P":
            game.check_power()
            return None
        elif player_input == "R":
            game.check_reputation()
            return None
        elif player_input == "D":
            print(game)
            return None
        elif player_input == "S":
            game.check_achievements()
            return None
    
        return player_input  
    
def scenario_selection(game, scenario_branches, player):

    """Presents new scenarios based on previous player choices and 
    current player attributes
    
    Technique: Conditional Expressions
    Author: Justin
    
    Args:
        game (Game): The game object that stores game decisions and attributes
        scenario_branches (dict): A dictionary mapping scenarios to scenario details
        player (Player): The player object that further defines our player's character
        
    Returns:
	    None
     
    Side Effects:
        Prints out a scenario for the user
        Updates game.decision_list and game.current_scenario based on player
        Triggers random events
        Exits game upon reaching an ending
        
    Raises: 
        None
    """

    
    scenario = scenario_branches.get(game.current_scenario)
    
    if not scenario:
        sys.exit("Error")
        
    print("\n" + scenario["Scenario Description"])
    
    choices = scenario.get("choices")
    
    if not choices:
        if scenario.get("next"):
            game.current_scenario = scenario["next"]
            return
        end = scenario.get("end")
        ending = (
            "VICTORY ACHIEVED" if end == "victory"
            else "YOU DIED" if end == "death"
            else "GAME OVER"
        )
        print("_" * 80)
        print(ending)
        game.check_achievements()
        sys.exit("\nGAME OVER")
        
    
    while True:
        print("\nChoices:")
        for key, value in scenario["choices"].items():
            print(f"    {key}: {value['text']}")
        print("_" * 80)    
    
        player_input = get_input(game)
    
        if player_input == None:
            continue
            
            
        if player_input in scenario["choices"]:
            game.decision_list.append(scenario["choices"][player_input]["text"])
            game.current_scenario = scenario["choices"][player_input]["next"]
            random_event(game, player)
            check_status(game)
            
            player.player["Skill Points"] += 1
            break
        else: 
            print("Invalid choice, select again.")

def random_event(game, player):
    """Randomly selects an event that changes the stats of the player. Changes can be positive,
	negative, or neutral. Selects a number randomly, then uses that number to display an event using
	story_events.

	Technique: f-strings containing expressions
    Main Author: Keenan

	Args: 
		game (Game): The game object that stores game decisions and attributes
		player (Player): The player object that further defines our player's character

	Side Effects:
		Prints the randomly selected event.
		May raise or decrease stats depending on the event.
    
	
	"""
    random_number = choice(game.decide_number())
    choose_event = story_events.events[random_number]
    
    if random_number == 1:
        print(f"Random Event: {choose_event}")
        game.manpower += 5
    elif random_number == 2:
        print(f"Random Event: {choose_event}")
        game.food +=4
    elif random_number == 3:
        print(f"Random Event: {choose_event}")
        game.power += 5
    elif random_number == 4:
        print(f"Random Event: {choose_event}")
        game.reputation += 3
    elif random_number == 5:
        print(f"Random Event: {choose_event}")
        game.manpower -= 3
        game.food -= 3
    elif random_number == 6:
        print(f"Random Event: {choose_event}")
        game.reputation -= 5
    elif random_number == 7:
        print(f"Random Event: {choose_event}")
        game.power -= 5
    elif random_number == 8:
        print(f"Random Event: {choose_event}")
        game.manpower += 6
        game.power += 2
    elif random_number == 9:
        print(f"Random Event: {choose_event}")
        game.manpower -= 3
        game.food -= 6
    elif random_number == 10:
        print(f"Random Event: {choose_event}")
        game.manpower -= 5
    elif random_number == 11:
        print(f"Random Event: {choose_event}")
        game.power += 5
    elif random_number == 12:
        print(f"Random Event: {choose_event}")
        game.reputation += 3
    elif random_number == 13:
        print(f"Random Event: {choose_event}")
        game.manpower += 4
        game.food += 3
    elif random_number == 14:
        print(f"Random Event: {choose_event}")
        game.manpower -= 7
    elif random_number == 15:
        print(f"Random Event: {choose_event}")
        game.manpower += 15
    elif random_number == 16:
        print(f"Random Event: {choose_event}")
        game.manpower += 8
        game.food += 6
        game.power += 10
    elif random_number == 17:
        print(f"Random Event: {choose_event}")
        game.food += 3
    elif random_number == 18:
        print(f"Random Event: {choose_event}")
        game.reputation += 15
    elif random_number == 19:
        print(f"Random Event: {choose_event}")
        game.power += 9
    elif random_number == 20:
        print(f"Random Event: {choose_event}")
        game.manpower -= 7
    elif random_number == 21:
        print(f"Random Event: {choose_event}")
        game.reputation += 10
    elif random_number == 22:
        print(f"Random Event: {choose_event}")
        game.reputation -= 10
    elif random_number == 23:
        print(f"Random Event: {choose_event}")
        game.food -= 5
    elif random_number == 24:
        print(f"Random Event: {choose_event}")
        game.manpower -= 10
    elif random_number == 25:
        print(f"Random Event: {choose_event}")
    elif random_number == 26:
        print(f"Random Event: {choose_event}")
        game.food += 15
        game.manpower += 10
        game.power += 5
        game.reputation += 10
    elif random_number == 27:
        print(f"Random Event: {choose_event}")
        game.manpower -= 4
        game.power -= 6
    elif random_number == 28:
        print(f"Random Event: {choose_event}")
        game.manpower -= 3
        game.reputation -= 5
    elif random_number == 29:
        print(f"Random Event: {choose_event}")
        game.reputation += 10
    elif random_number == 30:
        print(f"Random Event: {choose_event}")
        print("_" * 80)
        print("YOU DIED")
        sys.exit("GAME OVER")
        
    if player.player["Stats"]["Luck"] >= 7:
        game.food += 1
        game.power += 1
        print("You're a lucky guy. +1 Food, +1 Power")
    if player.player["Stats"]["Strength"] >= 7:
        game.manpower += 2
        print("Big strong man get big stat boost. Here's +2 Manpower!")
    if player.player["Stats"]["Intelligence"] >= 7:
        game.reputation += 2
        print("Your charisma has earned you friends in high places. +1 Reputation")
    

def check_status(game):
    """Checks the status of the player and decides if they are able to continue the game or not.
    Status effects are changed based on story decisions and random events.

    Args:
        game (Game): The game object that stores game decisions and attributes

    Side Effects:
        Could end the users' run if the status depletes too low.
        Prints a warning if a stat is critically low.
   
    Primary author: Keenan
    Technique: key function with min() and lambda
    """
    manpower, food, power, reputation = game.manpower, game.food, game.power, game.reputation

    lowest_stat = min(["manpower", "food", "power", "reputation"], key=lambda s: getattr(game, s))
   
    if getattr(game, lowest_stat) <= 5:
        print(f"Warning: Your {lowest_stat} is critically low!")

    if manpower <= 0:
        print("Your injuries were too much for you to handle.")
        print("_" * 80)
        print("YOU DIED")
        sys.exit("GAME OVER")
    elif food <= 0:
        print("You starved to death.")
        print("_" * 80)
        print("YOU DIED")
        sys.exit("GAME OVER")
    elif power <= 0:
        print("You became so weak that you cannot even hoist your weapon. You are rendered as a loser, and everyone gives up on you.")
        print("_" * 80)
        print("YOU ARE A LOSER")
        sys.exit("GAME OVER")
    elif reputation <= 0:
        print("Your reputation became so bad that your entire village turned on you and locked you in the county jail. Everyone eventually forgets about you, leading you to starve to death.")
        print("_" * 80)
        print("YOU DIED")
        sys.exit("GAME OVER")

class Game:
    """The purpose of this class is to set up the background for our game to
    run. For example, we're creating the 4 attributes the player will care about
    which is manpower, food, power, and reputation. We're also storing their 
    decisions in the self.decision_list so we have it on record. We also have 
    choose_scene methods to update the decisions list depending on choices made.
    """
    def __init__(self):
        """
        Initializes the Game object with default starting values.
        """
        self.decision_list = []
        starting_values = [ 8, 8, 8, 8]
        self.manpower, self.food, self.power, self.reputation = starting_values
        self.current_scenario = "start"
        self.name = ""
        self.character_class = ""
        
    
            
    def check_manpower(self):
        """Prints the player's current manpower stat upon request.

        Side Effects:
            Prints current manpower to the console
        """
        print(f"Your Manpower is: {self.manpower}")

    def check_food(self):
        """Prints the player's current food stat upon request.

        Side Effects:
            Prints current food to the console
        """
        print(f"Your Food is: {self.food}")

    def check_power(self):
        """Prints the player's current power stat upon request.

        Side Effects:
            Prints current power to the console
        """
        print(f"Your Power is: {self.power}")

    def check_reputation(self):
        """Prints the player's current reputation stat upon request.

        Side Effects:
            Prints current reputation to the console
        """
        print(f"Your Reputation is: {self.reputation}")
        
    def check_achievements(self):
        """Checks achievements earned based on player decisions. Uses set intersection
        and difference to find earned and missing achievements. 
        Displays earned and locked achievements as well as story path to unlock.
        
        Technique: Set Operations
        Author: Justin
        
        Args:
            None
        
        Returns:
            None
        
        Side Effects: 
            Prints earned achievements as well as locked achievements and
            the missing decision to unlock it.
        
        Raises: 
            None
        """
        decisions_made = set(self.decision_list)
        
        achievements = {
            "PETA's Worst Enemy": {"Ambush the nearby village"},
            "Feline Supremacy": {"Apologize"},
            "Last Cat Standing": {"Do not take on outsiders"},
        }
        
        print("\nACHIEVEMENTS")
        for achievement, required in achievements.items():
            if required & decisions_made == required:
                print(f"Unlocked: {achievement}!")
            else:
                missing = required - decisions_made
                (needed,) = missing
                print(f"Locked: {achievement}\nNeeded: {needed}")
        print("_" * 80)

    def decide_number(self):
        """Gives a random number for the random events function.

        Returns:
            lst: A list of numbers 1-30
            
        """
        return [i for i in range(1,31)]
	
    def __str__(self):
        """Returns a formatted string of all decisions the player has made during the game.
        
        Args:
            None
        
        Returns:
            str: A formatted string listing all decisions made
        
        Side Effects:
            None
        
        Primary author: Ryan
        Technique: magic methods other than __init__()
        """
        output = "Here are the following decisions you have made:\n"
        for decision in self.decision_list:
            output += f"{decision}\n"
        return output
    
        
class Player():
    """The purpose of this class is to represent the player. This holds skill point
    values pertaining to the player as well as the type of class they are. This class 
    works in tandem with the Game class.
    """
    def __init__(self, game):
        self.game = game
        self.player = {
        "Class": "",
        "Level": 0,
        "Skill Points": 0,
        "Stats": {"Luck": 0, "Strength": 0, "Intelligence": 0}
    }   
        
    def assign_class(self, class_choice="Peasant"):
        """Assigns a class to the player and sets their starting stats accordingly.
        
        Args:
            class_choice (str): The class the player wants to play as. 
            Options are Rogue, Knight, Wizard, or Peasant. Defaults to Peasant.
        
        Returns:
            None
        
        Side Effects:
            Updates self.player["Class"] with the chosen class.
            Updates self.player["Stats"] with starting stats for that class.
            Prints starting stats for the chosen class.
            Prints a message if an invalid class is provided.
        Primary Author: John
        Technique: Optional Parameters
        """
        class_stats = {
            "Rogue":   {"Luck": 6, "Strength": 3, "Intelligence": 5},
            "Knight":  {"Luck": 5, "Strength": 7, "Intelligence": 2},
            "Wizard":  {"Luck": 4, "Strength": 4, "Intelligence": 6},
            "Peasant": {"Luck": 5, "Strength": 5, "Intelligence": 4},
        }

        self.player["Class"] = class_choice.capitalize() if class_choice.capitalize() in class_stats else "Peasant"

        if self.player["Class"] == "Peasant" and class_choice.capitalize() != "Peasant":
            print("Invalid class choice - defaulting to Peasant")

        self.player["Stats"] = class_stats[self.player["Class"]]
        print("_" * 80)
        print(f"Starting stats for {self.player['Class']}:")
        for stat, value in self.player["Stats"].items():
            print(f"  {stat}: {value}")
        print("_" * 80)
    def get_class(self):
        """Returns the player's current class.
    
        Args:
            None
        
        Returns:
            str: The player's current class name
        """
        return self.player["Class"]
    
    def assign_skills(self):
        """
        Allows the player to allocate skill points into their stats.
        Tracks total stats spent to determine player level.

        Args:
            None

        Returns:
            dict: the updated player dictionary with modified stats and skill points

        Side Effects:
            Prints current stats and prompts for input each loop
            Updates self.player["Stats"], self.player["Skill Points"], self.player["Level"]
            Prints a level up message if the player levels up

        Primary Author: John
        Technique: comprehensions or generator expressions
        """
        while self.player["Skill Points"] > 0:
            print(f"\nClass: {self.player['Class']}  Level: {self.player['Level']}  Points: {self.player['Skill Points']}")

            for skill, value in self.player["Stats"].items():
                print(f"    {skill}: {value}")

            skill_choice = input("Choose a skill to upgrade (or 'Done' to stop): ").strip().capitalize()

            if skill_choice == "Done":
                break

            if skill_choice not in ["Luck", "Strength", "Intelligence"]:
                print("Invalid choice - choose again.")
                continue

            points = int(input(f"How many points to add to {skill_choice}? ").strip())

            if points <= 0 or points > self.player["Skill Points"]:
                print("Invalid amount - choose again.")
                continue

            self.player["Stats"][skill_choice] += points
            self.player["Skill Points"] -= points

            total_stats = sum(self.player["Stats"].values())
            new_level = total_stats // 10
            if new_level > self.player["Level"]:
                self.player["Level"] = new_level
                print(f"You leveled up! You are now level {self.player['Level']}!")
                
        print("_" * 80)
        print("Stats: " + ", ".join([f"{skill}: {value}" for skill, value in self.player["Stats"].items()]))
        return self.player
if __name__== "__main__":
    main()

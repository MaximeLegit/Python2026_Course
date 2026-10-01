
class PrintOuts():

    def main_loop_print():
        print("Now, let the quest begin! What would you like to do? Select the options that are of interest!"\
        "\n1. Begin Story" \
        "\n2. Brutal Brawl (Not for beginners!)" \
        "\n3. Show current character's statistics." \
        "\nX. Exit Game")

    def story_one_print(step):
        match step:
            case "part 1":
                print("Welcome to the game. You have several options to explore from. The story revolves around reaching the Carthia Cathedral, located at the West Valley. " \
                "In order to get there, you need to find someone to speak to, to get information about the journey. " \
                "\nCurrently, you are located at the starting point in the city tavern. " \
                "\nWould you like to talk to the keep or go straight into the unknown?\n" \
                "\n1. Talk to the keep\n2. Go straight into the unknown.")
            case "part 2":
                print("\nWould you like to talk to the keep again or go straight into the unknown?\n" \
                        "\n1. Talk to the keep\n2. Go straight into the unknown.")
            case "part 3":
                print("Well howdy there stranger, what brings you to these lands?")
            case "part 4":
                print("Well, as you know, you are currently in the capital's tavern. Legend has it that the fiercest warrior is located at the Carthia Cathedral," \
                    " at the heart of the West Valley. The road there goes through treaturous woods, city of the forgotten warriors, and the famous merridian bazar.")
            case "part 5":
                print("Ah, well, I am aftraid the only liquid matter we have in this establishment is ale, would you like some? Y/N.")
            case "part 6":
                print("Here you go deary, on the house. Now, best be on your way to the west walley!")
            case "part 7":
                print("No? Then best be on your way. Since you are a true warrior of unyielding faith, here is a lucky talisman for you.")

    def story_two_print(step):
        match step:
            case "part 1":
                print("\nChapter 1. Treaturous Woods." \
                "\nAs you step into the woods, you are feeling very enforced, very strong ( even if you are not ). Legend has it that all new travellers get a blessing" \
                "from the lady of the woods, as to not to succumb to the dangers that lie ahead. You feel warmth.")
            case "part 2":
                print("\nAs you go along the woods, you see that the path diverges. You have a choice to make. Go left or go right. Please select accordingly.")
            case "part 3":
                print("\nAs you progress along the path to the left, you feel a chill in the air. You sense danger.. Lo and behold, your first opponent" \
                        "\nPlease type any number from 1 to 9. This ritual is done by the lady of the woods to help new travellers get accross safely.\n")
            case "part 4":
                print("Narrator:\nIt is always right to go right when the path is most definitely right. You see a healing potion, you relise that it will come in handy. You pick it up." \
                        "\nMy young tarnished. Thou art weary. Does thou wish to look around to see if you find something before you leave this forest? Y/N")

    def story_three_print(step):
        match step:
            case "part 1":
                print("\nChapter 2. City of the Forgotten Warriors." \
                "\nYou have survived your first part of the journey. This city, the city of the forgotten warriors, is a an odd place. It is foggy, dark, and cold." \
                "The sudden chill in your bones, you have felt it before, this unease, this forebodem before a battle. Knowing this, you have the following options:")
            case "part 2":
                print("\n1. Continue majestically, like the fearless person you are and see what awaits you." \
                "\n2. Look around" \
                "\n3. Rest" \
                "\n4. Show current character's statistics.")
    
    def final_act(step):
        match step:
            case "part 1":
                print("\nChapter 3. Final Act." \
                "\nAs the story progresses, you know that someone grand will await you at the Cardia Cathedral. Now may be a good time to check if you have anything" \
                "useful in your inventory, heal up, say a prayer, or go forward like a true berserker and see what awaits you.")
            case "part 2":
                print("\n1. Proceed forward towards the final battle." \
                "\n2. Say a prayer." \
                "\n3. Get statistics." \
                "\n4. Use inventory items")
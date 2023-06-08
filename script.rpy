# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mv = Character("Mysterious Voice", color="#be0202")
define p = Character("Phoenix", color="#be0202")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music "audio/spooky.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    mv "oh"

    mv "no"

    mv "why are you here?"

    mv "are you ready to dance?"

    stop music
    scene bg dance
    show phoenix stare at right
    play music "audio/matador.mp3"

    "..."

    p "holdon... this isn't what i meant..."

    # This ends the game.

    return

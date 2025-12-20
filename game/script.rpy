
define p = Character(_("You"), color="#FFFFFF")
define c = Character(_("Chatbot"), color="FF1111")
define s = Character(_("Sara"), color="fc03d3")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show bg room:
        xzoom 0.4 yzoom 0.4

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    p "Hey Sara!"
    s "Hey! Are you done with the essay for English yet?"
    p "What essay?!?"
    s "Uhm, the essay that we had a month to work on?"
    p "Wait, what?!?"
    p "Oh crap, I got to get started on it, then!"
    p "Bye!"
    s "Wait-"

    "I ended the call."
    "When was there ever an essay for English class?"
    "I then remembered that I've used my English period as more of a time to nap than a time to write."
    "I guess I better start working on it."

    "{i}4 hours later...{/i}"

    show you normal:
        xalign 0.99 yalign 0.35
    p "Ugh, I still don't have any ideas for the assignment!"

    p "Oh wait..."
    p "My school just got a c"

    c "hey"

    "{b}Ending Ending{/b}" # Makes things bold

    return

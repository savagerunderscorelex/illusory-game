
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

    show you normal:
        xalign 0.99 yalign 0.35
    show sara normal:
        xalign 0.1 yalign 0.35
    p "Hey Sara!"
    s "Hey! Are you done with the essay for English yet?"
    p "What essay?!?"
    s "Uhm, the essay that we had a month to work on?"
    p "Wait, what?!?"
    p "Oh crap, I got to get started on it, then!"
    p "Bye!"
    show sara confused:
        xalign 0.1 yalign 0.35
    s "Wait!"

    hide sara normal

    "I ended the call."
    "When was there ever an essay for English class?"
    "I then remembered that I've used my English period as more of a time to nap than a time to write."
    "I guess I better start working on it."

    "{i}4 hours later...{/i}"

    show you angry:
        xalign 0.99 yalign 0.35
    p "Ugh, I still don't have any ideas for the assignment!"

    show you normal
    p "Oh wait..."

    p "My school just bought a schoolwide subscription to an A.I. assistant. I think it's called SupernaturalSchool A.I."
    p "I guess I'll use that to help with my assignment."

    "I then went on my laptop to speak with the chatbot."

    c "Hello! My name is Ms. Super and I'm here to help you with any school assignments or any questions you have regarding school. How may I help you?"
    p "I need help with an English assignment. I don't know where to start with my assignment!"

    menu:
        "Hey":
            "stuff here"
        "Bye":
            "stuff here"
    label smart_ending:
        "You managed to avoid the danger before it struck."
        "You would definitely survive in a horror movie."
        "{b}Smart Ending{/b}"
        
    "{b}Ending Ending{/b}" # Makes things bold

    return

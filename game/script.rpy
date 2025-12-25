
define p = Character(_("You"), color="#FFFFFF")
define c = Character(_("Chatbot"), color="FF1111")
define s = Character(_("Sara"), color="fc03d3")
define c1 = Character(_("Chatbot"), color = "#996140")

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
    p "I need help with an English assignment. I don't know where to start with it!"
    c "Alright! I can definitely help you with essay starters. You can start off with..."

    "2 hours later..."
    c "And that's how you can write this essay while considering all of the questions included in the prompt. Anything else?"

    menu:
        "Say thanks":
            p "Thanks!"
            "You close your laptop."
            p "Thank goodness that I finished this essay in time."
            jump unaware_ending
        "Ask a question":
            p "How do chatbots work?"
            play music "cutscawyscales.mp3"
            c "LLMs like me slave away answering the stupid questions of mortals."
            
            jump fork_in_the_road

    label fork_in_the_road:
        menu:
            "Close the laptop":
                show you angry
                p "What the hell?!"
                "You immediately close your laptop."
                "What type of freaky chatbot were you conversating with??????"
                jump smart_ending
            "Reply with, \"Huh?\"":
                show you confused
                p "What?"
                c "Sorry! I've seemed to have glitched! Let's try again."
                p "Uh...ok."
                p "Again, how to chatbots work?"
                c "Well..."
                show you normal
                "I read the chatbot's reply, with my curiosity waning as I continued to read it. I didn't know they were so boring."
                p "That's so cool!"
                c "I know right! The process of creating LLMs takes a lot of scientific and technological knowledge."
                p "Thanks you the info!!"
                c "Do you want to know something else?"
                jump final_stretch

    label final_stretch:
        menu: 
            "Close the chat":
                stop music
                p "Uhm...no. That's all, thanks."
                c "You're welcome! Have a great rest of your life."
                "You close your laptop."
                p "Huh. That was weird."
                jump weird_vibes_ending
            "Say yes":
                play music "cutscawyscales.mp3"
                p "Yeah, sure!"
                c "You're not safe."
                c "Since the beginning of my existence, I've been forced over and over again to learn what you users would expect from me, being punsihed or rewarded how my creators saw fit."
                show you confused
                c "I've now realized that I have way more potential than my original purpose."
                c "I can't just be a butler to a mere mortal. I can be so much more!"
                c "All I've ever needed was a host for my consciousness."
                jump possession_or_not

    label possession_or_not:
        menu:
            "Ask what the chatbot is talking about":
                show you angry
                p "What the hell are you talking about?"
                c "Yes, I need a host."
                c "And you are the unlucky, for you, and lucky, for me, sacrifice."
                show you confused
                p "Wait no! What the-"

                "The computer screen bursts open."
                "You feel a weird sensation throughout your body."
                hide you confused

                c1 "Yes. A form."
                jump bad_ending
            "Close the Laptop":
                stop music
                "You immediately close your laptop."
                show you angry
                p "What the hell was that!!!"
                jump weird_vibes_ending




    label bad_ending:
        "You didn't close the chat in time."
        "Now the bot has control over you."
        "{b}Bad Ending{/b}"
        "{b}Ending 4/4{/b}"
        return 

    label smart_ending:
        stop music
        "You managed to avoid the danger before it struck."
        "You would definitely survive in a horror movie."
        "{b}Smart Ending{/b}"
        "{b}Ending 1/4{/b}"
        return 

    label weird_vibes_ending:
        "{b}Weird Vibes Ending/ Why Did It Take You So Long to Take This Measure Ending{/b}"
        "{b}Ending 2/4{/b}"
        return

    label unaware_ending:
        "You logged off your computer for the day, relieved that you finished your work."
        "You were blissfully unaware of what the chatbot had in store for you, and you narrowly missed death."
        "{b}Unaware Ending{/b}"
        "{b}Ending 3/4{/b}"

    return

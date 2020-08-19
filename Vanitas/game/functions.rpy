screen arrow_watchoffice():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("watchnothingoffice")

screen arrow_watchhall():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("watchnothinghall")


#call screen pfeil_back
#hide screen pfeil_back

screen force_mouse_move_1():

    on "show":
        action MouseMove(x=960, y=540, duration=.3)

    timer .5 repeat True action MouseMove(x=960, y=540, duration=.3)

#show screen force_mouse_move

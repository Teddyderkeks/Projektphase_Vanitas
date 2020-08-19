screen pfeil_back():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "pfeil"
            hover "pfeil_rechts_blau"
            action Jump ("treppenhaus2")

image pfeil_rechts = Transform ("pfeil",rotate = 180)

#call screen pfeil_back
#hide screen pfeil_back

screen force_mouse_move():

    on "show":
        action MouseMove(x=960, y=540, duration=.3)

    timer .5 repeat True action MouseMove(x=960, y=540, duration=.3)

#show screen force_mouse_move

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

screen arrow_detail_ananpc():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_ananpc")

screen arrow_detail_servertext():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servertext")

screen arrow_detail_servergraph():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servergraph")


screen arrow_detail_servertext2():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servertext2")

screen arrow_detail_servergraph2():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servergraph2")


screen arrow_detail_servertext3():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servertext3")

screen arrow_detail_servergraph3():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servergraph3")

screen arrow_detail_servertext4():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servertext4")

screen arrow_detail_servergraph4():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_servergraph4")


screen arrow_detail_letter1():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_letter1")

screen arrow_detail_letter2():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_letter2")

screen arrow_detail_oldphotos():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_oldphotos")

screen arrow_detail_bookphoto():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_bookphoto")

screen arrow_detail_safe_open():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_safe_open")


screen arrow_detail_letterkloth():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_letterkloth")

screen arrow_detail_document():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_document")

screen arrow_detail_blog():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_blog")

screen arrow_detail_blog2():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_blog2")

screen arrow_detail_blog3():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_blog3")

screen arrow_detail_confession():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_confession")

screen arrow_detail_photoskloth():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_photoskloth")

screen arrow_detail_worldmap():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_worldmap")

screen arrow_detail_posterpills():
    frame:
        xpos 1700 ypos 500
        imagebutton:
            idle "arrow.png"
            hover "arrowblue.png"
            focus_mask True
            action Jump ("after_detail_posterpills")

#call screen pfeil_back
#hide screen pfeil_back

screen force_mouse_move_1():

    on "show":
        action MouseMove(x=960, y=540, duration=.3)

    timer .5 repeat True action MouseMove(x=960, y=540, duration=.3)

#show screen force_mouse_move

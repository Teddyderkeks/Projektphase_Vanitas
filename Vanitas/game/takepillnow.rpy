label takepillnow:

    play music "Sound/Music/Rooms/Labor/labor_duester.mp3" fadeout 3 fadein 3
    scene lab
    with fadeshort

    # Atropos Gedanken
    symb"Wo habe ich die Pillen nur hingetan? Sind sie in meiner Tasche?"
    show era normal

    "Era" "Was… was ist los, Atropos?"

    "Atropos" "Hast du meine Happiness-Pillen gesehen? Ich kann sie nicht finden?"

    show era confused

    "Era" "Nein, leider nicht… tut mir leid… aber du kannst gerne eine von meinen haben… Also, wenn du möchtest."

    show era normal

    "Era" "Oder du nimmst eine aus dem Notfallset…"

    "Atropos" "Muss ich dann wohl. (lacht) Aber danke trotzdem für das Angebot, Era."

    show era happy

    "Era" "K-Kein Problem…"

    scene detail_pillbox
    with fadeshort

    # Atropos Gedanken
    symb"Na los, ich tue das Richtige. Es ist die richtige Entscheidung, Happiness zu nehmen."

    scene detail_pill
    with fadeshort

    # Atropos Gedanken
    symb"Es ist die richtige Entscheidung, glücklich sein zu wollen."

    "Atropos" "(schluckt Happinesss)"

    play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

    scene lab
    with fadeshort

    # Symbiont
    symb"{i}Gut gemacht. Und nun vergiss, was dich unglücklich gemacht hat. Vergiss all den Stress und deine Ängste. {i}"

    # Symbiont
    symb"{i}Denk an dein einziges Ziel im Leben: glücklich zu sein. Egal wie diese Art von Glück für dich auch aussehen mag. {i}"

    # Atropos Gedanken
    symb"Ich bin glücklich! Und nun zurück an die Arbeit- es dauert nicht mehr lange bis zur Mittagspause."

jump escapelater

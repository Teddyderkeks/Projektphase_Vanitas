label escapelater:

    "Atropos" "…"

    show lab
    with startfade

    "Atropos" "Era, machst du auch Pause?"

    show era normal:
        xalign 0.5

    "Era" "Ich… Tut mir leid, ich muss noch das Protokoll hier fertig formulieren, solange ich alle Daten in meinem Kopf habe."

    "Era" "Ich kann also erst später Mittagspause machen."

    "Atropos" "Alles klar, kein Problem. Narcais, wie sieht es bei dir aus?"

    show era normal_gray:
        xalign 0.25

    show narcais normal:
        xalign 0.75

    "Narcais" "Ich brauche so etwas wie eine Pause nicht. Deswegen leiste ich ja auch so hervorragende Arbeit, weil ich viel mehr Zeit habe, mich dieser zu widmen."

    show narcais annoyed

    "Narcais" "Kann ich denn wenigstens heute noch von dir Feedback erwarten?"

    "Atropos" "Ich hatte erst einmal alles für Anans Bericht fertiggestellt, aber sobald ich von der Mittagspause zurückkomme, setze ich mich dran."

    show narcais normal

    "Narcais" "Danke, das klingt doch vielversprechend."

    "Atropos" "Also dann, ihr beiden. Wir sehen uns später."

    show narcais normal_gray
    show era happy

    "Era" "B-Bis später!"

    hide era
    hide narcais
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Jetzt suche ich erstmal nach Chesis- vielleicht will er mit in die Mittagspause kommen."

    scene shop_1
    with fadeshort

    # Atropos Gedanken
    symb"Aither ist mittlerweile ganz schön voll. Heute kommen wohl viele Leute, um ihre Vorräte neu aufzufüllen."

    "Zelos" "Atropos! Komm mal schnell her."

    show zelos normal

    "Atropos" "Was gibt’s?"

    "Zelos" "Wie du siehst, brummt uns der Laden. Ich muss meine Mittagspause verschieben. Aber Tycho und die anderen waren gerade da, sie wollten zur Mensa, wenn du sie suchst."

    "Atropos" "Danke für die Info, aber ich denke, ich suche erstmal nach Chesis."

    show zelos happy

    "Zelos" "Alles klar. Dir noch eine schöne Mittagspause!"

    "Atropos" "Danke, dir auch!"

    "Zelos" "Einen wunderschönen, glücklichen guten Morgen! Was kann ich dir heute Gutes tun?"

    # Atropos Gedanken
    symb"Zelos wirkt beschäftigt, ich sollte ihn nicht länger aufhalten. Dann suche ich mal nach Chesis."

    hide zelos
    scene shop_2
    with fadeshort

    # Atropos Gedanken
    symb"Da ist ja Chesis. Aber er scheint auch noch beschäftigt zu sein. Er hat wohl gerade ein Beratungsgespräch."

    # Hier Möglichkeit sich umzuschauen während man auf Chesis wartet.

    show chesis normal

    "Chesis" "Hey Atropos."

    "Atropos" "Hast du Zeit für eine Mittagspause?"

    show chesis happy

    "Chesis" "Bin gerade mit meinem Gespräch fertig geworden, wo wollen wir hin?"

    # Hier Option für weiteren Smalltalk wie Chesis Arbeitstag verlaufen ist

    "Atropos" "Gehen wir ins Büro und holen uns dort erstmal einen Kaffee?"

    show chesis happy_alt

    "Chesis" "Gerne."

    scene office_2
    show chesis normal
    with fadeshort

    "Atropos" "Die anderen sind nicht da, vermutlich sind sie bereits in der Mensa. Wollen wir uns ihnen nachher anschließen?"

    "Chesis" "Ich denke, mir reicht ein Kaffee, es sei denn, du willst unbedingt gehen?"

    "Atropos" "Alles gut, wegen mir müssen wir nicht in die Mensa. Ich weiß doch, dass du dich am wohlsten fühlst, wenn wir nur unter uns sind."

    show chesis happy

    "Chesis" "Danke."

    "Atropos" "Wie war dein Arbeitstag heute?"

    show chesis normal

    "Chesis" "Gut. Wie immer."

    "Atropos" "Meinen Tag heute wirst du mir nicht glauben!"

    show chesis confused

    "Chesis" "Was ist passiert?"

    "Atropos" "Ich durfte mehrmals mit Anan sprechen!"

    show chesis happy

    "Chesis" "Wow, wie kam es dazu?"

    "Atropos" "Ich… ich hatte meine Pille vergessen, aber Anan war so unglaublich verständnisvoll und öffnete mir die Augen."

    "Atropos" "Ich bin wirklich froh, für Aither arbeiten zu dürfen!"

    "Atropos" "Und ich bin froh, dass mir Anan meinen Fehler verziehen hat. Er ist wirklich der beste Chef, den man sich wünschen kann!"

    show chesis happy_alt

    "Chesis" "Das stimmt wohl!"

    show chesis confused

    "Chesis" "Sag mal, stört es dich, wenn Philote heute Abend mit uns isst?"

    "Atropos" "War sie nicht mit Freunden verabredet?"

    show chesis normal

    "Chesis" "Ja, aber die haben keine Zeit mehr."

    "Atropos" "Achso… ja, klar, kein Problem. Philote gehört doch schon seit Jahren unzertrennlich zu dir und ich mag sie wirklich gern."

    show chesis happy

    "Chesis" "Danke!"

    show chesis confused

    "Chesis" "Oh… tut mir leid, ich habe gleich noch einen wichtigen Termin. Ich muss zurück."

    "Atropos" "Kein Problem, wir sehen uns dann später!"

    show chesis happy

    "Chesis" "Bis dann!"

    hide chesis

    # Atropos Gedanken
    symb"Dann werde ich einfach schon Mal ins Labor zurück. Ich habe sonst ohnehin nichts mehr zu tun."

    scene lab
    with fadeshort

    # Atropos Gedanken
    symb"Era und Narcais scheinen beide in der Mittagspause zu sein. Dann kann ich mich jetzt ja in Ruhe dem Bericht für Anan widmen, den ich noch machen muss."

    scene lab
    with fadestart

    "Atropos" "…"

    "Atropos" "Verdammt!"

    # Atropos Gedanken
    symb"Warum funktioniert denn der Computer mit einem Mal nicht mehr?"

    if datewithera:

        show era confused:
            xalign 0.5

        "Era" "Atropos? W-Was ist los?"

        "Atropos" "Die Computer funktionieren aus irgendeinem Grund nicht."

        show era normal

        "Era" "Du könntest in den Serverraum gehen und dort mal nachfragen… Vi…Vielleicht wissen sie dort, was das Problem ist."

        "Atropos" "Stimmt, das ist eine gute Idee."

        "Atropos" "Wo liegt der Serverraum nochmal? Ich war schon seit Ewigkeiten nicht mehr dort."

        show era shy

        "Era" "Wenn…, wenn du willst könnte ich dich hinbringen?"

        menu:
            "Klar, gerne.":
                jump erabegleiten
            "Alles gut, ich finde es schon.":
                jump eranichtbegleiten

    else:

        show era shy_gray
        show narcais annoyed

        "Narcais" "Funktioniert dein Computer auch nicht mehr?"

        "Atropos" "Ja, keine Ahnung, was los ist…"

        "Narcais" "Ich kann ja vieles, aber keine Computer reparieren. Wir sollten vermutlich im Serverraum nachschauen."

        # Entscheidung 35
        menu:
            "Klar, lass uns gehen!":
                jump gowithnarcais
            "Geh du allein. Ich muss noch was anderes zwischenzeitlich fertigmachen.":
                jump dontgowithnarcais

label gowithnarcais:

    "Atropos" "Klar, lass uns gehen!"

    scene hall
    with fadeshort
    show narcais normal

    "Narcais" "Bist du schon dazugekommen mir über meinen Bericht drüber zuschauen?"

    "Atropos" "Ja, bin ich. Er ist wirklich gut geworden- wie immer."

    show narcais cocky

    "Narcais" "Ich weiß. Sag mal…"

    "Atropos" "Was?"

    show narcais confused

    "Narcais" "Hattest du schon mal eine Freundin?"

    "Atropos" "Was? Wie? Wie kommst du jetzt darauf?"

    show narcais normal

    "Narcais" "Hattest du?"

    "Atropos" "Nein, bisher noch nicht…"

    show narcais confused

    "Narcais" "Oh…"

    "Atropos" "Nein… sag mir nicht… du brauchst einen Rat? (lacht)"

    show narcais annoyed

    "Narcais" "Nein… nein… ich doch nicht…"

    "Atropos" "Na los, sag schon. Wie kann ich dir helfen?"

    "Atropos" "Um wen geht es?"

    show narcais confused

    "Narcais" "Kennst du Neiro?"

    "Atropos" "Neiro? Ja klar, wir sind befreundet."

    "Narcais" "Gibst du mir seine Nummer?"

    "Atropos" "Klar, kein Problem. (lacht) Hier, bitte, speichere sie dir ab."

    "Narcais" "Danke… und vergiss dieses Gespräch bitte…"

    "Atropos" "Keine Sorge. Ich denke, ihr wärt süß zusammen, ich drücke dir auf alle Fälle die Daumen!"

    show narcais normal

    "Narcais" "Danke."

    "Atropos" "…"

    "Narcais" "…"

    "Atropos" "Da vorne ist der Serverraum!"

    scene server_room
    with fadeshort

    "Atropos" "Hallo? Jemand da?"

    "Atropos" "Seltsam- es scheint keiner hier zu sein…"

    "Narcais" "Atropos?"

    "Atropos" "Hmm?"

    show narcais confused

    "Narcais" "Ich habe nächste Woche Geburtstag- feierst du ihn mit mir?"

    "Atropos" "Klar, gerne!"

    "Narcais" "Schaffst du es, Neiro mitzubringen?"

    "Atropos" "Mach dir da mal keine Sorgen! (lacht)"

    "Narcais" "Du kannst ihm ausrichten, dass es die beste Feier des Jahrzehnts wird- immerhin plane ich sie!"

    "Atropos" "Bestimmt! (lacht)"

    show narcais annoyed

    "Narcais" "Sei mal leise! Hörst du auch dieses seltsame Ticken?"

    "Atropos" "Du hast Recht… was ist das?"

    # Symbiont
    symb"{i}Lauf! {/i}"

    "Atropos" "Was?"

    show narcais confused

    "Narcais" "Was ist los?"

    "Atropos" "Warte… was ist das?"

    scene detail_bomb0006
    with fadeshort

    "Atropos" "Das… das kann doch nicht wahr sein…"

    scene serverroom
    with fadeshort

    "Narcais" "Eine Bombe?"

    "Atropos" "Wir haben keine Chance mehr…"

    "Atropos" "Tut mir leid wegen Neiro…"

    "Narcais" "Ich hoffe, er überlebt."


    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

label dontgowithnarcais:


    "Atropos" "Geh du allein. Ich muss noch was anderes zwischenzeitlich fertigmachen."

    hide narcais

    show era shy

    "Era" "A-An was arbeitest du gerade?"

    "Atropos" "Ach, ich muss noch ein paar Sachen fertigbekommen, nichts weiter wichtigstes."

    "Era" "O-Oh… okay…"

    "Atropos" "Kommst du mit deinen Analysen voran?"

    show era normal

    "Era" "J-Ja… ich denke schon!"

    "Atropos" "Freut mich zu hören, wenn du Hilfe brauchst, dann gib Bescheid."

    "Era" "Oh… danke… aber ich komme schon klar…"

    "Atropos" "Sag mal, Era…"

    "Era" "Hmm?"

    "Atropos" "Hast du Lust heute Abend zu grillen? Chesis, Kloth und ich sind verabredetet, aber sie haben bestimmt nichts gegen etwas Gesellschaft."

    show era shy

    "Era" "W-Was? Wie…? Ich…"

    "Atropos" "Also… du musst nicht… es war nur eine Idee gewesen."

    show era happy

    "Era" "Es würde mich sehr freuen…"

    "Atropos" "Super, dann ist es abgemacht!"

    show era shy

    "Era" "J-Ja…"

    "Atropos" "Soll ich dich dann nachher abholen?"

    show era happy

    "Era" "Gerne!"

    "Atropos" "Dann bin ich gegen 19 Uhr da."

    show era normal

    "Era" "Oh… Atropos…"

    "Atropos" "Was gibt’s? Kannst du doch nicht?"

    show era confused

    "Era" "Nein… nein! Ich… wollte nur fragen, ob meine Nichte uns begleiten kann. Seit meine Schwester und ihre Frau starben, kümmere ich mich um sie."

    "Era" "Ich weiß nicht, ob ich dir schonmal davon erzählt habe…"

    "Atropos" "Ich glaube du hattest es Mal erwähnt- Mögen sie nun für immer glücklich sein. Aber klar, bring sie mit! Es würde mich freuen sie kennenzulernen."

    show era happy

    "Era" "Danke…"

    show era shy

    "Era" "Und… und vielleicht können wir uns das nächste Mal dann ja zu zweit treffen?"


    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

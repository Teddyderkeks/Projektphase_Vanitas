label escapelater:

    "Atropos" "…"
    # Schwarzblende

    "Atropos" "Era, machst du auch Pause?"

    show era normal

    "Era" "Ich… Tut mir leid, ich muss noch das Protokoll hier fertig formulieren, solange ich alle Daten in meinem Kopf habe."

    "Era" "Ich kann also erst später Mittagspause machen."

    "Atropos" "Alles klar, kein Problem. Narcais, wie sieht es bei dir aus?"

    show narcais normal

    "Narcais" "Ich brauche so etwas wie eine Pause nicht. Deswegen leiste ich ja auch so hervorragende Arbeit, weil ich viel mehr Zeit habe, mich dieser zu widmen."

    "Narcais" "Kann ich denn wenigstens heute noch von dir Feedback erwarten?"

    "Atropos" "Ich hatte erst einmal alles für Anans Bericht fertiggestellt, aber sobald ich von der Mittagspause zurückkomme, setze ich mich dran."

    "Narcais" "Danke, das klingt doch vielversprechend."

    "Atropos" "Also dann, ihr beiden. Wir sehen uns später."

    "Era" "B-Bis später!"

    scene hall

    # Atropos Gedanken
    "Jetzt suche ich erstmal nach Chesis- vielleicht will er mit in die Mittagspause kommen."

    scene shop_1

    # Atropos Gedanken
    "Aither ist mittlerweile ganz schön voll. Heute kommen wohl viele Leute, um ihre Vorräte neu aufzufüllen."

    "Zelos" "Atropos! Komm mal schnell her."

    show zelos normal

    "Atropos" "Was gibt’s?"

    "Zelos" "Wie du siehst, brummt uns der Laden. Ich muss meine Mittagspause verschieben. Aber Tycho und die anderen waren gerade da, sie wollten zur Mensa, wenn du sie suchst."

    "Atropos" "Danke für die Info, aber ich denke, ich suche erstmal nach Chesis."

    "Zelos" "Alles klar. Dir noch eine schöne Mittagspause!"

    "Atropos" "Danke, dir auch!"

    "Zelos" "Einen wunderschönen, glücklichen guten Morgen! Was kann ich dir heute Gutes tun?"

    # Atropos Gedanken
    "Zelos wirkt beschäftigt, ich sollte ihn nicht länger aufhalten. Dann suche ich mal nach Chesis.¬¬"

    scene shop_2

    # Atropos Gedanken
    "Da ist ja Chesis. Aber er scheint auch noch beschäftigt zu sein. Er hat wohl gerade ein Beratungsgespräch.¬¬"

    # Hier Möglichkeit sich umzuschauen während man auf Chesis wartet.

    show chesis smiling

    "Chesis" "Hey Atropos."

    "Atropos" "Hast du Zeit für eine Mittagspause?"

    "Chesis" "Bin gerade mit meinem Gespräch fertig geworden, wo wollen wir hin?"

    # Hier Option für weiteren Smalltalk wie Chesis Arbeitstag verlaufen ist


    "Atropos" "Gehen wir ins Büro und holen uns dort erstmal einen Kaffee?"

    "Chesis" "Gerne."

    scene office_2

    "Atropos" "Die anderen sind nicht da, vermutlich sind sie bereits in der Mensa. Wollen wir uns ihnen nachher anschließen?"

    "Chesis" "Ich denke, mir reicht ein Kaffee, es sei denn, du willst unbedingt gehen?"

    "Atropos" "Alles gut, wegen mir müssen wir nicht in die Mensa. Ich weiß doch, dass du dich am wohlsten fühlst, wenn wir nur unter uns sind."

    "Chesis" "Danke."

    "Atropos" "Wie war dein Arbeitstag heute?"

    "Chesis" "Gut. Wie immer."

    "Atropos" "Meinen Tag heute wirst du mir nicht glauben!"

    "Chesis" "Was ist passiert?"

    "Atropos" "Ich durfte mehrmals mit Anan sprechen!"

    "Chesis" "Wow, wie kam es dazu?"

    "Atropos" "Ich… ich hatte meine Pille vergessen, aber Anan war so unglaublich verständnisvoll und öffnete mir die Augen."

    "Atropos" "Ich bin wirklich froh, für Aither arbeiten zu dürfen!"

    "Atropos" "Und ich bin froh, dass mir Anan meinen Fehler verziehen hat. Er ist wirklich der beste Chef, den man sich wünschen kann!"

    "Chesis" "Das stimmt wohl!"

    "Chesis" "Sag mal, stört es dich, wenn Philote heute Abend mit uns isst?"

    "Atropos" "War sie nicht mit Freunden verabredet?"

    "Chesis" "Ja, aber die haben keine Zeit mehr."

    "Atropos" "Achso… ja, klar, kein Problem. Philote gehört doch schon seit Jahren unzertrennlich zu dir und ich mag sie wirklich gern."

    "Chesis" "Danke!"

    "Chesis" "Oh… tut mir leid, ich habe gleich noch einen wichtigen Termin. Ich muss zurück."

    "Atropos" "Kein Problem, wir sehen uns dann später!"

    "Chesis" "Bis dann!"

    hide chesis

    # Atropos Gedanken
    "Dann werde ich einfach schon Mal ins Labor zurück. Ich habe sonst ohnehin nichts mehr zu tun."

    scene lab

    # Atropos Gedanken
    "Era und Narcais scheinen beide in der Mittagspause zu sein. Dann kann ich mich jetzt ja in Ruhe dem Bericht für Anan widmen, den ich noch machen muss."

    "Atropos" "…"

    "Atropos" "Verdammt!"

    # Atropos Gedanken
    "Warum funktioniert denn der Computer mit einem Mal nicht mehr?"

    if datewithera:

        show era normal:
            xalign 0.5

        "Era" "Atropos? W-Was ist los?"

        "Atropos" "Die Computer funktionieren aus irgendeinem Grund nicht."

        "Era" "Du könntest in den Serverraum gehen und dort mal nachfragen… Vi…Vielleicht wissen sie dort, was das Problem ist."

        "Atropos" "Stimmt, das ist eine gute Idee."

        "Atropos" "Wo liegt der Serverraum nochmal? Ich war schon seit Ewigkeiten nicht mehr dort."

        "Era" "Wenn…, wenn du willst könnte ich dich hinbringen?"

        menu:
            "Klar, gerne.":
                jump erabegleiten
            "Alles gut, ich finde es schon.":
                jump eranichtbegleiten

    else:

        show narcais normal

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
    show narcais normal

    "Narcais" "Bist du schon dazugekommen mir über meinen Bericht drüber zuschauen?"

    "Atropos" "Ja, bin ich. Er ist wirklich gut geworden- wie immer."

    "Narcais" "Ich weiß. Sag mal…"

    "Atropos" "Was?"

    "Narcais" "Hattest du schon Mal eine Freundin?"

    "Atropos" "Was? Wie? Wie kommst du jetzt darauf?"

    "Narcais" "Hattest du?"

    "Atropos" "Nein, bisher noch nicht…"

    "Narcais" "Oh…"

    "Atropos" "Nein… sag mir nicht… du brauchst einen Rat? (lacht)"

    "Narcais" "Nein… nein… ich doch nicht…"

    "Atropos" "Na los, sag schon. Wie kann ich dir helfen?"

    "Atropos" "Um wen geht es?"

    "Narcais" "Kennst du Neiro?"

    "Atropos" "Neiro? Ja klar, wir sind befreundet."

    "Narcais" "Gibst du mir seine Nummer?"

    "Atropos" "Klar, kein Problem. (lacht) Hier, bitte, speichere sie dir ab."

    "Narcais" "Danke… und vergiss dieses Gespräch bitte…"

    "Atropos" "Keine Sorge. Ich denke, ihr wärt süß zusammen, ich drücke dir auf alle Fälle die Daumen!"

    "Narcais" "Danke."

    "Atropos" "…"

    "Narcais" "…"

    "Atropos" "Da vorne ist der Serverraum!"

    scene server_room

    "Atropos" "Hallo? Jemand da?"

    "Atropos" "Seltsam- es scheint keiner hier zu sein…"

    "Narcais" "Atropos?"

    "Atropos" "Hmm?"

    "Narcais" "Ich habe nächste Woche Geburtstag- feierst du ihn mit mir?"

    "Atropos" "Klar, gerne!"

    "Narcais" "Schaffst du es, Neiro mitzubringen?"

    "Atropos" "Mach dir da mal keine Sorgen! (lacht)"

    "Narcais" "Du kannst ihm ausrichten, dass es die beste Feier des Jahrzehnts wird- immerhin plane ich sie!"

    "Atropos" "Bestimmt! (lacht)"

    "Narcais" "Sei mal leise! Hörst du auch dieses seltsame Ticken?"

    "Atropos" "Du hast Recht… was ist das?"

    # Symbiont
    "{i}Lauf! {/i}"

    "Atropos" "Was?"

    "Narcais" "Was ist los?"

    "Atropos" "Warte… was ist das?"

    # zeigt Bombe mit 6 Sekunden Zeit übrig

    "Atropos" "Das… das kann doch nicht wahr sein…"

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

    show era normal

    "Era" "A-An was arbeitest du gerade?"

    "Atropos" "Ach, ich muss noch ein paar Sachen fertigbekommen, nichts weiter wichtigstes."

    "Era" "O-Oh… okay…"

    "Atropos" "Kommst du mit deinen Analysen voran?"

    "Era" "J-Ja… ich denke schon!"

    "Atropos" "Freut mich zu hören, wenn du Hilfe brauchst, dann gib Bescheid."

    "Era" "Oh… danke… aber ich komme schon klar…"

    "Atropos" "Sag mal, Era…"

    "Era" "Hmm?"

    "Atropos" "Hast du Lust heute Abend zu grillen? Chesis, Kloth und ich sind verabredetet, aber sie haben bestimmt nichts gegen etwas Gesellschaft."

    "Era" "W-Was? Wie…? Ich…"

    "Atropos" "Also… du musst nicht… es war nur eine Idee gewesen."

    "Era" "Es würde mich sehr freuen…"

    "Atropos" "Super, dann ist es abgemacht!"

    "Era" "J-Ja…"

    "Atropos" "Soll ich dich dann nachher abholen?"

    "Era" "Gerne!"

    "Atropos" "Dann bin ich gegen 19 Uhr da."

    "Era" "Oh… Atropos…"

    "Atropos" "Was gibt’s? Kannst du doch nicht?"

    "Era" "Nein… nein! Ich… wollte nur fragen, ob meine Nichte uns begleiten kann. Seit meine Schwester und deren Frau starb, kümmere ich mich um sie."

    "Era" "Ich weiß nicht, ob ich dir schonmal davon erzählt habe…"

    "Atropos" "Ich glaube du hattest es Mal erwähnt- Mögen sie nun für immer glücklich sein. Aber klar, bring sie mit! Es würde mich freuen sie kennenzulernen."

    "Era" "Danke…"

    "Era" "Und… und vielleicht können wir uns das nächste Mal dann ja zu zweit treffen?"


    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

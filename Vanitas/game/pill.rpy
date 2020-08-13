label pill:
    scene lab

    # Atropos Gedanken
    "Endlich Mittagspause. Ich muss meinen Kopf ein bisschen frei bekommen. Von Narcais Vortrag schwirrt mir immer noch der Kopf."

    "Atropos" "Era, machst du auch Pause?"

    show era normal:
        xalign 0.5

    "Era" "Ich… tut mir leid, ich muss noch das Protokoll hier fertig formulieren solange ich alle Daten in meinem Kopf habe."

    "Era" "Ich kann also erst später Mittagspause machen."

    "Atropos" "Alles klar, kein Problem. Narcais, wie sieht es bei dir aus?"

    show narcais normal:
        xalign 0.25
    show era normal:
        xalign 0.75

    "Narcais" "Ich brauche so etwas wie eine Pause nicht. Deswegen leiste ich ja auch so hervorragende Arbeit, weil ich viel mehr Zeit habe mich dieser zu widmen."

    "Narcais" "Kann ich denn wenigstens von dir heute noch Feedback erwarten?"

    "Atropos" "Ich hatte erst einmal alles für Anans Bericht fertiggestellt, aber sobald ich von der Mittagspause zurückkomme, setze ich mich dran."

    "Narcais" "Danke, das klingt doch vielversprechend."

    "Atropos" "Also dann ihr beiden. Wir sehen uns später."

    "Era" "B-Bis später."

    hide era
    hide narcais

    scene hall

    # Atropos Gedanken
    "Soll ich erst nach Kloth suchen oder erst nach Chesis? Den anderen kann ich mich auch nachher noch anschließen."

    # Symbiont
    "{i}Verbringe die Pause besser mit Chesis allein. Kloth scheint beschäftigt zu sein, sonst hätte er dir schon längst auf deine Nachrichten geantwortet. {/i}"

    # Symbiont
    "{i}Du willst ihn doch nicht bei irgendetwas stören. {/i}"


    menu:
        "Ich sollte nach Kloth suchen.":

            # Atropos Gedanken
            "Ich sollte nach Kloth suchen. Ich wüsste zu gerne, warum er sich so lange nicht bei mir gemeldet hatte."

            # Atropos Gedanken
            "Ob etwas vorgefallen ist? Ich denke ich probiere mal ihn anzurufen."
            jump search_kloth
        "Ich werde erstmal nach Chesis suchen.":

            # Atropos Gedanken
            "Ich werde erstmal nach Chesis suchen. Danach werde ich weitersehen."

            # Atropos Gedanken
            "Wo könnte er gerade nur sein? Er müsste seine Mittagspause eigentlich auch bereits angefangen habe, aber sicherheitshalber kann ich ja mal im Geschäft unten nachsehen."
            jump still_search_chesis


label still_search_chesis:

    scene shop_1

    # Atropos Gedanken
    "Aither ist mittlerweile ganz schön voll. Heute kommen wohl viele Leute, um ihre Vorräte neu aufzufüllen."

    "Zelos" "Atropos! Komm mal schnell her."

    show zelos normal:
        xalign 0.5

    "Atropos" "Was gibt´s?"

    "Zelos" "Wie du siehst brummt uns der Laden. Ich muss meine Mittagspause verschieben. Aber Tycho und die anderen waren gerade da, sie wollten zur Mensa, wenn du sie suchst."

    "Atropos" "Danke für die Info, aber ich denke ich suche erstmal nach Chesis."

    "Zelos" "Alles klar. Dir noch eine schöne Mittagspause."

    "Atropos" "Danke, dir auch!"

    "Zelos" "Einen wunderschönen glücklichen guten Morgen. Was kann ich dir heute Gutes tun?"

    # Atropos Gedanken
    "Zelos wirkt beschäftigt, ich sollte ihn nicht länger aufhalten. Dann suche ich mal nach Chesis."

    scene shop_2

    # Atropos Gedanken
    "Da ist ja Chesis. Aber er scheint auch noch beschäftigt zu sein. Er hat wohl gerade ein Beratungsgespräch."

    show chesis smiling:
        xalign 0.5

    "Chesis" "Hey Atropos."

    "Atropos" "Hast du Zeit für eine Mittagspause?"

    show chesis grinning2

    "Chesis" "Bin gerade mit meinem Gespräch fertig geworden, wo wollen wir hin?"

    "Atropos" "Lass uns doch nach Kloth suchen. Er will seine Mittagspause bestimmt nicht alleine verbringen."

    show chesis confused

    "Chesis" "Ich weiß nicht."

    "Atropos" "Ach komm, wir haben doch schon seit Ewigkeiten die Mittagspause nicht mehr zu dritt verbracht, weil immer einer von uns beschäftigt gewesen war."

    "Atropos" "Lass uns das heute ändern!"

    show chesis angry

    "Chesis" "Er hat sich schon den ganzen Tag nicht gemeldet und ich kann mir besseres vorstellen als meine Mittagspause darauf zu verschwenden ihn zu suchen."

    "Atropos" "Wir sind doch Freunde und bestimmt ist er einfach nur in seinem Büro. Ich kann ihn auch einfach anrufen."

    show chesis confused

    "Chesis" "Ich weiß nicht."

    "Chesis" "Er wird schon auftauchen und wir sehen ihn dann beim Grillen heute Abend."

    "Atropos" "Du klingst fast als wüsstest du, warum Kloth nicht erreichbar ist."

    "Atropos" "Ist etwas vorgefallen? Ich fange langsam an mir Sorgen zu machen."

    # Symbiont
    "{i}Es gibt nichts, worüber du dir Sorgen machen müsstest. Es geht ihm bestimmt gut. {/i}"

    # Symbiont
    "{i}Nicht jeder ist nun mal ständig am Handy und erreichbar. Freu e dich lieber auf nachher, wenn du ihn wiedersiehst. {/i}"

    show chesis smiling

    "Chesis" "Ach spielt doch keine Rolle. Du zerbrichst dir unnötig den Kopf."

    menu:
        "Ich möchte trotzdem lieber nach Kloth suchen.":

            "Atropos" "Ich denke ich möchte trotzdem lieber nach Kloth suchen."

            "Atropos" "Ich bin glücklicher, wenn ich weiß, dass bei ihm alles in Ordnung ist."

            show chesis confused

            "Chesis" "Wie du meinst. Ich gehe lieber was essen, ich habe Hunger."

            "Atropos" "Klar, kein Problem. Wir sehen uns später."

            jump search_kloth
        "Du hast Recht.":

            "Atropos" "Du hast Recht. Es wird schon alles in Ordnung sein."

            "Atropos" "Kloth hat sich uns noch immer anvertraut, wenn ihn etwas beschäftigt hatte."

            "Atropos" "Ich kann ihn heute Abend ja auch mal darauf ansprechen."

            "Atropos" "Gehen wir ins Büro und holen uns dort einen Kaffee?"

            show chesis grinning

            "Chesis" "Gerne."

            jump mittagspausemitchesis

label mittagspausemitchesis:

    scene office_2
    show chesis smiling:
        xalign 0.5
    "Atropos" "Die anderen sind nicht da, vermutlich sind sie bereits in der Mensa. Wollen wir uns ihnen anschließen?"

    "Chesis" "Ich denke mir reicht ein Kaffee, es sei denn du willst unbedingt gehen?"

    "Atropos" "Alles gut, wegen mir müssen wir nicht in die Mensa. Ich weiß doch, dass du dich am wohlsten fühlst, wenn wir nur unter uns sind."

    show chesis grinning

    "Chesis" "Danke."
    # Gespräch über Kloths Schüchternheit und die Überwindung dieser dank Atropos und Kloth möglich.

    "Atropos" "Sag Mal, Chesis. Ist dir eine Veränderung an Kloth in der letzten Zeit aufgefallen?"

    show chesis confused

    "Chesis" "Wie meinst du das?"

    "Atropos" "Nicht nur, dass Kloth sich in letzter Zeit kaum bei uns gemeldet hat, aber er wirkte irgendwie fast schon erschöpft? Als würde ihn irgendetwas beschäftigen…"

    show chesis smiling

    "Chesis" "Ich denke du irrst dich."

    show chesis confused

    "Chesis" "Er hat einfach viel zu tun wegen der Gründungsfeier und ist deswegen bestimmt gestresst."

    "Atropos" "Ich weiß nicht… ich denke wir sollten vielleicht doch besser mal nach ihm schauen."

    show chesis grinning2

    "Chesis" "Du hast dir schon immer zu viele Gedanken um alles gemacht."

    "Atropos" "Denkst du, dass ich mir gerade wirklich zu viele Sorgen mache?"

    # Symbiont
    "{i}Ja, machst du dir. Vergiss all diese Zweifel, sie machen dich doch nur unglücklich. {/i}"

    # Symbiont
    "{i}Dein Leben ist ohne sie so viel einfacher und glücklicher. {/i}"

    show chesis smiling

    "Chesis" "Ja, bleibe einfach ruhig. Das wird sich alles aufklären und am Ende werden wir darüber lachen."

    menu:
        "Du hast ja Recht. Tut mir leid.":

            "Atropos" "Du hast ja Recht. Tut mir leid, ich weiß nicht, was in mich gefahren ist."

            "Atropos" "Ich sollte aufhören mir so viele Gedanken und Sorgen zu machen."

            # Atropos Gedanken
            "Vermutlich verhalte ich mich so, weil ich die Pille zu oft vergessen hatte. Es hat also doch Auswirkungen."

            # Atropos Gedanken
            "Zukünftig werde ich sie auf keinen Fall mehr vergessen. Ich will glücklich sein und ein glückliches Leben führen können."

            show chesis grinning

            "Chesis" "(lacht) Ja, solltest du."

            # weiterer Smalltalk möglich

            "Atropos" "Oh, es ist schon spät, ich muss langsam zurück. Ich habe noch einiges an Arbeit, die sich stapelt."

            "Chesis" "Kein Problem, wir sehen uns dann später."

            "Atropos" "Um 19 Uhr bei dir dann?"

            show chesis smiling

            "Chesis" "Ja genau, ich freue mich schon."

            "Atropos" "Ich mich auch, bis dann."

            jump not_search_kloth
        "Ich gehe trotzdem besser auf Nummer sicher und suche ihn.":

            "Atropos" "Ich gehe trotzdem besser auf Nummer sicher und suche ihn."

            show chesis confused

            "Chesis" "Wenn du meinst. Viel Erfolg und richte ihm schöne Grüße aus, wenn du ihn findest."

            "Atropos" "Klar mache ich. Wir sehen uns dann später. 19 Uhr, richtig?"

            show chesis smiling

            "Chesis" "Ja, genau. Ich freue mich, bis dann."

            "Atropos" "Mach´s gut, bis später."

            jump search_kloth


label not_search_kloth:
    if read_document_kloth:
        # Atropos Gedanken
        "Das sind firmeninterne Sachen. Die gehen mich nichts an, ich sollte lieber zurück zur Arbeit."

        # Atropos Gedanken
        "Über Kloth werde ich schon früher oder später mehr erfahren."

        # Atropos Gedanken
        "Wenn er so weit ist, wird er mir alles erzählen. Und bis dahin kann ich warten. Wir sind immerhin beste Freunde."

        # Atropos Gedanken
        "Und wenn er Hilfe braucht, dann werde ich ihm helfen. Wenn ich mich richtig erinnere und es ihm tatsächlich nicht gut geht…"

        # Atropos Gedanken
        "Ich werde immer an seiner Seite stehen und für ihn da sein, wenn er mich braucht."

        scene hall

        # Atropos Gedanken
        "So… ich habe Kloth nochmals eine Nachricht geschrieben. Ich bin mir sicher es wird sich alles aufklären."

        # Atropos Gedanken
        "Und jetzt zurück ins Labor."

        scene lab

        jump laborpillende

    if infos_count_kloth == 1 or infos_count_kloth == 2:
            # Atropos Gedanken
            "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein."

            # Atropos Gedanken
            "Das alles sind nichts anderes als Hirngespinste."

            # Atropos Gedanken
            "Ja, ganz bestimmt! Ich bilde mir das ganze nur ein…"

            # Atropos Gedanken
            "Ich kehre jetzt einfach ins Labor zurück und vergesse das Ganze. Alles wird wieder wie zuvor sein."
            # Symbiont
            "{i}Ja, vergiss es. Sei einfach nur glücklich. Du bist sicher, nichts kann dir passieren. Das alles hier ist niemals passiert. Du hast eine ganz normale Mittagspause verbracht. {/i}"

            # Symbiont
            "{i}Sei glücklich, Atropos. {/i}"

            scene hall

            # Atropos Gedanken
            "Ob wohl Era da ist? Ich würde gerne ein bisschen Zeit mit ihr alleine verbringen und sie besser kennenlernen."

            # Atropos Gedanken
            "Auch wenn sie manchmal anstrengend sein kann, ist sie doch ziemlich süß."

            scene lab
            jump laborpillende

label laborpillende:

    scene lab
    # Atropos Gedanken
    "Era und Narcais scheinen beide in der Mittagspause zu sein. Dann kann ich mich jetzt ja in Ruhe dem Bericht für Anan widmen, den ich noch machen muss."

    "Atropos" "…"

    "Atropos" "Verdammt!"

    # Atropos Gedanken
    "Warum funktioniert denn der Computer mit einem Mal nicht mehr?"

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

label erabegleiten:

    "Atropos" "Klar, gerne. Wenn du gerade die Zeit dafür hast?"

    "Era" "Ja… Ja… natürlich. "

    scene hall
    show era normal:
        xalign 0.5

    "Atropos" "…"

    "Era" "…"

    "Atropos" "Ich…"

    "Atropos" "Ist das dann ein Date? Also das bowlen?"

    "Era" "Ich… was? Wie? Ähmm… ahhh…"

    # etwas verlegen
    "Atropos" "Tut mir leid, ich wollte dich damit nicht überrumpeln, aber es würde mich sehr freuen."

    "Era" "Ja ist es…"

    "Atropos" "Du weißt gar nicht wie glücklich ich gerade bin. Ich freue mich schon sehr auf das Date!"

    "Era" "Ich mich auch."

    "Atropos" "So, wir sind da- mal schauen, ob sie uns weiterhelfen können."

    scene server_room

    show era normal:
        xalign 0.5

    "Atropos" "Hallo? Jemand da?"

    "Atropos" "Seltsam- es scheint keiner hier zu sein…"

    "Era" "Nicht? Aber man hört doch das Ticken einer Uhr- da, um die Ecke rum…"

    "Atropos" "Hallo? Wir haben ein Problem mit unserem Computer und können Hilfe gebrauchen… ist jemand hier?"

    "Era" "Vielleicht… ist die Person in ihre Arbeit vertieft und hört uns nicht?"

    "Atropos" "Gut möglich, lass uns nachschauen gehen."

    "Era" "…"

    "Era" "Das ist aber eine seltsame Uhr. So etwas habe ich noch nie gesehen…"

    # Atropos Gedanken
    "Warte… das ist doch keine Uhr, oder? Das sieht mehr aus wie…"

    "Atropos" "Era, geh da weg! Sofort!"

    # Symbiont
    "{i}Lauf, Atropos.{/i}"

    "Era" "Was, warum? Es ist doch alles in Ordnung. Aber hier ist niemand. Wir sollten wo anders suchen gehen."

    "Atropos" "Wirf sie sofort weg!"

    "Era" "Hmm?"

    "Atropos" "Era!"

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

label eranichtbegleiten:

    "Atropos" "Alles gut, ich finde es schon."

    "Era" "O-Okay… und Atropos…?"

    "Atropos" "Was gibt´s?"

    "Era" "Ich freue mich aufs Bowlen!"

    "Atropos" "Ich mich auch, Era. Sehr sogar."

    "Atropos" "Also, bis gleich."

    scene hall

    # Atropos Gedanken
    "Ich hoffe es ist überhaupt jemand da. Soweit ich weiß, machen die Kollegen aus dem Serverraum immer erst ziemlich spät Mittagspause."

    # Atropos Gedanken
    "Ah, da ist er ja schon. Mal sehen, ob mir dort jemand weiterhelfen kann."

    scene server_room

    "Atropos" "Hallo? Jemand hier?"

    "Atropos" "Hmmm… Sieht nicht danach aus…"

    # Atropos Gedanken
    "Was ist dieses Geräusch? Es hört sich irgendwie seltsam an."

    # Atropos Gedanken
    "Ich kenne es, aber gleichzeitig kann ich es nicht wirklich zuordnen…"

    # Atropos Gedanken
    "Ich sehe einfach mal nach."

    # Atropos Gedanken
    "Was ist das? Es sieht aus wie eine Uhr, aber…"

    # Symbiont
    "{i}Renn, Atropos!{/i}"

    # Atropos Gedanken
    "Wie? Was?"

    # Atropos Gedanken
    "Das kann nicht real sein."

    # Symbiont
    "{i}Renn! {/i}"

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

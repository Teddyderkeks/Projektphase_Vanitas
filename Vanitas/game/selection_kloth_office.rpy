default kloth_office_choice = False
default password_right = False
default kloth_office_visited = False

label selection_kloth_office:
    $ kloth_office_choice = True
    $ kloth_office_visited = True




    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                jump everything_seen
            else:
                menu:
                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        "Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        "Ich brauche jetzt Antworten, sonst werde ich verrückt…"

                        jump still_search_kloth
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        jump not_search_kloth
        else:
            if read_document_kloth:
                menu:
                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        "Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        "Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":

                        jump not_search_kloth
            else:
                menu:
                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth
                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        "Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        "Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        jump not_search_kloth
    else:
        if read_computer_kloth:
            if read_document_kloth:
                menu:
                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        "Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        "Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        jump not_search_kloth
            else:
                menu:
                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        "Ich muss Kloth sofort finden!"

                        # Atropos Gedanken
                        "Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":


                        jump not_search_kloth
        else:
            if read_document_kloth:
                menu:
                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth
                    "Ich muss Kloth sofort finden!":
                        # Atropos Gedanken
                        "Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        "Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Das sind firmeninterne Sachen. Die gehen mich nichts an, ich sollte lieber zurück zur Arbeit.":
                        jump not_search_kloth
            else:
                menu:
                    "Ich werde mir den Brief anschauen.":
                        jump letter_kloth
                    "Ich werde den Computer durchsuchen.":
                        jump computer_kloth
                    "Ich werde mir das Dokument anschauen.":
                        jump document_kloth

label letter_kloth:
    $ read_letter_kloth = True
    $ infos_count_kloth += 1

    # Atropos Gedanken
    "Ich werde mir den Brief anschauen."

    # Atropos Gedanken
    " Mal sehen, was darin steht."


    if read_computer_kloth:

        "Liest sich wie eine Art Abschiedsbrief voller Angst und Zweifel über Aither"

        # Atropos Gedanken
        "Was habe ich da gerade gelesen?"

        # Atropos Gedanken
        "Das alles wird ja immer schlimmer… was soll ich nur tun?"

        # Atropos Gedanken
        "Das macht mir Angst. Wo ist Kloth nur? Ich muss mit ihm über all das sprechen…"

    else:
        "Liest sich wie eine Art Abschiedsbrief voller Angst und Zweifel über Aither"

        # Atropos Gedanken
        "Was habe ich da gerade gelesen?"

        # Atropos Gedanken
        "Ich mache mir immer größere Sorgen um Kloth… Irgendetwas scheint nicht zu stimmen…"

        # Symbiont
        "{i}Du interpretierst zu viel in seine Worte. Er ist wahnsinnig. Glaubst du das alles hier wirklich? {/i}"

        # Symbiont
        "{i}Das alles sind nur seltsame Fantasien. Dinge, die sich Kloth zusammengebastelt hat wie es ihm gefällt. {/i}"

        # Symbiont
        "{i}Er scheint das Böse zu suchen und es in Aither gefunden zu haben. {/i}"

        # Symbiont
        "{i}Er braucht Hilfe. Er ist nicht mehr bei Sinnen. Höre nicht auf ihn, Atropos. {/i}"

        # Symbiont
        "{i}Du bist glücklich. Willst du dieses Glück riskieren? {/i}"

        if read_letter_kloth:
            if read_computer_kloth:
                if read_document_kloth:
                    jump everything_seen
                else:
                    # Atropos Gedanken
                    "Was soll ich jetzt tun?"

    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label computer_kloth:
    $ read_computer_kloth = True
    $ infos_count_kloth += 1

    # Atropos Gedanken
    "Ich werde den Computer durchsuchen."

    # Atropos Gedanken
    "Ob er wohl passwortgeschützt ist?"

    # Atropos Gedanken
    "Es gibt einen passwortgeschützten Teil und einen, für den ich kein Passwort brauche."

    # Atropos Gedanken
    "Hatte Kloth mir gegenüber mal erwähnt, was das Passwort ist?"

    # Atropos Gedanken
    "Ich kann es einfach mal ausprobieren."

    # Symbiont
    "{i}Du willst dich in den PC deines Freundes einhacken? Denkst du wirklich, dass du das tun solltest? {/i}"

    # Symbiont
    "{i}Letzten Endes wird es ihn und dich unglücklich machen. Denk nach Atropos und triff die richtige Entscheidung. {/i}"

    # Symbiont
    "{i}Du möchtest doch glücklich sein. {/i}"


    "Möglichkeit zur Eingabe Passwort"

    python:
        password = renpy.input ("Passwort:")

    if password == "Sadness" or password == "sadness":
        $ password_right = True
        "Kloth hat Bombe gelegt. Ist der Ansicht damit die Welt zu retten. Bombe kann nicht mehr gestoppt werden, Failsafe."

        # Atropos Gedanken
        "Was ist das? Das kann doch alles nicht wahr sein… Wie? Warum?"

        # Symbiont
        "{i}Du musst die Bombe stoppen, Atropos. Rette alle Menschen. Du kannst nicht zulassen, dass das Glück aller Menschen durch so etwas verpufft. {/i}"

        # Symbiont
        "{i}Lass nicht zu, dass so viele darunter leiden müssen, was ein einziger Irrer vollbracht hat! {/i}"

        # Symbiont
        "{i}Bringe den Menschen Glücklichkeit! {/i}"

        # Symbiont
        "{i}Bringe dir selbst Glücklichkeit! {/i}"


    else:

        # Atropos Gedanken
        "Falsches Passwort... Ich muss wo anderes weitersuchen..."


    # Atropos Gedanken
    "Was ist das hier? Es scheint eine Art Online Blog zu sein…"

    "Blog wird gezeigt. Bombenleger, der Aither vernichten will."

    # Atropos Gedanken
    "Eine Bombe?"


    python:
        password = password.strip()

    if password_right:
        # Atropos Gedanken
        "Also waren die Informationen von zuvor tatsächlich wahr?"

    else:
        # Symbiont
        "{i}Willst du die Bombe finden und entschärfen? {/i}"

        # Symbiont
        "{i}Würde es dich unglücklich machen alle Menschen im Stich zu lassen? {/i}"

        # Atropos Gedanken
        "Ist das alles wirklich wahr?"

        # Atropos Gedanken
        "Ich kann es kaum glauben…"


    # Atropos Gedanken
    "Was soll ich jetzt nur tun?"

    # Atropos Gedanken
    "Das alles ist zu viel für mich… wie soll ich mit diesen Informationen umgehen? Was soll ich tun?"

    # Atropos Gedanken
    "Das kann doch gar nicht wahr sein, oder? Aber was, wenn doch?"

    # Atropos Gedanken
    "Was ist, wenn es tatsächlich eine Bombe in Aither gibt? Was ist mit all den Menschen?"

    # Atropos Gedanken
    "Werden sie alle sterben?"

    # Atropos Gedanken
    "Aber was kann ich schon dagegen ausrichten?"

    # Atropos Gedanken
    "Ich bin doch nur ein bedeutungsloser kleiner Mensch."

    # Atropos Gedanken
    "Und was, wenn es doch alles nur Lügen sind? Kloth wirkte in meinen Erinnerungen wirklich wahnsinnig…"

    # Atropos Gedanken
    "Soll ich ihn zur Rede stellen?"


    if infos_count_kloth == 1 or infos_count_kloth == 2:
        # Atropos Gedanken
        "Oder soll ich noch mehr Sachen untersuchen, um mehr darüber herauszufinden? Aber will ich wirklich mehr wissen?"


    # Atropos Gedanken
    "Das alles macht mir Angst…"

    # Symbiont
    "{i}Du bist unglücklich. Es liegt an dir, wieder glücklich zu werden. {/i}"

    # Symbiont
    "{i}Es ist deine Entscheidung, wie du dieses Glück erreichen willst. {/i}"

    # Symbiont
    "{i}Allein deine Entscheidung und deine Wahl. {/i}"

    # Symbiont
    "{i}Dein Ziel ist klar: Werde wieder glücklich. Auf welchem Weg auch immer du dieses Glück erreichst. {/i}"


    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label document_kloth:
    $ read_document_kloth = True
    $ infos_count_kloth += 1

    # Atropos Gedanken
    "Ich werde mir das Dokument anschauen."

    # Atropos Gedanken
    "Was es mir wohl verrät?"


    if read_computer_kloth:
        "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

        # Atropos Gedanken
        "Die Server? Das spielt gerade keine Rolle… das sind doch nur unwichtige Informationen…"

        # Atropos Gedanken
        "Ist hier denn nichts mehr zu der Bombe?"

        # Atropos Gedanken
        "Und warum hatte Kloth diesen Blog offen?"

        # Atropos Gedanken
        "Sagt der Schreiber wirklich die Wahrheit?"

        # Atropos Gedanken
        "Was soll ich tun?"

        # Atropos Gedanken
        "Was soll ich tun?"

        # Atropos Gedanken
        "Was soll ich nur tun?"


    else:
        "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

        # Atropos Gedanken
        "Wenn ich das richtig verstehe… Wenn einer der Server zusammenbricht, würde alles untergehen, oder?"

        # Symbiont
        "{i}Warum machst du dir überhaupt darüber Gedanken? {/i}"

        # Symbiont
        "{i}Das ist nichts, was du wissen musst, um glücklich zu sein und ein glückliches Leben zu führen. {/i}"

        # Symbiont
        "{i}Schaue dir nichts mehr an. Schon für das, was du bereits gesehen hast, könntest du einen Haufen Ärger bekommen. {/i}"

        # Symbiont
        "{i}Du willst doch glücklich sein. {/i}"

        if read_letter_kloth:
            if read_computer_kloth:
                if read_document_kloth:
                    jump everything_seen
                else:
                    # Atropos Gedanken
                    "Was soll ich jetzt tun?"


    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

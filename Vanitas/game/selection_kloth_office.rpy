default kloth_office_choice = False
default password_right = False
default kloth_office_visited = False

label selection_kloth_office:
    $ renpy.fix_rollback()
    $ kloth_office_choice = True
    $ kloth_office_visited = True



    $ lookaroundklothsoffice = True
    if read_letter_kloth:
        if read_computer_kloth:
            if read_document_kloth:
                $ klothwatchedeverything= True
                $ lookaroundklothsofficewatchedeverything= True
                jump everything_seen
            else:
                show screen force_mouse_move_klothoffice
                menu:
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        $ lookaroundklothsofficewatcheddontsearchkloth = True
                        hide screen force_mouse_move_klothoffice
                        jump not_search_kloth
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ lookaroundklothsofficewatchedatleastonethensearchedkloth = True
                        hide screen force_mouse_move_klothoffice
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich werde mir das Dokument anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump document_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth
        else:
            if read_document_kloth:
                show screen force_mouse_move_klothoffice
                menu:
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        $ lookaroundklothsofficewatcheddontsearchkloth = True
                        hide screen force_mouse_move_klothoffice
                        jump not_search_kloth
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ lookaroundklothsofficewatchedatleastonethensearchedkloth = True
                        hide screen force_mouse_move_klothoffice
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        hide screen force_mouse_move_klothoffice
                        jump computer_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth
            else:
                show screen force_mouse_move_klothoffice
                menu:

                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        $ lookaroundklothsofficewatcheddontsearchkloth = True
                        hide screen force_mouse_move_klothoffice
                        jump not_search_kloth
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ lookaroundklothsofficewatchedatleastonethensearchedkloth = True
                        hide screen force_mouse_move_klothoffice
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich werde mir das Dokument anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump document_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        hide screen force_mouse_move_klothoffice
                        jump computer_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth
    else:
        if read_computer_kloth:
            if read_document_kloth:
                show screen force_mouse_move_klothoffice
                menu:
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        $ lookaroundklothsofficewatcheddontsearchkloth = True
                        hide screen force_mouse_move_klothoffice
                        jump not_search_kloth
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ lookaroundklothsofficewatchedatleastonethensearchedkloth = True
                        hide screen force_mouse_move_klothoffice
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde mir den Brief anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth
            else:
                show screen force_mouse_move_klothoffice
                menu:
                    "Ich habe genug. Ich gehe zurück zur Arbeit. Das alles macht mir Angst. Ich will einfach nur glücklich sein.":
                        $ lookaroundklothsofficewatcheddontsearchkloth = True
                        hide screen force_mouse_move_klothoffice
                        jump not_search_kloth
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ lookaroundklothsofficewatchedatleastonethensearchedkloth = True
                        hide screen force_mouse_move_klothoffice
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich werde mir das Dokument anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump document_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde mir den Brief anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth
        else:
            if read_document_kloth:
                show screen force_mouse_move_klothoffice
                menu:
                    "Das sind firmeninterne Sachen. Die gehen mich nichts an, ich sollte lieber zurück zur Arbeit.":
                        $ lookaroundklothsofficewatcheddontsearchkloth = True
                        hide screen force_mouse_move_klothoffice
                        jump not_search_kloth
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich muss Kloth sofort finden!":
                        $ lookaroundklothsofficewatchedatleastonethensearchedkloth = True
                        hide screen force_mouse_move_klothoffice
                        # Atropos Gedanken
                        symb"Ich muss Kloth sofort finden!"
                        # Atropos Gedanken
                        symb"Ich brauche jetzt Antworten, sonst werde ich verrückt…"
                        jump still_search_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        hide screen force_mouse_move_klothoffice
                        jump computer_kloth
                    "Ich werde mir den Brief anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth
            else:
                menu:
                    "Ich werde das Regal untersuchen."  if sawshelf == False:
                        hide screen force_mouse_move_klothoffice
                        jump shelf_kloth
                    "Ich werde mir das Dokument anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump document_kloth
                    "Ich werde die Bilder untersuchen." if sawpictureskloth == False:
                        hide screen force_mouse_move_klothoffice
                        jump pictureskloth_kloth
                    "Ich werde den Computer durchsuchen.":
                        hide screen force_mouse_move_klothoffice
                        jump computer_kloth
                    "Ich werde mir den Brief anschauen.":
                        hide screen force_mouse_move_klothoffice
                        jump letter_kloth
                    "Ich werde mir die Weltkarte einmal ansehen." if sawworldmap == False:
                        hide screen force_mouse_move_klothoffice
                        jump worldmap_kloth

label letter_kloth:
    $ renpy.fix_rollback()
    $ read_letter_kloth = True
    $ lookaroundklothsofficeletter = True
    $ infos_count_kloth += 1
    $ thingswatched += 1

    # Atropos Gedanken
    symb"Ich werde mir den Brief anschauen."

    # Atropos Gedanken
    symb"Mal sehen, was in diesem steht."

    scene detail_letterkloth
    with fadeshort
    call screen arrow_detail_letterkloth
    label after_detail_letterkloth:
        $ renpy.fix_rollback()

        if read_computer_kloth:

            if kloth_office_after_anan_office:
                # Atropos Gedanken
                symb"Was habe ich da gerade gelesen?"

                # Atropos Gedanken
                symb"Das alles wird ja immer schlimmer… was soll ich nur tun?"

                # Atropos Gedanken
                symb"Das macht mir Angst."

                # Atropos Gedanken
                symb"Es bestätigt meine schlimmsten Vermutungen."

            else:
                # Atropos Gedanken
                symb"Was habe ich da gerade gelesen?"

                # Atropos Gedanken
                symb"Das alles wird ja immer schlimmer… was soll ich nur tun?"

                # Atropos Gedanken
                symb"Das macht mir Angst. Wo ist Kloth nur? Ich muss mit ihm über all das sprechen…"

        else:

            if kloth_office_after_anan_office:
                # Atropos Gedanken
                symb"Was habe ich da gerade gelesen?"

                # Atropos Gedanken
                symb"Was hat das zu bedeuten? Ich mache mir Sorgen um Kloth…"

                # Atropos Gedanken
                symb"Und die Zweifel, die er gegenüber Aither hat… es bestätigt langsam immer mehr meine schlimmsten Vermutungen."

                # Symbiont
                symb"{i}Du interpretierst zu viel in seine Worte. Glaubst du das alles hier wirklich? {/i}"
                # Symbiont
                symb"{i}Du bist glücklich, willst du dieses Glück durch vorschnelles Urteil riskieren? {/i}"

            else:

                # Atropos Gedanken
                symb"Was habe ich da gerade gelesen?"

                # Atropos Gedanken
                symb"Ich mache mir immer größere Sorgen um Kloth… Irgendetwas scheint nicht zu stimmen…"

                # Symbiont
                symb"{i}Du interpretierst zu viel in seine Worte. Er ist wahnsinnig. Glaubst du das alles hier wirklich? {/i}"

                # Symbiont
                symb"{i}Das alles sind nur seltsame Fantasien. Dinge, die sich Kloth zusammengebastelt hat wie es ihm gefällt. {/i}"

                # Symbiont
                symb"{i}Er scheint das Böse zu suchen und es in Aither gefunden zu haben. {/i}"

                # Symbiont
                symb"{i}Er braucht Hilfe. Er ist nicht mehr bei Sinnen. Höre nicht auf ihn, Atropos. {/i}"

                # Symbiont
                symb"{i}Du bist glücklich. Willst du dieses Glück riskieren? {/i}"

        scene kloth_office
        with fadeshort


    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label computer_kloth:
    $ renpy.fix_rollback()
    $ read_computer_kloth = True
    $ infos_count_kloth += 1
    $ thingswatched += 1

    # Atropos Gedanken
    symb"Ich werde den Computer durchsuchen."

    # Atropos Gedanken
    symb"Ob er wohl passwortgeschützt ist?"

    scene detail_klothpassword
    with fadeshort

    # Atropos Gedanken
    symb"Es gibt einen passwortgeschützten Teil und einen, für den ich kein Passwort brauche."

    # Atropos Gedanken
    symb"Hatte Kloth mir gegenüber mal erwähnt, was das Passwort ist?"

    # Symbiont
    symb"{i}Du willst dich in den PC deines Freundes einhacken? Denkst du wirklich, dass du das tun solltest? {/i}"

    # Symbiont
    symb"{i}Letzten Endes wird es ihn und dich unglücklich machen. Denk nach Atropos und triff die richtige Entscheidung. {/i}"

    # Symbiont
    symb"{i}Du möchtest doch glücklich sein. {/i}"

    # Atropos Gedanken
    symb"Ich probiere einfach mal irgendetwas aus, es kann nicht schaden, selbst wenn es falsch ist."

    scene detail_enterpassword
    with fadeshort

    python:
        password = renpy.input ("Passwort:")

    if password == "Sadness" or password == "sadness":
        $ password_right = True

        scene detail_confession
        with fadeshort
        call screen arrow_detail_confession
        label after_detail_confession:
            $ renpy.fix_rollback()
            $ lookaroundklothsofficepcpasswordcorrect = True
            # Atropos Gedanken
            symb"Was ist das? Das kann doch alles nicht wahr sein… Wie? Warum?"

            # Symbiont
            symb"{i}Du musst die Bombe stoppen, Atropos. Rette alle Menschen. Du kannst nicht zulassen, dass das Glück aller Menschen durch so etwas verpufft. {/i}"

            # Symbiont
            symb"{i}Lass nicht zu, dass so viele darunter leiden müssen, was ein einziger Irrer vollbracht hat! {/i}"

            # Symbiont
            symb"{i}Bringe den Menschen Glücklichkeit! {/i}"

            # Symbiont
            symb"{i}Bringe dir selbst Glücklichkeit! {/i}"

            # Atropos Gedanken
            symb"Was ist mit dem nicht geschützten Teil? Was steht dort noch?"


    else:
        $ lookaroundklothsofficepcpasswordwrong = True
        # Atropos Gedanken
        symb"Falsches Passwort... Ich muss wo anderes weitersuchen..."

    # Atropos Gedanken
    symb"Was ist das hier? Es scheint eine Art Online Blog zu sein…"

    scene detail_blog
    with fadeshort
    call screen arrow_detail_blog
    label after_detail_blog:
        $ renpy.fix_rollback()

        # Atropos Gedanken
        symb"Eine Bombe?"

        python:
            password = password.strip()

        if password_right:
            # Atropos Gedanken
            symb"Also waren die Informationen von zuvor tatsächlich wahr?"

        else:
            # Symbiont
            symb"{i}Willst du die Bombe finden und entschärfen? {/i}"

            # Symbiont
            symb"{i}Würde es dich unglücklich machen alle Menschen im Stich zu lassen? {/i}"

            # Atropos Gedanken
            symb"Ist das alles wirklich wahr?"

            # Atropos Gedanken
            symb"Ich kann es kaum glauben…"


        if kloth_office_after_anan_office:
            # Atropos Gedanken
            symb"Aber warum wurde sie gelegt?"

            # Atropos Gedanken
            symb"Was soll ich jetzt nur tun?"

            # Atropos Gedanken
            symb"Steht das im Zusammenhang mit dem, was ich in Anans Büro herausgefunden habe?"

            # Atropos Gedanken
            symb"Aber die Bombe…Das kann doch gar nicht wahr sein, oder? Aber was, wenn doch?"

            # Atropos Gedanken
            symb"Was ist, wenn es tatsächlich eine Bombe in Aither gibt?"

            # Atropos Gedanken
            symb"Und warum hatte Kloth diese Information? Was wollte er mit dieser Information anstellen?"

            if infos_count_kloth == 1 or infos_count_kloth == 2:
                # Atropos Gedanken
                symb"Soll ich noch mehr Sachen untersuchen, um mehr darüber herauszufinden? Kann mir Kloth Antworten darauf geben?"

        else:
            # Atropos Gedanken
            symb"Was soll ich jetzt nur tun?"

            # Atropos Gedanken
            symb"Das alles ist zu viel für mich… wie soll ich mit diesen Informationen umgehen? Was soll ich tun?"

            # Atropos Gedanken
            symb"Das kann doch gar nicht wahr sein, oder? Aber was, wenn doch?"

            # Atropos Gedanken
            symb"Was ist, wenn es tatsächlich eine Bombe in Aither gibt? Was ist mit all den Menschen?"

            # Atropos Gedanken
            symb"Werden sie alle sterben?"

            # Atropos Gedanken
            symb"Aber was kann ich schon dagegen ausrichten?"

            # Atropos Gedanken
            symb"Ich bin doch nur ein bedeutungsloser kleiner Mensch."

            # Atropos Gedanken
            symb"Und was, wenn es doch alles nur Lügen sind? Kloth wirkte in meinen Erinnerungen wirklich wahnsinnig…"

            # Atropos Gedanken
            symb"Soll ich ihn zur Rede stellen?"

            if infos_count_kloth == 1 or infos_count_kloth == 2:
                # Atropos Gedanken
                symb"Oder soll ich noch mehr Sachen untersuchen, um mehr darüber herauszufinden? Aber will ich wirklich mehr wissen?"


            # Atropos Gedanken
            symb"Das alles macht mir Angst…"

            # Symbiont
            symb"{i}Du bist unglücklich. Es liegt an dir, wieder glücklich zu werden. {/i}"

            # Symbiont
            symb"{i}Es ist deine Entscheidung, wie du dieses Glück erreichen willst. {/i}"

            # Symbiont
            symb"{i}Allein deine Entscheidung und deine Wahl. {/i}"

            # Symbiont
            symb"{i}Dein Ziel ist klar: Werde wieder glücklich. Auf welchem Weg auch immer du dieses Glück erreichst. {/i}"



        scene kloth_office
        with fadeshort
        if kloth_office_choice:
            jump selection_kloth_office
        if kloth_office_back_to_work_choice:
            jump selection_kloth_office_back_to_work
        if kloth_office_after_anan_office:
            jump selection_kloth_office_after_anan_office

label document_kloth:
    $ renpy.fix_rollback()
    $ thingswatched += 1
    $ lookaroundklothsofficedocument = True
    $ read_document_kloth = True
    $ infos_count_kloth += 1

    # Atropos Gedanken
    symb"Ich werde mir das Dokument anschauen."

    # Atropos Gedanken
    symb"Was es mir wohl verrät?"

    scene detail_servertext
    with fadeshort
    call screen arrow_detail_servertext()

label after_detail_servertext:
    $ renpy.fix_rollback()
    scene detail_servergraph
    with fadeshort
    call screen arrow_detail_servergraph()

label after_detail_servergraph:
    $ renpy.fix_rollback()
    if read_computer_kloth:

        # Atropos Gedanken
        symb"Die Server? Das spielt gerade keine Rolle… das sind doch nur unwichtige Informationen…"

        # Atropos Gedanken
        symb"Ist hier denn nichts mehr zu der Bombe?"

        # Atropos Gedanken
        symb"Und warum hatte Kloth diesen Blog offen?"

        # Atropos Gedanken
        symb"Sagt der Schreiber wirklich die Wahrheit?"

        # Atropos Gedanken
        symb"Was soll ich tun?"

        # Atropos Gedanken
        symb"Was soll ich tun?"

        # Atropos Gedanken
        symb"Was soll ich nur tun?"


    else:

        # Atropos Gedanken
        symb"Wenn ich das richtig verstehe… Wenn einer der Server zusammenbricht, würde alles untergehen, oder?"

        # Symbiont
        symb"{i}Warum machst du dir überhaupt darüber Gedanken? {/i}"

        # Symbiont
        symb"{i}Das ist nichts, was du wissen musst, um glücklich zu sein und ein glückliches Leben zu führen. {/i}"

        # Symbiont
        symb"{i}Schaue dir nichts mehr an. Schon für das, was du bereits gesehen hast, könntest du einen Haufen Ärger bekommen. {/i}"

        # Symbiont
        symb"{i}Du willst doch glücklich sein. {/i}"
    scene kloth_office
    with fadeshort

    if infos_count_kloth<3:
        # Atropos Gedanken
        symb"Was soll ich jetzt tun?"

    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label shelf_kloth:
    $ renpy.fix_rollback()
    $ thingswatched += 1
    $ sawshelf = True
    # Atropos Gedanken
    symb"Hier ist das totale Chaos ausgebrochen! Was in aller Welt ist hier nur passiert? Ist hier jemand eingebrochen? Oder war Kloth das?"
    # Atropos Gedanken
    symb"Normalerweise ist er niemand, der einfach ausrastet. Aber in letzter Zeit kann ich ihn einfach nicht mehr richtig einschätzen."
    # Atropos Gedanken
    symb"Ich hoffe, es war nur ein Einbrecher. Ich habe gehört es gibt welche unter denen, die keine Happiness nehmen, weil sie neidisch über den Besitz anderer sind."
    # Atropos Gedanken
    symb"Hoffentlich war es ein Einbrecher. Bitte lass es nicht Kloth gewesen sein."
    scene kloth_office
    with fadeshort
    if kloth_office_choice:
        jump selection_kloth_office
    if kloth_office_back_to_work_choice:
        jump selection_kloth_office_back_to_work
    if kloth_office_after_anan_office:
        jump selection_kloth_office_after_anan_office

label pictureskloth_kloth:
    $ renpy.fix_rollback()
    $ thingswatched += 1
    $ sawpictureskloth = True
    scene detail_photoskloth
    with fadeshort
    # Atropos Gedanken
    symb"Bilder von uns. Wenn ich sie so miteinander vergleiche, komme ich mir schon ganz alt vor."
    # Atropos Gedanken
    symb"Ich vermisse die alten Zeiten. Damals hatten wir vielleicht keine Happiness, aber immerhin mehr Zeit füreinander."
    # Atropos Gedanken
    symb"Kloth war in letzter Zeit so beschäftigt, dass er kaum Zeit für Chesis und mich hatte."
    call screen arrow_detail_photoskloth
    label after_detail_photoskloth:
        $ renpy.fix_rollback()
        scene kloth_office
        with fadeshort
        if kloth_office_choice:
            jump selection_kloth_office
        if kloth_office_back_to_work_choice:
            jump selection_kloth_office_back_to_work
        if kloth_office_after_anan_office:
            jump selection_kloth_office_after_anan_office

label worldmap_kloth:
    $ renpy.fix_rollback()
    $ thingswatched += 1
    $ sawworldmap = True
    scene detail_map
    with fadeshort
    # Atropos Gedanken
    symb"Die Großen Drei – gerecht auf der Welt verteilt."
    symb"In den letzten Jahrhunderten hat sich einiges verändert- ich hatte neulich mal eine alte Weltkarte in der Hand."
    symb"Es ist kaum vorstellbar, dass damals überall Menschen lebten. Nicht, wenn man vergleicht, was jetzt noch bewohnbar ist."
    symb"Übrig sind nur noch Keposa, Astoa und Peria. Alles andere ist so zerstört, dass dort wohl lange Zeit niemand mehr leben kann."
    call screen arrow_detail_worldmap
    label after_detail_worldmap:
        $ renpy.fix_rollback()
        scene kloth_office
        with fadeshort
        if kloth_office_choice:
            jump selection_kloth_office
        if kloth_office_back_to_work_choice:
            jump selection_kloth_office_back_to_work
        if kloth_office_after_anan_office:
            jump selection_kloth_office_after_anan_office

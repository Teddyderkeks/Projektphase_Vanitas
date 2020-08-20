default sawbooks = False
default sawpictures = False
default sawsafe= False

label selection_anan_office:

    if read_letter_anan:
        if read_computer_anan:
            if read_document_anan:
                jump how_many_infos_anan
            else:
                menu:
                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan

        else:
            if read_document_anan:
                menu:
                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan

            else:
                menu:
                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan

    else:
        if read_computer_anan:
            if read_document_anan:
                menu:
                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan

            else:
                menu:
                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan

        else:
            if read_document_anan:
                menu:
                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan

            else:
                menu:

                    "Der Safe sieht interessant aus." if sawsafe == False:
                        jump safe_anan
                    "Ich sollte mich besser nicht in Anans Büro umschauen." if straight_anan_office == False:
                        jump how_many_infos_anan
                    "Ich sollte mich besser nicht in Anans Büro umschauen und das Zimmer verlassen." if straight_anan_office == True:
                        jump how_many_infos_anan
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mir die Fotos ansehen." if sawpictures == False:
                        jump pictures_anan
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich werfe einen Blick auf die Bücher." if sawbooks == False:
                        jump books_anan


label letter_anan:
    $ read_letter_anan =True
    $ infos_count_anan += 1

    # Atropos Gedanken
    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen."

    # Atropos Gedanken
    "Von wem dieser wohl stammt?"

    # Atropos Gedanken
    "Atlas? Was….? Das kann doch nicht sein… Ist das etwa {b}der{/b} Atlas?"

    # Atropos Gedanken
    "Der Brief sieht aus als wäre er schon etwas älter. Kennen sie sich wirklich schon so lange?"

    # Atropos Gedanken
    "Anan meinte zuvor bei seiner Ansprache, dass Adrés und Atlas ihn im Krieg retteten, aber irgendwie konnte ich es nicht ganz glauben. Sie müssen schon ewig Freunde sein, so wie Chesis, Kloth und ich."

    scene detail_letter1
    call screen arrow_detail_letter1()

    label after_detail_letter1:
        scene detail_letter2
        call screen arrow_detail_letter2()

    label after_detail_letter2:

        # Atropos Gedanken
        "Was hat das alles zu bedeuten?"

        # Atropos Gedanken
        "Ist Happiness wirklich so wichtig?"

        # Atropos Gedanken
        "Aber… was jetzt?"

        # Atropos Gedanken
        "Was soll ich mit diesem Wissen anfangen?"

        if infos_count_anan <3:
            scene anan_office

            # Atropos Gedanken
            "Soll ich nach mehr Hinweisen suchen? Aber Anan… er könnte jeden Moment zurückkommen."

            jump selection_anan_office
        else:
            scene anan_office
            jump selection_anan_office

label document_anan:
    $ read_document_anan =True
    $ infos_count_anan += 1

    # Atropos Gedanken
    "Ich könnte mir die herumliegenden Dokumente ansehen."

    # Atropos Gedanken
    "Ob ich sie überhaupt verstehe? Die wirken ziemlich kompliziert."

    scene detail_document
    call screen arrow_detail_document
    label after_detail_document:

        # Atropos Gedanken
        "Was ist das alles? Ich verstehe die Zusammenhänge nicht, aber es scheint um die Wirkungsweisen des Gehirns in Bezug auf bestimmte Substanzen zu gehen?"

        # Atropos Gedanken
        "Ob es wohl das ist, was die Pille mit unseren Köpfen anrichtet und uns so unsere Glücklichkeit bringt?"

        # Atropos Gedanken
        "Ich wünschte ich könnte besser verstehen, was hier alles steht, aber das sind alles Substanzen, mit denen ich selbst nicht arbeite und von denen ich noch nie gehört habe…"

        scene anan_office

        if infos_count_anan <3:

            # Atropos Gedanken
            "Ob ich wohl noch mehr Hinweise finde, die das hier irgendwie erklären?"

            if straight_anan_office:
                # Symbiont
                "{i}Bleibe weg und verlass augenblicklich das Büro! Diese Sachen gehen dich nichts an. Das wird dich in ein großes Unglück stürzen. {i}"

                # Symbiont
                "{i}Es wird nicht mehr lange dauern bis Anan kommt. {i}"
            else:
                # Symbiont
                "{i}Bleib weg und setz dich wieder auf deinen Stuhl! Diese Sachen gehen dich nichts an. Das wird dich in ein großes Unglück stürzen. {i}"

                # Symbiont
                "{i}Es wird nicht mehr lange dauern, bis Anan zurückkommt. {i}"

            jump selection_anan_office
        else:
            jump selection_anan_office


label computer_anan:
    $ read_computer_anan =True
    $ infos_count_anan += 1

    # Atropos Gedanken
    "Ich könnte mich auf Anans PC umsehen."

    # Atropos Gedanken
    "Oh verdammt… da ist ja alles passwortgeschützt… habe ich überhaupt auf irgendetwas Zugriff?"

    # Atropos Gedanken
    "Dieses Dokument, das offen ist… Anan scheint vergessen zu haben es zu schließen als er vorher sein Büro verließ."

    # Atropos Gedanken
    "Was wohl der Inhalt dessen ist?"

    scene detail_ananpc
    call screen arrow_detail_ananpc

    label after_detail_ananpc:

        # Atropos Gedanken
        "Was ist das für eine Tabelle? Und warum stehe ich als neuester Eintrag drinnen? Ich muss beobachtet werden?"

        # Atropos Gedanken
        "Was hat das zu bedeuten? Sind das alles Menschen, die keine Pille genommen haben?"

        # Atropos Gedanken
        "Die Liste ist nicht sonderlich lang… aber warum muss extra eine Liste über uns geführt werden?"

        # Atropos Gedanken
        "Ist es wirklich so gefährlich für die Menschheit, wenn ein paar wenige Menschen sie nicht nehmen?"

        scene anan_office

        if infos_count_anan <3:

            # Atropos Gedanken
            "Bringen mir andere Sachen mehr Antworten? Soll ich mir noch etwas anschauen oder sollte ich es lieber bleiben lassen?"
            # Symbiont
            "{i}Ja, lass die Finger von den Sachen, du hast genug gesehen. Deine Neugierde sollte schon längst befriedigt sein. Bist du jetzt glücklich? {i}"

            # Atropos Gedanken
            "Anan könnte jeden Moment zurückkommen und mich erwischen."
            jump selection_anan_office

        else:

            jump selection_anan_office

label pictures_anan:
    $ sawpictures =True
    scene detail_oldphotos
    # Atropos Gedanken
    "Das sind alte Fotos von Anan. Ein wenig seltsam, ihn so zu sehen. Im Vergleich dazu ist er heute manchmal der reine Ernst in Person."
    # Atropos Gedanken
    "Ob er damals gewusst hat, wie viel Verantwortung auf ihn zukommen würde?"
    # Atropos Gedanken
    "Der Kampf im Krieg muss ihn ziemlich verändert haben. Oder hat ihn der Frieden verändert?"
    # Atropos Gedanken
    "Da sind auch Atlas und Adrés. Aither muss damals noch relativ neu gewesen sein… Vielleicht ein, zwei Jahre alt?"
    call screen arrow_detail_oldphotos
    label after_detail_oldphotos:
        scene anan_office
        # Atropos Gedanken
        "Was soll ich jetzt machen?"
        jump selection_anan_office


label books_anan:
    $ sawbooks =True
    # Atropos Gedanken
    "Wow, was für Wälzer! Bücher sind schon Raritäten, aber solche wie diese hier werde ich wohl nirgendwo sonst wiederfinden."
    # Atropos Gedanken
    "…"
    # Atropos Gedanken
    "Ob es auffällt, wenn ich mal einen Blick in eines davon reinwerfe?"
    # Atropos Gedanken
    "Ach, bestimmt nicht. Ich bin vorsichtig."
    # Atropos Gedanken
    "Mal sehen…"
    # Atropos Gedanken
    "Oh? Da ist was rausgefallen. War ich das?"

    scene detail_bookphoto
    # Atropos Gedanken
    "Das ist ein Foto… Anan sieht darauf ziemlich jung aus. Von 2219? Wahnsinn. Wer sie wohl war?"
    # Atropos Gedanken
    "Ich sollte das Buch sorgfältig zurücklegen, damit es nicht auffällt."
    call screen arrow_detail_bookphoto
    label after_detail_bookphoto:
        scene anan_office
        # Atropos Gedanken
        "Was soll ich jetzt machen?"
        jump selection_anan_office

label safe_anan:
    $ sawsafe =True
    scene detail_safe
    if sawbooks:
        # Atropos Gedanken
        "Ein Safe? Da könnte etwas Interessantes drin sein…"
        # Atropos Gedanken
        "Was könnte Anan wohl darin verbergen? Es muss etwas Wichtiges sein, wenn er es so absichert."
        # Atropos Gedanken
        "Ich könnte versuchen, den Code zu erraten…"
        # Atropos Gedanken
        "Mal sehen. Sein Geburtsdatum vielleicht?"
        # Atropos Gedanken
        "…"
        # Atropos Gedanken
        "Nein… Der Gründungstag Aithers?"
        # Atropos Gedanken
        "…"
        # Atropos Gedanken
        "Auch nicht richtig. Hm… Vielleicht ja…"
        # Atropos Gedanken
        "2 – 2 – 1 – 9"
        scene detail_safe_open
        # Atropos Gedanken
        "Volltreffer! Aber das sind doch… Datenträger? Anan hat sie sogar beschriftet. Nachrichten von Atlas und Adrés …"
        # Atropos Gedanken
        "Und was sind die hier? ‘Kronos 2226’ … ‘Untersuchungen K 2226’ …"
        # Atropos Gedanken
        "’2229: Happiness’"
        # Atropos Gedanken
        "2226… Das war kurz vor Ende des Krieges. Also müssen das hier Daten zu ihren ersten Forschungen für Happiness sein."
        # Atropos Gedanken
        "Es wäre interessant, sich das mal anzusehen, aber ich kann damit nicht einfach durch das Gebäude laufen."
        # Atropos Gedanken
        "Ich lege es erstmal wieder zurück."
        call screen arrow_detail_safe_open
        label after_detail_safe_open:
            scene anan_office
            # Atropos Gedanken
            "Was soll ich jetzt machen?"
            jump selection_anan_office

    else:
        # Atropos Gedanken
        "Ein Safe? Da könnte etwas Interessantes drin sein…"
        # Atropos Gedanken
        "Was könnte Anan wohl darin verbergen? Es muss etwas Wichtiges sein, wenn er es so absichert."
        # Atropos Gedanken
        "Leider kenne ich den Code nicht."
        scene anan_office
        # Atropos Gedanken
        "Was soll ich jetzt machen?"
        jump selection_anan_office

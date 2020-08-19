label selection_anan_office:

    if read_letter_anan:
        if read_computer_anan:
            if read_document_anan:
                jump how_many_infos_anan
            else:
                menu:
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
        else:
            if read_document_anan:
                menu:
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
            else:
                menu:
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
    else:
        if read_computer_anan:
            if read_document_anan:
                menu:
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
            else:
                menu:
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
        else:
            if read_document_anan:
                menu:
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen.":
                        jump how_many_infos_anan
            else:

                "Was im Büro ansehen?"
                menu:
                    "Ich könnte mir den geöffneten Brief auf Anans Schreibtisch anschauen.":
                        jump letter_anan
                    "Ich könnte mich auf Anans PC umsehen.":
                        jump computer_anan
                    "Ich könnte mir die herumliegenden Dokumente ansehen.":
                        jump document_anan
                    "Ich sollte mich besser nicht in Anans Büro umschauen.":
                        jump how_many_infos_anan

label letter_anan:
    $ read_letter_anan =True
    $ infos_count_anan += 1

    "Informationen über die frühen Tage von Aither und den Aufbau der Strukturen, Wichtigkeit dass jeder Happiness nimmt weil sonst Chaos ausbricht!"

    jump selection_anan_office

label document_anan:
    $ read_document_anan =True
    $ infos_count_anan += 1

    "Nicht einfach zu verstehende Diagramme und co über das menschliche Gehirn/Psychologie/Wirkungsweisen"

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

    # Datei wird gezeigt

    "Liste von bekannten Nicht-Pillennehmern. Atropos als neuste Notation. Anmerkung: Beobachten."

    # Atropos Gedanken
    "Was ist das für eine Tabelle? Und warum stehe ich als neuester Eintrag drinnen? Ich muss beobachtet werden?"

    # Atropos Gedanken
    "Was hat das zu bedeuten? Sind das alles Menschen, die keine Pille genommen haben?"

    # Atropos Gedanken
    "Die Liste ist nicht sonderlich lang… aber warum muss extra eine Liste über uns geführt werden?"

    # Atropos Gedanken
    "Ist es wirklich so gefährlich für die Menschheit, wenn ein paar wenige Menschen sie nicht nehmen?"

    # wenn noch nicht alles angesehen

    # Atropos Gedanken
    "Bringen mir andere Sachen mehr Antworten? Soll ich mir noch etwas anschauen oder sollte ich es lieber bleiben lassen?"
    # Symbiont
    "{i}Ja, lass die Finger von den Sachen, du hast genug gesehen. Deine Neugierde sollte schon längst befriedigt sein. Bist du jetzt glücklich? {i}"

    # Atropos Gedanken
    "Anan könnte jeden Moment zurückkommen und mich erwischen."


    jump selection_anan_office

label pictures_anan:

label books_anan:

label safe_anan:

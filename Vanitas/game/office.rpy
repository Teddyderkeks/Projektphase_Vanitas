default infos_count_anan = 0
default infos_count_kloth = 0
default read_letter_anan = False
default read_document_anan = False
default read_computer_anan = False
default face_anan_in_office = False

label office:
    scene hall

    "Macht sich auf den Weg, Anan noch nicht da"

    scene anan_office

    "In Büro umsehen?"

    menu:
        "Ja":
            jump selection_anan_office
        "Nein":
            jump conversation_with_anan

label conversation_with_anan:
    "Anan kommt an, Schelte für Atropos weil er die Pille nicht genommen hat, Aufforderung dies jetzt zu tun"

    "Reaktion auf die Schelte"

    menu:
        "Einsicht":
            jump understanding
        "Sinn der Pille hinterfragen":
            jump questioning
        #"Wütend":
            #jump rueffel

label understanding:
    scene hall

    "Atropos geht zurück an seinen Arbeitsplatz und nimmt die Pille"

    jump pill

label questioning:
    "Anan erklärt Wichtigkeit der Pille mit üblichen Argumenten"

    "Reaktion darauf?"

    menu:
        "Einsicht":
            jump understanding
        "Unverständnis":
            jump misunderstanding

label misunderstanding:

    "Anan wird wütend, wird jedoch angerufen und muss kurz weg, befiehlt Atropos hier zu warten"

    jump selection_anan_office

label how_many_infos_anan:
    "Wie viele Sachen angesehen?"

    if infos_count_anan == 0:
        "Anan kommt zurück, Atropos zeigt Einsicht, Anan fragt nach ob Atropos Kloth gesehen hat und schickt ihn zurück um die Pille zu nehmen"

        jump understanding

    if infos_count_anan == 1:
        jump one_or_two_infos

    if infos_count_anan == 2:
        jump one_or_two_infos

    if infos_count_anan == 3:
        "Anan erwischt Atropos und es kommt zum riesen Streit, Atropos konfrontiert Anan mit den Hinweisen, Anan wirft ihn raus und kündigt den Rauswurf aus der Firma an"

        jump visit_kloth

label one_or_two_infos:
    "Anan kommt zurück und bemerkt nichts; fragt nach ob Atropos Kloth schon gesehen hat und will ihn zurückschicken um die Pille zu nehmen"

    "Anan mit den Tatsachen konfrontieren?"

    menu:
        "Ja":
            jump face_anan
        "Nein":
            jump not_face_anan

label face_anan:
    "Riesen Streit, da Atropos in privaten Dokumenten geschnüffelt hat; Anan wirft Atropos raus und kündigt den Rauswurf aus der Firma an"

    jump  visit_kloth

label not_face_anan:
    scene hall

    "Atropos verlässt das Büro; Monolog über Sinn der Firma und Moralischen Aspekt"

    "Firma OK oder böse?"

    menu:
        "OK":
            jump ###prototyp
        "Böse":
            $ face_anan_in_office = True
            jump visit_kloth

label visit_kloth:
    scene hall
    if face_anan_in_office:
        "Beschließt, Kloth aufzusuchen und ihn dazu zu befragen, da dieser ja Sekretär von Anan ist"

    else:
        "Atropos beschließt Kloth aufzusuchen und ihn nach diesen Sachen zu befragen, da er ja Sekretär von Anan ist"

    "Kloth antwortet nicht auf Anrufe/Nachrichten; Beschluss sein Büro aufzusuchen;"

    scene kloth_office

    "Kloth nicht da, Atropos durchsucht das Büro"

    "Was untersuchen? Oder Kloth suchen?"

    jump selection_kloth_office_after_anan_office

label search_kloth_in_stairwell:
    scene hall

    "Sucht Kloth,"

    scene stairwell

    "findet die Leiche im Treppenhaus"

    scene hall

    "Erinnerung an das Gespräch mit Kloth"

    jump ###prototyp
    
label how_many_infos_kloth:

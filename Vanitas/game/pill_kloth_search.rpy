default read_letter_kloth = False
default read_computer_kloth = False
default read_document_kloth = False
image glitch:
        "glitch1"
        pause .2
        #"glitch2"
        #pause .09
        "glitch3"
        pause .2
        "glitch4"
        pause .2
        "glitch5"
        pause .2
        "glitch6"
        pause .2
        #"glitch7"
        #pause .09
        repeat


label search_kloth:
    scene hall
    with fadeshort

    # Symbiont
    symb"{i}Du solltest ihn nicht anrufen. Was ist, wenn er gerade in einer Besprechung ist und du ihn störst? {/i}"

    # Symbiont
    symb"{i}Schreibe ihm doch lieber, warte ab bis er antwortet und verbringe unterdessen Zeit mit deinen Freunden. Das macht dich glücklich. {/i}"

    # Atropos Gedanken
    symb"Ich sollte es wirklich erstmal mit einer Nachricht versuchen."

    "Atropos" "…"

    # Atropos Gedanken
    symb"Seltsam. Es wird nicht angezeigt, dass er meine Nachricht überhaupt empfängt. Hat er sein Handy ausgeschaltet? Ich sollte ihn besser doch anrufen."

    "Atropos" "…"

    "Atropos" "…"

    "Atropos" "…"

    "Atropos" "Verdammt, Kloth. Geh dran, bitte…"

    "Atropos" "…"

    # Symbiont
    symb"{i}Er ist gerade bestimmt in einer Besprechung und hat deswegen sein Handy abgeschaltet. {/i}"

    # Atropos Gedanken
    symb"Ich sollte dennoch in seinem Büro nachschauen gehen."

    "Atropos" "…"

    "Atropos" "Kloth? Bist du da? Darf ich reinkommen?"

    # Atropos Gedanken
    symb"Kein Laut zu hören… vielleicht hat er mich ja nicht gehört? Kloth wird schon nicht sauer sein, wenn ich einfach eintrete."
    play music "Sound/Music/Rooms/kloth_buero.mp3" fadeout 3 fadein 3
    scene kloth_office
    with fadeshort

    "Atropos" "Kloth?"

    # Atropos Gedanken
    symb"Niemand hier."

    # Atropos Gedanken
    symb"Das wäre auch zu schön gewesen."

    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Aber wo kann er sonst sein?"

    # Atropos Gedanken
    symb"Vielleicht in Anans Büro? Aber dort kann ich doch nicht einfach so hineinplatzen…"


    menu:
        "Einen Versuch ist es wert, selbst wenn ich dafür Ärger von Anan bekommen sollte.":

            # Atropos Gedanken
            symb"Einen Versuch ist es wert, selbst wenn ich dafür Ärger von Anan bekommen sollte."

            # Atropos Gedanken
            symb"Zum Glück ist es gleich nebenan."

            jump search_kloth_in_anan_office
        "Nein, ich sollte wo anders nach ihm suchen.":

            # Atropos Gedanken
            symb"Nein, ich sollte wo anders nach ihm suchen."

            # Atropos Gedanken
            symb"Aber was soll ich jetzt nur tun?"

            # Atropos Gedanken
            symb"Es fühlt sich falsch an, einfach ins Labor zurückzukehren."

            jump search_kloth_without_anan_office

label search_kloth_in_anan_office:

    # Atropos Gedanken
    symb"Ich klopfe besser an."

    "Atropos" "…"

    "Atropos" "Hallo? Jemand da?"

    # Atropos Gedanken
    symb"Es scheint auch hier niemand da zu sein…"

    # Atropos Gedanken
    symb"Sollte ich nachschauen? Aber bei Anan ist es noch einmal etwas anderes, einfach einzutreten als bei Kloth…"

    menu:
        "Ich will es riskieren.":
            symb "Ich will es riskieren."
            jump wannariskanan
        "Nein, reingehen gehört sich wirklich nicht.":
            symb "Nein, reingehen gehört sich wirklich nicht."
            # Atropos Gedanken
            symb"Aber was soll ich jetzt nur tun?"
            # Atropos Gedanken
            symb"Es fühlt sich falsch an, einfach ins Labor zurückzukehren."
            jump search_kloth_without_anan_office

label wannariskanan:
    play music "Sound/Music/Rooms/AnansBuero/anan_buero_2St_ganz.mp3" fadeout 3 fadein 3
    scene anan_office
    with fadeshort

    # Atropos Gedanken
    symb"Es ist tatsächlich verlassen."

    # Atropos Gedanken
    symb"Ich bin noch nie hier gewesen. Es ist wirklich beeindruckend."

    # Atropos Gedanken
    symb"Soll ich mich ein wenig umschauen? Vielleicht finde ich ja irgendwelche Hinweise auf Kloth."

    # Symbiont
    symb"{i}Lass es bleiben. {/i}"

    # Symbiont
    symb"{i}Anan könnte jeden Moment zurückkommen und du willst nicht, dass er dich dabei erwischt, wie du in seinen Sachen herumstöberst. {/i}"

    # Symbiont
    symb"{i}Willst du das etwa? Das würde dein Glück nur gefährden. {/i}"
    show screen force_mouse_move_twooptionsdown
    menu:
        "Ich möchte das Risiko eingehen und mich trotzdem umsehen.":
            hide screen force_mouse_move_twooptionsdown
            jump symbiont_in_between
        "Ich suche besser wo anders nach ihm.":
            hide screen force_mouse_move_twooptionsdown
            jump search_kloth_without_anan_offices

label symbiont_in_between:
    # Atropos Gedanken
    symb"Ich möchte das Risiko eingehen und mich trotzdem umsehen."

    # Symbiont
    symb"{i}Verlasse diesen Raum! Du gefährdest deine Glücklichkeit mit jeder Sekunde mehr. Siehst du es nicht? {/i}"

    # Symbiont
    symb"{i}Das wird kein gutes Ende nehmen. Suche an einem anderen Ort nach Kloth oder lass es ganz bleiben. {/i}"

    # Symbiont
    symb"{i}Es geht ihm gut. Er ist glücklich, so wie jeder andere Mensch auch. {/i}"

    # Symbiont
    symb"{i}Ist es dir das Risiko wirklich wert, auch wenn du wahrscheinlich nichts finden wirst, was dich zu Kloth führt? {/i}"

    # Symbiont
    symb"{i}Verlasse diesen Raum, Atropos! Denk an deine Glücklichkeit. {/i}"

    # Symbiont
    symb"{i}Riskiere sie nicht! {/i}"

    # Atropos Gedanken
    symb"Ja, meine Glücklichkeit ist wichtiger… Was tue ich hier noch?"


    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Aber was soll ich jetzt nur tun?"

    # Atropos Gedanken
    symb"Es fühlt sich falsch an, einfach ins Labor zurückzukehren."


    jump search_kloth_without_anan_office


label search_kloth_without_anan_office:
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Wo könnte ich Kloth nur suchen?"

    # Atropos Gedanken
    symb"Die Orte, an denen er sich am wahrscheinlichsten aufhält, habe ich bereits nach ihm abgesucht."

    # Atropos Gedanken
    symb"Hatte Kloth neulich etwas in die Richtung erwähnt?"

    # Überschwung zu Erinnerung, Ort: Kloths Büro; Über der gesamten Erinnerung liegt ein Rauschen

    play music "Sound/Music/Rooms/kloth_buero.mp3" fadeout 3 fadein 3
    scene kloth_office
    with fadeshort
    show sepia
    show kloth unsuresmiling_neutral_alt behind sepia:
        xalign 0.5

    "Atropos" "Zu so früher Stunde schon ein Bier? (lacht)"

    show glitch

    "Kloth" "Warum nicht- es schmeckt halt gut und lässt einen vieles vergessen."

    hide glitch

    "Atropos" "Vergessen? Es gibt doch nichts in diesem wundervollen Leben, das man vergessen möchte."

    show kloth angry_alt
    show glitch

    "Kloth" "Wundervoll? Glücklich? Bestimmt… Träum weiter Atropos, bleibe in deiner Traumwelt gefangen."

    hide glitch

    "Atropos" "Von was redest du nur?"

    show kloth vest_open
    show glitch

    "Kloth" "Sieh dich doch mal um. All diese glücklichen, breit grinsenden Menschen, die alles toll finden, was andere sagen und tun. Nennst du das Glück?"
    hide glitch

    "Atropos" "Kloth, was ist denn nur los mit dir? Du machst mir ja fast schon Angst."

    show kloth angry_alt
    show glitch

    "Kloth" "Immerhin würdest du dann nicht mehr seelenlos glücklich sein. Das wäre schon mal ein Fortschritt."
    hide glitch

    "Atropos" "Wie viel hast du getrunken? Du fantasierst ja schon! Dein Alkoholkonsum ist in den letzten Monaten viel zu sehr angestiegen."

    show kloth crazy
    show glitch

    "Kloth" "Nein, ist er nicht! Mir geht es gut. Hörst du Atropos? Mir geht es gut!"

    hide glitch

    "Atropos" "Schon okay, ich habe verstanden. Du bist glücklich und das freut mich."

    show kloth scared1
    show glitch

    "Kloth" "Sie werden kommen, Atropos. Ich warne dich! Sie werden kommen und uns holen!"

    "Kloth" "Sie warten nur darauf, dass wir alle zu seelenlosen Kreaturen werden. Und dann holen sie uns."

    show kloth crazy

    "Kloth" "Aber mich werden sie nicht bekommen. Ich werde ihnen entkommen. Ich werde fliehen, hörst du?"
    hide glitch

    "Atropos" "Ja, das wirst du, Kloth. Alles wird in Ordnung. Ruhe dich einfach ein wenig aus und beruhige dich."

    # Ende der Erinnerung, zurück im Flur
    hide kloth
    hide sepia
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Was war das denn für eine seltsame Erinnerung? Die hatte ich ja vollkommen vergessen…"

    # Atropos Gedanken
    symb"Das Gespräch war ein paar Monate her. Ob es mittlerweile wohl noch schlimmer geworden ist?"

    # Atropos Gedanken
    symb"Kloth wirkte fast schon besessen. Und es würde erklären, warum er sich in letzter Zeit so selten gemeldet hat."

    # Atropos Gedanken
    symb"Er scheint auch ein Alkoholproblem zu haben. Warum ist mir das nur nicht früher aufgefallen? Ich muss unbedingt mit ihm sprechen."

    # Atropos Gedanken
    symb"Vielleicht finde ich aber auch in seinem Büro mehr Hinweise auf das, was ihn im Moment so sehr aus der Bahn wirft."

    # Symbiont
    symb"{i}Deine Mittagspause ist gleich vorbei. Du solltest besser ins Labor zurückkehren. {/i}"

    # Symbiont
    symb"{i}Höre auf dir so viele Gedanken um Kloth zu machen, das gefährdet am Ende nur deine Glücklichkeit. Siehst du es denn nicht? {/i}"

    # Symbiont
    symb"{i}Er ist nicht mehr bei Sinnen gewesen in der letzten Zeit. Sei für ihn da, sobald er dazu bereit ist. {/i}"

    # Symbiont
    symb"{i}Aber jetzt geh. Er ist doch ohnehin nicht da, willst du durch ganz Aither rennen, um ihn zu suchen? {/i}"

    # Symbiont
    symb"{i}Du musst heute noch so viel Arbeit erledigen. Kümmere dich darum! Das macht dich glücklich. {/i}"



    show screen force_mouse_move_670
    menu:
        "Ich suche weiter nach Kloth. Ich muss sofort mit ihm persönlich darüber sprechen.":
            hide screen force_mouse_move_670
            # Atropos Gedanken
            symb"Ich suche weiter nach Kloth. Ich muss sofort mit ihm persönlich darüber sprechen."

            # Atropos Gedanken
            symb"So kann ich ihm am besten helfen."

            # Atropos Gedanken
            symb"Ich muss endlich wissen, was los ist!"

            jump still_search_kloth
        "Ich sehe mich in Kloths Büro nach Hinweisen um, damit ich ihm helfen kann.":
            hide screen force_mouse_move_670
            # Atropos Gedanken
            symb"Ich sehe mich in Kloths Büro nach Hinweisen um, damit ich ihm helfen kann."

            # Atropos Gedanken
            symb"Vielleicht finde ich dort ja irgendetwas, was mir weiterhilft."

            # Atropos Gedanken
            symb"Irgendeinen Anhaltspunkt auf den ich Kloth ansprechen kann."

            # Atropos Gedanken
            symb"Ich will, dass er endlich wieder glücklich sein kann und nicht so leiden muss, wie es in der Erinnerung den Anschein hatte."
            play music "Sound/Music/Rooms/kloth_buero.mp3" fadeout 3 fadein 3
            scene kloth_office
            with fadeshort

            # Atropos Gedanken
            symb"Kloths Büro… ich habe mich schon lange nicht mehr wirklich hier aufgehalten. Wo könnte ich nur Hinweise finden?"

            # Atropos Gedanken
            symb"Hmmm… hier liegen eine ganze Menge an Sachen herum, ich werde…"

            jump selection_kloth_office
        "Ich sollte besser zurück ins Labor. Vielleicht hat Kloth den anderen dort ja auch eine Nachricht für mich hinterlassen?":
            hide screen force_mouse_move_670
            # Atropos Gedanken
            symb"Ich sollte besser zurück ins Labor. Vielleicht hat Kloth den anderen dort ja auch eine Nachricht für mich hinterlassen?"

            # Atropos Gedankens
            symb"Oder er hat mich gesucht und wir sind aneinander vorbeigelaufen und nun wartet er beim Labor auf mich."

            # Atropos Gedanken
            symb"So oder so. Ich muss ohnehin zurück zur Arbeit. Wenn Kloth nicht beim Labor ist, dann werde ich ihm einfach nochmal eine Nachricht schreiben."
            play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3
            scene lab
            with fadeshort
            # Atropos Gedanken
            symb"Er ist nicht hier. Schade. Ich hatte schon Hoffnung gehabt. Aber er wird sich schon melden."

            # Atropos Gedanken
            symb"Und nachher beim Grillen werden wir alle über diese ewige Herumsucherei lachen."

            jump not_search_kloth

label everything_seen:
    # Atropos Gedanken
    symb"Was soll ich jetzt nur tun?"

    # Atropos Gedanken
    symb"Ich habe Angst…"

    # Atropos Gedanken
    symb"Ich will das alles nicht…"

    # Atropos Gedanken
    symb"Was hat das alles zu bedeuten?"

    # Atropos Gedanken
    symb"Was soll ich machen? Kloth suchen? Den Hinweisen nachgehen? Verrückt werden?"

    # Atropos Gedanken
    symb"Mich in einem Schrank verkriechen und nie wieder daraus hervorkommen?"

    # Atropos Gedanken
    symb"Es klingt verlockend…"

    # Atropos Gedanken
    symb"Wie soll ich mit meinem Wissen umgehen?"

    # Atropos Gedanken
    symb"Was kann ich tun?"

    # Atropos Gedanken
    symb"Ich bin vor Angst wie erstarrt."

    # Atropos Gedanken
    symb"Geht die Bombe wirklich hoch? Werden wir alle sterben?"

    # Atropos Gedanken
    symb"Aber wann und wo?"

    # Atropos Gedanken
    symb"Was soll ich tun?"

    # Atropos Gedanken
    symb"Und was ist mit Kloth?"

    # Atropos Gedanken
    symb"Ich…"


    menu:
        "Ich will doch einfach nur glücklich sein.":
            # Atropos Gedanken
            symb"Ich will doch einfach nur glücklich sein."

            # Atropos Gedanken
            symb"Ich habe genug… Ich gehe zurück zur Arbeit. Das alles macht mir Angst."

            # Atropos Gedanken
            symb"Das alles sind nichts anderes als Hirngespinste."

            # Atropos Gedanken
            symb"Ja, ganz bestimmt! Ich bilde mir das ganze nur ein…"

            # Atropos Gedanken
            symb"Ich kehre jetzt einfach ins Labor zurück und vergesse das Ganze. Alles wird wieder wie zuvor sein."

            # Symbiont
            symb"{i}Ja, vergiss es. Sei einfach nur glücklich. Du bist sicher, nichts kann dir passieren. Das alles hier ist niemals passiert. Du hast eine ganz normale Mittagspause verbracht. {/i}"

            # Symbiont
            symb"{i}Sei glücklich, Atropos! {/i}"
            scene hall
            with fadeshort

            # Atropos Gedanken
            symb"Ob wohl Era da ist? Ich würde gerne ein bisschen Zeit mit ihr alleine verbringen und sie besser kennenlernen."

            # Atropos Gedanken
            symb"Auch wenn sie manchmal anstrengend sein kann, ist sie doch ziemlich süß."
            play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3
            scene lab
            with fadeshort
            jump laborpillende
        "Ich muss versuchen den Hinweisen nachzugehen.":
            jump choice_bomb
        "Ich muss Kloth finden und ihn fragen, was all das zu bedeuten hat.":
            # Atropos Gedanken
            symb"Ich muss Kloth finden und ihn fragen, was das alles zu bedeuten hat."

            # Atropos Gedanken
            symb"Vielleicht hat er Antworten…"

            # Atropos Gedanken
            symb"Ich weiß nicht, was ich sonst tun soll…"

            # Atropos Gedanken
            symb"Ich weiß nicht, was ich sonst mit dem Wissen anfangen soll…"

            # Atropos Gedanken
            symb"Ich habe Angst…"

            jump still_search_kloth

label still_search_kloth:

    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Aber wo könnte er nur sein? Ich habe doch schon an so vielen Orten nach ihm gesucht…"

    # Atropos Gedanken
    symb"Ich muss ihn unbedingt finden. Er ist mir ein paar Antworten schuldig… und außerdem will ich endlich für ihn so da sein, wie ich es schon lange hätte sein sollen."

    # Atropos Gedanken
    symb"Ist das dort vorne nicht Anan? Vielleicht sollte ich einfach mal ihn fragen, ob er Kloth gesehen hat…"

    # Atropos Gedanken
    symb"Das hätte ich gleich heute Morgen tun sollen."

    "Atropos" "Anan?"

    show anan normal_mid:
        xalign 0.5

    "Anan" "Atropos? Was kann ich für dich tun? Aber ich befürchte, du musst dich kurzhalten, ich bin beschäftigt."

    "Atropos" "Kloth, dein Sekretär… er ist ein guter Freund von mir und ich habe schon seit einer ganzen Weile nichts mehr von ihm gehört."

    "Atropos" "Ich mache mir Sorgen um ihn!"

    if read_computer_kloth:

        # Atropos Gedanken
        symb"Sollte ich Anan von der Bombe erzählen?"

        # Atropos Gedanken
        symb"Nein, besser nicht… noch kann ich nicht über die Situation urteilen. Ich muss erst Kloths Meinung dazu hören."

    if read_letter_kloth:

        # Atropos Gedanken
        symb"Ich hoffe nur, es ist nicht schon zu spät… Ich habe ein ungutes Gefühl…"

    "Anan" "Kloth Hetair? Ich bin ebenfalls auf der Suche nach ihm. Er ist heute nicht bei mir zu Arbeitsbeginn aufgetaucht."

    show anan strict_mid

    "Anan" "Er hat sich sonst immer abgemeldet, aber heute hat er es nicht getan."

    "Anan" "Weißt du etwas darüber?"

    show anan normal_mid

    "Atropos" "Nein… nein! Ich bin doch selbst auf der Suche nach ihm!"

    "Anan" "(mustert Atropos prüfend)"

    "Anan" "Gut. Lass uns zusammen weitersuchen. Es ist ihm nicht möglich, spurlos zu verschwinden."

    "Atropos" "Wieso bist du dir so sicher, dass er hier ist?"

    "Atropos" "Gibt es keine Möglichkeit, dass er sich vielleicht einen Tag frei genommen hat und nun irgendwo in Astoa aufhält?"

    show anan strict_mid

    "Anan" "Es gab gestern keine Registrierung, dass er das Gebäude verlassen hätte."

    "Anan" "Er befindet sich innerhalb Aithers."

    # Symbiont
    symb"{i}Willst du Kloth wirklich finden? Du weißt nicht, ob du die Wahrheit erträgst… Was ist, wenn du sie nicht verkraftest? {/i}"

    # Atropos Gedanken
    symb"Ich kann die Wahrheit verkraften. Egal was Kloth mir zu erzählen hat, ich werde ihm zuhören und für ihn da sein."

    "Atropos" "Okay… Wo hast du noch nicht gesucht?"

    "Atropos" "Wir könnten bei allen Personen nachfragen."

    "Anan" "Auf die Erinnerung der Menschen ist kein Verlass. Der menschliche Geist kann sich irren. Ich verlasse mich nur auf Fakten."

    "Atropos" "Okay… die Fahrzüge sind komplett überfüllt. Wenn wir unten starten und uns nach oben vorarbeiten wollen, müssen wir das Treppenhaus nehmen."

    hide anan

    play music "Sound/Music/Rooms/Serverraum/serverraum_normal.mp3" fadeout 3 fadein 3
    scene corpse
    with fadeshort

    "Atropos" "Kloth? Kloth?"

    "Atropos" "Nein, das darf doch nicht wahr sein! Das darf einfach nicht Kloth sein… bitte… nein…"

    "Atropos" "Das ganze Blut… ist er… ist er etwa tot?"

    # Symbiont
    symb"{i}Alles kommt wieder in Ordnung. Alles wird gut. Alles wird glücklich. Entspann dich. Kloth geht es gut. Mach dir keine Sorgen! {/i}"

    "Atropos" "Neeeein! Kloth liegt hier vor mir…"

    "Atropos" "Tot…"

    "Atropos" "Er ist tot…"

    "Atropos" "Wie?"

    "Atropos" "Warum?"

    "Atropos" "Das darf doch nicht wahr sein…"

    play music "Sound/Music/treppenhaus_ohne_Symbiont.mp3" fadeout 3 fadein 3
    # Wechsel zu Erinnerung
    scene stairs_up
    with fadeshort
    show sepia
    show kloth scared2 behind sepia:
        xalign 0.5
    "Kloth" "Atropos!"

    "Atropos" "Kloth, was ist los?"

    show kloth unsuresmiling_alt

    "Kloth"  "Ich habe dich überall gesucht. Endlich habe ich dich gefunden… ich muss mit dir reden. Hast du kurz einen Moment Zeit? Bitte…"

    "Atropos"  "Beruhige dich erst einmal und atme tief durch. Was ist passiert?"

    show kloth scared2

    "Kloth" "Nicht hier … es könnte jemand kommen und dann…"

    "Atropos"  "Kloth, es ist alles in Ordnung. Niemand kann dir etwas tun. Was ist denn nur los mit dir?"

    show kloth scared1

    "Kloth" "Ich… ich…"

    "Atropos"  "Ich wollte eigentlich gerade Mittagspause machen. Willst du nicht einfach mitkommen und wir reden dann? Chesis scheint auch Pause zu haben."

    show kloth unsuresmiling

    "Kloth" "Du hörst mir ja gar nicht richtig zu… bitte… ich… ich weiß nicht, an wen ich mich sonst wenden soll. Ich brauche dich jetzt!"

    "Kloth" "Es gibt da etwas, das ich schon eine ganze Weile mit mir herumtrage und ich komme alleine einfach nicht damit klar. Bitte, ich muss mit jemandem darüber sprechen!"

    "Atropos"  "Ja natürlich helfe ich dir. Erzähl endlich was los ist. Wie kann ich dir helfen?"

    hide kloth
    hide sepia

    # Erinnerung endet.
    show anan normal_mid:
        xalign 0.5


    # Atropos Gedanken
    symb"Was war das für eine Erinnerung gewesen? Ich kann mich nicht an das gesamte Gespräch erinnern…"

    # Atropos Gedanken
    symb"Und davor hatte ich es komplett vergessen…"

    # Atropos Gedanken
    symb"Aber… war das nicht gestern gewesen? Was hatte Kloth mir erzählt oder wollte es zumindest tun?"

    # Atropos Gedanken
    symb"Ist das der Grund für seinen Tod?"

    # Atropos Gedanken
    symb"Kloth… nein… Wieso?"

    # Atropos Gedanken
    symb"Hätte ich deinen Tod irgendwie verhindern können?"

    show anan disappointed_mid

    play music "Sound/Music/Rooms/AnansBuero/anan_buero_3St_ganz.mp3" fadeout 3 fadein 3

    "Anan" "Ich bedauere seinen Tod. Wir verlieren einen geschätzten Mitarbeiter. Ich hatte große Hoffnungen in ihn gesetzt."

    "Anan" "Er ist einer der größten Verfechter des Glücks gewesen, aber letztlich hat er der Verantwortung wohl doch nicht standhalten können und ist unter der Last zerbrochen."

    "Anan" "Immerhin hat er der Menschheit viel Gutes getan. Ich werde ihn bei der Gründungsfeier ehren lassen. Ihm war das Glück aller Menschen stets am Wichtigsten."

    show anan normal_mid

    "Anan" "Eine solche Person trifft man viel zu selten an."

    "Atropos"  "Ist das alles? Er war dein persönlicher Sekretär!"

    "Atropos"  "Aber dir scheint das ja alles vollkommen egal zu sein…"

    "Atropos"  "Ich dachte, dir sei das Glück der Menschen so unglaublich wichtig?"

    "Atropos"  "Das macht mir gerade aber nicht den Anschein!"

    # Symbiont
    symb"{i}Beruhige dich, Atropos. Deine Wut auf Anan ist nicht angemessen. Er hat dir nichts getan. Du bist wütend auf dich selbst, weil du Kloths Tod nicht verhindern konntest. {i}"

    # Symbiont
    symb"{i}Möchtest du das alles nicht vergessen und einfach nur glücklich sein? {i}"

    "Atropos"  "Ich will gerade nicht glücklich sein, verdammt noch mal! Ich will gerade einfach nur wütend und sauer und traurig sein!"

    "Atropos"  "Ich will den Schmerz fühlen, damit ich begreifen kann, dass es real ist."

    "Atropos"  "Ich will… ich will…"

    "Anan" "Atropos. Leid ist nicht das, was du brauchst um stärker zu werden. Glaube mir."

    "Anan" "Du willst kein Leid fühlen. Du willst den Schmerz nicht durchleben, welchen ich auf mich genommen habe."

    "Anan" "Nimm das Geschenk an, welches ich der Menschheit gemacht habe. Sei glücklich und zufrieden! Der Preis dafür war hoch und der Kampf dafür war lange."

    show anan disappointed_mid

    "Anan" "Wieso kämpfst du gerade so sehr gegen dein eigenes Glück an?"

    "Anan" "Willst du wirklich Schmerz empfinden? Willst du diesen grauenhaften Schmerz empfinden, der dir die Luft zum Atmen nimmt?"

    "Anan" "Willst du dir jede Sekunde deines Lebens vor Augen halten müssen, wen du alles verloren hast?"

    "Anan" "All die Bilder der Toten? Ihre Augen, wie sie dich verzweifelt anblicken, voller Hoffnung, dass du sie retten kannst, obwohl es doch nicht möglich ist."

    show anan normal_mid

    "Anan" "Es gibt für diese Welt keine andere Hoffnung als Glück."

    "Anan" "Nur das Glück und die Zufriedenheit jedes einzelnen Individuums sorgt dafür, dass die Welt in ihren Fugen bleibt."

    show anan happy_mid

    "Anan" "Werde wieder glücklich, Atropos. Bitte. Bringe die Welt nicht aus dem Gleichgewicht. Ich will, dass es dir gut geht."

    "Anan" "Ich werde deinen Schmerz auf mich nehmen."

    "Anan" "Sei glücklich."

    hide anan

    "Atropos"  "Ist das sein Ernst? Ist das sein verdammter Ernst?"

    # Atropos Gedanken
    symb"Wie könnte ich glücklich sein?"

    # Symbiont
    symb"{i}Du könntest glücklich werden. Du könntest vergessen. All den Schmerz vergessen. Du wirst Kloth in guter Erinnerung behalten. Ist es nicht das, was du willst? {i}"

    # Atropos Gedanken
    symb"Ich will Kloth nicht in guter Erinnerung behalten. Ich will ihn an meiner Seite haben!"

    "Atropos"  "Aber dafür ist es zu spät…"

    "Atropos"  "(schluchzt) Kloth…"

    "Atropos"  "Kloth!"

    # Atropos Gedanken
    symb"Anans Reaktion… was sollte der Mist?"

    # Atropos Gedanken
    symb"Er schwingt große Reden, aber letztlich sind wir ihm doch alle egal."

    # Symbiont
    symb"{i}Anan sagt nichts als die Wahrheit. Du solltest auf ihn hören. Er würde niemals die Menschen anlügen, die er so sehr liebt. {i}"

    # Atropos Gedanken
    symb"Aither ist an all diesem Mist schuld… sie zwingen mich dazu, um jeden Preis glücklich zu sein, auch wenn ich das gerade einfach nicht sein möchte!"

    if kloth_office_visited:

        # Atropos Gedanken
        symb"Kloth hatte recht mit allem… das, was ich im Büro herausgefunden habe… es muss etwas zu bedeuten haben… Kloth hatte etwas herausgefunden… er wollte handeln."

        # Atropos Gedanken
        symb"Und letzten Endes wurde er umgebracht. Es würde mich nicht wundern, wenn es Anan höchstpersönlich gewesen wäre."

    # Atropos Gedanken
    symb"Vermutlich hatte Kloth eine Wahrheit herausgefunden, die Anan unbequem geworden wäre."

    # Atropos Gedanken
    symb"Was auch immer Kloth begonnen hat, ich muss es zu Ende führen."

    # Symbiont
    symb"{i}Würde dich das glücklich machen? {i}"

    "Atropos"  "Es würde mich glücklich machen!"

    # Symbiont
    symb"{i}Dein Glück ist es, das letztlich zählt. Du solltest deinem eigenen Pfad folgen, der dafür sorgt, dass du glücklich bist. {i}"

    "Atropos"  "So bin ich glücklich!"

    if read_document_kloth:
        if read_computer_kloth:
            "Atropos"  "Ich muss in den Serverraum… sofort."

            "Atropos"  "Ich denke ich weiß, was mich dort erwartet."
            jump serverraumpille
        else:
            if thingswatched>0:
                "Atropos"  "Ich muss zurück in Kloths Büro… ich muss irgendwelche Anhaltspunkte übersehen haben."
            else:
                "Atropos"  "Ich muss zurück in Kloths Büro… ich hätte mich doch umsehen sollen."
            scene hall
            with fadeshort
            "Atropos"  "Aber was?"
            scene kloth_office
            with fadeshort
            "Atropos"  "Natürlich…"

            if kloth_office_visited:
                if thingswatched>0:
                    "Atropos"  "Der PC… Wie konnte ich nur vergessen auf diesem nachzuschauen?"
                else:
                    "Atropos"  "Der PC… es würde Sinn machen, wenn dort Informationen sind…"
            else:
                "Atropos"  "Der PC… es würde Sinn machen, wenn dort Informationen sind…"

            scene detail_blog
            with fadeshort
            call screen arrow_detail_blogkloth2


    else:
        if read_computer_kloth:
            if thingswatched>0:
                "Atropos"  "Ich muss zurück in Kloths Büro… ich muss irgendwelche Anhaltspunkte übersehen haben."
            else:
                "Atropos"  "Ich muss zurück in Kloths Büro… ich hätte mich doch umsehen sollen."
            scene hall
            with fadeshort
            "Atropos"  "Aber was?"
            scene kloth_office
            with fadeshort
            "Atropos"  "Natürlich…"
            "Atropos"  "Das Dokument auf seinem Tisch…"
            scene detail_servertext
            with fadeshort
            call screen arrow_detail_servertextkloth2

        else:
            if thingswatched>0:
                "Atropos"  "Ich muss zurück in Kloths Büro… ich muss irgendwelche Anhaltspunkte übersehen haben."
            else:
                "Atropos"  "Ich muss zurück in Kloths Büro… ich hätte mich doch umsehen sollen."
            scene hall
            scene hall
            with fadeshort
            "Atropos"  "Aber was?"
            scene kloth_office
            with fadeshort
            "Atropos"  "Natürlich…"
            if kloth_office_visited:
                if thingswatched>0:
                    "Atropos"  "Der PC… Wie konnte ich nur vergessen auf diesem nachzuschauen?"
                else:
                    "Atropos"  "Der PC… es würde Sinn machen, wenn dort Informationen sind…"
            else:
                "Atropos"  "Der PC… es würde Sinn machen, wenn dort Informationen sind…"

            scene detail_blog
            with fadeshort
            call screen arrow_detail_blogkloth


label after_detail_blogkloth2:
    "Atropos"  "Das erklärt alles. Ich muss in den Serverraum. Sofort."
    jump serverraumpille
label after_detail_servertextkloth2:
    scene detail_servergraph
    with fadeshort
    call screen arrow_detail_servergraphkloth2

label after_detail_servergraphkloth2:
    "Atropos"  "Das erklärt alles. Ich muss in den Serverraum. Sofort."
    jump serverraumpille

label after_detail_blogkloth:

    "Atropos"  "Eine Bombe?"

    "Atropos"  "Was hat das zu bedeuten? War es das, was Kloth erreichen wollte? Wollte er Aither in die Luft jagen?"

    "Atropos"  "Aber wo kann sie versteckt sein?"

    "Atropos"  "Es muss noch andere Hinweise geben…"

    scene kloth_office
    with fadeshort

    "Atropos"  "Was ist mit diesem Dokument? Enthält das irgendwelche Informationen?"

    scene detail_servertext
    with fadeshort
    call screen arrow_detail_servertextkloth

label after_detail_servertextkloth:
    scene detail_servergraph
    with fadeshort
    call screen arrow_detail_servergraphkloth

label after_detail_servergraphkloth:
    "Atropos"  "Das erklärt alles. Ich muss in den Serverraum. Sofort."
    jump serverraumpille


label serverraumpille:
    scene hall
    with fadeshort
    "Atropos"  "Ich muss mich beeilen. Ich weiß nicht, wie viel Zeit mir noch bleibt."

    # Symbiont
    symb"{i}Was willst du tun, wenn du dort bist? Welche Entscheidung wirst du treffen? Wirst du mit dieser Entscheidung glücklich sein? {i}"

    play music "Sound/Music/Rooms/Serverraum/serverraum_normal.mp3" fadeout 3 fadein 3
    scene server_room
    with fadeshort
    "Atropos"  "Ein Ticken… Es ist also tatsächlich wahr. Hier ist eine Bombe versteckt, welche jeden Moment hochgehen kann."

    # Symbiont
    symb"{i}Was wirst du tun? Wirst du glücklich sein? {i}"

    "Atropos"  "Die Bombe. Sie wird explodieren und ich werde sie nicht daran hindern. Ich werde Aither zerstören. Dieses erzwungene Glück ist kein Glück."

    "Atropos"  "Ich will lieber das größte Leid ertragen als weiterhin in dieser Scheinwelt leben zu müssen."

    # Symbiont
    symb"{i}Was ist mit all den Menschen im Gebäude? Wirst du sie retten? Sie sind unschuldig und wissen von nichts. Wenn du dich selbst als Opfer betrachtest. Sind sie dann nicht Opfer genau wie du? {i}"

    show screen force_mouse_move_630
    menu:
        "Wenn ich den Menschen helfe, rette ich damit vielleicht auch Anan. Das kann ich nicht zulassen.":
            hide screen force_mouse_move_630
            jump menschennichthelfen
        "Ich muss den Menschen helfen. Sie können nichts dafür.":
            hide screen force_mouse_move_630
            jump menschenhelfen

label menschennichthelfen:
    "Atropos"  "Wenn ich den Menschen helfe, rette ich damit vielleicht auch Anan. Das kann ich nicht zulassen."

    "Atropos"  "Anan ist überhaupt erst schuld an der gesamten Lage, in der wir uns gerade befinden."

    "Atropos"  "Er hat Kloth umgebracht und uns unser scheinbares Glück aufgezwungen."

    "Atropos"  "Ich darf nicht zulassen, dass er sein Werk weiterführen kann."

    "Atropos"  "Mit seinem Wissen könnte Aither mit Leichtigkeit wiederaufgebaut werden."

    "Atropos"  "Das darf ich nicht zulassen."

    scene detail_bomb1000
    with fadeshort

    # Symbiont
    symb"{i}Noch 10 Minuten. {i}"

    scene server_room
    with fadeshort

    "Atropos"  "Ich bin bereit für alles, was kommen wird."

    "Atropos"  "Ich bin bereit die Verantwortung zu tragen."

    "Atropos"  "Chesis… Era… Tycho… ihr alle… es tut mir leid."

    "Atropos"  "Aber es gibt keine andere Wahl… manchmal müssen Opfer gebracht werden, damit die Welt zu einem besseren Ort wird."

    "Atropos"  "Bereinigt von den Menschen, die sie verseuchen. Ich muss dem Treiben von Anan und seinem Triumvirat endlich ein Ende setzen!"

    "Atropos"  "Ich werde Kloths Werk vollenden!"

    scene server_room
    with fadestart

    "Atropos"  "…"

    "Atropos"  "Koth… ich wünschte, du wärst jetzt an meiner Seite…"

    "Atropos"  "Ich wünschte, du wärst in dem Wissen gestorben, tatsächlich etwas erreicht zu haben."

    "Atropos"  "Ich hoffe, du kannst den Triumph noch von irgendwo anders auskosten."

    scene detail_bomb0010
    with fadeshort

    # Symbiont
    symb"{i}10 Sekunden. {i}"

    "Atropos"  "Jetzt ist also alles vorbei, was?"

    scene detail_bomb0009

    # Symbiont
    symb"{i}9 Sekunden. {i}"

    "Atropos"  "Die 10 Minuten gingen schneller um, als ich dachte… ich wünschte, ich hätte etwas mehr Zeit, um mich gedanklich von allen zu verabschieden."

    scene detail_bomb0008

    # Symbiont
    symb"{i}8 Sekunden. Bereust du deine Entscheidung? Oder bist du glücklich?{i}"

    "Atropos"  "Ich bin glücklich."

    scene detail_bomb0007

    # Symbiont
    symb"{i}7 Sekunden. {i}"

    "Atropos"  "Denke ich."

    scene detail_bomb0006

    # Symbiont
    symb"{i}6 Sekunden. {i}"

    "Atropos"  "Vielleicht hätte ich doch alle warnen sollen."

    scene detail_bomb0005

    # Symbiont
    symb"{i}5 Sekunden. {i}"

    "Atropos"  "Ob sie mir wohl jemals verzeihen werden?"

    scene detail_bomb0004

    # Symbiont
    symb"{i}4 Sekunden. Ja, das werden sie. Du hast es für das Wohl der gesamten Menschheit getan.{i}"

    "Atropos"  "Danke."

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return
label menschenhelfen:

    "Atropos"  "Ich muss den Menschen helfen. Sie können nichts dafür."

    "Atropos"  "Selbst wenn sich Anan dadurch retten kann… ich könnte es nicht mit meinem Gewissen vereinbaren alle deswegen sterben zu lassen."

    "Atropos"  "Und die Vernichtung dieser Filiale sowie der Server wird uns wenigstens etwas Zeit verschaffen."

    "Atropos"  "Zeit, in der auch andere Menschen erkennen können, was wahres Glück bedeutet."

    # Symbiont
    symb"{i}Was bedeutet für dich wahres Glück? {i}"

    "Atropos"  "Die Möglichkeit, selbst zu entscheiden, wie ich in bestimmten Momenten fühlen möchte. Es sollte allein meine Entscheidung sein."

    # Symbiont
    symb"{i}Und so bist du wahrhaft glücklich? {i}"

    scene hall
    with fadealarm
    scene detail_alarm
    with fadealarm

    # Atropos Gedanken
    symb"Es sollte ausreichen, wenn ich den Handfeuermelder betätige. Das sollte zumindest den meisten Menschen die Chance geben zu entkommen. Mehr kann ich nicht tun."

    # Symbiont
    symb"{i}Atropos. Kannst du wirklich damit leben, dass Menschen deswegen sterben oder verletzt werden? {i}"

    # Atropos Gedanken
    symb"Ich denke, das ist es wert."

    scene detail_alarmbroken
    with fadeshort

    # Atropos Gedanken
    symb"Der Alarm ist ganz schön laut und all diese aufgeregten Stimmen, welche durcheinanderrufen."

    scene hall
    with fadeshort


    show ireia confused:
        xalign 0.25
    show armene normal_gray:
        xalign 0.75

    "Ireia" "Atropos, was ist los? Ist Aither in Gefahr?"

    "Atropos"  "Ich weiß es nicht, der Alarm ging mit einem Mal los. Aber ihr solltet besser bald das Gebäude verlassen."

    show ireia confused_gray
    show armene shy

    "Armene" "Ich will nicht, dass Aither etwas passiert. Wie soll ich denn sonst glücklich sein?"

    "Armene" "Die Firma ist alles, was ich im Leben noch habe. Ich bin glücklich- ich will nicht, dass sich etwas ändert."

    "Atropos"  "Aber erkennt ihr es denn nicht? Wollt ihr wirklich auf diese Art und Weise glücklich sein? Euch ist jede andere Emotion genommen. Jede andere Option zu empfinden."

    show armene shy_gray
    show ireia normal

    "Ireia" "Ich will einfach nur glücklich sein. Ich möchte nicht, dass sich so etwas wie der 50-jährige Krieg wiederholt. Meine Eltern hatten mir von dieser Zeit erzählt…"

    "Ireia" "Da ist das hier doch nur ein kleiner Preis, nicht wahr? Ich bin glücklich so wie ich bin."

    show ireia happy

    "Ireia" "Na los, Armene. Lass uns weiterarbeiten."

    "Ireia" "Ein Brand wird uns doch nicht einfach aufhalten. Der wird sicher bald gelöscht werden und wir haben nachher noch ein Meeting."

    show ireia happy_gray
    show armene nromal

    "Armene" "Natürlich Ireia. Man sieht sich später, Atropos!"

    "Atropos"  "Nein, geht nicht! Verlasst das Gebäude!"

    hide ireia
    hide armene

    "Atropos"  "Verlasst das Gebäude! Es brennt!"

    "Atropos"  "Wieso arbeitet ihr denn alle weiter als wäre nichts?"

    "Atropos"  "Verlasst das Gebäude… bitte…"

    # Symbiont
    symb"{i}Rette sie! Du könntest mit ihrem Tod nicht leben. {i}"

    "Atropos"  "Verdammt… ich darf nicht zu spät kommen… der Serverraum… ich muss zurück und die Bombe aufhalten!"

    scene server_room
    with fadealarm

    scene detail_bomb0004
    with fadeshort

    # Symbiont
    symb"{i}4 Sekunden. Atropos, bist du glücklich? {i}"

    "Atropos"  "Was soll die Frage? Nein… nein, das wollte ich nicht…"

    # Symbiont
    symb"{i}Es tut mir leid. {i}"

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

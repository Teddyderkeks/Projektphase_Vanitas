default read_letter_kloth = False
default read_computer_kloth = False
default read_document_kloth = False

label search_kloth:
    scene hall

    # Symbiont
    "{i}Du solltest ihn nicht anrufen. Was ist, wenn er gerade in einer Besprechung ist und du ihn störst? {/i}"

    # Symbiont
    "{i}Schreibe ihm doch lieber, warte ab bis er antwortet und verbringe unterdessen Zeit mit deinen Freunden. Das macht dich glücklich. {/i}"

    # Atropos Gedanken
    "Ich sollte es wirklich erstmal mit einer Nachricht versuchen."

    "Atropos" "…"

    # Atropos Gedanken
    "Seltsam. Es wird nicht angezeigt, dass er meine Nachricht überhaupt empfängt. Hat er sein Handy ausgeschaltet? Ich sollte ihn besser doch anrufen."

    "Atropos" "…"

    "Atropos" "…"

    "Atropos" "…"

    "Atropos" "Verdammt, Kloth. Geh dran, bitte…"

    "Atropos" "…"

    # Symbiont
    "{i}Er ist gerade bestimmt in einer Besprechung und hat deswegen sein Handy abgeschaltet. {/i}"

    # Atropos Gedanken
    "Ich sollte dennoch in seinem Büro nachschauen gehen."

    "Atropos" "…"


    "Atropos" "Kloth? Bist du da? Darf ich reinkommen?"

    # Atropos Gedanken
    "Kein Laut zu hören… vielleicht hat er mich ja nicht gehört? Kloth wird schon nicht sauer sein, wenn ich einfach eintrete."

    # Wechsel zu Kloths Büro

    "Atropos" "Kloth?"

    # Atropos Gedanken
    "Niemand hier."

    # Atropos Gedanken
    "Das wäre auch zu schön gewesen."

    # Atropos Gedanken
    "Aber wo kann er sonst sein?"

    # Atropos Gedanken
    "Vielleicht in Anans Büro? Aber dort kann ich doch nicht einfach so hineinplatzen…"


    menu:
        "Einen Versuch ist es wert, selbst wenn ich dafür Ärger von Anan bekommen sollte.":

            # Atropos Gedanken
            "Einen Versuch ist es wert, selbst wenn ich dafür Ärger von Anan bekommen sollte."

            # Atropos Gedanken
            "Zum Glück ist es gleich nebenan."

            jump search_kloth_in_anan_office
        "Nein, ich sollte wo anders nach ihm suchen.":

            # Atropos Gedanken
            "Nein, ich sollte wo anders nach ihm suchen."

            # Atropos Gedanken
            "Aber was soll ich jetzt nur tun?"

            # Atropos Gedanken
            "Es fühlt sich falsch an einfach ins Labor zurückzukehren."

            jump search_kloth_without_anan_office

label search_kloth_in_anan_office:

    # Atropos Gedanken
    "Ich klopfe besser an."

    "Atropos" "…"

    "Atropos" "Hallo? Jemand da?"

    # Atropos Gedanken
    "Es scheint auch hier niemand da zu sein…"

    # Atropos Gedanken
    "Sollte ich nachschauen? Aber bei Anan ist es noch einmal etwas anderes einfach einzutreten als bei Kloth…"

    # Atropos Gedanken
    "Was soll’s… ich muss Kloth finden."

    scene anan_office

    # Atropos Gedanken
    "Es ist tatsächlich verlassen."

    # Atropos Gedanken
    "Ich bin noch nie hier gewesen. Es ist wirklich beeindruckend."

    # Atropos Gedanken
    "Soll ich mich ein wenig umschauen? Vielleicht finde ich ja irgendwelche Hinweise auf Kloth."

    # Symbiont
    "{i}Lass es bleiben. {/i}"

    # Symbiont
    "{i}Anan könnte jeden Moment zurückkommen und du willst nicht, dass er dich dabei erwischt, wie du in seinen Sachen herumstöberst. {/i}"

    # Symbiont
    "{i}Willst du das etwa? Das würde dein Glück nur gefährden. {/i}"

    menu:
        "Ich möchte das Risiko eingehen und mich trotzdem umsehen.":
            jump symbiont_in_between
        "Ich suche besser wo anders nach ihm.":
            jump search_kloth_without_anan_office

label symbiont_in_between:
    # Atropos Gedanken
    "Ich möchte das Risiko eingehen und mich trotzdem umsehen."

    # Symbiont
    "{i}Verlasse diesen Raum. Du gefährdest deine Glücklichkeit mit jeder Sekunde mehr. Siehst du es nicht? {/i}"

    # Symbiont
    "{i}Das wird kein gutes Ende nehmen. Suche an einem anderen Ort nach Kloth oder lass es ganz bleiben. {/i}"

    # Symbiont
    "{i}Es geht ihm gut. Er ist glücklich so wie jeder andere Mensch auch. {/i}"

    # Symbiont
    "{i}Ist es dir das Risiko wirklich wert, auch wenn du wahrscheinlich nichts finden wirst, was dich zu Kloth führt? {/i}"

    # Symbiont
    "{i}Verlasse diesen Raum, Atropos. Denk an deine Glücklichkeit. {/i}"

    # Symbiont
    "{i}Riskiere sie nicht. {/i}"

    # Atropos Gedanken
    "Ja, meine Glücklichkeit ist wichtiger… was tue ich hier noch?"

    scene hall

    # Atropos Gedanken
    "Aber was soll ich jetzt nur tun?"

    # Atropos Gedanken
    "Es fühlt sich falsch an einfach ins Labor zurückzukehren."


    jump search_kloth_without_anan_office


label search_kloth_without_anan_office:
    scene hall

    # Atropos Gedanken
    "Wo könnte ich Kloth nur suchen?"

    # Atropos Gedanken
    "Die Orte, an denen er sich am wahrscheinlichsten aufhält, habe ich bereits nach ihm abgesucht."

    # Atropos Gedanken
    "Hatte Kloth neulich etwas in die Richtung erwähnt?"

    # Überschwung zu Erinnerung, Ort: Kloths Büro; Über der gesamten Erinnerung liegt ein Rauschen

    scene kloth_office
    show kloth aengstlich2:
        xalign 0.5

    "Atropos" "Zu so früher Stunde schon ein Bier? (lacht)"

    "Kloth" "Warum nicht- es schmeckt halt gut und lässt einen vieles vergessen."

    "Atropos" "Vergessen? Es gibt doch nichts in diesem wundervollen Leben, das man vergessen möchte."

    "Kloth" "Wundervoll? Glücklich? Bestimmt… Träum weiter Atropos, bleibe in deiner Traumwelt gefangen."

    "Atropos" "Von was redest du nur?"

    "Kloth" "Sieh dich doch mal um. All diese glücklichen, breit grinsenden Menschen, die alles toll finden, was andere sagen und tun. Nennst du das Glück?"

    "Atropos" "Kloth, was ist denn nur los mit dir? Du machst mir ja fast schon Angst."

    "Kloth" "Immerhin würdest du dann nicht mehr seelenlos glücklich sein. Das wäre schon mal ein Fortschritt."

    "Atropos" "Wie viel hast du getrunken? Du fantasierst ja schon. Dein Alkoholkonsum ist in den letzten Monaten viel zu sehr angestiegen."

    "Kloth" "Nein, ist er nicht! Mir geht es gut. Hörst du Atropos? Mir geht es gut!"

    "Atropos" "Schon okay, ich habe verstanden. Du bist glücklich und das freut mich."

    "Kloth" "Sie werden kommen, Atropos. Ich warne dich. Sie werden kommen und uns holen."

    "Kloth" "Sie warten nur darauf, dass wir alle zu seelenlosen Kreaturen werden. Und dann holen sie uns."

    "Kloth" "Aber mich werden sie nicht bekommen. Ich werde ihnen entkommen. Ich werde fliehen, hörst du?"

    "Atropos" "Ja, das wirst du, Kloth. Alles wird in Ordnung. Ruhe dich einfach ein wenig aus und beruhige dich."

    # Ende der Erinnerung, zurück im Flur
    hide kloth
    scene hall

    # Atropos Gedanken
    "Was war das denn für eine seltsame Erinnerung gewesen? Die hatte ich ja vollkommen vergessen…"

    # Atropos Gedanken
    "Das Gespräch war ein paar Monate her, ob es mittlerweile wohl noch schlimmer geworden ist?"

    # Atropos Gedanken
    "Kloth wirkte fast schon besessen. Und es würde erklären, warum er sich in letzter Zeit so selten gemeldet hat."

    # Atropos Gedanken
    "Er scheint auch ein Alkoholproblem zu haben. Warum ist mir das nur nicht früher aufgefallen? Ich muss unbedingt mit ihm sprechen."

    # Atropos Gedanken
    "Vielleicht finde ich aber auch in seinem Büro mehr Hinweise auf das, was ihn im Moment so sehr aus der Bahn wirft."

    # Symbiont
    "{i}Deine Mittagspause ist gleich vorbei. Du solltest besser ins Labor zurückkehren. {/i}"

    # Symbiont
    "{i}Höre auf dir so viele Gedanken um Kloth zu machen, das gefährdet am Ende nur deine Glücklichkeit. Siehst du es denn nicht? {/i}"

    # Symbiont
    "{i}Er ist nicht mehr bei Sinnen gewesen in der letzten Zeit. Sei für ihn da, sobald er dazu bereit ist. {/i}"

    # Symbiont
    "{i}Aber jetzt geh. Er ist doch ohnehin nicht da, willst du durch ganz Aither rennen, um ihn zu suchen? {/i}"

    # Symbiont
    "{i}Du musst heute noch so viel Arbeit erledigen. Kümmere dich darum. Das macht dich glücklich. {/i}"


    menu:
        "Ich suche weiter nach Kloth. Ich muss sofort mit ihm persönlich darüber sprechen.":
            # Atropos Gedanken
            "Ich suche weiter nach Kloth. Ich muss sofort mit ihm persönlich darüber sprechen."

            # Atropos Gedanken
            "So kann ich ihm am besten helfen."

            # Atropos Gedanken
            "Ich muss endlich wissen, was los ist."

            jump still_search_kloth
        "Ich sehe mich in Kloths Büro nach Hinweisen um, damit ich ihm helfen kann.":
            # Atropos Gedanken
            "Ich sehe mich in Kloths Büro nach Hinweisen um, damit ich ihm helfen kann."

            # Atropos Gedanken
            "Vielleicht finde ich dort ja irgendetwas, was mir weiterhilft."

            # Atropos Gedanken
            "Irgendeinen Anhaltspunkt auf den ich Kloth ansprechen kann."

            # Atropos Gedanken
            "Ich will, dass er endlich wieder glücklich sein kann und nicht so leiden muss, wie es in der Erinnerung den Anschein hatte."

            scene kloth_office

            # Atropos Gedanken
            "Kloths Büro… ich habe mich schon lange nicht mehr wirklich hier aufgehalten. Wo könnte ich nur Hinweise finden?"

            # Atropos Gedanken
            "Hmmm… hier liegen eine ganze Menge an Sachen herum, ich werde…"

            jump selection_kloth_office
        "Ich sollte besser zurück ins Labor. Vielleicht hat Kloth den anderen dort ja auch eine Nachricht für mich hinterlassen?":
            # Atropos Gedanken
            "Ich sollte besser zurück ins Labor. Vielleicht hat Kloth den anderen dort ja auch eine Nachricht für mich hinterlassen?"

            # Atropos Gedankens
            "Oder er hat mich gesucht und wir sind aneinander vorbeigelaufen und nun wartet er beim Labor auf mich."

            # Atropos Gedanken
            "So oder so. Ich muss ohnehin zurück zur Arbeit. Wenn Kloth nicht beim Labor ist, dann werde ich ihm einfach nochmal eine Nachricht schreiben."

            scene lab
            # Atropos Gedanken
            "Er ist nicht hier. Schade. Ich hatte schon Hoffnung gehabt. Aber er wird sich schon melden."

            # Atropos Gedanken
            "Und nachher beim Grillen werden wir alle über diese ewige Herumsucherei lachen."

            jump not_search_kloth

label everything_seen:
    # Atropos Gedanken
    "Was soll ich jetzt nur tun?"

    # Atropos Gedanken
    "Ich habe Angst…"

    # Atropos Gedanken
    "Ich will das alles nicht…"

    # Atropos Gedanken
    "Was hat das alles zu bedeuten?"

    # Atropos Gedanken
    "Was soll ich machen? Kloth suchen? Den Hinweisen nachgehen? Verrückt werden?"

    # Atropos Gedanken
    "Mich in einem Schrank verkriechen und nie wieder daraus hervorkommen?"

    # Atropos Gedanken
    "Es klingt verlockend…"

    # Atropos Gedanken
    "Wie soll ich mit meinem Wissen umgehen?"

    # Atropos Gedanken
    "Was kann ich tun?"

    # Atropos Gedanken
    "Ich bin vor Angst wie erstarrt."

    # Atropos Gedanken
    "Geht die Bombe wirklich hoch? Werden wir alle sterben?"

    # Atropos Gedanken
    "Aber wann und wo?"

    # Atropos Gedanken
    "Was soll ich tun?"

    # Atropos Gedanken
    "Und was ist mit Kloth?"

    # Atropos Gedanken
    "Ich…"


    menu:
        "Ich will doch einfach nur glücklich sein.":
            # Atropos Gedanken
            "Ich will doch einfach nur glücklich sein."

            # Atropos Gedanken
            "Ich habe genug… Ich gehe zurück zur Arbeit. Das alles macht mir Angst."

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
        "Ich muss versuchen den Hinweisen nachzugehen.":
            jump choice_bomb
        "Ich muss Kloth finden und ihn fragen, was all das zu bedeuten hat.":
            # Atropos Gedanken
            "Ich muss Kloth finden und ihn fragen, was das alles zu bedeuten hat."

            # Atropos Gedanken
            "Vielleicht hat er Antworten…"

            # Atropos Gedanken
            "Ich weiß nicht, was ich sonst tun soll…"

            # Atropos Gedanken
            "Ich weiß nicht, was ich sonst mit dem Wissen anfangen soll…"

            # Atropos Gedanken
            "Ich habe Angst…"

            jump still_search_kloth

label still_search_kloth:

    scene hall

    # Atropos Gedanken
    "Aber wo könnte er nur sein? Ich habe doch schon an so vielen Orten nach ihm gesucht…"

    # Atropos Gedanken
    "Ich muss ihn unbedingt finden. Er ist mir ein paar Antworten schuldig… und außerdem will ich endlich für ihn so da sein, wie ich es schon lange hätte sein sollen."

    # Atropos Gedanken
    "Ist das dort vorne nicht Anan? Vielleicht sollte ich einfach mal ihn fragen, ob er Kloth gesehen hat…"

    # Atropos Gedanken
    "Das hätte ich gleich heute Morgen tun sollen."

    "Atropos" "Anan?"

    show anan 2:
        xalign 0.5

    "Anan" "Atropos? Was kann ich für dich tun? Aber ich befürchte du musst dich kurzhalten, ich bin beschäftigt."

    "Atropos" "Kloth, dein Sekretär… er ist ein guter Freund von mir und ich habe schon seit einer ganzen Weile nichts mehr von ihm gehört."

    "Atropos" "Ich mache mir Sorgen um ihn!"

    if read_computer_kloth:

        # Atropos Gedanken
        "Sollte ich Anan von der Bombe erzählen?"

        # Atropos Gedanken
        "Nein, besser nicht… noch kann ich nicht über die Situation urteilen. Ich muss erst Kloths Meinung dazu hören."

    if read_letter_kloth:

        # Atropos Gedanken
        "Ich hoffe nur es ist nicht schon zu spät… ich habe ein ungutes Gefühl…"

    "Anan" "Kloth Hetair? Ich bin ebenfalls auf der Suche nach ihm. Er ist heute nicht bei mir zu Arbeitsbeginn aufgetaucht."

    "Anan" "Er hatte sich sonst immer abgemeldet, aber heute hat er es nicht getan."

    "Anan" "Weißt du etwas darüber?"

    "Atropos" "Nein… nein! Ich bin doch selbst auf der Suche nach ihm!"

    "Anan" "(mustert Atropos prüfend)"

    "Anan" "Gut. Lass uns zusammen weitersuchen. Es ist ihm nicht möglich spurlos zu verschwinden."

    "Atropos" "Wieso bist du dir so sicher, dass er hier ist?"

    "Atropos" "Gibt es keine Möglichkeit, dass er sich vielleicht einen Tag frei genommen hat und nun irgendwo in Astoa aufhält?"

    "Anan" "Sein Verlassen des Gebäudes gestern wurde nicht registriert."

    "Anan" "Er befindet sich innerhalb Aithers."

    # Symbiont
    "{i}Willst du Kloth wirklich finden? Du weißt nicht, ob du die Wahrheit erträgst… was ist, wenn du sie nicht verkraftest? {/i}"

    # Atropos Gedanken
    "Ich kann die Wahrheit verkraften. Egal was Kloth mir zu erzählen hat, ich werde ihm zuhören und für ihn da sein."

    "Atropos" "Okay… Wo hast du noch nicht gesucht?"

    "Atropos" "Wir könnten bei allen Personen nachfragen."

    "Anan" "Auf die Erinnerung der Menschen ist kein Verlass. Der menschliche Geist kann sich irren. Ich verlasse mich nur auf Fakten."

    "Atropos" "Okay… die Fahrzüge sind komplett überfüllt. Wenn wir unten starten und uns nach oben vorarbeiten wollen, müssen wir das Treppenhaus nehmen."

    scene stairs_up

    "Atropos" "Kloth? Kloth?"

    "Atropos" "Nein, das darf doch nicht wahr sein! Das darf einfach nicht Kloth sein… bitte… nein…"

    "Atropos" "Das ganze Blut… ist er… ist er etwa tot?"

    # Symbiont
    "{i}Alles kommt wieder in Ordnung. Alles wird gut. Alles wird glücklich. Entspanne dich. Kloth geht es gut. Mach dir keine Sorgen.{/i}"

    "Atropos" "Neeeein! Kloth liegt hier vor mir…"

    "Atropos" "Tot…"

    "Atropos" "Er ist tot…"

    "Atropos" "Wie?"

    "Atropos" "Warum?"

    "Atropos" "Das darf doch nicht wahr sein…"

    hide anan

    # Wechsel zu Erinnerung
    show kloth aengstlich1:
        xalign 0.5
    "Kloth" "Atropos!"

    "Atropos" "Kloth, was ist los?"

    "Kloth"  "Ich habe dich überall gesucht. Endlich habe ich dich gefunden… ich muss mit dir reden. Hast du kurz einen Moment Zeit? Bitte…"

    "Atropos"  "Beruhige dich erst einmal und atme tief durch. Was ist passiert?"

    "Kloth" "Nicht hier … es könnte jemand kommen und dann…"

    "Atropos"  "Kloth, es ist alles in Ordnung. Niemand kann dir etwas tun. Was ist denn nur los mit dir?"

    "Kloth" "Ich… ich…"

    "Atropos"  "Ich wollte eigentlich gerade Mittagspause machen. Willst du nicht einfach mitkommen und wir reden dann? Chesis scheint auch Pause zu haben."

    "Kloth" "Du hörst mir ja gar nicht richtig zu… bitte… ich… ich weiß nicht an wen ich mich sonst wenden soll. Ich brauche dich jetzt."

    "Kloth" "Es gibt da etwas, das ich schon eine ganze Weile mit mir herumtrage und ich komme alleine einfach nicht damit klar. Bitte, ich muss mit jemandem darüber sprechen."

    "Atropos"  "Ja natürlich helfe ich dir. Erzähl endlich was los ist. Wie kann ich dir helfen?"

    hide kloth

    # Erinnerung endet.
    show anan 2:
        xalign 0.5


    # Atropos Gedanken
    "Was war das für eine Erinnerung gewesen? Ich kann mich nicht an das gesamte Gespräch erinnern…"

    # Atropos Gedanken
    "Und davor hatte ich es komplett vergessen…"

    # Atropos Gedanken
    "Aber… war das nicht gestern gewesen? Was hatte Kloth mir erzählt oder wollte es zumindest tun?"

    # Atropos Gedanken
    "Ist das der Grund für seinen Tod?"

    # Atropos Gedanken
    "Kloth… nein… Wieso?"

    # Atropos Gedanken
    "Hätte ich deinen Tod irgendwie verhindern können?"

    "Anan" "Ich bedauere seinen Tod. Wir verlieren einen geschätzten Mitarbeiter. Ich hatte große Hoffnungen in ihn gesetzt."

    "Anan" "Er war einer der größten Verfechter des Glücks gewesen, aber letztlich hatte er der Verantwortung wohl doch nicht standhalten können und ist unter der Last zerbrochen."

    "Anan" "Immerhin hat er der Menschheit viel Gutes getan. Ich werde ihn bei der Gründungsfeier ehren lassen. Ihm war das Glück aller Menschen stets am Wichtigsten."

    "Anan" "Eine solche Person trifft man viel zu selten an."

    "Atropos"  "Ist das alles? Er war dein persönlicher Sekretär gewesen!"

    "Atropos"  "Aber dir scheint das ja alles vollkommen egal zu sein…"

    "Atropos"  "Ich dachte dir sei das Glück der Menschen so unglaublich wichtig?"

    "Atropos"  "Das macht mir gerade aber nicht den Anschein!"

    # Symbiont
    "{i}Beruhige dich Atropos. Deine Wut auf Anan ist nicht angemessen. Er hat dir nichts getan. Du bist wütend auf dich selbst, weil du Kloths Tod nicht verhindern konntest. {i}"

    # Symbiont
    "{i}Möchtest du das alles nicht vergessen und einfach nur glücklich sein? {i}"

    "Atropos"  "Ich will gerade nicht glücklich sein, verdammt noch mal! Ich will gerade einfach nur wütend und sauer und traurig sein!"

    "Atropos"  "Ich will den Schmerz fühlen, damit ich begreifen kann, dass es real ist."

    "Atropos"  "Ich will… ich will…"

    "Anan" "Atropos. Leid ist nicht das, was du brauchst um stärker zu werden. Glaube mir."

    "Anan" "Du willst kein Leid fühlen. Du willst den Schmerz nicht durchleben, welchen ich auf mich genommen habe."

    "Anan" "Nimm das Geschenk an, welches ich der Menschheit gemacht habe. Sei glücklich und zufrieden. Der Preis dafür war hoch und der Kampf dafür war lange."

    "Anan" "Wieso kämpfst du gerade so sehr gegen dein eigenes Glück an?"

    "Anan" "Willst du wirklich Schmerz empfinden? Willst du diesen grauenhaften Schmerz empfinden, der dir die Luft zum Atmen nimmt?"

    "Anan" "Willst du dir jede Sekunde deines Lebens vor Augen halten müssen, wen du alles verloren hast?"

    "Anan" "All die Bilder der Toten? Ihre Augen, wie sie dich verzweifelt anblicken, voller Hoffnung, dass du sie retten kannst, obwohl es doch nicht möglich ist."

    "Anan" "Es gibt für diese Welt keine andere Hoffnung als Glück."

    "Anan" "Nur das Glück und die Zufriedenheit jedes einzelnen Individuums sorgt dafür, dass die Welt in ihren Fugen bleibt."

    "Anan" "Werde wieder glücklich, Atropos. Bitte. Bringe die Welt nicht aus dem Gleichgewicht. Ich will, dass es dir gut geht."

    "Anan" "Ich werde deinen Schmerz auf mich nehmen."

    "Anan" "Sei glücklich."

    hide anan

    "Atropos"  "Ist das sein Ernst? Ist das sein verdammter Ernst?"

    # Atropos Gedanken
    "Wie könnte ich glücklich sein?"

    # Symbiont
    "{i}Du könntest glücklich werden. Du könntest vergessen. All den Schmerz vergessen. Du wirst Kloth in guter Erinnerung behalten. Ist es nicht das, was du willst? {i}"

    # Atropos Gedanken
    "Ich will Kloth nicht in guter Erinnerung behalten. Ich will ihn an meiner Seite haben!"

    "Atropos"  "Aber dafür ist es zu spät…"

    "Atropos"  "(schluchzt) Kloth…"

    "Atropos"  "Kloth!"

    # Atropos Gedanken
    "Anans Reaktion… was sollte der Mist?"

    # Atropos Gedanken
    "Er schwingt große Reden, aber letztlich sind wir ihm doch alle egal."

    # Symbiont
    "{i}Anan sagt nichts als die Wahrheit. Du solltest auf ihn hören. Er würde niemals die Menschen anlügen, die er so sehr liebt. {i}"

    # Atropos Gedanken
    "Aither ist an all diesem Mist schuld… sie zwingen mich dazu um jeden Preis glücklich zu sein, auch wenn ich das gerade einfach nicht sein möchte!"

    # Atropos Gedanken
    "Kloth hatte Recht mit allem… das, was ich im Labor herausgefunden habe… es muss etwas zu bedeuten haben… Kloth hatte etwas herausgefunden… er wollte handeln."

    # Atropos Gedanken
    "Und letzten Endes wurde er umgebracht. Es würde mich nicht wundern, wenn es Anan höchstpersönlich gewesen wäre."

    # Atropos Gedanken
    "Vermutlich hatte Kloth eine Wahrheit herausgefunden, die Anan unbequem geworden wäre."

    # Atropos Gedanken
    "Was auch immer Kloth begonnen hat, ich muss es zu Ende führen."

    # Symbiont
    "{i}Würde dich das glücklich machen? {i}"

    "Atropos"  "Es würde mich glücklich machen!"

    # Symbiont
    "{i}Dein Glück ist es, das letztlich zählt. Du solltest deinem eigenen Pfad folgen, der dafür sorgt, dass du glücklich bist. {i}"

    "Atropos"  "So bin ich glücklich!"

    if read_document_kloth:
        if read_computer_kloth:
            "Atropos"  "Ich muss in den Serverraum… sofort."

            "Atropos"  "Ich denke ich weiß, was mich dort erwartet."
            jump serverraumpille
        else:
            "Atropos"  "Ich muss zurück in Kloths Büro… ich muss irgendwelche Anhaltspunkte übersehen haben."
            scene hall
            "Atropos"  "Aber was?"
            scene kloth_office
            "Atropos"  "Natürlich…"

            "Atropos"  "Der PC… Wie konnte ich nur vergessen auf diesem nachzuschauen?"
            # Spieler wird PC ohne Passwort-Kennung angezeigt
            "Blog über Bombenleger, der Aither vernichten will."
            "Atropos"  "Das erklärt alles. Ich muss in den Serverraum. Sofort."
            jump serverraumpille

    else:
        if read_computer_kloth:
            "Atropos"  "Ich muss zurück in Kloths Büro… ich muss irgendwelche Anhaltspunkte übersehen haben."
            scene hall
            "Atropos"  "Aber was?"
            scene kloth_office
            "Atropos"  "Natürlich…"

            "Atropos"  "Das Dokument auf seinem Tisch…"
            # Spieler wird Dokument gezeigt
            "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

            "Atropos"  "Das erklärt alles. Ich muss in den Serverraum. Sofort."
            jump serverraumpille

        else:

            "Atropos"  "Ich muss zurück in Kloths Büro… ich muss irgendwelche Anhaltspunkte übersehen haben."
            scene hall
            "Atropos"  "Aber was?"
            scene kloth_office
            "Atropos"  "Natürlich…"
            "Atropos"  "Der PC… Wie konnte ich nur vergessen auf diesem nachzuschauen?"
            # Spieler wird PC ohne Passwort-Kennung angezeigt
            "Blog über Bombenleger, der Aither vernichten will."

            "Atropos"  "Eine Bombe?"

            "Atropos"  "Was hat das zu bedeuten? War es das, was Kloth erreichen wollte? Wollte er Aither in die Luft jagen?"

            "Atropos"  "Aber wo kann sie versteckt sein?"

            "Atropos"  "Es muss noch andere Hinweise geben…"

            "Atropos"  "Was ist mit diesem Dokument? Enthält das irgendwelche Informationen?"

            # Spieler wird Dokument gezeigt
            "Strukturen von Aither (interkontinental), Wichtigkeit des Servers"

            "Atropos"  "Das erklärt alles. Ich muss in den Serverraum. Sofort."
            jump serverraumpille

label serverraumpille:
    scene hall
    "Atropos"  "Ich muss mich beeilen. Ich weiß nicht, wie viel Zeit mir noch bleibt."

    # Symbiont
    "{i}Was willst du tun, wenn du dort bist? Welche Entscheidung wirst du treffen? Wirst du mit dieser Entscheidung glücklich sein? {i}"
    scene server_room
    "Atropos"  "Ein Ticken… Es ist also tatsächlich wahr. Hier ist eine Bombe versteckt, welche jeden Moment hochgehen kann."

    # Symbiont
    "{i}Was wirst du tun? Wirst du glücklich sein? {i}"

    "Atropos"  "Die Bombe. Sie wird explodieren und ich werde sie nicht daran hindern. Ich werde Aither zerstören. Dieses erzwungene Glück ist kein Glück."

    "Atropos"  "Ich will lieber das größte Leid ertragen als weiterhin in dieser Scheinwelt leben zu müssen."

    # Symbiont
    "{i}Was ist mit all den Menschen im Gebäude? Wirst du sie retten? Sie sind unschuldig und wissen von nichts. Wenn du dich selbst als Opfer betrachtest. Sind sie dann nicht Opfer genau wie du? {i}"


    menu:
        "Wenn ich den Menschen helfe, rette ich damit vielleicht auch Anan. Das kann ich nicht zulassen.":
            jump menschennichthelfen
        "Ich muss den Menschen helfen. Sie können nichts dafür.":
            jump menschenhelfen

label menschennichthelfen:
    "Atropos"  "Wenn ich den Menschen helfe, rette ich damit vielleicht auch Anan. Das kann ich nicht zulassen."

    "Atropos"  "Anan ist überhaupt erst schuld für die gesamte Lage, in der wir uns gerade befinden."

    "Atropos"  "Er hat Kloth umgebracht und uns unser scheinbares Glück aufgezwungen."

    "Atropos"  "Ich darf nicht zulassen, dass er sein Werk weiterführen kann."

    "Atropos"  "Mit seinem Wissen könnte Aither mit Leichtigkeit wiederaufgebaut werden."

    "Atropos"  "Das darf ich nicht zulassen."

    # Symbiont
    "{i}Noch 10 Minuten. {i}"

    "Atropos"  "Ich bin bereit für alles, was kommen wird."

    "Atropos"  "Ich bin bereit die Verantwortung zu tragen."

    "Atropos"  "Chesis… Era… Tycho… ihr alle… es tut mir leid."

    "Atropos"  "Aber es gibt keine andere Wahl… manchmal müssen Opfer gebracht werden, damit die Welt zu einem besseren Ort wird."

    "Atropos"  "Bereinigt von den Menschen, die sie verseuchen. Ich muss dem Treiben von Anan und seinem Triumvirat endlich ein Ende setzen!"

    "Atropos"  "Ich werde Kloths Werk vollenden!"

    "Atropos"  "…"

    "Atropos"  "…"

    "Atropos"  "Koth… ich wünschte du wärst jetzt an meiner Seite…"

    "Atropos"  "Ich wünschte du wärst in dem Wissen gestorben, tatsächlich etwas erreicht zu haben."

    "Atropos"  "Ich hoffe du kannst den Triumph noch von irgendwo anders auskosten."

    # Symbiont
    "{i}10 Sekunden. {i}"

    "Atropos"  "Jetzt ist also alles vorbei, was?"

    # Symbiont
    "{i}9 Sekunden. {i}"

    "Atropos"  "Die 10 Minuten gingen schneller um als ich dachte… ich wünschte, ich hätte etwas mehr Zeit, um mich gedanklich von allen zu verabschieden."

    # Symbiont
    "{i}8 Sekunden. Bereust du deine Entscheidung? Oder bist du glücklich?{i}"

    "Atropos"  "Ich bin glücklich."

    # Symbiont
    "{i}7 Sekunden. {i}"

    "Atropos"  "Denke ich."

    # Symbiont
    "{i}6 Sekunden. {i}"

    "Atropos"  "Vielleicht hätte ich doch alle warnen sollen."

    # Symbiont
    "{i}5 Sekunden. {i}"

    "Atropos"  "Ob sie mir wohl jemals verzeihen werden?"

    # Symbiont
    "{i}4 Sekunden. Ja, das werden sie. Du hast es für das Wohl der gesamten Menschheit getan.{i}"

    "Atropos"  "Danke."

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return
label menschenhelfen:

    "Atropos"  "Ich muss den Menschen helfen. Sie können nichts dafür."

    "Atropos"  "Selbst wenn sich Anan dadurch retten kann… ich könnte es nicht mit meinem Gewissen vereinbaren alle deswegen sterben zu lassen."

    "Atropos"  "Und die Vernichtung dieser Filiale sowie der Server wird uns wenigstens etwas Zeit verschaffen."

    "Atropos"  "Selbst wenn sich Anan dadurch retten kann… ich könnte es nicht mit meinem Gewissen vereinbaren alle deswegen sterben zu lassen."

    "Atropos"  "Zeit, in der auch andere Menschen erkennen können, was wahres Glück bedeutet."

    # Symbiont
    "{i}Was bedeutet für dich wahres Glück? {i}"

    "Atropos"  "Die Möglichkeit selbst zu entscheiden wie ich in bestimmten Momenten fühlen möchte. Es sollte allein meine Entscheidung sein."

    # Symbiont
    "{i}Und so bist du wahrhaft glücklich? {i}"

    scene hall

    # Atropos Gedanken
    "Es sollte ausreichen, wenn ich den Handfeuermelder betätige. Das sollte zumindest den meisten Menschen die Chance geben zu entkommen. Mehr kann ich nicht tun."

    # Symbiont
    "{i}Atropos. Kannst du wirklich damit leben, dass Menschen deswegen sterben oder verletzt werden? {i}"

    # Atropos Gedanken
    "Ich denke das ist es wert."

    # Atropos Gedanken
    "Der Alarm ist ganz schön laut und all diese aufgeregten Stimmen, welche durcheinanderrufen."

    show ireia normal:
        xalign 0.25
    show armene normal:
        xalign 0.75

    "Ireia" "Atropos, was ist los? Ist Aither in Gefahr?"

    "Atropos"  "Ich weiß es nicht, der Alarm ging mit einem Mal los. Aber ihr solltet besser bald das Gebäude verlassen."

    "Armene" "Ich will nicht, dass Aither etwas passiert. Wie soll ich denn sonst glücklich sein?"

    "Armene" "Die Firma ist alles, was ich im Leben noch habe. Ich bin glücklich- ich will nicht, dass sich etwas ändert."

    "Atropos"  "Aber erkennt ihr es denn nicht? Wollt ihr wirklich auf diese Art und Weise glücklich sein? Euch ist jede andere Emotion genommen. Jede andere Option zu empfinden."

    "Ireia" "Ich will einfach nur glücklich sein. Ich möchte nicht, dass sich so etwas wie der 50-jährige Krieg wiederholt. Meine Eltern hatten mir von dieser Zeit erzählt…"

    "Ireia" "Da ist das hier doch nur ein kleiner Preis, nicht wahr? Ich bin glücklich so wie ich bin."

    "Ireia" "Na los, Armene. Lass uns weiterarbeiten."

    "Ireia" "Ein Brand wird uns doch nicht einfach aufhalten. Der wird sicher bald gelöscht werden und wir haben nachher noch ein Meeting."

    "Armene" "Natürlich Ireia. Man sieht sich später, Atropos!"

    "Atropos"  "Nein, geht nicht! Verlasst das Gebäude!"

    hide ireia
    hide armene

    "Atropos"  "Verlasst das Gebäude! Es brennt!"

    "Atropos"  "Wieso arbeitet ihr denn alle weiter als wäre nichts?"

    "Atropos"  "Verlasst das Gebäude… bitte…"

    # Symbiont
    "{i}Rette sie. Du könntest mit ihrem Tod nicht leben. {i}"

    "Atropos"  "Verdammt… ich darf nicht zu spät kommen… der Serverraum… ich muss zurück und die Bombe aufhalten!"

    scene server_room

    # Symbiont
    "{i}4 Sekunden. Atropos, bist du glücklich? {i}"

    "Atropos"  "Was soll die Frage? Nein… nein, das wollte ich nicht…"

    # Symbiont
    "{i}Es tut mir leid. {i}"

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")
    return

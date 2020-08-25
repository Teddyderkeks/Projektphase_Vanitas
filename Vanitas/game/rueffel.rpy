label rueffel:
    $ ruffel= True
    if loudspeaker:
        # Atropos Gedanken
        symb"Da ist Anans Büro… ich habe absolut keine Lust reinzugehen."

        # Atropos Gedanken
        symb"Der Ärger wird vermutlich noch größer ausfallen, weil ich nicht früher aufgetaucht bin, aber ich habe keine Lust auf seine Belehrungen."

        # Atropos Gedanken
        symb"Ich werde nicht klopfen, sondern einfach eintreten. Jetzt ist ohnehin alles zu spät und Anan soll mein Missfallen zu spüren bekommen."

    play music "Sound/Music/Rooms/AnansBuero/anan_buero_3St_ganz.mp3" fadeout 3 fadein 3
    scene anan_office
    with fadeshort
    show anan normal_mid

    "Anan" "Nimm Platz."

    "Atropos"  "…"

    # Atropos Gedanken
    symb"Er spricht gar nicht an, dass ich zu spät und einfach in sein Zimmer hineingeplatzt bin?"

    # Atropos Gedanken
    symb"Und warum sagt er nichts? Das macht mich nervös… soll ich etwa anfangen? Erwartet Anan eine Entschuldigung von mir?"

    menu:
        "Es tut mir leid.":
            jump imsorry

        "Ich werde mich nicht entschuldigen!":
            jump imnotsorry

    label imsorry:

        "Atropos"  "…"

        "Atropos"  "Es tut mir leid..."

        "Anan" "Es tut dir also leid."
        jump afterimsorry

    label imnotsorry:

        # Atropos Gedanken
        symb"Das kann er aber so was von vergessen. Es ist schon schlimm genug, dass ich seiner Aufforderung überhaupt gefolgt bin. Aber ich werde mich auf keinen Fall entschuldigen."

        # Atropos Gedanken
        symb"Niemals!"

        # Symbiont
        symb"{i}Entschuldige dich, egal aus welchem Grund. Willst du etwa noch mehr Ärger bekommen? {i}"

        # Symbiont
        symb"{i}Sowohl Anan als auch du werdet glücklicher sein, wenn du dich entschuldigst. Mehr als das will er nicht hören. Einfach nur eine Entschuldigung für dein Verhalten. {i}"

        # Symbiont
        symb"{i}Tu es! {i}"

        # Atropos Gedanken
        symb"Ich werde weiterhin schweigen…"

        # Atropos Gedanken
        symb"Aber warum sagt Anan nichts? Das macht mir langsam Angst…"

        # Atropos Gedanken
        symb"Wartet er wirklich bis ich mich entschuldige?"

        "Atropos"  "Ich werde mich nicht entschuldigen, dass ich die Pille nicht genommen habe."
        jump afterimsorry

    label afterimsorry:

        show anan strict_mid

        "Anan" "Ich bin mir noch nicht so sicher, ob du begreifst, was du für einen Schaden angerichtet hast. Sowohl bei dir selbst als auch bei deinen Mitmenschen."

        "Atropos"  "Schaden? Aber…"

        "Anan" "Ja, schaden. Wenn du unglücklich bist, wirst du dadurch auch andere unglücklich machen. Du wirst sie aus ihrem glücklichen Leben herausreißen und ins Unglück stürzen."

        "Anan" "Verstehst du das, Atropos?"

        "Atropos"  "Ich…"

        show anan normal_mid

        "Anan" "Ich bin nicht dein Feind. Und auch Happiness ist es nicht. Wir wollen alle nur ein einziges Ziel: Dass alle Menschen glücklich sind."

        "Anan" "Dass alle Menschen eine Vergangenheit, eine Gegenwart, eine Zukunft haben können, die glücklich ist. Die sie erfüllt und die sorglos ist."

        show anan disappointed_mid

        "Anan" "Der Krieg war eine düstere Zeit voller Leid und Elend. Du kannst es dir nicht vorstellen und darüber solltest du froh sein."

        "Anan" "Du solltest dankbar sein für das Leben, das wir dir geschenkt haben."

        show anan normal_mid

        "Anan" "Du solltest dein Leben genießen und glücklich sein."

        "Anan" "Die Welt ist zerstört, es gibt nur noch Astoa, Peria und Keposa. Was denkst du würde passieren, wenn die Menschen alle aufhören würden Happiness zu nehmen?"

        "Anan" "Denkst du, das würde ein gutes Ende nehmen? In einer Welt, die immer noch aus den Fugen geraten ist?"

        "Anan" "Die Menschen verdienen es, glücklich zu sein und sie brauchen das Glück, um friedlich leben zu können."

        "Anan" "Nimm Happiness, Atropos, und werde wieder glücklich! Nicht nur für deine eigene Glücklichkeit, sondern für die aller Menschen."

        "Atropos"  "Ich…"

        show screen force_mouse_move_twooptions

        menu:
            "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen.":
                $ ruffleunderstanding = True
                hide screen force_mouse_move_twooptions
                play music "Sound/Music/Rooms/AnansBuero/anans_buero_normal.mp3" fadeout 3 fadein 3

                "Atropos"  "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen. Es war ein Fehler."

                "Atropos"  "Ein Fehler, den ich nicht mehr wiederholen werde. Es tut mir aufrichtig leid. Wirklich."

                "Atropos"  "Ich will glücklich sein und wenn Happiness der einzige Weg dorthin ist, dann werde ich diesem Weg folgen."

                show anan strict_mid

                "Anan" "Happiness ist der einzige Weg. Wir haben viele andere Wege versucht, aber keiner hatte den Erfolg gebracht, welchen wir uns erhofft hatten."

                "Anan" "Das Glück aller Menschen steht an oberster Stelle und nur auf diese Weise können wir das Glück erreichen."

                "Anan" "Willst du glücklich sein?"

                "Atropos"  "Ja."

                "Anan" "Wirst du zukünftig stets zuerst an dein eigenes Glück und das Glück aller denken?"

                "Atropos"  "Ja."

                show anan normal_mid

                "Anan" "Du darfst zurück ins Labor. Nimm die Pille sofort, wenn du dort bist und vergiss sie zukünftig nicht mehr."

                "Atropos"  "Werde ich nicht. Und danke Anan."

                "Anan" "Sei einfach nur glücklich. Mehr will ich nicht. Du hast es verdient, glücklich zu sein, du leistet wertvolle Arbeit für die Gesellschaft."

                show anan happy_mid

                "Anan" "Jemand, der Menschen ihr Glück bringt, sollte selbst nicht unglücklich sein."

                "Atropos"  "Du hast recht. Es tut mir leid."

                scene hall
                with fadeshort

                jump back_to_work
            "Ich soll mich also für alle Menschen aufopfern? Was soll das denn bitte? Ich will selbst über mein Glück bestimmen können!":
                $ ruffleangry = True
                play music "Sound/Music/Rooms/AnansBuero/anan_buero_4St_ganz.mp3" fadeout 3 fadein 3
                hide screen force_mouse_move_twooptions
                jump ichsollmichopfern


label ichsollmichopfern:
    "Atropos" "Ich soll mich also für alle Menschen aufopfern? Was soll das denn bitte? Ich will selbst über mein Glück bestimmen können!"

    "Atropos"  "Das ist doch nicht fair. Ich habe keine Lust mehr darauf. Wieso wird uns nie irgendetwas erklärt?"

    "Atropos"  "Wenn wir wenigstens wüssten, was die Pille eigentlich überhaupt mit uns anstellt, aber nicht mal das wird uns gesagt."

    "Atropos"  "Das ist… das ist… ich will nicht mehr… ich werde diese verdammte Pille nicht mehr nehmen. Ich will auf meine eigene Art und Weise glücklich sein!"

    show anan strict_mid

    "Anan" "Das ist also deine Antwort? Das ist die Antwort, zu der du gekommen bist?"

    "Atropos"  "Ja! Du kannst mich nicht dazu zwingen, Happiness zu nehmen! Ich kann mich einfach weigern!"

    show anan disappointed_mid

    "Anan" "Ich bin enttäuscht von dir Atropos. Ich habe mehr von dir erwartet."

    "Anan" "Ich dachte, dass du verstehen würdest, wie wichtig das Glück für die Menschen ist und dass du voll und ganz hinter Aither stehen würdest."

    "Anan" "Aber das scheint nicht der Fall zu sein. Was soll ich jetzt nur mit dir anstellen?"

    "Anan" "Kann man noch vernünftig mit dir reden und dich überzeugen? Oder gehörst du bereits zu den verlorenen Seelen?"

    "Atropos"  "Verlorene Seelen? Sprichst du von denen, die sich gegen Happiness wehren und die Pille verweigern?"

    show anan strict_mid

    "Anan" "Sie schaden mit ihrem Verhalten der gesamten Menschheit und bedrohen unsere Existenz. Verlorene Seelen scheint da doch ein passendes Wort zu sein, nicht wahr?"

    "Anan" "Sie sind verloren, aber sie können gerettet werden. Wir können sie finden und ihnen die Wahrheit und Erkenntnis zurückbringen."

    show anan normal_mid

    "Anan" "Und genauso können wir auch dir helfen Atropos. Alle verlorenen Seelen sind Teil der Menschheit und auch ihr Glück ist wichtig, egal wie egoistisch sie auch gehandelt haben mögen."

    "Anan" "Egal wie unwichtig ihnen das Glück der Menschheit auch ist. Wir können sie läutern und dafür sorgen, dass eines Tages alle Menschen wahrhaftes Glück empfinden können."

    jump expulsion_office

label expulsion_office:

    "Atropos"  "Wahrhaftes Glück? Das ist alles vollkommen absurd. Hörst du dich eigentlich selbst reden?"

    show anan strict_mid

    "Anan" "Wenn du dich weiterhin dagegen weigerst Happiness zu nehmen, bleibt mir keine andere Wahl als dir die Kündigung zu reichen."

    "Anan" "Du verstehst, dass niemand Menschen Happiness bringen kann, der selbst nicht glücklich ist."

    show anan normal_mid

    "Anan" "Ich biete dir eine letzte Chance. Nimm jetzt die Pille und werde glücklich. Kehre in dein altes Leben zurück. Sonst müssen wir ein anderes Leben für dich finden, das dich glücklich macht."

    "Atropos"  "Vergiss es. Ich werde die Pille nicht nehmen! Ich bin auch ohne glücklich und ich werde mir nicht vorschreiben lassen, wie ich mein Leben zu leben habe!"

    "Anan" "Es ist deine freie Entscheidung. War es schon immer. Du kannst selbst wählen, ob du Happiness einnehmen möchtest, aber du musst auch die Konsequenzen dafür tragen."

    "Atropos"  "Besser Konsequenzen als weiterhin zu etwas gezwungen zu werden, das ich nicht möchte!"

    hide anan
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Wer denkt er eigentlich, wer er ist?"

    # Atropos Gedanken
    symb"Nur weil er mitunter den Krieg beendet hat, kann er doch nicht jedem Menschen vorschreiben, wie dieser zu leben und glücklich zu leben hat!"

    # Atropos Gedanken
    symb"Es war die richtige Entscheidung die Firma zu verlassen! Ich stehe einfach nicht mehr hinter dieser und kann nicht so weiterarbeiten."

    "Chesis"  "Atropos?"

    "Chesis"  "Atropos? Hallo?"

    show chesis normal

    "Atropos"  "Oh… tut mir leid, ich war in Gedanken versunken."

    show chesis happy

    "Chesis"  "Kein Problem. Kamst du aus Anans Büro?"

    "Atropos"  "Ja, ich verlasse die Firma."

    show chesis confused

    "Chesis"  "Du verlässt die Firma?"

    "Atropos"  "Genauer gesagt verlasse ich nicht die Firma, ich wurde gefeuert… Anan ist… grauenhaft. Wie können die Menschen ihn nur so vergöttern?"

    "Atropos"  "Er schwingt große Reden, aber letztlich steckt nichts dahinter."

    "Chesis"  "Gefeuert?"

    "Atropos"  "Ach, ich hatte die Pille nicht genommen und das war Anan aufgefallen. Nachdem ich mich weigerte sie weiterhin zu nehmen, meinte er, dass ich die Firma verlassen muss."

    "Atropos"  "Aber ich will auch nicht länger hierbleiben. Ich will die Pille nicht weiter auf Zwang nehmen müssen und ich will auch nicht dafür arbeiten, andere Menschen dazu zu zwingen."

    show chesis angry

    "Chesis"  "Aber warum nimmst du denn Happiness nicht? Willst du denn nicht glücklich sein?"

    "Atropos"  "Ich will glücklich sein, aber ich will nicht zu diesem Glück gezwungen werden! Verstehst du das nicht?"

    "Chesis"  "Nein… nicht wirklich. Nimm Happiness. Du hast heute nur einen schlechten Tag."

    "Chesis"  "Am Ende wirst du es bereuen."

    "Atropos"  "Wieso bist du auf Anans Seite? Schalte doch mal deinen Kopf ein! Bist das wirklich du, der da gerade spricht? Oder sind deine Worte durch die Tablette beeinflusst?"

    show chesis normal

    "Chesis"  "Ich bin immer ich und darin ändert Happiness nichts."

    "Atropos"  "Nein- du bist nicht mehr du. Wir reden, wenn du wieder bei klarem Verstand bist."
    play music "Sound/Music/Rooms/Labor/labor_duester.mp3" fadeout 3 fadein 3
    hide chesis
    scene lab
    with fadeshort
    show narcais normal
    "Narcais"  "Atropos, wo warst du? Ich brauche noch dein Feedback…"

    "Atropos"  "Das muss dir jemand anderer geben. Ich höre auf. Ich packe heute nur noch meine Sachen zusammen und räume meinen Arbeitsplatz auf."

    show narcais confused

    "Narcais"  "Du verlässt uns? Welchen Grund könnte es dafür geben?"

    "Atropos"  "Viele Gründe und sie spielen für dich keine Rolle."

    show narcais normal

    "Narcais"  "Ich wünsche dir Glücklichkeit für deinen weiteren Weg. Kannst du bei Anan ein gutes Wort für mich einlegen, damit ich deinen Posten übernehmen kann?"

    show narcais cocky

    "Narcais"  "Ich wäre vermutlich ohnehin besser geeignet."

    "Atropos"  "Mal sehen."

    show narcais normal

    "Narcais"  "Danke! Also dann, ich muss weiterarbeiten."

    "Narcais"  "Die Arbeit erledigt sich nicht von alleine und im Gegensatz zu gewissen anderen Personen habe ich einen Stapel an Proben, die zu analysieren sind."

    hide narcais

    # Atropos Gedanken
    symb"Dann packe ich mal meine Sachen zusammen… ist nicht bald ohnehin Zeit für die Mittagspause? Dann kann ich mich nochmal von meinen Freunden verabschieden."

    scene lab
    with fadestart

    "Atropos"  "…"

    "Durchsage"  "Atropos Laiotas. Dein Glück erwartet dich. Dein weiterer Weg liegt vor dir. Komm bitte für ein Abschlussgespräch in Anans Büro."

    "Atropos"  "Also, mach’s gut, Narcais. Viel Erfolg weiterhin."

    show narcais normal

    "Narcais"  "Keine Sorge, ich werde es noch besser machen. Pass auf dich auf!"

    "Atropos"  "Danke! Sag mal, hast du Era gesehen? Ich würde mich gerne von ihr verabschieden."

    show narcais confused

    "Narcais"  "Sie ist auf die Toilette gegangen, sollte aber in kürzester Zeit wieder hier sein."

    "Atropos"  "Vielleicht begegne ich ihr ja auf dem Flur. Also, bis bald."

    hide narcais
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Era ist nicht zu sehen. Na gut, dann eben ohne sie… auf zu Anans Büro."

    show era normal
    "Era"  "A-Atropos? Wo- Wohin gehst du? Und warum hast du deine Tasche dabei? Machst du Mittagspause?"

    "Atropos"  "Oh hey… ich bin auf dem Weg zu Anan. Ich wechsle meinen Job. Es gab ein paar Schwierigkeiten, die sich nicht lösen ließen."

    show era confused

    "Era"  "Oh… okay… das… das ist wirklich schade."

    if datewithera:
        "Atropos"  "Aber keine Sorge, das Date steht natürlich trotzdem noch. Wenn du möchtest, zumindest…"

        show era happy

        "Era"  "Das… das wäre wirklich schön."

        "Atropos"  "Dann ist es abgemacht, wir sehen uns am Donnerstag. Noch einen wunderschönen Tag."
    else:
        "Atropos"  "Aber wir können ja trotzdem weiterhin den Kontakt halten. Ich bin ja nicht aus der Welt."

        show era shy

        "Era"  "Das… das wäre wirklich schön."

        "Atropos"  "Also, wir hören bald voneinander. Noch einen wunderschönen Tag."


    $ renpy.movie_cutscene("cutscene_intro.mpg")

    jump ending

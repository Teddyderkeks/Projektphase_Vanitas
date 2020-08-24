default infos_count_anan = 0
default infos_count_kloth = 0
default thingswatched=0
default read_letter_anan = False
default read_document_anan = False
default read_computer_anan = False
default face_anan_in_office = False
default bomb_trigger_choice = False
default last_try_find_kloth = False
default rage_atropos_bomb = False
default straight_anan_office = False

label office:
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Immerhin ist Anans Büro nicht so weit entfernt."

    if badmood:

        # Atropos Gedanken
        symb"Ich habe echt keine Lust zu gehen, aber was will man machen…"

        # Atropos Gedanken
        symb"Ich hoffe nur, Anan hält seine Ansprache kurz und es hat keine weiteren Konsequenzen für mich. Das könnte ich echt nicht gebrauchen."
    else:

        # Atropos Gedanken
        symb"Ich hoffe nur, er hält seine Ansprache kurz und es hat keine weiteren Konsequenzen für mich."

        # Atropos Gedanken
        symb"Das ist das Letzte, das ich möchte. Ich habe immer wieder mitbekommen, dass Menschen, die keine Pille genommen haben, bestimmte Privilegien genommen werden."

        # Atropos Gedanken
        symb"Einfach aus dem Grund, dass ihr Verhalten rücksichtlos anderen Menschen gegenüber ist, die einfach nur glücklich sein wollen."

        # Atropos Gedanken
        symb"Ob da wohl etwas Wahres dran ist?"

    # Atropos Gedanken
    symb"Da ist das Büro. Mal sehen, ob Anan da ist. Ich klopfe besser an."

    # Atropos Gedanken
    symb"Seltsam, keine Antwort… ob ich wohl einfach eintreten sollte?"

    # Atropos Gedanken
    symb"Immerhin hatte Anan gesagt, dass ich um diese Uhrzeit hier sein soll."

    # Atropos Gedanken
    symb"Vielleicht hat er das Klopfen ja nicht gehört?"

    # Atropos Gedanken
    symb"Hmm…"

    if okaymood== False:
        symb"Wenn er nicht im Büro ist, könnte ich die Chance nutzen, mich dort mal umzusehen. Vielleicht finde ich ja irgendetwas heraus?"

    # Atropos Gedanken
    symb"Was soll ich tun?"

    # Symbiont
    symb"{i}Lass es besser bleiben, Atropos. Warte auf Anan! Du möchtest nicht noch mehr Ärger bekommen. Du willst doch glücklich sein. Ärger bringt kein Glück.{i}"

    # Symbiont
    symb"{i}Verhalte dich richtig. {i}"

    # Symbiont
    symb"{i}Triff die richtige Entscheidung.{i}"
    show screen force_mouse_move_twooptionsdownweak
    menu:
        "Ich trete einfach mal ein und sehe dann weiter.":
            hide screen force_mouse_move_twooptionsdownweak
            # Atropos Gedanken
            symb"Ich trete einfach mal ein und sehe dann weiter. Es wird schon nichts Schlimmes deswegen passieren."
            scene anan_office
            with fadeshort

            # Atropos Gedanken
            symb"Der Raum ist tatsächlich leer. Anan schafft es also nicht mal, pünktlich zu seinem eigenen Termin zu erscheinen."

            # Atropos Gedanken
            symb"Was soll ich jetzt tun? Soll ich es riskieren? Soll ich die Chance nutzen, um mich mal etwas in Anans Büro umzusehen, wenn ich schon hier bin?"

            # Atropos Gedanken
            symb"Vielleicht finde ich ja irgendetwas interessantes raus."

            # Symbiont
            symb"{i}Kehre sofort um und verlasse Anans Büro. Worauf wartest du noch? Das ist die dümmste Entscheidung, die du treffen könntest. Sie würde dich am Ende nur unglücklich machen. {i}"

            # Symbiont
            symb"{i}Was, wenn Anan zurückkehrt und dich dabei erwischt, dass du in seinem Büro bist? Denkst du, dann würde er es bei einer Mahnung belassen? Du gefährdest damit alles, aber vor allem dein Glück. {i}"

            # Symbiont
            symb"{i}Geh aus dem Zimmer raus und tu so, als hättest du es niemals betreten. Sofort. {i}"


            $ straight_anan_office = True
            jump selection_anan_office
        "Ich sollte besser vor der Tür auf Anan warten.":
            hide screen force_mouse_move_twooptionsdownweak

            # Atropos Gedanken
            symb"Ich sollte besser vor der Tür auf Anan warten. Ich gehe lieber kein Risiko ein."

            # Atropos Gedanken
            symb"Ich will nicht noch mehr Ärger bekommen als ohnehin schon."

            jump conversation_with_anan

label conversation_with_anan:
    scene hall
    with fadeshort

    show anan normal_mid

    "Anan" "Atropos Laiotas. Ich lobe deine Pünktlichkeit. Folge mir!"

    # Atropos Gedanken
    symb"Ich kann nicht einschätzen, ob Anan gute oder schlechte Laune hat. Ich hoffe einfach nur, ich bekomme nicht zu viel Ärger."

    scene anan_office
    with fadeshort
    show anan normal_mid

    "Anan" "Nimm bitte Platz."

    "Atropos"  "Danke…"

    "Atropos"  "…"

    # Atropos Gedanken
    symb"Wieso sagt er denn nichts?"

    # Atropos Gedanken
    symb"Das macht mich nervös… soll ich etwa anfangen? Erwartet Anan eine Entschuldigung von mir?"

    if badmood:
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

    # alle

    "Atropos"  "Anan… es tut mir leid…"

    show anan disappointed_mid

    "Anan" "Es tut dir also leid."

    "Anan" "Ich bin mir noch nicht so sicher, ob du begreifst, was du für einen Schaden angerichtet hast. Sowohl bei dir selbst als auch bei deinen Mitmenschen."

    "Atropos"  "Schaden? Aber…"

    show anan strict_mid

    "Anan" "Ja, Schaden. Wenn du unglücklich bist, wirst du dadurch auch andere unglücklich machen. Du wirst sie aus ihrem glücklichen Leben herausreißen und ins Unglück stürzen."

    "Anan" "Verstehst du das, Atropos?"

    "Atropos"  "Ich…"

    show anan happy_mid

    "Anan" "Ich bin nicht dein Feind. Und auch Happiness ist es nicht. Wir wollen alle nur ein einziges Ziel: Dass alle Menschen glücklich sind."

    "Anan" "Dass alle Menschen eine Vergangenheit, eine Gegenwart, eine Zukunft haben können, die glücklich ist. Die sie erfüllt und die sorglos ist."

    show anan disappointed_mid

    "Anan" "Der Krieg war eine düstere Zeit voller Leid und Elend. Du kannst es dir nicht vorstellen und darüber solltest du froh sein."

    "Anan" "Du solltest dankbar sein für das Leben, das wir dir geschenkt haben."

    "Anan" "Du solltest dein Leben genießen und glücklich sein."

    "Anan" "Die Welt ist zerstört, es gibt nur noch Astoa, Peria und Keposa. Was denkst du würde passieren, wenn die Menschen alle aufhören würden Happiness zu nehmen?"

    "Anan" "Denkst du, das würde ein gutes Ende nehmen? In einer Welt, die immer noch aus den Fugen geraten ist?"

    show anan happy_mid

    "Anan" "Die Menschen verdienen es, glücklich zu sein und sie brauchen das Glück, um friedlich leben zu können."

    "Anan" "Nimm Happiness, Atropos, und werde wieder glücklich! Nicht nur für deine eigene Glücklichkeit, sondern für die aller Menschen."

    "Atropos"  "Ich…"


    menu:
        "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen.":
            jump understanding
        "Aber wirkt die Pille wirklich? Ich fühle mich auch ohne sie glücklich.":
            jump questioning
        "Ich soll mich also für alle Menschen aufopfern? Was soll das denn bitte? Ich will selbst über mein Glück bestimmen können!":
            "Atropos" "Ich soll mich also für alle Menschen aufopfern? Was soll das denn bitte? Ich will selbst über mein Glück bestimmen können!"

            "Atropos"  "Das ist doch nicht fair. Ich habe keine Lust mehr darauf. Wieso wird uns nie irgendetwas erklärt?"

            "Atropos"  "Wenn wir wenigstens wüssten, was die Pille eigentlich überhaupt mit uns anstellt, aber nicht mal das wird uns gesagt."

            "Atropos"  "Das ist… das ist… ich will nicht mehr… ich werde diese verdammte Pille nicht mehr nehmen. Ich will auf meine eigene Art und Weise glücklich sein!"

            show anan disappointed_mid

            "Anan" "Das ist also deine Antwort? Das ist die Antwort, zu der du gekommen bist?"

            "Atropos"  "Ja! Du kannst mich nicht dazu zwingen, Happiness zu nehmen! Ich kann mich einfach weigern!"

            "Anan" "Ich bin enttäuscht von dir Atropos. Ich habe mehr von dir erwartet."

            "Anan" "Ich dachte, dass du verstehen würdest, wie wichtig das Glück für die Menschen ist und dass du voll und ganz hinter Aither stehen würdest."

            "Anan" "Aber das scheint nicht der Fall zu sein. Was soll ich jetzt nur mit dir anstellen?"

            "Anan" "Kann man noch vernünftig mit dir reden und dich überzeugen? Oder gehörst du bereits zu den verlorenen Seelen?"

            "Atropos"  "Verlorene Seelen? Sprichst du von denen, die sich gegen Happiness wehren und die Pille verweigern?"

            show anan normal_mid

            "Anan" "Sie schaden mit ihrem Verhalten der gesamten Menschheit und bedrohen unsere Existenz. Verlorene Seelen scheint da doch ein passendes Wort zu sein, nicht wahr?"

            "Anan" "Sie sind verloren, aber sie können gerettet werden. Wir können sie finden und ihnen die Wahrheit und Erkenntnis zurückbringen."

            "Anan" "Und genauso können wir auch dir helfen Atropos. Alle verlorenen Seelen sind Teil der Menschheit und auch ihr Glück ist wichtig, egal wie egoistisch sie auch gehandelt haben mögen."

            "Anan" "Egal wie unwichtig ihnen das Glück der Menschheit auch ist. Wir können sie läutern und dafür sorgen, dass eines Tages alle Menschen wahrhaftes Glück empfinden können."

            jump expulsion_office

label understanding:
    "Atropos"  "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen. Es war ein Fehler."

    "Atropos"  "Ein Fehler, den ich nicht mehr wiederholen werde. Es tut mir aufrichtig leid. Wirklich."

    "Atropos"  "Ich will glücklich sein und wenn Happiness der einzige Weg dorthin ist, dann werde ich diesem Weg folgen."

    show anan happy_mid

    "Anan" "Happiness ist der einzige Weg. Wir haben viele andere Wege versucht, aber keiner hatte den Erfolg gebracht, welchen wir uns erhofft hatten."

    "Anan" "Das Glück aller Menschen steht an oberster Stelle und nur auf diese Weise können wir das Glück erreichen."

    "Anan" "Willst du glücklich sein?"

    "Atropos"  "Ja."

    "Anan" "Wirst du zukünftig stets zuerst an dein eigenes Glück und das Glück aller denken?"

    "Atropos"  "Ja."

    "Anan" "Du darfst zurück ins Labor. Nimm die Pille sofort, wenn du dort bist und vergiss sie zukünftig nicht mehr."

    "Atropos"  "Werde ich nicht. Und danke Anan."

    "Anan" "Sei einfach nur glücklich. Mehr will ich nicht. Du hast es verdient, glücklich zu sein, du leistet wertvolle Arbeit für die Gesellschaft."

    "Anan" "Jemand, der Menschen ihr Glück bringt, sollte selbst nicht unglücklich sein."

    "Atropos"  "Du hast recht. Es tut mir leid."

    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Dann mal auf ins Labor, um die Pille zu nehmen."

    # Atropos Gedanken
    symb"Ich hoffe, es hat keine weiteren Auswirkungen, dass ich meine Pille nicht genommen hatte."

    # Atropos Gedanken
    symb"Aber jetzt sollte ich nicht weiter darüber nachdenken. Ich will einfach nur glücklich sein."

    # Symbiont
    symb"{i}Nimm Happiness und du kannst wieder glücklich werden. {i}"

    # Atropos Gedanken
    symb"Ja, das stimmt wohl."

    jump takepillnow

label understandingpart2:

    "Atropos"  "Nein… nein, möchte ich nicht. Du hast ja recht."

    "Atropos"  "Es tut mir leid."

    "Atropos"  "Ich sollte aufhören, so viele Fragen zu stellen."

    show anan normal_mid

    "Anan" "Fragen sind gut. Fragen sind sogar wichtig, denn ohne Fragen kann man nicht zu Antworten kommen."

    "Anan" "Aber es ist wichtig, welche Art von Fragen gestellt werden. Es gibt falsche und es gibt richtige Fragen."

    "Anan" "Es gibt die Art von Fragen, die eine Rolle spielen. Die sinnvoll sind, die zu Veränderungen führen können."

    show anan strict_mid

    "Anan" "Aber es gibt auch die Art von Fragen, die Unheil mit sich bringen. Fragen, die gefährlich sind. Fragen, auf die man besser keine Antwort bekommen möchte."

    "Anan" "Fragen, die dafür sorgen, dass falsche Vorstellungen im Kopf der Menschen gepflanzt werden."

    "Anan" "Und die Frage nach Happiness ist eine eben solche Frage."

    show anan normal_mid

    "Anan" "Kannst du es denn nicht einfach akzeptieren und glücklich zu sein? Ich trage das Gewicht der Wahrheit auf meinen Schultern. Es sollte nicht auch noch auf deinen lasten müssen."

    "Atropos"  "Wie viele Menschen kennen die Wahrheit?"

    "Anan" "Es gibt keine universelle Wahrheit. Nur verschiedene Varianten von Lügen und Halbwahrheiten."

    "Anan" "Letztlich weiß wohl niemand genau, was die Wahrheit dahinter ist."

    show anan strict_mid

    "Anan" "Deine Frage zielt wohl eher darauf ab, wie viele Menschen die Wirkung von Happiness verstehen können? Nimmst du die Pille, wenn ich dir eine Antwort auf diese Frage gebe?"

    "Anan" "Bist du dann glücklich und akzeptierst dein Glück?"

    # Atropos Gedanken
    symb"Ich will eigentlich noch mehr wissen, aber mehr Antworten werde ich vermutlich nicht bekommen."

    # Atropos Gedanken
    symb"Also sollte ich mich vermutlich mit dieser Antwort zufriedengeben… oder?"

    # Symbiont
    symb"{i}Ja, solltest du. Anan hat recht, manchmal ist es besser nicht die vollständige Wahrheit zu kennen.{i}"

    # Atropos Gedanken
    symb"Ich frage mich nur, warum Anan nicht sagen kann, wie die Pille wirkt? Was kann das nur für eine Art von Wissen sein, das so gefährlich ist? Ich kann mir beim besten Willen nichts vorstellen."

    # Symbiont
    symb"{i}Spielt es eine Rolle? Du bist glücklich und Happiness schenkt dir eben jene Glücklichkeit. Ist es nicht egal, welche Wirkstoffe nun dafür sorgen, dass du glücklich bist? {i}"

    # Atropos Gedanken
    symb"Manchmal habe ich einfach das Gefühl, dass mehr hinter allem steckt als nur irgendwelche Wirkstoffe."

    # Atropos Gedanken
    symb"Ich kenne nicht alle Wirkstoffe der Happiness-Pille, aber die, die ich kenne, sind nützlich für den Körper, aber sorgen nicht für Glücklichkeit."

    # Atropos Gedanken
    symb"Und wie wird diese Glücklichkeit überhaupt erreicht? Nach was unterscheidet die Pille, was jedes einzelne Individuum glücklich macht?"

    # Symbiont
    symb"{i}Musst du diese Antworten wirklich kennen, um glücklich zu sein, Atropos? {i}"

    # Atropos Gedanken
    symb"Vermutlich nicht, oder?"

    # Symbiont
    symb"{i}Du bist ehrlich zu dir selbst. Danke. {i}"

    # Symbiont
    symb"{i}Dann sei wieder glücklich. Vergiss alles, was dich unglücklich macht. Nimm Happiness und lebe dein Leben so weiter, wie du es bisher gelebt hast. Glücklich und zufrieden. {i}"

    "Atropos" "Ich bin glücklich und ich werde die Pille nehmen. Ich brauche dafür die Wahrheit nicht. Weder die vollständige noch wie viele über die Wahrheit Bescheid wissen."

    show anan happy_mid

    "Anan" "Ich danke dir."

    "Anan" "Ich danke dir für das Glück, das du den Menschen aufgrund deiner Entscheidung schenkst."

    "Anan" "Mach weiter so, Atropos."

    "Anan" "Kehre jetzt ins Labor zurück und nimm deine Pille. Lebe dein Leben glücklich weiter."

    "Anan" "Ich wünsche dir einen Tag voller Glücklichkeit."

    "Atropos" "Danke vielmals. Ich dir auch."

    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Dann mal auf ins Labor, um die Pille zu nehmen."

    # Atropos Gedanken
    symb"Ich hoffe, es hat keine weiteren Auswirkungen, dass ich meine Pille nicht genommen hatte."

    # Atropos Gedanken
    symb"Aber jetzt sollte ich nicht weiter darüber nachdenken. Ich will einfach nur glücklich sein."

    # Symbiont
    symb"{i}Nimm Happiness und du kannst wieder glücklich werden. {i}"

    # Atropos Gedanken
    symb"Ja, das stimmt wohl."

    jump takepillnow

label understandingpart3:
    "Atropos"  "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen. Es war ein Fehler gewesen."

    "Atropos"  "Ein Fehler, den ich nicht mehr wiederholen werde. Es tut mir aufrichtig leid. Wirklich."

    "Atropos"  "Ich will glücklich sein und wenn Happiness der einzige Weg dorthin ist, dann werde ich diesem Weg folgen."

    show anan strict_mid

    "Anan" "Happiness ist der einzige Weg. Wir haben viele andere Wege versucht, aber keiner hatte den Erfolg gebracht, welchen wir uns erhofft hatten."

    "Anan" "Das Glück aller Menschen steht an oberster Stelle und nur auf diese Weise können wir das Glück erreichen."

    show anan normal_mid

    "Anan" "Willst du glücklich sein?"

    "Atropos"  "Ja."

    "Anan" "Wirst du zukünftig stets zuerst an dein eigenes Glück und das Glück aller denken?"

    "Atropos"  "Ja."

    "Anan" "Du darfst zurück ins Labor. Nimm die Pille sofort, wenn du dort bist, und vergiss sie zukünftig nicht mehr."

    "Atropos"  "Werde ich nicht. Und danke, Anan."

    "Anan" "Sei einfach nur glücklich. Mehr will ich nicht. Du hast es verdient glücklich zu sein, du leistet wertvolle Arbeit für die Gesellschaft."

    show anan happy_mid

    "Anan" "Jemand, der Menschen ihr Glück bringt, sollte selbst nicht unglücklich sein."

    "Atropos"  "Du hast recht. Es tut mir leid."

    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Zum Glück habe ich mich nicht in Anans Büro umgesehen. Sonst wäre ich wohl nicht so glimpflich davongekommen."

    # Atropos Gedanken
    symb"Dann Mal auf ins Labor, um die Pille zu nehmen."

    # Atropos Gedanken
    symb"Ich hoffe, es hat keine weiteren Auswirkungen, dass ich meine Pille nicht genommen hatte."

    # Atropos Gedanken
    symb"Aber jetzt sollte ich nicht weiter darüber nachdenken. Ich will einfach nur glücklich sein."

    # Symbiont
    symb"{i}Nimm Happiness und du kannst wieder glücklich werden. {i}"

    # Atropos Gedanken
    symb"Ja, das stimmt wohl."

    jump takepillnow



label questioning:
    "Atropos"  "Aber wirkt die Pille wirklich? Ich fühle mich auch ohne sie glücklich."

    "Atropos"  "Ich habe in der letzten Zeit keinerlei Veränderungen bemerkt, obwohl ich sie nicht genommen habe."

    "Atropos"  "Ich denke, ich bin glücklich."

    show anan strict_mid

    "Anan" "Du {b}denkst{/b} also, dass du glücklich bist? Aber weißt du es auch? Bist du dir ganz sicher, dass du glücklich bist?"

    "Anan" "Bevor du mir diese Frage nicht mit einem überzeugten {b}Ja{/b} beantworten kannst, bist du nicht glücklich."

    # Atropos Gedanken
    symb"Kann ich ihm die Frage mit einem überzeugten Ja beantworten? Ich weiß es nicht…"

    # Atropos Gedanken
    symb"Was, wenn es doch immer noch die Wirkung meiner letzten Pille ist, warum ich mich glücklich fühle?"

    "Atropos"  "…"

    "Anan" "Dein Schweigen ist mir Antwort genug."

    "Anan" "Die Pille ist für dein Glück verantwortlich. Ohne Happiness kannst du nicht glücklich sein."

    show anan disappointed_mid

    "Anan" "Nicht dauerhaft."

    show anan normal_mid

    "Anan" "Es mag Momente geben, in denen du glücklich bist, so wie es vor Happiness der Fall war…"

    "Anan" "Aber letztlich werden dich Selbstzweifel, quälende Ängste, Unsicherheiten, Neid, Hass und Wut zerfressen, bis sie nichts mehr von dir übriglassen."

    "Anan" "Möchtest du das wirklich sein? Diese Art von Monster, welche sich selbst und anderen Menschen schadet?"


    menu:
        "Nein… nein, möchte ich nicht. Du hast ja Recht.":
            jump understandingpart2
        "Aber das erklärt immer noch nicht wie die Pille eigentlich wirkt.":
            jump misunderstanding

label misunderstanding:

    "Atropos" "Aber das erklärt immer noch nicht wie die Pille eigentlich wirkt."

    "Atropos" "Wie macht sie uns glücklich?  Wirkt sie wie eine Droge? Lässt sie uns unglückliche Sachen vergessen und verdrängen? Sind wir dadurch einfach… glücklich?"

    show anan normal_mid

    "Anan" "Wieso spielt es für dich eine Rolle auf welche Weise sie dich glücklich macht?"

    "Anan" "Was ändert es?"

    "Atropos" "Alles… einfach alles… ich will die Wahrheit wissen… ist das Glück gar kein Glück, sondern einfach nur erzwungen? Nicht mehr als ein Schein?"

    "Anan" "Das Glück ist echt. Wie kann es falsches Glück geben? Glück ist, wenn du in einem Moment wirklich glücklich bist. Wenn es keine Sorgen, Zweifel und Probleme mehr gibt."

    show anan happy_mid

    "Anan" "Glück ist die Erfüllung menschlichen Wünschens und Strebens. Der Weg dorthin spielt keine Rolle."

    "Atropos" "Aber bin ich wirklich glücklich? Was ist, wenn ich unglücklich mit dem Glück bin, welches mir die Pille bringt?"

    "Anan" "Glück ist das persönliche Glück jedes Menschen. Happiness sorgt dafür, dass du dieses persönliche Glück erreichst. Es ist unmöglich, dass du mit deinem Glück unglücklich bist."

    "Atropos" "Du bleibst die ganze Zeit so schwammig mit deinen Aussagen. Warum kann ich keine klaren Antworten bekommen?"

    show anan normal_mid

    "Anan" "Weil es keine eindeutigen Antworten gibt und niemals geben wird. Uns bleibt allen nichts anderes als zu glauben, dass wir das Richtige tun und auf dem richtigen Weg sind."

    "Anan" "Und genau das tue ich."

    show anan strict_mid

    "Anan" "(wirft einen raschen Blick auf sein Handy) Ich muss kurz weg."

    "Anan" "Dieses Gespräch ist noch nicht beendet. Wir setzen es fort, sobald ich zurück bin."

    hide anan

    # Atropos Gedanken
    symb"Das war… seltsam… Anan wirkt so überzeugt von dem, was er sagt, aber irgendwie…"

    # Atropos Gedanken
    symb"Ich weiß nicht…"

    # Atropos Gedanken
    symb"Ich würde zu gerne mehr erfahren, was Happiness bewirkt. Was es in unseren Körpern mit uns anstellt."

    # Atropos Gedanken
    symb"Ob ich wohl hier in Anans Büro mehr dazu erfahre? Ich bin allein und könnte die Chance nutzen."

    # Symbiont
    symb"{i}Du scheinst es ja fast schon anzustreben unglücklich zu sein. Willst du dein Glück nur für ein paar Informationen riskieren? {i}"

    # Symbiont
    symb"{i}Manche Wahrheiten bleiben besser für immer verborgen… und außerdem, willst du einen noch größeren Anschiss riskieren? {i}"

    # Symbiont
    symb"{i}Hast du nicht genug davon? Wenn du so weiter machst, wirst du ernsthafte Konsequenzen erwarten müssen… und das würde dich bestimmt unglücklich machen. {i}"

    # Symbiont
    symb"{i}Lass dir Zeit und überlege noch einmal in Ruhe, ob du das wirklich tun möchtest.{i}"

    # Atropos Gedanken
    symb"Darüber muss ich nicht noch länger nachdenken. Ich weiß, was ich will."

    # Symbiont
    symb"{i}Tu es nicht, Atropos. Lass es sein! Bleib auf diesem Stuhl sitzen und warte, bis Anan zurückkommt. Du wirst dadurch glücklicher sein.{i}"

    # Symbiont
    symb"{i}Riskiere es nicht. Riskiere dein Glück nicht. Was auch immer hier in Anans Büro ist, geht dich nichts an.{i}"

    # Atropos Gedanken
    symb"Was soll ich nur tun?"

    jump selection_anan_office

label how_many_infos_anan:

    if infos_count_anan == 0:
        if  straight_anan_office:

            if (sawsafe==True) or (sawpictures==True) or (sawbooks==True):
                # Atropos Gedanken
                symb"Ich sollte mich besser nicht weiter in Anans Büro umschauen und das Zimmer verlassen."
            else:

                # Atropos Gedanken
                symb"Ich sollte mich besser nicht in Anans Büro umschauen und das Zimmer verlassen."

            # Atropos Gedanken
            symb"Er könnte jeden Moment zurückkommen, und außerdem gehört es sich einfach nicht."

            # Symbiont
            symb"{i}Es war eine dumme Idee gewesen… {i}"

            # Atropos Gedanken
            symb"Es war eine dumme Idee, das Zimmer überhaupt zu betreten. Ich hätte einfach vor der Tür auf Anan warten sollen."

            # Atropos Gedanken
            symb"Ich hoffe nur, Anan bekommt davon am Ende nichts mit."

            # Symbiont
            symb"{i}Verlass das Zimmer und Anan wird nichts mitbekommen. Sei einfach glücklich, nimm die Pille und bringe alles wieder in Ordnung!{i}"

            scene hall
            with fadeshort

            # Atropos Gedanken
            symb"Zum Glück… Anan ist noch nicht zu sehen."

            scene hall
            with fadestart

            "Atropos" "…"

            show anan normal_mid

            "Anan" "Atropos Laiotas. Ich lobe deine Pünktlichkeit. Folge mir!"

            # Atropos Gedanken
            symb"Ich kann nicht einschätzen, ob Anan gute oder schlechte Laune hat. Ich hoffe einfach nur, ich bekomme nicht zu viel Ärger."

            # Atropos Gedanken
            symb"Immerhin hat er nicht mitbekommen, dass ich in seinem Büro war."

            scene anan_office
            with fadeshort
            show anan normal_mid

            "Anan" "Nimm bitte Platz."

            "Atropos"  "Danke…"

            "Atropos"  "…"

            # Atropos Gedanken
            symb"Wieso sagt er denn nichts?"

            # Atropos Gedanken
            symb"Das macht mich nervös… soll ich etwa anfangen? Erwartet Anan eine Entschuldigung von mir?"

            if badmood:

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

            # alle

            "Atropos"  "Anan… es tut mir leid…"

            show anan disappointed_mid

            "Anan" "Es tut dir also leid."

            "Anan" "Ich bin mir noch nicht so sicher, ob du begreifst, was du für einen Schaden angerichtet hast. Sowohl bei dir selbst als auch bei deinen Mitmenschen."

            "Atropos"  "Schaden? Aber…"

            show anan strict_mid

            "Anan" "Ja, Schaden. Wenn du unglücklich bist, wirst du dadurch auch andere unglücklich machen. Du wirst sie aus ihrem glücklichen Leben herausreißen und ins Unglück stürzen."

            "Anan" "Verstehst du das, Atropos?"

            "Atropos"  "Ich…"

            show anan normal_mid

            "Anan" "Ich bin nicht dein Feind. Und auch Happiness ist es nicht. Wir wollen alle nur ein einziges Ziel: Dass alle Menschen glücklich sind."

            "Anan" "Dass alle Menschen eine Vergangenheit, eine Gegenwart, eine Zukunft haben können, die glücklich ist. Die sie erfüllt und die sorglos ist."

            show anan disappointed_mid

            "Anan" "Der Krieg war eine düstere Zeit voller Leid und Elend. Du kannst es dir nicht vorstellen und darüber solltest du froh sein."

            show anan normal_mid

            "Anan" "Du solltest dankbar sein für das Leben, das wir dir geschenkt haben."

            "Anan" "Du solltest dein Leben genießen und glücklich sein."

            "Anan" "Die Welt ist zerstört, es gibt nur noch Astoa, Peria und Keposa. Was denkst du würde passieren, wenn die Menschen alle aufhören würden Happiness zu nehmen?"

            "Anan" "Denkst du, das würde ein gutes Ende nehmen? In einer Welt, die immer noch aus den Fugen geraten ist?"

            "Anan" "Die Menschen verdienen es, glücklich zu sein und sie brauchen das Glück, um friedlich leben zu können."

            show anan happy_mid

            "Anan" "Nimm Happiness, Atropos und werde wieder glücklich. Nicht nur für deine eigene Glücklichkeit, sondern für die aller Menschen."

            "Atropos"  "Ich…"


            menu:
                "Ich soll mich also für alle Menschen aufopfern? Was soll das denn bitte? Ich will selbst über mein Glück bestimmen können!":
                    "Atropos" "Ich soll mich also für alle Menschen aufopfern? Was soll das denn bitte? Ich will selbst über mein Glück bestimmen können!"

                    "Atropos"  "Das ist doch nicht fair. Ich habe keine Lust mehr darauf. Wieso wird uns nie irgendetwas erklärt?"

                    "Atropos"  "Wenn wir wenigstens wüssten, was die Pille eigentlich überhaupt mit uns anstellt, aber nicht mal das wird uns gesagt."

                    "Atropos"  "Das ist… das ist… ich will nicht mehr… ich werde diese verdammte Pille nicht mehr nehmen. Ich will auf meine eigene Art und Weise glücklich sein!"

                    show anan disappointed_mid

                    "Anan" "Das ist also deine Antwort? Das ist die Antwort, zu der du gekommen bist?"

                    "Atropos"  "Ja! Du kannst mich nicht dazu zwingen, Happiness zu nehmen! Ich kann mich einfach weigern!"

                    "Anan" "Ich bin enttäuscht von dir Atropos. Ich habe mehr von dir erwartet."

                    "Anan" "Ich dachte, dass du verstehen würdest, wie wichtig das Glück für die Menschen ist und dass du voll und ganz hinter Aither stehen würdest."

                    show anan strict_mid

                    "Anan" "Aber das scheint nicht der Fall zu sein. Was soll ich jetzt nur mit dir anstellen?"

                    "Anan" "Kann man noch vernünftig mit dir reden und dich überzeugen? Oder gehörst du bereits zu den verlorenen Seelen?"

                    "Atropos"  "Verlorene Seelen? Sprichst du von denen, die sich gegen Happiness wehren und die Pille verweigern?"

                    "Anan" "Sie schaden mit ihrem Verhalten der gesamten Menschheit und bedrohen unsere Existenz. Verlorene Seelen scheint da doch ein passendes Wort zu sein, nicht wahr?"

                    "Anan" "Sie sind verloren, aber sie können gerettet werden. Wir können sie finden und ihnen die Wahrheit und Erkenntnis zurückbringen."

                    "Anan" "Und genauso können wir auch dir helfen Atropos. Alle verlorenen Seelen sind Teil der Menschheit und auch ihr Glück ist wichtig, egal wie egoistisch sie auch gehandelt haben mögen."

                    "Anan" "Egal wie unwichtig ihnen das Glück der Menschheit auch ist. Wir können sie läutern und dafür sorgen, dass eines Tages alle Menschen wahrhaftes Glück empfinden können."

                    jump expulsion_office
                "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen.":
                    jump understandingpart3

        else:
            # Atropos Gedanken
            symb"Ich sollte mich besser nicht in Anans Büro umschauen."

            # Atropos Gedanken
            symb"Er könnte jeden Moment zurückkommen und außerdem gehört es sich einfach nicht."

            # Atropos Gedanken
            symb"Egal, welche Informationen ich auch daraus gewinnen könnte."

            # Atropos Gedanken
            symb"Mir hier und jetzt die Sachen anzuschauen, würde mich ins Unglück stürzen."

            # Atropos Gedanken
            symb"Ich werde einfach warten, bis Anan zurückkommt und nichts anrühren."

            scene anan_office
            with startfade

            "Atropos" "…"
            # Atropos Gedanken
            symb"Ich frage mich nur… warum will Anan nicht mehr verraten? Welches Geheimnis steckt hinter Happiness?"

            # Symbiont
            symb"{i}Wieso ist dir das so wichtig? Es spielt keine Rolle. Vergiss es. Das sind alles überflüssige Informationen, die du nicht brauchst, um glücklich zu sein. {i}"

            # Symbiont
            symb"{i}Frage dich selbst: Warum willst du diese Informationen haben? Warum spielt es eine Rolle für dich? {i}"

            # Atropos Gedanken
            symb"Ich… ich weiß es nicht."

            # Symbiont
            symb"{i}Und das ist das Problem. Ohne Happiness bist du verwirrt. Unsicher. Ängstlich. Und einfach nicht glücklich. Mach dir nicht länger Gedanken und Sorgen darüber. {i}"

            # Symbiont
            symb"{i}Dein Leben könnte so viel einfacher sein. Einfacher und so viel glücklicher. {i}"

            # Atropos Gedanken
            symb"Glücklicher…"

            show anan normal_mid

            "Anan" "Wo waren wir stehen geblieben?"

            "Atropos" "Es… es tut mir leid."

            "Anan" "Was genau tut dir leid?"

            "Atropos" "Ich denke ich hätte nicht so neugierig sein sollen. Du hast recht. Es ist gut so, wie es ist."

            "Anan" "Es freut mich zu hören, dass du zur Einsicht gekommen bist. Und glaube mir. Wir wollen alle nur das Beste für dich. Wir wollen alle nur, dass du glücklich sein kannst."

            "Atropos" "Ich weiß, es tut mir leid… ich wollte glücklich sein und das Glück auf meinem eigenen Weg erreichen, ohne zu erkennen, wie falsch das ist."

            "Atropos" "Was soll ich jetzt tun? Werde ich dafür bestraft, dass ich die Pille nicht genommen habe?"

            show anan happy_mid

            "Anan" "Kehre ins Labor zurück und nimm Happiness. Werd wieder glücklich. Du wirst nicht bestraft."

            "Anan" "Jeder macht mal Fehler und es sollen die belohnt werden, die danach wieder den richtigen Pfad einschlagen."

            "Anan" "Das ist das Wichtigste: Werde wieder glücklich, Atropos. Lebe das glückliche Leben, das du verdient hast."

            "Atropos" "Danke. Das werde ich tun."

            "Anan" "Und vielleicht findest du eines Tages Antworten auf die Fragen, die dich gerade verunsichern. Aber jetzt bist du noch nicht bereit."

            "Anan" "Sei geduldig und lass dich von den quälenden Fragen nicht länger peinigen. Sieh nach vorne und richte den Blick auf dein Glück."

            show anan normal_mid

            "Anan" "Und jetzt zurück an die Arbeit. Ich erwarte deinen Bericht heute noch. Hab einen Tag voller Glück!"

            "Atropos" "Danke, ich werde mein Bestes geben."

            hide anan
            scene hall
            with fadeshort
            jump takepillnow

    if infos_count_anan == 1 or infos_count_anan == 2:
        if  straight_anan_office:
            # Atropos Gedanken
            symb"Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen und dabei sollte er mich besser nicht erwischen."

            # Symbiont
            symb"{i}Ja, lass die Finger von den Sachen, du hast genug gesehen! Deine Neugierde sollte schon längst befriedigt sein. Bist du jetzt glücklich? {i}"

            # Atropos Gedanken
            symb"Nach all dem, was ich gesehen habe, soll ich glücklich sein?"

            # Atropos Gedanken
            symb"Was habe ich da überhaupt alles gesehen? Ich kann es immer noch nicht richtig begreifen…"

            # Atropos Gedanken
            symb"Was hat das zu bedeuten? Soll ich Anan darauf ansprechen, wenn er zurückkommt?"

            # Symbiont
            symb"{i}Nein, es würde dich unglücklich machen. Anan wäre bestimmt nicht erfreut zu hören, dass du in seinen Sachen herumgewühlt hast. Verlasse jetzt sofort das Zimmer. {i}"

            # Atropos Gedanken
            symb"Ja, es ist wohl besser jetzt erstmal nach draußen zu gehen und zu hoffen, dass Anan nichts bemerkt hat…"

            # Atropos Gedanken
            symb"Und danach…"

            scene hall
            with fadeshort

            # Atropos Gedanken
            symb"Anan ist noch nicht zu sehen. Ich habe Glück."

            scene hall
            with fadestart

            "Atropos" "…"

            show anan normal_mid

            "Anan" "Atropos Laiotas. Ich lobe deine Pünktlichkeit. Folge mir."

            # Atropos Gedanken
            symb"Ich kann nicht einschätzen, ob Anan gute oder schlechte Laune hat. Ich hoffe einfach nur, ich bekomme nicht zu viel Ärger."

            # Atropos Gedanken
            symb"Immerhin hat er nicht mitbekommen, dass ich in seinem Büro war."

            scene anan_office
            with fadeshort
            show anan normal_mid

            "Anan" "Nimm bitte Platz."

            "Atropos"  "Danke…"

            "Atropos"  "…"

            # Atropos Gedanken
            symb"Wieso sagt er denn nichts?"

            # Atropos Gedanken
            symb"Das macht mich nervös… soll ich etwa anfangen? Erwartet Anan eine Entschuldigung von mir?"

            if badmood:

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

            # alle

            "Atropos"  "Anan… es tut mir leid…"

            "Anan" "Es tut dir also leid."

            show anan disappointed_mid

            "Anan" "Ich bin mir noch nicht so sicher, ob du begreifst, was du für einen Schaden angerichtet hast. Sowohl bei dir selbst als auch bei deinen Mitmenschen."

            "Atropos"  "Schaden? Aber…"

            show anan strict_mid

            "Anan" "Ja, Schaden. Wenn du unglücklich bist, wirst du dadurch auch andere unglücklich machen. Du wirst sie aus ihrem glücklichen Leben herausreißen und ins Unglück stürzen."

            "Anan" "Verstehst du das, Atropos?"

            "Atropos"  "Ich…"

            show anan normal_mid

            "Anan" "Ich bin nicht dein Feind. Und auch Happiness ist es nicht. Wir wollen alle nur ein einziges Ziel: Dass alle Menschen glücklich sind."

            "Anan" "Dass alle Menschen eine Vergangenheit, eine Gegenwart, eine Zukunft haben können, die glücklich ist. Die sie erfüllt und die sorglos ist."

            # Atropos Gedanken
            symb"Soll ich Anan unterbrechen?"

            show anan disappointed_mid

            "Anan" "Der Krieg war eine düstere Zeit voller Leid und Elend. Du kannst es dir nicht vorstellen und darüber solltest du froh sein."

            show anan normal_mid

            "Anan" "Du solltest dankbar sein für das Leben, das wir dir geschenkt haben."

            # Atropos Gedanken
            symb"Soll ich ihn auf das ansprechen, was ich herausgefunden habe?"

            "Anan" "Du solltest dein Leben genießen und glücklich sein."

            "Anan" "Die Welt ist zerstört, es gibt nur noch Astoa, Peria und Keposa. Was denkst du, würde passieren, wenn die Menschen alle aufhören würden Happiness zu nehmen?"

            # Atropos Gedanken
            symb"Aber wie würde er reagieren?"

            "Anan" "Denkst du, das würde ein gutes Ende nehmen? In einer Welt, die immer noch aus den Fugen geraten ist?"

            "Anan" "Die Menschen verdienen es, glücklich zu sein und sie brauchen das Glück, um friedlich leben zu können."

            # Atropos Gedanken
            symb"Immerhin würde ich dadurch gleichzeitig zugeben, dass ich mich in seinem Büro ohne sein Wissen umgesehen habe."

            "Anan" "Nimm Happiness, Atropos und werde wieder glücklich. Nicht nur für deine eigene Glücklichkeit sondern für die aller Menschen."

            # Symbiont
            symb"{i}Lass es bleiben! Es würde dir nichts bringen außer Unglück und Elend. Du würdest keine Antworten bekommen, aber gleichzeitig würdest du zugeben, was du getan hast.{i}"


        else:
            # Atropos Gedanken
            symb"Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen und dabei sollte er mich besser nicht erwischen."

            # Symbiont
            symb"{i}Ja, lass die Finger von den Sachen, du hast genug gesehen. Deine Neugierde sollte schon längst befriedigt sein. Bist du jetzt glücklich? {i}"

            # Atropos Gedanken
            symb"Nach all dem, was ich gesehen habe, soll ich glücklich sein?"

            # Atropos Gedanken
            symb"Was habe ich da überhaupt alles gesehen? Ich kann es immer noch nicht richtig begreifen…"

            # Atropos Gedanken
            symb"Was hat das zu bedeuten? Soll ich Anan darauf ansprechen, wenn er zurückkommt?"


        jump one_or_two_infos

    if infos_count_anan == 3:
        if straight_anan_office:
            # Atropos Gedanken
            symb"Hier scheint sonst nichts mehr Wichtiges herumzuliegen…"

            # Atropos Gedanken
            symb"Jetzt sollte ich besser so schnell wie möglich aus dem Büro raus, bevor Anan zurückkommt."

            # Symbiont
            symb"{i}Schnell, beeile dich. Und denk an den Bildschirm, er war aus. {i}"

            "Atropos"  "Verdammt…"
        else:
            # Atropos Gedanken
            symb"Hier scheint sonst nichts mehr Wichtiges herumzuliegen…"

            # Atropos Gedanken
            symb"Ich sollte mich besser sofort wieder hinsetzen, bevor Anan zurückkommt."

            # Symbiont
            symb"{i}Schnell, beeile dich. Und denk an den Bildschirm, er war aus. {i}"

            "Atropos"  "Verdammt…"

        $ last_try_find_kloth = True
        show anan normal_mid

        "Anan" "Atropos."

        # Atropos Gedanken
        symb"Verdammt… verdammt… verdammt… das darf doch nicht wahr sein. Nicht genau jetzt…"

        # Atropos Gedanken
        symb"Was soll ich jetzt sagen? Was soll ich jetzt tun? Ich kann mich nicht mehr rausreden, oder?"

        # Atropos Gedanken
        symb"Anan hat gesehen, wie ich an seinem Computer stand und dort etwas gemacht habe."

        show anan strict_mid

        "Anan" "Ich verlange augenblicklich eine Erklärung."

        "Atropos"  "Ich… ich…"

        "Anan" "Ich warte. Und ich erwarte eine gute Erklärung. Ich kann mir keinen Grund vorstellen, der es dir erlauben sollte, durch meine Sachen durchzugehen."

        # Atropos Gedanken
        symb"Ich… verdammt… was soll ich nur tun? Das alles kann doch nicht wahr sein… ich hätte doch früher rausgehen sollen…"

        # Atropos Gedanken
        symb"Dass er so ruhig bleibt, macht mir noch mehr Angst, als wenn er wütend geworden wäre. Er ist zu ruhig. Gefährlich ruhig…"

        # Atropos Gedanken
        symb"Als würde er nur auf meinen nächsten Atemzug warten und mich dann verschlingen."

        # Symbiont
        symb"{i}Bleib ehrlich, sag die Wahrheit. Es ist ohnehin schon zu spät. Du kannst vielleicht nichts retten, aber du kannst es wenigstens bewusst nicht verschlimmern. {i}"

        "Atropos" "Ich dachte, ich könnte vielleicht mehr über Happiness herausfinden, indem ich mich umschaue…"

        show anan disappointed_mid

        "Anan" "(seufzt) Ich hatte gehofft, ich könnte dir eine zweite Chance geben. Ich hatte geglaubt, du würdest sie verdienen."

        # Atropos Gedanken
        symb"Wie kann er nur so ruhig bleiben? Ich an seiner Stelle wäre vermutlich ausgerastet."

        # Atropos Gedanken
        symb"Aber ich habe Anan noch nie wütend erlebt… er wirkt immer so unnahbar und kalkuliert, aber gleichzeitig auch warm und freundlich."

        # Atropos Gedanken
        symb"Letzteres fehlt verständlicherweise gerade. Und vielleicht macht gerade das es so beängstigend."

        "Anan" "Aber du hast dich eigenmächtig befugt, mein Büro zu durchsuchen und mein Eigentum anzurühren."

        "Atropos"  "Ich… ich…"

        "Anan" "Ich will doch nur, dass die Menschen glücklich sind, Atropos. Ich will, dass du glücklich bist."

        show anan strict_mid

        "Anan" "Aber irgendwann ist ein Maß erreicht, ich denke, das verstehst du? Wir können nicht so weitermachen, als wäre das nicht passiert. Die Zweifel sitzen bereits zu tief in dir."

        "Anan" "Deine Handlungen werden Konsequenzen mit sich ziehen. Du musst die Firma verlassen. Aber hab keine Sorge. Du kannst trotzdem glücklich sein."

        show anan normal_mid

        "Anan" "Du wirst glücklich sein. Wir werden einen guten Job für dich finden, einen Job, der dich glücklich macht."

        "Atropos" "Das… das ist unfair! Ich wollte doch nur mehr herausfinden, weil nie jemand etwas erzählt. Warum werden wir über das alles im Dunklen gelassen?"

        "Atropos" "Was hat das alles zu bedeuten? Pfuscht ihr in unserem Gehirn herum mit Happiness? Macht ihr uns abhängig?"

        "Atropos" "Werde ich jetzt ins Abseits geschossen, wie auch die anderen Menschen auf dieser Liste? Im Auge hattet ihr mich ja wohl bereits."

        "Atropos" "Und der Brief über das angebliche Chaos, ohne Happiness. Das sind nichts anderes als Lügen, oder?"

        show anan disappointed_mid

        "Anan" "Ich wünschte, es wären Lügen. Vielleicht würden die Menschen dann Happiness nicht brauchen, um glücklich zu sein."

        show anan normal_mid

        "Anan" "Aber es sind keine Lügen. Und die Menschen brauchen Happiness, es gibt keine andere Lösung."

        "Anan" "Hättest du damals zu Kriegszeiten bereits gelebt, würdest du das vielleicht besser verstehen, aber dank Happiness bist du in Zeiten des Friedens aufgewachsen."

        "Anan" "Und nur weil du die Wahrheit herausfinden möchtest, erlaubt dir das zudem nicht, dich an fremdem Eigentum zu vergreifen."

        "Atropos" "Ich… ich weiß…"

        "Atropos" "Aber was ist mit der Liste, auf der mein Name steht?"

        "Atropos" "Willst du alle beseitigen, die dir gefährlich werden könnten?"

        "Anan" "Wir machen uns nur Sorgen um eure Sicherheit. Um eure Glücklichkeit. Und darum, dass ihr das Glück der anderen Menschen gefährden könntet."

        "Anan" "Wir wollen euch vor euch selbst beschützen. Keiner soll beseitigt werden oder darunter leiden müssen."

        "Anan" "Es wird akzeptiert, wenn es Menschen gibt, die keine Happinesspille nehmen. Niemand zwingt dich dazu. Aber es muss klar sein, dass man dafür auch mit den Konsequenzen dieser Entscheidung leben muss."

        "Anan" "Letztlich schadest du und auch andere damit der gesamten restlichen Menschheit."

        # Atropos Gedanken
        symb"Ich weiß nicht mehr, was ich denken soll… Das alles wird mir zu viel… soll ich Anans Worten Glauben schenken?"

        "Anan" "Du brauchst Zeit, um das alles zu vergessen. Zeit, bis sich dein Geist wieder beruhigt hat."

        "Anan" "Nimm die Happiness-Pille, sie wird dir helfen. Ich verspreche dir, dass dein Leben wieder glücklicher wird."

        "Anan" "Bezüglich deiner neuen Arbeitsstelle wirst du morgen von Kloth hören."

        # Symbiont
        symb"{i}Widersprich nicht! Du hast genug Ärger am Hals. Willst du noch mehr riskieren? Sei dankbar, dass Anan dich so einfach davonkommen lässt! {i}"

        # Symbiont
        symb"{i}Nimm Happiness, vergiss den Vorfall und starte von vorne. Ein neues, besseres und glücklicheres Leben.{i}"

        "Atropos" "(leise) Ja."

        "Anan" "Ich wünsche dir einen Tag voller Glücklichkeit. Und Atropos: Gewöhne es dir besser ab, in den Sachen anderer Leute herumzuwühlen."

        "Atropos" "Ja."

        hide anan
        scene hall
        with fadeshort

        jump visit_kloth

label one_or_two_infos:
    if straight_anan_office== False:

        #Atropos Gedanken
        symb"Das ist alles so verwirrend."

        show anan normal_mid

        "Anan" "Wo waren wir stehen geblieben?"

        "Atropos" "Wir…"

        "Anan" "Ich denke du hattest inzwischen genug Zeit, noch einmal über alles nachzudenken. Verstehst du nun, warum Happiness so wichtig ist?"

        "Anan" "Haben sich deine Fragen geklärt?"

        # Atropos Gedanken
        symb"Warte… weiß Anan etwa, dass ich mir etwas angeschaut habe?"

        #Atropos Gedanken
        symb"Verdammt… soll ich alles zugeben? Oder einfach nur schweigen und hoffen, dass er es doch nicht mitbekommen hat?"

        # Atropos Gedanken
        symb"Aber vielleicht sollte ich ihn auch einfach mit dem, was ich gefunden habe konfrontieren? Angriff ist immerhin die beste Verteidigung."


    menu:
        "Ich sollte Anan mit den Tatsachen konfrontieren.":
            $ last_try_find_kloth = True
            jump face_anan
        "Ich lasse den Rest seiner Ansprache über mich ergehen und hoffe, dass er nichts bemerkt hat.":
            jump not_face_anan

label face_anan:
    $ bomb_trigger_choice = True

    # Atropos Gedanken
    symb"Ich sollte Anan mit den Tatsachen konfrontieren."

    # Atropos Gedanken
    symb"Vielleicht bringt es mir wenigstens ein paar Antworten."

    if read_letter_anan:
        "Atropos" "Nein! Der Brief… was hat es damit auf sich?"

    if read_computer_anan:
        if read_letter_anan == False:
            "Atropos" "Nein! Diese Liste auf deinem PC, was hat es damit auf sich?"

    if read_computer_anan==False:
        if read_letter_anan == False:
            if read_document_anan:
                "Atropos" "Nein! Dieses Dokument auf deinem Schreibtisch… was hat es damit auf sich?"

    # alle
    "Atropos" "Was soll das alles? Was hat das zu bedeuten?"

    show anan strict_mid

    "Anan" "Es ist wohl viel eher an mir, {b}dir{/b} diese Frage zu stellen."

    "Anan" "Ich verlange augenblicklich eine Erklärung."

    "Atropos"  "Ich… ich…"

    "Anan" "Ich warte. Und ich erwarte eine gute Erklärung. Ich kann mir keinen Grund vorstellen, der es dir erlauben sollte, meine Sachen anzufassen."

    # Atropos Gedanken
    symb"Ich… verdammt… was soll ich nur tun? Ich hätte es besser nicht zur Sprache bringen sollen. Ich fühle mich so klein, wenn ich mit ihm spreche."

    # Atropos Gedanken
    symb"Dass er so ruhig bleibt, macht mir noch mehr Angst, als wenn er wütend geworden wäre. Er ist zu ruhig. Gefährlich ruhig…"

    # Atropos Gedanken
    symb"Als würde er nur auf meinen nächsten Atemzug warten und mich dann verschlingen."

    # Symbiont
    symb"{i}Bleib ehrlich, sag die Wahrheit! Es ist ohnehin schon zu spät. Du kannst vielleicht nichts retten, aber du kannst es wenigstens bewusst nicht verschlimmern. {i}"

    "Atropos" "Ich dachte, ich könnte vielleicht mehr über Happiness herausfinden, indem ich mich umschaue…"

    show anan disappointed_mid

    "Anan" "(seufzt) Ich hatte gehofft, ich könnte dir eine zweite Chance geben. Ich hatte geglaubt du würdest sie verdienen."

    # Atropos Gedanken
    symb"Wie kann er nur so ruhig bleiben? Ich an seiner Stelle wäre vermutlich ausgerastet."

    # Atropos Gedanken
    symb"Aber ich habe Anan noch nie wütend erlebt… er wirkt immer so unnahbar und kalkuliert, aber gleichzeitig auch warm und freundlich."

    # Atropos Gedanken
    symb"Letzteres fehlt verständlicherweise gerade. Und vielleicht macht gerade das es so beängstigend."

    "Anan" "Aber du hast dich eigenmächtig befugt mein Büro zu durchsuchen und mein Eigentum anzurühren."

    "Atropos"  "Ich… ich…"

    "Anan" "Ich will doch nur, dass die Menschen glücklich sind, Atropos. Ich will, dass du glücklich bist."

    show anan strict_mid

    "Anan" "Aber irgendwann ist ein Maß erreicht, ich denke, das verstehst du? Wir können nicht so weitermachen, als wäre das nicht passiert. Die Zweifel sitzen bereits zu tief in dir."

    "Anan" "Deine Handlungen werden Konsequenzen mit sich ziehen. Du musst die Firma verlassen. Aber hab keine Sorge! Du kannst trotzdem glücklich sein."

    "Anan" "Du wirst glücklich sein. Wir werden einen guten Job für dich finden, einen Job, der dich glücklich macht."

    "Atropos" "Das… das ist unfair! Ich wollte doch nur mehr herausfinden, weil nie jemand etwas erzählt. Warum werden wir über das alles im Dunklen gelassen?"

    "Anan" "Es ist also unfair, dass du dich an fremdem Eigentum vergreifst?"

    "Anan" "Vergiss, was auch immer du gesehen hast. Es ist nichts, was dich glücklich macht, eher im Gegenteil. Du solltest aufhören, dir darüber Gedanken zu machen."

    "Anan" "Es ist gefährliches Wissen. Wissen, das dich ins Unglück stürzen kann- nein, sogar sicher wird."

    show anan normal_mid

    "Anan" "Vertraue mir, Atropos. Ich will nur dein Bestes. Was denkst du hätte ich davon dich anzulügen?"

    "Anan" "Vertraue Happiness. Wir bringen dir dein glückliches Leben zurück, versprochen."

    # Atropos Gedanken
    symb"Ich weiß nicht mehr, was ich denken soll… Das alles wird mir zu viel… soll ich Anans Worten Glauben schenken?"

    "Anan" "Du brauchst Zeit, um das alles zu vergessen. Zeit, bis sich dein Geist wieder beruhigt hat."

    "Anan" "Nimm die Happiness-Pille, sie wird dir helfen. Ich verspreche dir, dass dein Leben wieder glücklicher werden wird."

    show anan strict_mid

    "Anan" "Bezüglich deiner neuen Arbeitsstelle wirst du morgen von Kloth hören."

    # Symbiont
    symb"{i}Widersprich nicht! Du hast genug Ärger am Hals. Willst du noch mehr riskieren? Sei dankbar, dass Anan dich so einfach davonkommen lässt. {i}"

    # Symbiont
    symb"{i}Nimm Happiness, vergiss den Vorfall und starte von vorne. Ein neues, besseres und glücklicheres Leben.{i}"

    "Atropos" "(leise) Ja."

    "Anan" "Ich wünsche dir einen Tag voller Glücklichkeit. Und Atropos: Gewöhne es dir besser ab, in den Sachen anderer Leute herumzuwühlen."

    "Atropos" "Ja."

    jump  visit_kloth

label not_face_anan:

    # Atropos Gedanken
    symb"Ich lasse den Rest seiner Ansprache über mich ergehen und hoffe, dass er nichts bemerkt hat."

    "Atropos" "Ja… ja, haben sie… es tut mir leid…"

    show anan strict_mid

    "Anan" "Kehre zurück ins Labor und nimm deine Pille. Sie wird dich wieder glücklich machen und all deine Zweifel vergessen lassen."

    "Anan" "Es ist die beste Lösung. Die einzige Lösung."

    "Anan" "Happiness kann dir helfen. Happiness kann dir dein Glück zurückbringen. Noch ist es nicht zu spät."

    "Atropos" "Ja…"

    show anan happy_mid

    "Anan" "Ich wünsche dir einen Tag voller Glücklichkeit, Atropos."

    "Atropos" "Danke… ich dir auch…"

    hide anan
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Was soll ich jetzt nur tun? Was soll ich mit meinem Wissen anfangen?"

    # Atropos Gedanken
    symb"Was bedeutet das, was ich gesehen habe, für Aither?"

    # Atropos Gedanken
    symb"Was ist Aither?"

    # Atropos Gedanken
    symb"Kann ich Aither vertrauen? Kann ich Anan vertrauen? Seinen Worten?"

    # Atropos Gedanken
    symb"Ich weiß einfach nicht mehr, was ich denken soll…"

    # Atropos Gedanken
    symb"Ich weiß nicht mehr, was ich glauben soll…"

    # Atropos Gedanken
    symb"Ich… ich…"

    # Atropos Gedanken
    symb"Vielleicht wäre es wirklich besser gewesen, ich hätte niemals mehr erfahren. Ich hätte niemals etwa zu Gesicht bekommen…"

    # Atropos Gedanken
    symb"Aber das beantwortet immer noch nicht die Frage, ob ich Aither vertrauen kann und sollte…"

    # Atropos Gedanken
    symb"Was sind die Absichten von Anan und dem Triumvirat? Wollen sie uns wirklich nur glücklich machen? Oder steckt mehr dahinter?"

    # Atropos Gedanken
    symb"Und zu welchem Preis verkaufen sie uns diese Glücklichkeit?"

    # Atropos Gedanken
    symb"Was soll ich nur von Aither halten?"


    menu:
        "Ich vertraue immer noch auf Aither. Ich glaube an das Gute in der Firma.":
            # Atropos Gedanken
            symb"Ich vertraue immer noch auf Aither. Ich glaube an das Gute in der Firma."

            # Atropos Gedanken
            symb"Vielleicht mag es irgendwo Unstimmigkeiten geben und Sachen, die ich nicht ganz verstehe…"

            # Atropos Gedanken
            symb"Aber dennoch… Aither hat niemals etwas getan, was mich an der moralischen Absicht der Firma zweifeln lassen würde…"

            # Atropos Gedanken
            symb"Sie haben nie etwas getan, das den Menschen schaden würde. Ganz im Gegenteil. Dank dem Triumvirat ist die ganze Menschheit glücklicher als sie es jemals zuvor war."
            # Atropos Gedanken
            symb"Aber bin ich wirklich glücklich?"

            # Atropos Gedanken
            symb"Ist das hier das, was ich will?"

            # Atropos Gedanken
            symb"Egal, ich sollte jetzt erstmal zurück an die Arbeit."

            jump back_to_work
        "Ich traue Aither nicht.":
            # Atropos Gedanken
            symb"Ich traue Aither nicht."

            # Atropos Gedanken
            symb"Irgendetwas stimmt nicht."

            # Atropos Gedanken
            symb"Das, was ich entdeckt habe… es lässt mich noch mehr zweifeln."

            # Atropos Gedanken
            symb"Happiness mag uns Glück bringen, aber zu welchem Preis? Sollten wir diesen Preis wirklich bezahlen?"

            # Atropos Gedanken
            symb"Ist Glücklichkeit wirklich jeden Preis wert? Egal, wie teuer dieser auch sein mag? Egal auf wie viel wir dafür verzichten müssen?"

            # Symbiont
            symb"{i}Ist glücklich zu sein nicht jeden Preis wert? Was gibt es Besseres als glücklich zu sein?"

            # Atropos Gedanken
            symb"Was ist mit Freiheit? Die Freiheit eigene Entscheidungen zu treffen und selbst zu bestimmen, was ich tun möchte?"

            # Symbiont
            symb"{i}Ist es nicht manchmal besser sich in seinen Freiheiten ein wenig einzuschränken, damit man jeglichem Unglück, Übel, Schmerz und Leid entgeht?"

            # Symbiont
            symb"{i}Es gibt nichts Wichtigeres als dein Glück."

            # Atropos Gedanken
            symb"Da bin ich mir nicht so sicher…"

            $ rage_atropos_bomb = True
            $ face_anan_in_office = True
            $ bomb_trigger_choice = True
            jump visit_kloth

label visit_kloth:
    scene hall
    with fadeshort
    if face_anan_in_office:
        # Atropos Gedanken
        symb"Ich sollte Kloth suchen. Vielleicht kann er mir Antworten geben."

        # Atropos Gedanken
        symb"Immerhin ist er Anans persönlicher Sekretär… das muss ja irgendetwas zu bedeuten haben, oder?"

        # Atropos Gedanken
        symb"Er muss dadurch irgendwelche Informationen besitzen, die ich nicht habe… Informationen, die Klarheit in alles bringen."

        # Atropos Gedanken
        symb"Vielleicht kann er mir dabei helfen, entweder meine Zweifel zu zerstreuen oder meine Sorgen zu bestätigen."

        # Atropos Gedanken
        symb"So oder so… ich brauche einfach Gewissheit."

        # Atropos Gedanken
        symb"Das alles macht mich halb wahnsinnig…"

    # Atropos Gedanken
    symb"Wo er wohl gerade ist? Gesehen habe ich ihn heute immer noch nicht. Ich kann ihn ja mal anrufen."

    # Symbiont
    symb"{i}Du solltest ihn nicht anrufen. Was ist, wenn er gerade in einer Besprechung ist und du ihn störst? {/i}"

    # Symbiont
    symb"{i}Schreib ihm doch lieber, warte ab, bis er antwortet und verbringe unterdessen Zeit mit deinen Freunden oder kehre zurück ins Labor. Das macht dich glücklich. {/i}"

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

    scene kloth_office
    with fadeshort

    "Atropos" "Kloth?"

    # Atropos Gedanken
    symb"Niemand hier."

    # Atropos Gedanken
    symb"Das wäre auch zu schön gewesen."

    # Atropos Gedanken
    symb"Vielleicht sollte ich mich umschauen? Bestimmt gibt es hier irgendetwas, das mir weiterhilft."

    # Atropos Gedanken
    symb"Und wenn es mir nur eine noch so kleine Antwort geben sollte."

    jump selection_kloth_office_after_anan_office

label search_kloth_in_stairwell:
    $ rage_atropos_bomb = False
    # Atropos Gedanken
    symb"Aber wo kann er nur sein? Habe ich nicht überall nach ihm gesucht?"

    # Atropos Gedanken
    symb"Ich muss das ganze Gebäude nochmal absuchen… irgendwo muss er ja sein…"

    # Atropos Gedanken
    symb"Ich werde mich einfach von unten nach oben durcharbeiten."

    # Atropos Gedanken
    symb"Ich brauche Antworten!"

    # Atropos Gedanken
    symb"Nicht irgendwann, sondern jetzt sofort!"

    # Atropos Gedanken
    symb"Die Aufzüge sind so voll- ich nehme besser die Treppe…"

    scene stairs_up
    with fadeshort

    # Atropos Gedanken
    symb"Wo mag er nur sein? Ob ihm etwas zugestoßen ist? Wenn ja… ich könnte es nicht ertragen…"

    scene stairs_down
    with fadeshort

    # Atropos Gedanken
    symb"Warte… was ist das?"

    # Atropos Gedanken
    symb"Das… das…"

    # Symbiont
    symb"{i}Vergiss die Pille nicht, Atropos! Du fängst schon an, dir Sachen einzubilden. Hier ist nichts zu sehen. {/i}"

    # Symbiont
    symb"{i}Langsam wirst du ja schon fast wahnsinnig. Nimm die Pille und werde wieder glücklich, so wie all deine Kollegen es sind! {/i}"

    # Symbiont
    symb"{i}Du hast dein Glück verdient. So wie alle Menschen Glück verdient haben. {/i}"

    # Symbiont
    symb"{i}Du willst das hier nicht sehen. Es würde dich unglücklich machen. Hier ist nichts. Vergiss, was du zu sehen glaubtest. {/i}"

    # Symbiont
    symb"{i}Brich die Suche ab und kehre ins Labor zurück! Nimm die Pille! Lebe weiterhin ein glückliches Leben. {/i}"

    # Atropos Gedanken
    symb"Ist das… ist das eine Leiche?"

    # Atropos Gedanken
    symb"Aber wie? Warum? Warum ist sie noch niemandem aufgefallen?"

    # Atropos Gedanken
    symb"Was hat das alles zu bedeuten? Es macht mir Angst…"

    # Atropos Gedanken
    symb"Will ich die Wahrheit dahinter überhaupt wissen?"

    # Atropos Gedanken
    symb"Nein… ja… ich… ich…"

    # Atropos Gedanken
    symb"Was, wenn das Kloth ist?"

    # Atropos Gedanken
    symb"Das… das würde ich nicht ertragen…"

    # Symbiont
    symb"{i}Brich die Suche ab und kehre ins Labor zurück! Nimm die Pille! Lebe weiterhin ein glückliches Leben. {/i}"

    # Symbiont
    symb"{i}Tu es! {/i}"


    jump leave_or_corpse

label how_many_infos_kloth:

    if infos_count_kloth == 1 or infos_count_kloth == 2:
        jump choice_bomb

    if infos_count_kloth == 3:
        if last_try_find_kloth:
            jump last_search_kloth
        else:
            jump sawallthreekloth

label last_search_kloth:
    $ rage_atropos_bomb = True

    # Atropos Gedanken
    symb"Was ist das alles?"

    # Atropos Gedanken
    symb"Was habe ich da nur gesehen?"

    # Atropos Gedanken
    symb"Was hat das zu bedeuten?"

    # Atropos Gedanken
    symb"Diese ganzen Informationen… ich weiß nicht, was ich mit ihnen anstellen soll."

    # Atropos Gedanken
    symb"Mein Kopf droht, bald zu platzen. Ich… mir ist das alles zu viel…"

    # Atropos Gedanken
    symb"Das sind zu viele Informationen auf einmal."

    # Atropos Gedanken
    symb"Ich… was soll ich mit all dem Wissen tun?"

    # Atropos Gedanken
    symb"Was soll ich mit all diesen Informationen anstellen? Soll ich nach Kloth suchen? Oder besser nach der Bombe?"


    menu:
        "Ich muss nach Kloth suchen!":
            jump end_search_kloth
        "Ich muss nach der Bombe suchen!":
            jump nextstepwithbomb

label end_search_kloth:
    scene hall
    with fadeshort

    # Atropos Gedanken
    symb"Ich muss nach Kloth suchen!"

    # Atropos Gedanken
    symb"Ich habe Angst, dass ihm vielleicht schon was zugestoßen ist… und die Bombe… was hat er damit zu tun?"

    # Atropos Gedanken
    symb"Hat er sie gelegt?"

    # Atropos Gedanken
    symb"Was wusste er?"

    # Atropos Gedanken
    symb"Ich muss ihn finden! Vielleicht schaffe ich es, so zu verarbeiten, was ich gesehen habe…"

    # Atropos Gedanken
    symb"Ich weiß nicht mehr, was ich noch denken soll… Das alles macht mir Angst."

    # Atropos Gedanken
    symb"Die Bombe… Happiness… der Abschiedsbrief… die Liste… all die Sachen machen mir Angst…"

    # Atropos Gedanken
    symb"Und wo ist Kloth nur?"

    # Atropos Gedanken
    symb"Ich habe ja bereits vergeblich versucht, ihn zu finden."

    # Atropos Gedanken
    symb"Aber ich muss ihn finden… ich muss, ich muss, ich muss…"

    # Atropos Gedanken
    symb"Wo kann er nur sein?"

    # Atropos Gedanken
    symb"Wo?"

    # Atropos Gedanken
    symb"WO?"

    # Atropos Gedanken
    symb"Notfalls werde ich ganz Aither auf den Kopf stellen, um ihn zu finden!"

    # Atropos Gedanken
    symb"Vor den Aufzügen warten so viele Menschen, ich nehme die Treppe…"

    scene stairs_down
    with fadeshort

    "Atropos"  "Kloth?"

    "Atropos"  "{b}Kloth?{/b}"
    scene corpse
    with fadeshort

    "Atropos"  "KLOTH!"

    "Atropos"  "Wer hat dir das angetan?"

    "Atropos"  "Ich werde ihn finden und…"

    "Atropos"  "Kloth… (schluchzt)"

    "Atropos"  "Komm zu mir zurück!"

    "Atropos"  "Kloth…"

    "Atropos"  "Wer war es?"

    "Atropos"  "Wer verdammt noch mal war es?"

    "Atropos"  "Dafür wird die Person büßen! Sie wird es bereuen!"

    "Atropos"  "Wer war es?!!!"

    # Start Erinnerung

    scene stairs_up
    show sepia
    with fadeshort
    show kloth smiling behind sepia

    "Kloth"  "Atropos!"

    "Atropos" "Kloth, was ist los?"

    show kloth scared1_neutral

    "Kloth" "Ich habe dich überall gesucht. Endlich habe ich dich gefunden… ich muss mit dir reden. Hast du kurz einen Moment Zeit? Bitte…"

    "Atropos" "Beruhige dich erst einmal und atme tief durch. Was ist passiert? "

    show kloth scared2

    "Kloth" "Nicht hier … es könnte jemand kommen und dann…"

    "Atropos" "Kloth, es ist alles in Ordnung. Niemand kann dir etwas tun. Was ist denn nur los mit dir?"

    show kloth scared1

    "Kloth" "Ich… ich…"

    "Atropos" "Ich wollte eigentlich gerade Mittagspause machen. Willst du nicht einfach mitkommen und wir reden dann? Chesis scheint auch Pause zu haben."

    show kloth scared2

    "Kloth" "Du hörst mir ja gar nicht richtig zu… bitte… ich… ich weiß nicht, an wen ich mich sonst wenden soll. Ich brauche dich jetzt."

    show kloth scared1_neutral

    "Kloth" "Es gibt da etwas, das ich schon eine ganze Weile mit mir herumtrage und ich komme alleine einfach nicht damit klar. Bitte, ich muss mit jemandem darüber sprechen."

    show kloth scared2

    "Kloth" "Du bist der Einzige, der mir helfen kann!"

    "Atropos" "Tut mir leid, aber ich habe gerade nicht den Nerv für ein solches Gespräch. Ich hatte heute einen stressigen Tag und brauche jetzt erstmal wieder etwas Ruhe und Entspannung."
    # ab hier Glitch
    show kloth scared1

    "Kloth" "Neeeein!"

    show kloth crazy

    "Kloth" "Atropos! Sie verfolgen uns. Wir haben keine Chance gegen sie!"

    "Kloth" "Sie werden uns finden und dann töten. Erst dich und dann mich!"

    show kloth scared2

    "Kloth" "Sie mögen es nicht, wenn die Wahrheit über sie herauskommt! Sie werden alles dafür tun, dass sie verborgen bleibt!"

    show kloth crazy

    "Kloth" "Sie leben! Sie sind in unserem Kopf! Immer, ganz laut!"

    "Kloth" "Und trotzdem nimmst du sie nicht wahr. Sie sind ein Teil von dir."

    show kloth scared1

    "Kloth" "Ich bin sie losgeworden, aber nun wollen sie mich töten. Ich darf dieses Wissen nicht weitergeben!"

    show kloth scared2

    "Kloth" "Wenn ich es tue, dann sterbe ich!"

    show kloth scared1

    "Kloth" "Du wirst mich töten, nicht wahr?"

    show kloth crazy

    "Kloth" "Du wirst uns alle töten!"

    "Kloth" "Sie werden kommen uns holen!"

    "Kloth" "Uns alle!"

    $ renpy.movie_cutscene("atropos_pushes_kloth.mpg")

    # Symbiont
    symb"{i}Bleib ruhig! Du warst es nicht. Vergiss alles! Sei glücklich! {/i}"

    "Atropos" "Vergessen? (lacht) Wie soll ich all das vergessen?"

    "Atropos" "Ich… Ich war es, der ihn getötet hat! (lacht)"

    "Atropos" "Natürlich… ich!"

    "Atropos" "Wie hatte ich das nur vergessen können? (lacht)"

    # Symbiont
    symb"{i}Beruhige dich! Verlier nicht deinen Verstand! So machst du nur dich und alle anderen unglücklich. {/i}"

    "Atropos" "Und die Bombe wird booom gehen."

    "Atropos" "Sie werden brennen. Sie werden alle brennen."

    "Atropos" "Hörst du das? Sie werden brennen und sie haben es alle verdient! (lacht)"

    # Symbiont
    symb"{i}Das waren zu viele Informationen auf einmal für dich, dein Kopf konnte die Informationen nicht verarbeiten. Werd glücklich und vergiss all das!{/i}"

    "Atropos" "Die Bombe wird explodieren und sie alle mit in den Abgrund reißen!"

    "Atropos" "Tick Tack… Boom!"

    "Atropos" "Arme kleine Menschen… sie werden bluten…"

    # Symbiont
    symb"{i}Sei glücklich! {/si}"

    "Atropos" "Aber Happiness wird euch doch bestimmt glücklich machen, oder?"

    "Atropos" "Ihr seid doch alle glücklich! (lacht)"

    "Atropos" "Die Bombe… die Bombe sie tickt und tickt. Nicht mehr lange, bis sie euch zu Grabe bringt!"

    "Atropos" "Hahahaha…"

    "Atropos" "Es ist zu lustig. Sie alle wollten glücklich sein und jetzt bezahlen sie den Preis dafür."

    "Atropos" "Ich wusste es… diese Pillen sind böööööse…"

    "Atropos" "Sie werden brennen und verglühen bis nichts mehr übrig ist. Keine Happiness wird überleben!"

    "Atropos" "Sterbt! Sterbt! Sterbt! Mal sehen, ob du wirklich ein unsterblicher Gott bist, Anan!"

    "Atropos" "Oder bist du doch nur ein armes, kleines Menschlein?"

    "Atropos" "Boooooom. Dein Leben wird von einer Sekunde auf die andere enden und du wirst endlich vom Thron gestoßen…"

    "Atropos" "Ein gefallener Herrscher, es muss traurig sein…"

    "Atropos" "Sterbt! Sterbt alle!"

    "Atropos" "Tick, Tack- wie viel Zeit bleibt euch wohl noch?"

    scene server_room
    with fadealarm

    scene detail_bomb1000
    with fadeshort

    "Atropos" "10 Minuten… dann werdet ihr endlich alle brennen. Und ich mit euch!"

    scene server_room
    with fadeshort

    "Atropos" "Kloth, siehst du mir zu? Bist du stolz auf mich? Ich erfülle deinen Wunsch!"

    "Atropos" "(lacht)"

    "Atropos" "Tick. Tack. Tick. Tack."

    "Atropos" "Flieht ihr dummen Menschen, flieht!"

    "Atropos" "Ich werde über euch kommen und ihr werdet nicht wissen wie euch geschieht!"

    "Atropos" "Tick. Tack."

    scene hall
    with fadeshort

    "Atropos" "Hört ihr das? Ohh, eine Bombe! Sie ist hier bei mir und ihr werdet alle sterben…"

    "Atropos" "(lacht)"

    "Atropos" "Seht euch nur an, wie ihr eurer Arbeit weiter nachgeht als hätte ich nichts gesagt. Nur, weil euch meine Worte unglücklich machen würden, arbeitet ihr weiter als wäre nichts."

    "Atropos" "Brave Opferlämmchen."

    "Atropos" "Aber ihr sterbt zu einem guten Zweck! Ihr werdet mir noch dankbar sein!"

    "Atropos" "Ja, ganz bestimmt!"

    "Atropos" "Die Stimme wird sterben. Endlich! Bei allen! Seid mir dankbar. Lacht! Lebt! Ach, nein… ihr sterbt ja… Sterbt!"

    "Atropos" "Brennt… Brennt lichterloh!"

    "Atropos" "Ihr werdet wie eine Fackel brennen, obwohl es doch mitten am Tag ist! (lacht)"

    "Atropos" "Wieso ignoriert ihr mich denn alle? Schaut mich an! Ich bin euer neuer Gott!"

    "Atropos" "Der Gott einer neuen Welt!"

    "Atropos" "Ich werde die Erde in einen völlig neuen Zustand einleiten. Ihr werdet mich noch alle anbeten!"

    "Atropos" "Tick. Tack."

    "Atropos" "(lacht)"

    "Atropos" "Bye, bye. Schlaft gut und träumt süß!"

    "Atropos" "So tief werdet ihr nie wieder schlafen!"

    scene server_room
    with fadeshort

    "Atropos" "So, und damit ihr auch alle schön schlafen könnt, schließe ich die Tür ab!"

    "Atropos" "Ihr dürft mich doch nicht an meinem toooollen Plan hindern…"

    "Atropos" "Das wäre wirklich nicht nett…"

    scene detail_bomb0010
    with fadeshort

    "Atropos" "Noch 10 Sekunden… mein Baby… du wirst uns alle retten…"

    scene server_room
    with fadeshort

    "Atropos" "Reiße ganz Aither in die Luft, ja?"

    "Atropos" "Boooom und weg…"

    "Atropos" "(lacht)"

    "Atropos" "Schlaf, Kindlein schlaf…"

    "Atropos" "Ihr alle liegt im Grab…"

    "Atropos" "Gute Nacht!"

    "Atropos" "(lacht)"

    $ renpy.movie_cutscene("cutscene_intro.mpg")

    $ renpy.movie_cutscene("cutscene_ende.mpg")

    return

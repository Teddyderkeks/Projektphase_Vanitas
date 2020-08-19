default infos_count_anan = 0
default infos_count_kloth = 0
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

    # Atropos Gedanken
    "Immerhin ist Anans Büro nicht so weit entfernt."

    if badmood:

        # Atropos Gedanken
        "Ich habe echt keine Lust zu gehen, aber was will man machen…"

        # Atropos Gedanken
        "Ich hoffe nur, Anan hält seine Ansprache kurz und es hat keine weiteren Konsequenzen für mich. Das könnte ich echt nicht gebrauchen."
    else:

        # Atropos Gedanken
        "Ich hoffe nur, er hält seine Ansprache kurz und es hat keine weiteren Konsequenzen für mich."

        # Atropos Gedanken
        "Das ist das Letzte, das ich möchte. Ich habe immer wieder mitbekommen, dass Menschen, die keine Pille genommen haben, bestimmte Privilegien genommen werden."

        # Atropos Gedanken
        "Einfach aus dem Grund, dass ihr Verhalten rücksichtlos anderen Menschen gegenüber ist, die einfach nur glücklich sein wollen."

        # Atropos Gedanken
        "Ob da wohl etwas Wahres dran ist?"

    # Atropos Gedanken
    "Da ist das Büro. Mal sehen, ob Anan da ist. Ich klopfe besser an."

    # Atropos Gedanken
    "Seltsam, keine Antwort… ob ich wohl einfach eintreten sollte?"

    # Atropos Gedanken
    "Immerhin hatte Anan gesagt, dass ich um diese Uhrzeit hier sein soll."

    # Atropos Gedanken
    "Vielleicht hat er das Klopfen ja nicht gehört?"

    # Atropos Gedanken
    "Hmm…"

    if okaymood== False:
        "Wenn er nicht im Büro ist, könnte ich die Chance nutzen, mich dort mal umzusehen. Vielleicht finde ich ja irgendetwas heraus?"

    # Atropos Gedanken
    "Was soll ich tun?"

    # Symbiont
    "{i}Lass es besser bleiben, Atropos. Warte auf Anan! Du möchtest nicht noch mehr Ärger bekommen. Du willst doch glücklich sein. Ärger bringt kein Glück.{i}"

    # Symbiont
    "{i}Verhalte dich richtig. {i}"

    # Symbiont
    "{i}Triff die richtige Entscheidung.{i}"

    menu:
        "Ich trete einfach Mal ein und sehe dann weiter.":
            # Atropos Gedanken
            "Ich trete einfach mal ein und sehe dann weiter. Es wird schon nichts Schlimmes deswegen passieren."

            $ straight_anan_office = True
            jump selection_anan_office
        "Ich sollte besser vor der Tür auf Anan warten.":

            # Atropos Gedanken
            "Ich sollte besser vor der Tür auf Anan warten. Ich gehe lieber kein Risiko ein."

            # Atropos Gedanken
            "Ich will nicht noch mehr Ärger bekommen als ohnehin schon."

            jump conversation_with_anan

label conversation_with_anan:
    scene hall

    show anan normal_mid

    "Anan" "Atropos Laiotas. Ich lobe deine Pünktlichkeit. Folge mir!"

    # Atropos Gedanken
    "Ich kann nicht einschätzen, ob Anan gute oder schlechte Laune hat. Ich hoffe einfach nur, ich bekomme nicht zu viel Ärger."

    scene anan_office
    show anan normal_mid

    "Anan" "Nimm bitte Platz."

    "Atropos"  "Danke…"

    "Atropos"  "…"

    # Atropos Gedanken
    "Wieso sagt er denn nichts?"

    # Atropos Gedanken
    "Das macht mich nervös… soll ich etwa anfangen? Erwartet Anan eine Entschuldigung von mir?"

    if badmood:
        # Atropos Gedanken
        "Das kann er aber so was von vergessen. Es ist schon schlimm genug, dass ich seiner Aufforderung überhaupt gefolgt bin. Aber ich werde mich auf keinen Fall entschuldigen."

        # Atropos Gedanken
        "Niemals!"

        # Symbiont
        "{i}Entschuldige dich, egal aus welchem Grund. Willst du etwa noch mehr Ärger bekommen? {i}"

        # Symbiont
        "{i}Sowohl Anan als auch du werdet glücklicher sein, wenn du dich entschuldigst. Mehr als das will er nicht hören. Einfach nur eine Entschuldigung für dein Verhalten. {i}"

        # Symbiont
        "{i}Tu es! {i}"

    # alle

    "Atropos"  "Anan… es tut mir leid…"

    "Anan" "Es tut dir also leid."

    "Anan" "Ich bin mir noch nicht so sicher, ob du begreifst, was du für einen Schaden angerichtet hast. Sowohl bei dir selbst als auch bei deinen Mitmenschen."

    "Atropos"  "Schaden? Aber…"

    "Anan" "Ja, Schaden. Wenn du unglücklich bist, wirst du dadurch auch andere unglücklich machen. Du wirst sie aus ihrem glücklichen Leben herausreißen und ins Unglück stürzen."

    "Anan" "Verstehst du das, Atropos?"

    "Atropos"  "Ich…"

    "Anan" "Ich bin nicht dein Feind. Und auch Happiness ist es nicht. Wir wollen alle nur ein einziges Ziel: Dass alle Menschen glücklich sind."

    "Anan" "Dass alle Menschen eine Vergangenheit, eine Gegenwart, eine Zukunft haben können, die glücklich ist. Die sie erfüllt und die sorglos ist."

    "Anan" "Der Krieg war eine düstere Zeit voller Leid und Elend. Du kannst es dir nicht vorstellen und darüber solltest du froh sein."

    "Anan" "Du solltest dankbar sein für das Leben, das wir dir geschenkt haben."

    "Anan" "Du solltest dein Leben genießen und glücklich sein."

    "Anan" "Die Welt ist zerstört, es gibt nur noch Astoa, Peria und Keposa. Was denkst du würde passieren, wenn die Menschen alle aufhören würden Happiness zu nehmen?"

    "Anan" "Denkst du, das würde ein gutes Ende nehmen? In einer Welt, die immer noch aus den Fugen geraten ist?"

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

            "Anan" "Das ist also deine Antwort? Das ist die Antwort, zu der du gekommen bist?"

            "Atropos"  " Ja! Du kannst mich nicht dazu zwingen, Happiness zu nehmen! Ich kann mich einfach weigern!"

            "Anan" "Ich bin enttäuscht von dir Atropos. Ich habe mehr von dir erwartet."

            "Anan" "Ich dachte, dass du verstehen würdest, wie wichtig das Glück für die Menschen ist und dass du voll und ganz hinter Aither stehen würdest."

            "Anan" "Aber das scheint nicht der Fall zu sein. Was soll ich jetzt nur mit dir anstellen?"

            "Anan" "Kann man noch vernünftig mit dir reden und dich überzeugen? Oder gehörst du bereits zu den verlorenen Seelen?"

            "Atropos"  "Verlorene Seelen? Sprichst du von denen, die sich gegen Happiness wehren und die Pille verweigern?"

            "Anan" "Sie schaden mit ihrem Verhalten der gesamten Menschheit und bedrohen unsere Existenz. 'Verlorene Seelen' scheint da doch ein passendes Wort zu sein, nicht wahr?"

            "Anan" "Sie sind verloren, aber sie können gerettet werden. Wir können sie finden und ihnen die Wahrheit und Erkenntnis zurückbringen."

            "Anan" "Und genauso können wir auch dir helfen, Atropos. Alle verlorenen Seelen sind Teil der Menschheit und auch ihr Glück ist wichtig, egal wie egoistisch sie auch handeln mögen."

            "Anan" "Egal wie unwichtig ihnen das Glück der Menschheit auch ist, wir können sie läutern und dafür sorgen, dass eines Tages alle Menschen wahrhaftes Glück empfinden können."

            jump rueffel

label understanding:
    "Atropos"  "Du hast ja recht. Ich hätte Happiness niemals vergessen dürfen. Es war ein Fehler."

    "Atropos"  "Ein Fehler, den ich nicht mehr wiederholen werde. Es tut mir aufrichtig leid. Wirklich."

    "Atropos"  "Ich will glücklich sein und wenn Happiness der einzige Weg dorthin ist, dann werde ich diesem Weg folgen."

    "Anan" "Happiness ist der einzige Weg. Wir haben viele andere Wege versucht, aber keiner hatte den Erfolg gebracht, welchen wir uns erhofft hatten."

    "Anan" "Das Glück aller Menschen s teht an oberster Stelle und nur auf diese Weise können wir das Glück erreichen."

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
    jump takepillnow

label understandingpart2:

    "Atropos"  "Nein… nein, möchte ich nicht. Du hast ja recht."

    "Atropos"  "Es tut mir leid."

    "Atropos"  "Ich sollte aufhören, so viele Fragen zu stellen."

    "Anan" "Fragen sind gut. Fragen sind sogar wichtig, denn ohne Fragen kann man nicht zu Antworten kommen."

    "Anan" "Aber es ist wichtig, welche Art von Fragen gestellt werden. Es gibt falsche und es gibt richtige Fragen."

    "Anan" "Es gibt die Art von Fragen, die eine Rolle spielen. Die sinnvoll sind, die zu Veränderungen führen können."

    "Anan" "Aber es gibt auch die Art von Fragen, die Unheil mit sich bringen. Fragen, die gefährlich sind. Fragen, auf die man besser keine Antwort bekommen möchte."

    "Anan" "Fragen, die dafür sorgen, dass falsche Vorstellungen im Kopf der Menschen gepflanzt werden."

    "Anan" "Und die Frage nach Happiness ist eine eben solche Frage."

    "Anan" "Kannst du es denn nicht einfach akzeptieren und glücklich zu sein? Ich trage das Gewicht der Wahrheit auf meinen Schultern. Es sollte nicht auch noch auf deinen lasten müssen."

    "Atropos"  "Wie viele Menschen kennen die Wahrheit?"

    "Anan" "Es gibt keine universelle Wahrheit. Nur verschiedene Varianten von Lügen und Halbwahrheiten."

    "Anan" "Letztlich weiß wohl niemand genau, was die Wahrheit dahinter ist."

    "Anan" "Deine Frage zielt wohl eher darauf ab, wie viele Menschen die Wirkung von Happiness verstehen können? Nimmst du die Pille, wenn ich dir eine Antwort auf diese Frage gebe?"

    "Anan" "Bist du dann glücklich und akzeptierst dein Glück?"

    # Atropos Gedanken
    "Ich will eigentlich noch mehr wissen, aber mehr Antworten werde ich vermutlich nicht bekommen."

    # Atropos Gedanken
    "Also sollte ich mich vermutlich mit dieser Antwort zufriedengeben… oder?"

    # Symbiont
    "{i}Ja, solltest du. Anan hat recht, manchmal ist es besser nicht die vollständige Wahrheit zu kennen.{i}"

    # Atropos Gedanken
    "Ich frage mich nur, warum Anan nicht sagen kann, wie die Pille wirkt? Was kann das nur für eine Art von Wissen sein, das so gefährlich ist? Ich kann mir beim besten Willen nichts vorstellen."

    # Symbiont
    "{i}Spielt es eine Rolle? Du bist glücklich und Happiness schenkt dir eben jene Glücklichkeit. Ist es nicht egal, welche Wirkstoffe nun dafür sorgen, dass du glücklich bist? {i}"

    # Atropos Gedanken
    "Manchmal habe ich einfach das Gefühl, dass mehr hinter allem steckt als nur irgendwelche Wirkstoffe."

    # Atropos Gedanken
    "Ich kenne nicht alle Wirkstoffe der Happiness-Pille, aber die, die ich kenne, sind nützlich für den Körper, aber sorgen nicht für Glücklichkeit."

    # Atropos Gedanken
    "Und wie wird diese Glücklichkeit überhaupt erreicht? Nach was unterscheidet die Pille, was jedes einzelne Individuum glücklich macht?"

    # Symbiont
    "{i}Musst du diese Antworten wirklich kennen, um glücklich zu sein, Atropos? {i}"

    # Atropos Gedanken
    "Vermutlich nicht, oder?"

    # Symbiont
    "{i}Du bist ehrlich zu dir selbst. Danke. {i}"

    # Symbiont
    "{i}Dann sei wieder glücklich. Vergiss alles, was dich unglücklich macht. Nimm Happiness und lebe dein Leben so weiter, wie du es bisher gelebt hast. Glücklich und zufrieden. {i}"

    "Atropos" "Ich bin glücklich und ich werde die Pille nehmen. Ich brauche dafür die Wahrheit nicht. Weder die vollständige noch wie viele über die Wahrheit Bescheid wissen."

    "Anan" "Ich danke dir."

    "Anan" "Ich danke dir für das Glück, das du den Menschen aufgrund deiner Entscheidung schenkst."

    "Anan" "Mach weiter so, Atropos."

    "Anan" "Kehre jetzt ins Labor zurück und nimm deine Pille. Lebe dein Leben glücklich weiter."

    "Anan" "Ich wünsche dir einen Tag voller Glücklichkeit."

    "Atropos" "Danke vielmals. Ich dir auch."

    scene hall
    jump takepillnow


label questioning:
    "Atropos"  "Aber wirkt die Pille wirklich? Ich fühle mich auch ohne sie glücklich."

    "Atropos"  "Ich habe in der letzten Zeit keinerlei Veränderungen bemerkt, obwohl ich sie nicht genommen habe."

    "Atropos"  "Ich denke, ich bin glücklich."

    "Anan" "Du {b}denkst{/b} also, dass du glücklich bist? Aber weißt du es auch? Bist du dir ganz sicher, dass du glücklich bist?"

    "Anan" "Bevor du mir diese Frage nicht mit einem überzeugten {b}Ja{/b} beantworten kannst, bist du nicht glücklich."

    # Atropos Gedanken
    "Kann ich ihm die Frage mit einem überzeugten Ja beantworten? Ich weiß es nicht…"

    # Atropos Gedanken
    "Was, wenn es doch immer noch die Wirkung meiner letzten Pille ist, warum ich mich glücklich fühle?"

    "Atropos"  "…"

    "Anan" "Dein Schweigen ist mir Antwort genug."

    "Anan" "Die Pille ist für dein Glück verantwortlich. Ohne Happiness kannst du nicht glücklich sein."

    "Anan" "Nicht dauerhaft."

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

    "Anan" "Wieso spielt es für dich eine Rolle auf welche Weise sie dich glücklich macht?"

    "Anan" "Was ändert es?"

    "Atropos" "Alles… einfach alles… ich will die Wahrheit wissen… ist das Glück gar kein Glück, sondern einfach nur erzwungen? Nicht mehr als ein Schein?"

    "Anan" "Das Glück ist echt. Wie kann es falsches Glück geben? Glück ist, wenn du in einem Moment wirklich glücklich bist. Wenn es keine Sorgen, Zweifel und Probleme mehr gibt."

    "Anan" "Glück ist die Erfüllung menschlichen Wünschens und Strebens. Der Weg dorthin spielt keine Rolle."

    "Atropos" "Aber bin ich wirklich glücklich? Was ist, wenn ich unglücklich mit dem Glück bin, welches mir die Pille bringt?"

    "Anan" "Glück ist das persönliche Glück jedes Menschen. Happiness sorgt dafür, dass du dieses persönliche Glück erreichst. Es ist unmöglich, dass du mit deinem Glück unglücklich bist."

    "Atropos" "Du bleibst die ganze Zeit so schwammig mit deinen Aussagen. Warum kann ich keine klaren Antworten bekommen?"

    "Anan" "Weil es keine eindeutigen Antworten gibt und niemals geben wird. Uns bleibt allen nichts anderes als zu glauben, dass wir das Richtige tun und auf dem richtigen Weg sind."

    "Anan" "Und genau das tue ich."

    "Anan" "(wirft einen raschen Blick auf sein Handy) Ich muss weg."

    "Anan" "Dieses Gespräch ist noch nicht beendet. Wir setzen es fort, sobald ich zurück bin."

    hide Anan
    # Atropos Gedanken
    "Das war… seltsam… Anan wirkt so überzeugt von dem, was er sagt, aber irgendwie…"

    # Atropos Gedanken
    "Ich weiß nicht…"

    # Atropos Gedanken
    "Ich würde zu gerne mehr erfahren, was Happiness bewirkt. Was es in unseren Körpern mit uns anstellt."

    # Atropos Gedanken
    "Ob ich wohl hier in Anans Büro mehr dazu erfahre? Ich bin allein und könnte die Chance nutzen."

    # Symbiont
    "{i}Du scheinst es ja fast schon anzustreben unglücklich zu sein. Willst du dein Glück nur für ein paar Informationen riskieren? {i}"

    # Symbiont
    "{i}Manche Wahrheiten bleiben besser für immer verborgen… und außerdem, willst du einen noch größeren Anschiss riskieren? {i}"

    # Symbiont
    "{i}Hast du nicht genug davon? Wenn du so weiter machst, wirst du ernsthafte Konsequenzen erwarten müssen… und das würde dich bestimmt unglücklich machen. {i}"

    # Symbiont
    "{i}Lass dir Zeit und überlege noch einmal in Ruhe, ob du das wirklich tun möchtest.{i}"

    # Atropos Gedanken
    "Darüber muss ich nicht noch länger nachdenken. Ich weiß, was ich will."

    # Symbiont
    "{i}Tu es nicht, Atropos. Lass es sein! Bleib auf diesem Stuhl sitzen und warte, bis Anan zurückkommt. Du wirst dadurch glücklicher sein.{i}"

    # Symbiont
    "{i}Riskiere es nicht. Riskiere dein Glück nicht. Was auch immer hier in Anans Büro ist, geht dich nichts an.{i}"

    # Atropos Gedanken
    "Was soll ich nur tun?"

    jump selection_anan_office

label how_many_infos_anan:
    "Wie viele Sachen angesehen?"

    if infos_count_anan == 0:
        if  straight_anan_office:
            scene hall

            "Atropos verlässt das Büro wieder weil ihn Gewissensbisse (Symbiont) plagen, Anan kommt an, Schelte für Atropos weil er die Pille nicht genommen hat, Aufforderung dies jetzt zu tun"

            "Reaktion auf die Schelte"

            menu:
                "Wütend":
                    jump rueffel
                "Einsichtig":
                    jump understanding

        else:
            # Atropos Gedanken
            "Ich sollte mich besser nicht in Anans Büro umschauen."

            # Atropos Gedanken
            "Er könnte jeden Moment zurückkommen und außerdem gehört es sich einfach nicht."

            # Atropos Gedanken
            "Egal, welche Informationen ich auch daraus gewinnen könnte."

            # Atropos Gedanken
            "Mir hier und jetzt die Sachen anzuschauen, würde mich ins Unglück stürzen."

            # Atropos Gedanken
            "Ich werde einfach warten, bis Anan zurückkommt und nichts anrühren."

            # hier evtl Option sich die Bilder in Anans Büro näher anzuschauen und darüber Gedanken zu machen

            "Atropos" "…"
            # Atropos Gedanken
            "Ich frage mich nur… warum will Anan nicht mehr verraten? Welches Geheimnis steckt hinter Happiness?"

            # Symbiont
            "{i}Wieso ist dir das so wichtig? Es spielt keine Rolle. Vergiss es. Das sind alles überflüssige Informationen, die du nicht brauchst, um glücklich zu sein. {i}"

            # Symbiont
            "{i}Frage dich selbst: Warum willst du diese Informationen haben? Warum spielt es eine Rolle für dich? {i}"

            # Atropos Gedanken
            "Ich… ich weiß es nicht."

            # Symbiont
            "{i}Und das ist das Problem. Ohne Happiness bist du verwirrt. Unsicher. Ängstlich. Und einfach nicht glücklich. Mach dir nicht länger Gedanken und Sorgen darüber. {i}"

            # Symbiont
            "{i}Dein Leben könnte so viel einfacher sein. Einfacher und so viel glücklicher. {i}"

            # Atropos Gedanken
            "Glücklicher…"



            show normal_mid

            "Anan" "Wo waren wir stehen geblieben?"

            "Atropos" "Es… es tut mir leid."

            "Anan" "Welche Fakten tun dir leid?"

            "Atropos" "Ich denke ich hätte nicht so neugierig sein sollen. Du hast recht. Es ist gut so, wie es ist."

            "Anan" "Es freut mich zu hören, dass du zur Einsicht gekommen bist. Und glaube mir. Wir wollen alle nur das Beste für dich. Wir wollen alle nur, dass du glücklich sein kannst."

            "Atropos" "Ich weiß, es tut mir leid… ich wollte glücklich sein und das Glück auf meinem eigenen Weg erreichen, ohne zu erkennen, wie falsch das ist."

            "Atropos" "Was soll ich jetzt tun? Werde ich dafür bestraft, dass ich die Pille nicht genommen habe?"

            "Anan" "Kehre ins Labor zurück und nimm Happiness. Werd wieder glücklich. Du wirst nicht bestraft."

            "Anan" "Jeder macht mal Fehler und es sollen die belohnt werden, die danach wieder den richtigen Pfad einschlagen."

            "Anan" "Das ist das Wichtigste: Werde wieder glücklich, Atropos. Lebe das glückliche Leben, das du verdient hast."

            "Atropos" "Danke. Das werde ich tun."

            "Anan" "Und vielleicht findest du eines Tages Antworten auf die Fragen, die dich gerade verunsichern. Aber jetzt bist du noch nicht bereit."

            "Anan" "Sei geduldig und lass dich von den quälenden Fragen nicht länger peinigen. Sieh nach vorne und richte den Blick auf dein Glück."

            "Anan" "Und jetzt zurück an die Arbeit. Ich erwarte deinen Bericht heute noch. Hab einen Tag voller Glück!"

            "Atropos" "Danke, ich werde mein Bestes geben."

            scene hall
            jump takepillnow

    if infos_count_anan == 1 or infos_count_anan == 2:
        if  straight_anan_office:

            scene hall
            "Atropos verlässt das Büro und wartet auf Anan, welcher kurze Zeit später ankommt und anfängt Atropos wegen der nicht genommenen Pille zu rüffeln"

        else:
            # Atropos Gedanken
            "Ich sollte aufhören. Es ist zu riskant. Anan könnte jeden Moment zurückkommen und dabei sollte er mich besser nicht erwischen."

            # Symbiont
            "{i}Ja, lass die Finger von den Sachen, du hast genug gesehen. Deine Neugierde sollte schon längst befriedigt sein. Bist du jetzt glücklich? {i}"

            # Atropos Gedanken
            "Nach all dem, was ich gesehen habe, soll ich glücklich sein?"

            # Atropos Gedanken
            "Was habe ich da überhaupt alles gesehen? Ich kann es immer noch nicht richtig begreifen…"

            # Atropos Gedanken
            "Was hat das zu bedeuten? Soll ich Anan darauf ansprechen, wenn er zurückkommt?"


        jump one_or_two_infos

    if infos_count_anan == 3:
        if straight_anan_office:
            "Atropos erhebt sich vom Schreibtisch als Anan in seinem Büro kommt"

        $ last_try_find_kloth = True
        "Anan erwischt Atropos und es kommt zum riesen Streit, Atropos konfrontiert Anan mit den Hinweisen, Anan wirft ihn raus und kündigt den Rauswurf aus der Firma an"

        jump visit_kloth

label one_or_two_infos:
    "Anan mit den Tatsachen konfrontieren?"

    menu:
        "Ja":
            $ last_try_find_kloth = True
            jump face_anan
        "Nein":
            jump not_face_anan

label face_anan:
    $ bomb_trigger_choice = True

    "Riesen Streit, da Atropos in privaten Dokumenten geschnüffelt hat; Anan wirft Atropos raus und kündigt den Rauswurf aus der Firma an"

    jump  visit_kloth

label not_face_anan:
    scene hall

    "Atropos verlässt das Büro; Monolog über Sinn der Firma und Moralischen Aspekt"

    "Firma OK oder böse?"

    menu:
        "OK":
            jump back_to_work
        "Böse":
            $ rage_atropos_bomb = True
            $ face_anan_in_office = True
            $ bomb_trigger_choice = True
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
    $ rage_atropos_bomb = False
    scene hall

    "Sucht Kloth,"

    scene stairs_down

    "findet die Leiche im Treppenhaus"

    jump leave_or_corpse

label how_many_infos_kloth:

    "Wie viele Sachen angesehen?"

    if infos_count_kloth == 1 or infos_count_kloth == 2:
        jump choice_bomb

    if infos_count_kloth == 3:
        if last_try_find_kloth:
            jump last_search_kloth
        else:
            jump next_step_with_bomb

label last_search_kloth:
    $ rage_atropos_bomb = True
    "Kloth suchen?"

    menu:
        "Ja":
            jump end_search_kloth
        "Nein, diese Informationen sind genug":
            jump next_step_with_bomb

label end_search_kloth:
    scene hall

    "Sucht Kloth"

    scene stairs_down

    "findet die Leiche im Treppenhaus und erinnert sich dass er ihn selbst gestoßen hat"
    "Kann nicht begreifen, wie ein Produkt, welches Glücklichkeit verspricht so etwas bewirken kann/mit Menschen anstellen kann"

    scene hall
    "Verfällt in Wahnsinn,"
    scene server_room
    "sucht die Bombe auf und stellt den Timer auf 10 Minuten,"
    scene hall
    "geht dann (immer noch dem Wahnsinn verfallen) hinaus und Verbarrikadiert so viele Türen wie möglich"

    scene server_room
    "Kehrt zur Bombe zurück und setzt sich mit irrem Lachen davor und wartet bis sie runterzählt; hört auch klopfen und verwirrte Stimmen vor der Tür"

    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return

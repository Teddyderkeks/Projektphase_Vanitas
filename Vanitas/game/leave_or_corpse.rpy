default murderer = False
default reschedule_kloth = False

label leave_or_corpse:
    $ last_try_find_kloth = False
    $ weak_symbiont = True

    menu:
        "Ich kann die Leiche nicht einfach liegenlassen, ohne zu wissen, wer es ist!":
            jump kloth_corpse
        "Ich will das nicht sehen… ich habe Angst!":
            jump leave_and_go_pill

label leave_and_go_pill:
    # Atropos Gedanken
    "Ich will das nicht sehen… ich habe Angst."

    # Symbiont
    "{i}Ja, geh zurück! Geh zurück ins Labor und vergiss, was du gesehen hast. Nimm Happiness und werde glücklich! {/i}"

    # Atropos Gedanken
    "Vermutlich sollte ich Happiness wohl wirklich besser nehmen… ich will es einfach nur vergessen."

    # Atropos Gedanken
    "Ich will einfach nur glücklich sein. Mein Leben war zuvor so einfach und ohne Probleme… das hier macht mir Angst."

    scene lab

    # Atropos Gedanken
    "Wo habe ich die Pillen nur hingetan? Sind sie in meiner Tasche?"
    show era normal

    "Era" "Was… was ist los, Atropos?"

    "Atropos" "Hast du meine Happiness-Pillen gesehen? Ich kann sie nicht finden?"

    "Era" "Nein, leider nicht… tut mir leid… aber du kannst gerne eine von meinen haben… Also, wenn du möchtest."

    "Era" "Oder du nimmst eine aus dem Notfallset…"

    "Atropos" "Muss ich dann wohl. (lacht) Aber danke trotzdem für das Angebot, Era."

    "Era" "K-Kein Problem…"

    # Atropos Gedanken
    "Na los, ich tue das Richtige. Es ist die richtige Entscheidung Happiness zu nehmen."

    # Atropos Gedanken
    "Es ist die richtige Entscheidung, glücklich sein zu wollen."

    "Atropos" "(schluckt Happiness)"

    # Symbiont
    "{i}Gut gemacht. Und nun vergiss, was dich unglücklich gemacht hat. Vergiss all den Stress und deine Ängste. {i}"

    # Symbiont
    "{i}Denk an dein einziges Ziel im Leben: glücklich zu sein. Egal wie diese Art von Glück für dich auch aussehen mag. {i}"

    # Atropos Gedanken
    "Ich bin glücklich! Und nun zurück an die Arbeit- es dauert nicht mehr lange bis zur Mittagspause."

    jump escapelater

label kloth_corpse:
    # Atropos Gedanken
    "Ich kann die Leiche nicht einfach liegenlassen, ohne zu wissen, wer es ist!"

    # Atropos Gedanken
    "Trotzdem habe ich Angst…"

    scene corpse

    "Atropos" "Kloth?"

    "Atropos" "Nein, verdammt… Das darf doch nicht wahr sein…"

    "Atropos" "Das… das ist keine Illusion, oder? Es ist so real… das ganze Blut… und…"

    "Atropos" "So etwas kann ich mir nicht irgendwie einbilden, oder?"

    "Atropos" "Aber wie? Warum? Kloth?"

    "Atropos" "Kloth, bitte rede mit mir… Du kannst doch nicht tot sein…"

    "Atropos" "Kloth… bitte…"

    # Symbiont
    "{i}Pille, du musst deine Pille nehmen. Du halluzinierst, merkst du es denn nicht? Das hier kann nicht wahr sein. {i}"

    # Symbiont
    "{i}Wie könnte so etwas Schreckliches wahr sein? Du bist doch eigentlich glücklich.{i}"

    "Atropos" "Nein… es ist wahr… es ist wahr… ich will nicht, dass es wahr ist, aber es ist wahr…"

    "Atropos" "Kloth… Kloth… komm zu mir zurück. Bitte… ich… Wie soll ich nur ohne dich zurechtkommen? Du warst mein Leben lang an meiner Seite."

    "Atropos" "Ich brauche dich."

    "Atropos" "Ich…"

    "Atropos" "Bitte…"

    "Atropos" "Verdammt, das darf doch alles nicht wahr sein! Warum nur? Warum? Warum?"

    "Atropos" "WARUM?"

    "Atropos" "Kann das alles einfach nur ein schlechter Traum sein? Ich habe nicht die Kraft, es durchzustehen, falls es wirklich wahr sein sollte…"

    # Symbiont
    "{i}Ja, genau. Es ist nicht mehr als nur ein Traum. Du solltest weitergehen und eine Pause machen. Nimm die Pille, danach wird es dir besser gehen.{i}"

    "Atropos" "Ich weiß nicht mehr, was ich tun soll… Ich will weggehen, aber gleichzeitig habe ich das Gefühl, dass das hier real ist."

    "Atropos" "Ahhh- mein Kopf tut weh. Da ist irgendeine Erinnerung, aber ich bekomme sie nicht ganz zu fassen… Was ist das?"

    "Atropos" "Warte. Hatte ich mich nicht gestern mit Kloth unterhalten? Er kam zu mir und…?"

    show sepia
    show kloth smiling behind sepia
    scene stairs_up

    "Kloth" "Atropos!"

    "Atropos" "Kloth, was ist los?"

    "Kloth" "Ich habe dich überall gesucht. Endlich habe ich dich gefunden… ich muss mit dir reden. Hast du kurz einen Moment Zeit? Bitte…"

    "Atropos" "Beruhige dich erst einmal und atme tief durch. Was ist passiert? "

    "Kloth" "Nicht hier … es könnte jemand kommen und dann…"

    "Atropos" "Kloth, es ist alles in Ordnung. Niemand kann dir etwas tun. Was ist denn nur los mit dir?"

    # zeige Chesis klein weiter hinten

    "Kloth" "Ich… ich…"

    "Atropos" "Ich wollte eigentlich gerade Mittagspause machen. Willst du nicht einfach mitkommen und wir reden dann? Chesis scheint auch Pause zu haben."

    "Kloth" "Du hörst mir ja gar nicht richtig zu… bitte… ich… ich weiß nicht, an wen ich mich sonst wenden soll. Ich brauche dich jetzt."

    "Kloth" "Es gibt da etwas, das ich schon eine ganze Weile mit mir herumtrage und ich komme alleine einfach nicht damit klar. Bitte, ich muss mit jemandem darüber sprechen."

    "Kloth" "Du bist der Einzige, der mir helfen kann!"




    jump conversation_with_kloth

label conversation_with_kloth:
    if reschedule_kloth:
        menu:
            "Alles gut, von mir aus. Ich höre dir zu.":
                "Atropos" "Alles gut, von mir aus. Ich höre dir zu. Aber hier und jetzt. Ich möchte noch ein bisschen was von meiner Mittagspause haben."
                jump accept_conversation_kloth
            "Nein, tut mir leid, aber das ist mir alles zu riskant und unsicher.":
                "Atropos" "Nein, tut mir leid, aber das ist mir alles zu riskant und unsicher. Ich will lieber weiterhin mein glückliches Leben führen."
                jump refuse_conversation_kloth
    else:
        menu:
            "Ja, natürlich helfe ich dir. Erzähl endlich, was los ist. Wie kann ich dir helfen?":
                jump accept_conversation_kloth
            "Können wir das Gespräch vielleicht vertagen? Ich habe echt Hunger und will Chesis zudem nicht warten lassen.":
                jump reschedule_conversation_kloth
            "Tut mir leid, aber ich habe gerade nicht den Nerv für ein solches Gespräch.":
                jump refuse_conversation_kloth

label reschedule_conversation_kloth:
    $ reschedule_kloth = True
    "Atropos" "Können wir das Gespräch vielleicht vertagen? Ich habe echt Hunger und will Chesis zudem nicht warten lassen."

    "Kloth" "Kannst du dir nicht jetzt kurz fünf Minuten nehmen? Bitte… es dauert wirklich nicht lange…"

    "Atropos" "Muss es jetzt sein? Kloth, so wichtig kann es doch gar nicht sein, dass du nicht noch ein bisschen länger warten kannst, oder?"

    "Atropos" "Ich bezweifle sehr, dass du irgendwelche Staatsgeheimnisse entdeckt hast. Also los, entspann dich und wir sprechen wann anders darüber, okay?"

    "Kloth" "Jetzt hör mir doch bitte einen Moment zu… es braucht wirklich nicht lange, okay? Ich verspreche es dir…"

    "Atropos"  "Um was geht es denn überhaupt?"

    "Kloth" "Ich arbeite ja bei Anan als Chefsekretär und, nun ja… es ist alles nicht so wie es scheint, Atropos. Ich habe mehr erfahren und ich komme mit dieser Wahrheit nicht alleine klar…"

    "Atropos" "Wieso flüsterst du? So schlimm kann die Wahrheit schon nicht sein."

    "Kloth" "Und wie sie es ist. Sie ist gefährlich, vielleicht sogar tödlich… Bitte… können wir an einen ruhigen Ort gehen und ich erzähle dir dann alles?"

    # Symbiont
    "Rede nicht mit ihm! Er hat nichts Gutes im Sinn. Siehst du es denn nicht? Er versucht dich zu manipulieren und zu beeinflussen."

    # Symbiont
    "Siehst du nicht das grausame Lächeln, welches für einen Moment über sein Gesicht huschte? Lauf weg, solange du noch die Gelegenheit hast!"

    # Symbiont
    "Hast du nicht gehört, dass es sich um ein tödliches Wissen handelt? Willst du dich und deine Glücklichkeit in Gefahr bringen?"

    # Symbiont
    "Lehne das Gespräch ab. Es wäre ein großer Fehler, mit ihm zu sprechen. Er wird dein Glück zerstören und dich in einen dunklen Abgrund mitreißen."


    jump conversation_with_kloth

label accept_conversation_kloth:
    "Atropos" "Ja, natürlich helfe ich dir. Erzähl endlich, was los ist. Wie kann ich dir helfen?"

    "Kloth" "(atmet erleichtert auf) Danke Atropos! Wirklich… vielen, vielen Dank… du weißt nicht, wie froh ich bin endlich jemanden zu haben, dem ich mich anvertrauen kann."

    "Atropos" "Schon okay, nichts zu danken. Wir sind Freunde. Ich bin für dich da. Also, worum geht es?"

    "Kloth" "Die Happiness-Pille ist nicht das, was du und jeder andere Mensch auf dieser Welt denkt."

    "Atropos" "Von was redest du? Sie sorgt dafür, dass wir glücklich sind und endlich das Leben unserer Träume leben können. Nicht mehr und nicht weniger."

    "Kloth" "Nein, das stimmt nicht. Also doch… zum Teil schon, aber es ist nur die halbe Wahrheit. Die Tabletten bewirken nicht wirklich etwas…"

    "Atropos" "Hör auf, um den heißen Brei herumzureden und sag schon, was los ist."

    "Kloth" "Atropos. Es gibt etwas anderes, das die Menschen… "

    # Schwarzer Bildschirm, dann Glitch-Effekte

    # Symbiont
    "Hör nicht hin. Das sind nichts anderes als Lügen. Alles nur Lügen! Er ist vollkommen wahnsinnig. Siehst du es denn nicht? "

    # Symbiont
    "Er ist nicht glücklich und er wird auch dich unglücklich machen. Willst du dein restliches Leben in Furcht und Angst und Unglücklichkeit verbringen?"

    # Symbiont
    "Willst du ein tristes, graues Leben führen, wenn du ein Leben voller Farben und Freude haben kannst?"

    "Atropos" "Nein… nein, ich will ein glückliches Leben haben."
    # Ende Glitch-Effekt

    "Kloth" "Hast du was gesagt? Geht es dir gut? Du hast ziemlich weggetreten gewirkt."

    "Atropos" "Ich… was? Ja… ja, mir geht es gut… ich…"

    "Kloth" "Gut, ich hatte mir schon Sorgen gemacht. Also? Was meinst du sollen wir tun? Das müssen die Menschen erfahren. Wir können sie nicht im Unwissenden lassen…"

    # Symbiont
    "Ein glückliches Leben. Ein Leben voller Happiness."

    $ renpy.movie_cutscene("atropos_accepts_conversation.mpg")

    "Atropos" "Nein."

    "Atropos" "Nein!"

    "Atropos" "Kloth… verdammt… wie konnte das nur passieren? Und was habe ich nur getan? Was hatte ich tun wollen?"

    "Atropos" "Wie konnte er einem seiner besten Freunde so etwas antun? Wie hatte er Kloth in den Abgrund stürzen können?"

    "Atropos" "Hätte ich es verhindern können? Nein- das spielt keine Rolle. Ich hätte es verhindern müssen."

    "Atropos" "Das hätte alles niemals passieren dürfen. Ich werde… ich werde dafür sorgen, dass jemand dafür büßt."

    "Atropos" "Ich werde dich rächen, Kloth, das verspreche ich dir! Dein Mord wird nicht ungesühnt bleiben!"


    if back_to_work_bevore:
        "Was untersuchen?"
        jump selection_kloth_office_back_to_work
    else:
        jump ananorjustbombwho

label refuse_conversation_kloth:
    "Atropos" "Tut mir leid, aber ich habe gerade nicht den Nerv für ein solches Gespräch. Ich hatte heute einen stressigen Tag und brauche jetzt erstmal wieder etwas Ruhe und Entspannung."

    "Kloth" "Oh okay. Ja klar… wenn du nicht willst… ich kann dich nicht dazu zwingen. Ich wünschte, du hättest mir zugehört, Atropos. Ich dachte, wir wären Freunde."

    "Kloth" "Aber da habe ich mich wohl getäuscht. Ich habe mich in dir getäuscht. In dem Moment, in dem ich dich am meisten brauche, bist du nicht für mich da."

    # Symbiont
    "{i}Lass dir kein schlechtes Gewissen einreden. Du hast die richtige Entscheidung getroffen. {/i}"

    # Symbiont
    "{i}Wie kann er sich dein Freund nennen und dich gleichzeitig in ein tödliches Geheimnis einweihen wollen? So jemand darf sich nicht dein Freund schimpfen. {/i}"

    "Kloth" "Vielleicht ist Chesis ja ein besserer Freund. Vielleicht hört wenigstens er mir zu."

    "Kloth" "Wenn du doch jemals mehr wissen willst. Wähle das Gegenteil von Happiness."

    # Kloth gesellt sich zu Chesis

    "Kloth" "…"

    "Chesis" "…"

    "Kloth" "…"

    "Kloth" "Wir werden kontrolliert! Verstehst du das nicht?"

    "Kloth" "…"

    $ renpy.movie_cutscene("atropos_refuse_conversation.mpg")

    "Atropos" "Nein."

    "Atropos" "Nein!"

    "Atropos" "Kloth… verdammt… wie konnte das nur passieren?"

    "Atropos" "Dieser… dieser miese…. Ich dachte wir wären Freunde. Wie konnte Chesis ihm das nur antun?"

    "Atropos" "Wie konnte er einem seiner besten Freunde so etwas antun? Wie hatte er Kloth in den Abgrund stürzen können?"

    "Atropos" "Und ich… warum verdammt noch mal war ich nicht da, als er mich gebraucht hat? Dann wäre das alles nicht passiert."

    "Atropos" "Ich werde… ich werde dafür sorgen, dass jemand dafür büßt."

    "Atropos" "Ich werde dich rächen, Kloth, das verspreche ich dir! Dein Mord wird nicht ungesühnt bleiben!"

    "Atropos" "Chesis wird dafür büßen! Dafür sorge ich."

    if talkchesismorning:
        "Atropos" "Wie konnte er es wagen, heute Morgen so zu tun, als wäre das alles nicht passiert?"

        "Atropos" "Wie konnte er es wagen, mich anzulächeln und glücklich zu sein? Er hat es nicht verdient, glücklich zu sein. Keiner hat das."

    "Atropos" "Ich werde dich rächen, Kloth und wenn es das Letzte ist, was ich tue."


    if back_to_work_bevore:
        "Was untersuchen?"
        jump selection_kloth_office_back_to_work
    else:
        $ murderer = True
        jump ananorjustbombwho

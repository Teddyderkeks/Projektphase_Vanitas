default pilltakenyes = False
default pilltakenno = False
default pilltakenlater = False
default beginnoffice = False
default beginnlab = False
default pillnottakenananhall = False
default pillnottakenananhallananright = False
default pillnottakenananhallananwhy = False
default pillnottakenananhallananwrong = False
default gotoananofficeornot = False
default gotoananofficeornotyes = False
default gotoananofficeornotno = False
default whotolookfor = False
default whotolookforklothimmediately = False
default whotolookforklothlater = False
default whotolookforchesis = False
default whattosearchafteranansoffice = False
default whattosearchafteranansofficekloth = False
default whattosearchafteranansofficebacklab = False
default whattosearchafteranansofficeklothsoffice = False
default searchklothorsolveclue = False
default searchklothorsolveclueclue = False
default searchklothorsolvecluekloth = False
default searchklothorsolvecluehappiness = False
default savepeopleorkillall = False
default savepeopleorkillallsave = False
default savepeopleorkillallkill = False
default lookaroundklothsoffice = False
default lookaroundklothsofficewatchedatleastonethensearchedkloth = False
default lookaroundklothsofficeletter = False
default lookaroundklothsofficedocument = False
default lookaroundklothsofficepcpasswordcorrect = False
default lookaroundklothsofficepcpasswordwrong = False
default lookaroundklothsofficelab = False
default part14before = False
default part18before = False
default part14_2before = False
default part18_2before = False
default part14_3before = False
default part18_3before = False
default lookaroundklothsofficewatchedeverything = False
default lookaroundklothsofficewatcheddontsearchkloth = False
default takeerawithyoutobomb = False
default takeerawithyoutobombyes = False
default takeerawithyoutobombno = False
default whatwithbomb = False
default whatwithbombtrydefuse = False
default whatwithbombexplode = False
default whatwithbombsavepeoplebutexplode = False
default whatwithbombkillanan = False
default lookaroundinanansoffice = False
default lookaroundinanansofficeyes = False
default lookaroundinanansofficeyesatleastonebutnotall = False
default lookaroundinanansofficeyesatleastonebutnotallcomputer = False
default lookaroundinanansofficeyesatleastonebutnotalldocument = False
default lookaroundinanansofficeyesatleastonebutnotallletter = False
default lookaroundinanansofficeyesall = False
default lookaroundinanansofficeno = False
default lookaroundinanansofficenoangry = False
default lookaroundinanansofficenounderstanding = False
default lookaroundinanansofficenonounderstanding = False
default lookaroundinanansofficeseenatleastone = False
default lookaroundinanansofficeseenpcbutnoteverything = False
default lookaroundinanansofficeseendocumentbutnoteverything = False
default lookaroundinanansofficeseenletterbutnoteverything  = False
default lookaroundinanansofficeseeneverything = False
default lookaroundinanansofficeseennothing = False
default seekafterklothpng = False
default seekafterklothpngyes = False
default seekafterklothpngenoughinfo = False
default confrontanan = False
default confrontananyes = False
default confrontananno = False
default firmaok = False
default firmabad = False
default klothwatchedeverything = False
default savepeoplewarnoralarm = False
default savepeoplewarnoralarmbomb = False
default savepeoplewarnoralarmfriends = False
default savepeoplewarnoralarmfriendsera = False
default savepeoplewarnoralarmfriendseralab = False
default savepeoplewarnoralarmfriendseraelsewhere = False
default savepeoplewarnoralarmfriendschesis = False
default savepeoplewarnoralarmfriendskloth = False
default savepeoplewarnoralarmfriendstycho = False
default savepeoplewarnoralarmalarm = False
default foundcorpse = False
default foundcorpselook = False
default foundcorpsegoaway = False
default rememberklothtalk = False
default rememberklothtalkyes = False
default rememberklothtalkyeskillanan= False
default rememberklothtalkyeskillanannot = False
default rememberklothtalkno = False
default ruffle = False
default ruffleangry = False
default ruffleunderstanding = False
default backtoworkpart = False
default backtoworkparttakepill = False
default backtoworkparttalkfriends = False
default lategoback = False
default datewitheratakeherwithyou = False
default datewitheradonttakeherwithyou  = False
default takenarcaiswithyou = False
default donttakenarcaiswithyou = False
default pilltakenyesbutnosecret = False
default secretending = False
default klotheverythingseenbutnotsafeopen = False
default klotheverythingseensafeopen = False
default safeopen = False
default saneorseek = False
default endhappy= False
default endsad=False
default endcrazy=False


label ending:
    scene atropos_falling
    if endsad:
        play music ("Sound/cutscene_ende/loop_sad.mp3") fadein 3 fadeout 3
    else:
        if endhappy:
            play music ("Sound/cutscene_ende/loop_happy.mp3") fadein 3 fadeout 3
        else:
            if endcrazy:
                play music ("Sound/cutscene_ende/loop_crazy.mp3") fadein 3 fadeout 3

    if klotheverythingseenbutnotsafeopen== False and klotheverythingseensafeopen== False:

        #Symbiont
        symb "{i} Du bist so gut wie tot. Nicht mal mehr Sekunden dauert es, bis du auf dem Boden ankommst. {/i}"

        #Symbiont
        symb"{i} Du wirst sterben und es scheint keinen Ausweg aus dieser Lage zu geben. {/i}"

        #Symbiont
        symb"{i} Der Tag unseres Todes. Denkst du, dass du alles getan hast, das du tun konntest, um glücklich zu sein und in Frieden gehen zu können? {/i}"

        jump part1

    else:
        if klotheverythingseenbutnotsafeopen:
            #Symbiont
            "S." "{i} Du bist so gut wie tot. Nicht mal mehr Sekunden dauert es, bis du auf dem Boden ankommst. {/i}"

            #Symbiont
            "S.""{i} Du wirst sterben und es scheint keinen Ausweg aus dieser Lage zu geben. {/i}"

            #Symbiont
            "S.""{i} Der Tag unseres Todes. Denkst du, dass du alles getan hast, das du tun konntest, um glücklich zu sein und in Frieden gehen zu können? {/i}"

            jump part1_2
        else:
            if klotheverythingseensafeopen:
                #Symbiont
                "Kronos" "{i} Du bist so gut wie tot. Nicht mal mehr Sekunden dauert es, bis du auf dem Boden ankommst. {/i}"

                #Symbiont
                "Kronos""{i} Du wirst sterben und es scheint keinen Ausweg aus dieser Lage zu geben. {/i}"

                #Symbiont
                "Kronos""{i} Der Tag unseres Todes. Denkst du, dass du alles getan hast, das du tun konntest, um glücklich zu sein und in Frieden gehen zu können? {/i}"

                jump part1_3



label part1_2:

    if pilltakenyes:
        # Symbiont
        "S.""{i}Dein Glück lag in deinen Händen. Früh am Morgen hattest du dich für Happiness entschieden und die Pillen eingenommen. {/i}"
        jump part2_2
    else:
        if pilltakenno:
            # Symbiont
            "S.""{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du der Überzeugung, selbst darüber entscheiden zu wollen und hattest die Pillen nicht eingenommen. {/i}"
            jump part2_2
        else:
            if pilltakenlater:
                #Symbiont
                "S.""{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du dir nicht sicher, was genau das bedeutet. Du hattest dich dafür entschieden, die Pillen später zu nehmen. {/i}"
                jump part2_2

label part2_2:

    if beginnoffice:
        #Symbiont
        "S.""{i}Nachdem du auf der Arbeit angekommen warst, wolltest du deine Freunde aufsuchen. Hattest du die Zeit mit ihnen genossen? {/i}"

        #Symbiont
        "S.""{i}Deine Freunde waren dir schon immer wichtig. Ja, manchmal sogar wichtiger als dein eigenes Glück. {/i}"

        if pilltakenno or pilltakenlater:
            #Symbiont
            "S.""{i}Doch danach bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
            jump part3_2

        else:
            jump part5_2

    else:
        if beginnlab:
            #Symbiont
            "S.""{i}Nachdem du auf der Arbeit angekommen warst, wolltest du dich direkt an die Arbeit machen. Aber was war mit deinen Freunden? {/i}"

            if pilltakenyes:
                #Symbiont
                "S.""{i}Es gab für dich kaum etwas Schöneres als den Gedanken, dass deine Arbeit andere Menschen glücklich machte.{/i}"
                jump part5_2
            else:
                if pilltakenno or pilltakenlater:
                    # Symbiont
                    "S.""{i}Aber auf dem Weg dahin bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
                    jump part3_2

label part3_2:

    if pillnottakenananhall:
        if pillnottakenananhallananright:
            #Symbiont
            "S.""{i}Du musstest zugeben, dass Anan mit seinen Worten recht hatte. Hattest du dein eigenes Glück damit gefährdet, die Pille nicht zu nehmen? {/i}"

            #Symbiont
            "S.""{i}Das wolltest du natürlich nicht riskieren. {/i}"

            jump part12_2
        else:
            if pillnottakenananhallananwhy:
                #Symbiont
                "S.""{i}Nachdem Anan wieder weg war, hattest du deine Zweifel. Wieso sollte man die Pille brauchen? Glücklich sein konntest du auch ohne. Das dachtest du. {/i}"
                jump part12_2
            else:
                if pillnottakenananhallananwrong:
                    #Symbiont
                    "S.""{i}Auf Anans Worte wolltest du keinen Wert legen. Als Chef sollte er noch lange kein Recht über deine privaten Entscheidungen haben. {/i}"
                    jump part4_2


label part4_2:

    if gotoananofficeornot:
        if gotoananofficeornotyes:
            #Symbiont
            "S.""{i}Trotzdem hattest du dich dafür entschieden, seiner Bitte zu folgen und zu seinem Büro zu gehen. {/i}"
            jump part12_2
        else:
            if gotoananofficeornotno:
                #Symbiont
                "S.""{i}Deswegen hattest du dich dafür entschieden, nicht in sein Büro zu kommen. Doch Anan ließ dir keine Wahl. Oder hattest du die Wahl schon davor? {/i}"
                jump part18_2

label part5_2:

    if whotolookfor:
        if whotolookforklothimmediately:
            #Symbiont
            "S.""{i}In der Pause hattest du dich auf die Suche nach Kloth begeben. {/i}"
            #Symbiont
            "S.""{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
            jump part6_2

        else:
            if whotolookforklothlater:
                #Symbiont
                "S.""{i}In der Pause hattest du dich auf die Suche nach Chesis begeben. Aus Sorge um den dritten in eurem Bunde, wolltest du aber auch nach Kloth suchen. {/i}"
                #Symbiont
                "S.""{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
                jump part6_2

            else:
                if whotolookforchesis:
                    #Symbiont
                    "S.""{i}In der Pause hattest du dich auf die Suche nach Chesis begeben und deine Zeit mit ihm verbracht. {/i}"

                    #Symbiont
                    "S.""{i}Es sollten eure letzten gemeinsamen Minuten sein, ohne dass es euch bewusst war. Hättet ihr die Zeit anders nutzen können? Vielleicht mit Kloth? {/i}"

                    #Symbiont
                    "S.""{i} Als eure Zeit vorbei war, bist du zurück ins Labor gegangen. {/i}"
                    jump part10_2

label part6_2:

    if whattosearchafteranansoffice:
        if whattosearchafteranansofficekloth:
            #Symbiont
            "S.""{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

            #Symbiont
            "S.""{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. {/i}"

            #Symbiont
            "S.""{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

            #Symbiont
            "S.""{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
            jump part8_2

        else:
            if whattosearchafteranansofficebacklab:
                #Symbiont
                "S.""{i}Deine Pause neigte sich dem Ende zu und letztendlich musstest du aufgeben. War es die richtige Entscheidung, ins Labor zurückzukehren? {/i}"
                jump part10_2
            else:
                if whattosearchafteranansofficeklothsoffice:
                    #Symbiont
                    "S.""{i}Du warst schon immer ein neugieriger Junge, Atropos, nicht wahr? Dir ließ es keine Ruhe, dass dein Freund nicht erreichbar war. Du machtest dir Sorgen. {/i}"

                    #Symbiont
                    "S.""{i}Das war für dich Grund genug, um sein Büro zu durchsuchen. Dein Freund war wahnsinnig geworden. Hättest du das wirklich sehen sollen? {/i}"
                    jump part9_2

label part7_2:

    if searchklothorsolveclue:
        if searchklothorsolveclueclue:
            #Symbiont
            "S.""{i}Du wolltest den Hinweisen nachgehen, die er hinterlassen hatte – was du fandest, sollte deinen Tod verantworten. {/i}"
            jump part11_2
        else:
            if searchklothorsolvecluekloth:
                #Symbiont
                "S.""{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

                #Symbiont
                "S.""{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. {/i}"

                #Symbiont
                "S.""{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

                #Symbiont
                "S.""{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
                jump part8_2
            else:
                if searchklothorsolvecluehappiness:
                    #Symbiont
                    "S.""{i}Du wolltest zurück ins Labor. War das die richtige Entscheidung? {/i}"
                    jump part10_2



label part8_2:

    if savepeopleorkillall:
        if savepeopleorkillallsave:
            "S.""{i}Dein Versuch, deine Freunde zu retten, blieb ohne Erfolg. Sie wollten einfach nicht verstehen. Was konntest du nur tun? {/i}"
            jump part11_2
        if savepeopleorkillallkill:
            #Symbiont
            "S.""{i}Du wolltest niemanden mehr retten. Dein Freund, Kloth, starb und keinen interessierte es. Es machte dich glücklich, zu denken, dass dies die richtige Entscheidung sei. {/i}"
            jump part11_2

label part9_2:

    if lookaroundklothsoffice:
        if lookaroundklothsofficewatchedatleastonethensearchedkloth:
            #Symbiont
            "S.""{i}In seinem Büro bist du letztendlich fündig geworden. {/i}"
            if lookaroundklothsofficeletter:
                #Symbiont
                "S.""{i}Du hattest einen Brief von Kloth gefunden, adressiert an dich und Chesis. Darin verabschiedete er sich von euch, seinen besten Freunden. {/i}"
            if lookaroundklothsofficedocument:
                #Symbiont
                "S.""{i}Du hattest dir ein Dokument angesehen, das verriet, wie wichtig die Server im Gebäude wirklich waren. {/i}"
            if lookaroundklothsofficepcpasswordcorrect:
                #Symbiont
                "S.""{i}Am Computer hattest du das richtige Passwort eingegeben und eine Nachricht von Kloth gefunden. Er war es, der die Bombe gelegt hatte. {/i}"
            if lookaroundklothsofficepcpasswordwrong:
                #Symbiont
                "S.""{i}Am Computer konntest du nicht das richtige Passwort eingeben. Hättest du dort vielleicht mehr herausfinden könnten? {/i}"

                #Symbiont
                "S.""{i}Trotzdem bist du auf einen Blog gestoßen. In diesem wurde davon berichtet, dass sich eine Bombe im Gebäude befindet. {/i}"


            #Symbiont
            "S.""{i}Vielleicht hättest du mehr herausgefunden, wenn du dir noch mehr angesehen hättest?"
            if saneorseek:
                jump part13_2
            if part14_2before and confrontananno:
                jump part15_2
            if part14_2before and confrontananyes:
                jump part13_2
            if pilltakenyes:
                jump part7_2

        else:
            if lookaroundklothsofficewatchedeverything:

                #Symbiont
                "S.""{i}Nur nicht, wo er war. {/i}"
                if saneorseek:
                    jump part13_2
                if part14_2before and confrontananno:
                    jump part15_2
                if part14_2before and confrontananyes:
                    jump part13_2
                if pilltakenyes:
                        jump part7_2


            else:
                if lookaroundklothsofficewatcheddontsearchkloth:
                    #Symbiont
                    "S.""{i}Was du gefunden hattest, hatte dich beängstigt. Es hatte dich nicht glücklich gemacht, Atropos. Du hattest entschieden, zurück an die Arbeit zu gehen. {/i}"

                    #Symbiont
                    "S.""{i}Hätte es dich noch mehr in das Unglück getrieben, wenn du mehr herausgefunden hättest? {/i}"
                    jump part10_2

label part10_2:
    if takeerawithyoutobomb:
        if takeerawithyoutobombyes:
            #Symbiont
            "S.""{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Gemeinsam mit Era bist du zum Serverraum gegangen. {/i}"

            #Symbiont
            "S.""{i}Era hielt die Bombe in ihren Händen, als sie explodierte. {/i}"

            #Symbiont
            "S.""{i}Hattest du sie geliebt? Hat sie dich glücklich gemacht? {/i}"
            jump partend_2
        else:
            if takeerawithyoutobombno:
                #Symbiont
                "S.""{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Also bist du zum Serverraum gegangen. {/i}"

                #Symbiont
                "S.""{i}Dein Schicksal wurde besiegelt, bevor du wirklich realisieren konntest, was geschah. {/i}"

                #Symbiont
                "S.""{i}Du warst allein. Und jetzt wird dir bewusst, dass es anders hätte sein können. {/i}"
                jump partend_2

label part11_2:
    if whatwithbomb:
        if whatwithbombtrydefuse:
            #Symbiont
            "S.""{i}Du fandest die Bombe im Serverraum und wolltest sie entschärfen. Aber wie hättest du es ohne Erfahrung schaffen können? {/i}"

            #Symbiont
            "S.""{i}Die Bombe explodierte, während du nur versuchen wolltest, das zu retten, was dir wichtig war. {/i}"
            jump partend_2
        else:
            if whatwithbombexplode:
                #Symbiont
                "S.""{i}Der Gedanke, Kloths Werk zu vollenden, machte dich jedoch glücklich. Du fandest die Bombe im Serverraum und hattest dort darauf gewartet, dass die Zeit abläuft. {/i}"

                #Symbiont
                "S.""{i}Warst du auch glücklich, als du in den letzten Momenten an deine Freunde gedacht hattest? {/i}"

                #Symbiont
                "S.""{i}Wäre es anders gekommen, wenn du sie gerettet hättest? {/i}"
                jump partend_2
            else:
                if whatwithbombsavepeoplebutexplode:
                    #Symbiont
                    "S.""{i}All diese Erlebnisse haben dich nicht glücklich gemacht. Du wolltest, wie Kloth, Aither ein Ende setzen. {/i}"

                    #Symbiont
                    "S.""{i}Doch all deine Kollegen und Freunde – in deinen Augen konnten sie nichts dafür. Du wolltest sie retten, bevor die Bombe explodierte. {/i}"

                    #Symbiont
                    "S.""{i}Deine Zweifel, am Ende… Ich habe sie gehört. Würdest du noch zweifeln, wenn du etwas an deinen Entscheidungen ändern könntest? {/i}"
                    jump partend_2
                else:
                    if whatwithbombkillanan:
                        #Symbiont
                        "S.""{i}Du hattest dir einen Plan überlegt: Anan war derjenige, der sterben musste. Dazu musstest du ihn nur in den Serverraum locken. {/i}"

                        #Symbiont
                        "S.""{i}Vielleicht hattest du davor zu viel Zeit verloren – vielleicht hatte der Plan auch nie eine Chance. {/i}"
                        jump partend_2

label part12_2:
    if lookaroundinanansoffice:
        if lookaroundinanansofficeyes:

            if lookaroundinanansofficeyesatleastonebutnotall:
                #Symbiont
                "S.""{i}Als du bei Anans Büro angekommen bist, war er noch nicht da. Also hattest du dich dazu entschieden, dich ein wenig umzusehen. {/i}"

                #Symbiont
                "S.""{i}Glaubst du, dass es im Nachhinein eine gute Idee war, Atropos? {/i}"
                if lookaroundinanansofficeyesatleastonebutnotallcomputer:
                    #Symbiont
                    "S.""{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotalldocument:
                    #Symbiont
                    "S.""{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotallletter:
                    "S.""{i}Der Brief von Atlas an Anan hat dich neugierig gemacht. Aber hat sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"

                #Symbiont
                "S.""{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"
                jump part14_2

            else:
                if lookaroundinanansofficeyesall:
                    #Symbiont
                    "S.""{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                    #Symbiont
                    "S.""{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                    #Symbiont
                    "S.""{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"

                    jump part9_2
        else:
            if lookaroundinanansofficeno:
                #Symbiont
                "S.""{i}Geduldig hattest du auf Anan gewartet. Vielleicht hättest du etwas rausgefunden, wenn du dich umgesehen hättest? {/i}"

                #Symbiont
                "S.""{i}Anan war nicht amüsiert über die Tatsache, dass du deine Pille nicht genommen hattest. {/i}"

                if lookaroundinanansofficenoangry:
                    jump part18_2

                else:
                    if lookaroundinanansofficenounderstanding:
                        #Symbiont
                        "S.""{i}Aber du bist nach seiner Ansprache wieder zur Vernunft gekommen. War es dein Glück, oder die Besiegelung deines Todes? {/i}"

                        #Symbiont
                        "S.""{i}Du kanntest dein Schicksal nicht. Also bist du zurück in das Labor, um die Pille zu nehmen und weiter zu arbeiten. {/i}"
                        jump part19_2
                    else:
                        if lookaroundinanansofficenonounderstanding:
                            #Symbiont
                            "S.""{i}Doch es war dir egal, was er dir zu sagen hatte. War es ein Fehler, zu denken, dass du dein Glück in deine eigene Hand nehmen könntest? {/i}"

                            #Symbiont
                            "S.""{i}Du konntest aber die Chance nutzen, als Anan wegmusste, um sein Büro genauer unter die Lupe zu nehmen. {/i}"

                            if lookaroundinanansofficeseenatleastone:

                                if lookaroundinanansofficeseenpcbutnoteverything:
                                    #Symbiont
                                    "S.""{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"
                                if lookaroundinanansofficeseendocumentbutnoteverything:
                                    #Symbiont
                                    "S.""{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"
                                if lookaroundinanansofficeseenletterbutnoteverything:
                                    #Symbiont
                                   "S.""{i}Der Brief von Atlas an Anan hatte dich neugierig gemacht. Aber hatte sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"
                                #Symbiont
                                "S.""{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"

                                jump part14_2
                            else:
                                if lookaroundinanansofficeseeneverything:
                                    #Symbiont
                                    "S.""{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                                    #Symbiont
                                    "S.""{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                                    #Symbiont
                                    "S.""{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"
                                    jump part9_2
                                else:
                                    if lookaroundinanansofficeseennothing:
                                        #Symbiont
                                        "S.""{i}Du wolltest die Gelegenheit nicht nutzen. Vielleicht wäre alles anders gekommen, wenn du es getan hättest? {/i}"

                                        #Symbiont
                                        "S.""{i} Als Anan wieder zurückkam, schickte er dich zurück in das Büro, wo du die Pille nehmen solltest. {/i}"

                                        #Symbiont
                                        "S.""{i}Gesagt, getan… Und zurück an die Arbeit. {/i}"
                                        jump part19_2

label part13_2:
    if seekafterklothpng:
        if seekafterklothpngyes:
            #Symbiont
            "S.""{i}Als du ihn fandest, war es aber schon zu spät. {/i}"

            #Symbiont
            "S.""{i}Hörst du mich, Atropos? {/i}"

            #Symbiont
            "S.""{i}Du hattest alle in deinem Wahnsinn getötet. Bist du glücklich mit diesem Wissen? {/i}"
            jump partend_2
        else:
            if seekafterklothpngenoughinfo:
                #Symbiont
                "S.""{i}Du wolltest ihn nicht suchen. Du glaubtest, genug gesehen zu haben. {/i}"
                jump part11_2

label part14_2:
    $ part14_2before  = True
    if confrontanan:
        if confrontananyes:
            #Symbiont
            "S.""{i}War deine Neugier berechtigt? Du wolltest mehr herausfinden – die Wahrheit herausfinden. {/i}"

            #Symbiont
            "S.""{i}Deshalb hattest du Anan mit dem, was du gesehen hattest, konfrontiert. Doch das brachte dir keine weiteren hilfreichen Informationen. {/i}"

            #Symbiont
            "S.""{i}Nur seinen Ärger und eine Kündigung. Das hatte dich nur noch mehr dazu motiviert, in Kloths Büro weiterzusuchen. Nicht wahr? {/i}"
            if klothwatchedeverything == False:
                symb"{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                jump part16_2
            else:
                jump part9_2
        if confrontananno:
            if firmaok:
                #Symbiont
                "S.""{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb ein Geheimnis und du hattest dich danach zurück an deine Arbeit begeben. {/i}"
                jump part18_2
            else:
                if firmabad:
                    if klothwatchedeverything:
                        #Symbiont
                        "S.""{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        "S.""{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        "S.""{i}Du hast dir alles in Kloths Büro angesehen. Dadurch konntest du alles über die Bombe herausfinden. {/i}"

                        #Symbiont
                        #"S.""{i}Macht es dich glücklich zu wissen, dass du die Explosion nicht aufgehalten hattest? {/i}"
                        jump part9_2
                    else:
                        #Symbiont
                        "S.""{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        "S.""{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        "S.""{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                        jump part16_2


label part15_2:
    if savepeoplewarnoralarm:
        if savepeoplewarnoralarmbomb:
            #Symbiont
            "S.""{i}Allein bist du zum Serverraum gegangen… Deine Freunde, deine Kollegen, die Firma… Du wolltest sie nicht retten. {/i}"

            #Symbiont
            "S.""{i}Sag mir, Atropos, stehst du zu deinen Entscheidungen? {/i}"

            #Symbiont
            "S.""{i}Du hattest Zweifel, bis zum letzten Augenblick. Und nun hast du dein Schicksal besiegelt. {/i}"
            jump partend_2
        else:
            if savepeoplewarnoralarmfriends:
                #Symbiont
                "S.""{i}Trotz allem wolltest du deine Freunde warnen. Sie sollten nicht mit Aither untergehen. Aber die Zeit war begrenzt – das war dir bewusst. {/i}"
                if savepeoplewarnoralarmfriendsera:
                    #Symbiont
                    "S.""{i}Ich hatte schon gewusst, dass du dich für Era entscheiden würdest. Du hattest etwas für sie empfunden, nicht wahr? {/i}"
                    if savepeoplewarnoralarmfriendseralab:
                        #Symbiont
                        "S.""{i}Du konntest sie warnen, doch es war schon zu spät, um noch mehr zu tun. Eure beiden Lebensfäden wurden bemessen. {/i}"
                        jump partend_2
                    else:
                        if savepeoplewarnoralarmfriendseraelsewhere:
                            #Symbiont
                            "S.""{i}Auf der Suche nach ihr hattest du viel Zeit verloren. Sie stand gerade eben noch neben dir – im Flur. Gab es Momente, an denen du Zeit hättest sparen können? {/i}"
                            jump partend_2
                else:
                    if savepeoplewarnoralarmfriendschesis:
                        #Symbiont
                        "S.""{i}Du hattest dich dafür entschieden, deinen besten Freund zu warnen. Er schuldet dir jetzt sein Leben. Doch all deine anderen Freunde… hm…{/i}"
                        jump partend_2
                    else:
                        if savepeoplewarnoralarmfriendskloth:
                            #Symbiont
                            "S.""{i}Du wolltest Kloth suchen und fandest ihn. Für ihn war es jedoch schon zu spät… Hättest du die Zeit nutzen sollen, um jemand anderen zu retten? {/i}"
                            jump partend_2
                        else:
                            if savepeoplewarnoralarmfriendstycho:
                                #Symbiont
                                "S.""{i}Du wolltest Tycho retten. Auf dem Weg dahin hattest du es bereits geschafft, Armene vom Gehen zu überzeugen. Doch er schien dir nicht zuzuhören. {/i}"

                                #Symbiont
                                "S.""{i}Dein Versuch, den Feueralarm auszulösen, kam zu spät. {/i}"

                                #Symbiont
                                "S.""{i}Glaubst du, irgendwann einen Fehler gemacht zu haben, Atropos? {/i}"
                                jump partend_2
                            else:
                                if savepeoplewarnoralarmalarm:

                                    #Symbiont
                                    "S.""{i}Letztlich rettete Anan dein Glück und das Leben aller Menschen. {/i}"

                                    jump partend_2


label part16_2:
    if foundcorpse:
        if foundcorpselook:
            #Symiont
            "S.""{i}Dein Freund, Kloth… Es hatte dich unglücklich gemacht, ihn tot daliegen zu sehen. Die Erinnerung, die dir kam, machte es unerträglich. {/i}"
            jump part17_2
        else:
            if foundcorpsegoaway:
                #Symbiont
                "S.""{i}Als du deinen toten Freund daliegen gesehen hattest, wolltest du die richtige Entscheidung treffen. {/i}"

                #Symbiont
                "S.""{i}Du musstest glücklich werden, um keine schrecklichen Dinge mehr sehen zu können. Du brauchtest Happiness - und hattest sie eingenommen. {/i}"
                jump part20_2

label part17_2:
    if rememberklothtalk:
        if rememberklothtalkyes:
            #Symbiont
            "S.""{i}Kloth wollte mit dir reden, aber er sprach nur wirres Zeug. {/i}"

            #Symbiont
            "S.""{i}Ihr musstet es tun, Atropos. Ihr musstet glücklich sein. {/i}"
            if rememberklothtalkyeskillanan:
                #Symbiont
                "S.""{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend_2
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    "S.""{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend_2
        if rememberklothtalkno:
            #Symbiont
            "S.""{i}Kloth wollte mit dir reden. Er war verzweifelt. Du und Chesis – ihr beide wolltet einfach eure Glücklichkeit nicht riskieren. {/i}"

            #Symbtion
            "S.""{i}Siehst du es jetzt etwa anders? {/i}"

            if rememberklothtalkyeskillanan:
                #Symbiont
                "S.""{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend_2
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    "S.""{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend_2

label part18_2:
    $ part18_2before = True
    if ruffle:
        if ruffleangry:
            #Symbiont
            "S.""{i}Du warst wütend. Aber glaubst du, dass Anan dir die Kündigung angedroht hätte, wenn du glücklich gewesen wärst? {/i}"

            #Symbiont
            "S.""{i}Bist du dir immer noch sicher, dass du ohne Happiness glücklich sein konntest? Wohin hat es dich gebracht? {/i}"

            #Symbiont
            "S.""{i}Anans Büro konntest du nicht mehr erreichen. {/i}"
            jump partend_2
        if ruffleunderstanding:
            #Symbiont
            "S.""{i}Dachtest du, dass es der richtige Weg zum Glück sei, Vernunft zu zeigen? Du warst dir immer noch unsicher… {/i}"
            jump part19_2

label part19_2:
    if backtoworkpart:
        if backtoworkparttakepill:
            #Symbiont
            "S.""{i}Ich glaube, dass es eine gute Entscheidung von dir war, die Pille zu nehmen, als du zu deinem Arbeitsplatz zurückgekehrt bist. {/i}"

            #Symbiont
            "S.""{i}Aber denkst du das auch, jetzt wo wir hier sind? {/i}"
            if part18before:
                jump part12_2
            else:
                jump part20_2

        if backtoworkparttalkfriends:
            #Symbiont
            "S.""{i}Deine Kollegen schienen danach deine Kritik gar nicht wahrzunehmen. Hätte es sie vielleicht unglücklich gemacht? {/i}"

            #Symbiont
            "S.""{i}War vielleicht das auch der Grund, warum sie die Leiche nicht bemerkt hatten? {/i}"
            jump part16_2


label part20_2:
    if lategoback:
        #Symbiont
        "S.""{i}Deine Mittagspause hattest du dann mit Chesis verbracht. Es waren eure letzten gemeinsamen Minuten. {/i}"

        #Symbiont
        "S.""{i}Ihr wart gute Freunde. Vielleicht hätte er eine Chance gehabt zu überleben. {/i}"
        if datewithera:
            if datewitheratakeherwithyou:
                #Symbiont
                "S.""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Era im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                "S.""{i}Gib dir keine Schuld, Atropos. Sie ist gerne mit dir gegangen. Sie war glücklich, als sie neben dir stand und die Bombe explodierte. {/i}"
                jump partend_2
            else:
                if datewitheradonttakeherwithyou:
                    #Symbiont
                    "S.""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    "S.""{i}Du wirst nie erfahren, ob Era die Explosion überlebt hat. Vielleicht hattest du sie gerettet, vielleicht sterbt ihr beide in diesem Augenblick einsam. {/i}"
                    jump partend_2
        else:
            if takenarcaiswithyou:
                #Symbiont
                "S.""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Narcais im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                "S.""{i}Nun ist euer Schicksal besiegelt, doch Narcais war glücklich bis zum letzten Moment. {/i}"
                jump partend_2
            else:
                if donttakenarcaiswithyou:
                    #Symbiont
                    "S.""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und Narcais wollte im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    "S.""{i}Währenddessen bist du im Labor geblieben. Die Bombe explodierte, ohne dass jemand etwas dagegen tun konnte. Hättest du das verhindern können? {/i}"
                    jump partend_2



label partend_2:
    scene atropos_falling
    #Symbiont
    "S.""{i}… {/i}"

    #Symbiont
    "S.""{i}Du hast viele Entscheidungen getroffen. Eine einzige hätte alles ändern können. {/i}"

    # Symbiont
    "S.""{i}Warst du glücklich, Atropos? {/i}"

    # Symbiont
    "S.""{i}Bist du zufrieden mit den Entscheidungen, die du getroffen hast? {/i}"

    # Symbiont
    "S.""{i}Dein Glück ist letztlich das Einzige, das zählt. {/i}"

    if secretending:
        # Symbiont
        "S.""{i}Lebe wohl. {/i}"

        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")

        play music "Sound/Music/Rooms/verkaufsraum.mp3" fadeout 3 fadein 3

        scene street

        # Atropos Gedanken
        "S.""Heute ist ein guter Tag. Ein glücklicher Tag. Ein Tag voller Zufriedenheit und Erfüllung."

        # Atropos Gedanken
        "S.""Endlich fühle ich mich wirklich glücklich."

        # Atropos Gedanken
        "S.""Ich weiß nicht, warum ich in letzter Zeit unglücklicher gewesen war, aber jetzt bin ich glücklich und das ist das Einzige, das zählt."

        # Atropos Gedanken
        "S.""Da vorne ist ja auch schon Tartaros. Und nachher treffe ich mich mit meinen Freunden- besser kann der Tag gar nicht mehr werden."

        # Atropos Gedanken
        "S.""Ich bin froh für eine Firma wie Tartaros zu arbeiten. Es muss schrecklich für die Menschen gewesen sein, die in Aither gearbeitet hatten."

        # Atropos Gedanken
        "S.""Diese Bombe… einfach grauenhaft… wer könnte so etwas nur tun? All die Menschen, die gestorben sind…"

        # Atropos Gedanken
        "S.""Aber ich sollte mir keine Gedanken mehr darüber machen. Es liegt in der Vergangenheit und hat mich zum Glück nicht betroffen."

        # Atropos Gedanken
        "S.""Jetzt sollte ich mich ganz auf das Hier und Jetzt konzentrieren."

        # Atropos Gedanken
        "S.""Was steht heute alles an?"

        # Symbiont
        "S.""{i}Atropos. Bist du glücklich? {/i}"

        "Atropos" "Ja. Ja, das bin ich."

    else:
        if pilltakenyes:
            # Symbiont
            "S.""{i}Es tut mir leid. {/i}"
            if endhappy:
                $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_gluecklich.mpg")
                return
            else:
                if endsad:
                    $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
                    return
                else:
                    if endcrazy:
                        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_crazy.mpg")
                        return
        else:
            if pilltakenno or pilltakenlater:
                # Symbiont
                "S.""{i}Wir sterben gemeinsam. {/i}"
                if endhappy:
                    $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_gluecklich.mpg")
                    return
                else:
                    if endsad:
                        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
                        return
                    else:
                        if endcrazy:
                            $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_crazy.mpg")
                            return




label part1_3:

    if pilltakenyes:
        # Symbiont
        "Kronos""{i}Dein Glück lag in deinen Händen. Früh am Morgen hattest du dich für Happiness entschieden und die Pillen eingenommen. {/i}"
        jump part2_3
    else:
        if pilltakenno:
            # Symbiont
            "Kronos""{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du der Überzeugung, selbst darüber entscheiden zu wollen und hattest die Pillen nicht eingenommen. {/i}"
            jump part2_3
        else:
            if pilltakenlater:
                #Symbiont
                "Kronos""{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du dir nicht sicher, was genau das bedeutet. Du hattest dich dafür entschieden, die Pillen später zu nehmen. {/i}"
                jump part2_3

label part2_3:

    if beginnoffice:
        #Symbiont
        "Kronos""{i}Nachdem du auf der Arbeit angekommen warst, wolltest du deine Freunde aufsuchen. Hattest du die Zeit mit ihnen genossen? {/i}"

        #Symbiont
        "Kronos""{i}Deine Freunde waren dir schon immer wichtig. Ja, manchmal sogar wichtiger als dein eigenes Glück. {/i}"

        if pilltakenno or pilltakenlater:
            #Symbiont
            "Kronos""{i}Doch danach bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
            jump part3_3

        else:
            jump part5_3

    else:
        if beginnlab:
            #Symbiont
            "Kronos""{i}Nachdem du auf der Arbeit angekommen warst, wolltest du dich direkt an die Arbeit machen. Aber was war mit deinen Freunden? {/i}"

            if pilltakenyes:
                #Symbiont
                "Kronos""{i}Es gab für dich kaum etwas Schöneres als den Gedanken, dass deine Arbeit andere Menschen glücklich machte.{/i}"
                jump part5_3
            else:
                if pilltakenno or pilltakenlater:
                    # Symbiont
                    "Kronos""{i}Aber auf dem Weg dahin bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
                    jump part3_3

label part3_3:

    if pillnottakenananhall:
        if pillnottakenananhallananright:
            #Symbiont
            "Kronos""{i}Du musstest zugeben, dass Anan mit seinen Worten recht hatte. Hattest du dein eigenes Glück damit gefährdet, die Pille nicht zu nehmen? {/i}"

            #Symbiont
            "Kronos""{i}Das wolltest du natürlich nicht riskieren. {/i}"

            jump part12_3
        else:
            if pillnottakenananhallananwhy:
                #Symbiont
                "Kronos""{i}Nachdem Anan wieder weg war, hattest du deine Zweifel. Wieso sollte man die Pille brauchen? Glücklich sein konntest du auch ohne. Das dachtest du. {/i}"
                jump part12_3
            else:
                if pillnottakenananhallananwrong:
                    #Symbiont
                    "Kronos""{i}Auf Anans Worte wolltest du keinen Wert legen. Als Chef sollte er noch lange kein Recht über deine privaten Entscheidungen haben. {/i}"
                    jump part4_3


label part4_3:

    if gotoananofficeornot:
        if gotoananofficeornotyes:
            #Symbiont
            "Kronos""{i}Trotzdem hattest du dich dafür entschieden, seiner Bitte zu folgen und zu seinem Büro zu gehen. {/i}"
            jump part12_3
        else:
            if gotoananofficeornotno:
                #Symbiont
                "Kronos""{i}Deswegen hattest du dich dafür entschieden, nicht in sein Büro zu kommen. Doch Anan ließ dir keine Wahl. Oder hattest du die Wahl schon davor? {/i}"
                jump part18_3

label part5_3:

    if whotolookfor:
        if whotolookforklothimmediately:
            #Symbiont
            "Kronos""{i}In der Pause hattest du dich auf die Suche nach Kloth begeben. {/i}"
            #Symbiont
            "Kronos""{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
            jump part6_3

        else:
            if whotolookforklothlater:
                #Symbiont
                "Kronos""{i}In der Pause hattest du dich auf die Suche nach Chesis begeben. Aus Sorge um den dritten in eurem Bunde, wolltest du aber auch nach Kloth suchen. {/i}"
                #Symbiont
                "Kronos""{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
                jump part6_3

            else:
                if whotolookforchesis:
                    #Symbiont
                    "Kronos""{i}In der Pause hattest du dich auf die Suche nach Chesis begeben und deine Zeit mit ihm verbracht. {/i}"

                    #Symbiont
                    "Kronos""{i}Es sollten eure letzten gemeinsamen Minuten sein, ohne dass es euch bewusst war. Hättet ihr die Zeit anders nutzen können? Vielleicht mit Kloth? {/i}"

                    #Symbiont
                    "Kronos""{i} Als eure Zeit vorbei war, bist du zurück ins Labor gegangen. {/i}"
                    jump part10_3

label part6_3:

    if whattosearchafteranansoffice:
        if whattosearchafteranansofficekloth:
            #Symbiont
            "Kronos""{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

            #Symbiont
            "Kronos""{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. {/i}"

            #Symbiont
            "Kronos""{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

            #Symbiont
            "Kronos""{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
            jump part8_3

        else:
            if whattosearchafteranansofficebacklab:
                #Symbiont
                "Kronos""{i}Deine Pause neigte sich dem Ende zu und letztendlich musstest du aufgeben. War es die richtige Entscheidung, ins Labor zurückzukehren? {/i}"
                jump part10_3
            else:
                if whattosearchafteranansofficeklothsoffice:
                    #Symbiont
                    "Kronos""{i}Du warst schon immer ein neugieriger Junge, Atropos, nicht wahr? Dir ließ es keine Ruhe, dass dein Freund nicht erreichbar war. Du machtest dir Sorgen. {/i}"

                    #Symbiont
                    "Kronos""{i}Das war für dich Grund genug, um sein Büro zu durchsuchen. Dein Freund war wahnsinnig geworden. Hättest du das wirklich sehen sollen? {/i}"
                    jump part9_3

label part7_3:

    if searchklothorsolveclue:
        if searchklothorsolveclueclue:
            #Symbiont
            "Kronos""{i}Du wolltest den Hinweisen nachgehen, die er hinterlassen hatte – was du fandest, sollte deinen Tod verantworten. {/i}"
            jump part11_3
        else:
            if searchklothorsolvecluekloth:
                #Symbiont
                "Kronos""{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

                #Symbiont
                "Kronos""{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen.{/i}"

                #Symbiont
                "Kronos""{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

                #Symbiont
                "Kronos""{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
                jump part8_3
            else:
                if searchklothorsolvecluehappiness:
                    #Symbiont
                    "Kronos""{i}Du wolltest zurück ins Labor. War das die richtige Entscheidung? {/i}"
                    jump part10_3

label part8_3:

    if savepeopleorkillall:
        if savepeopleorkillallsave:
            "Kronos""{i}Dein Versuch, deine Freunde zu retten, blieb ohne Erfolg. Sie wollten einfach nicht verstehen. Was konntest du nur tun? {/i}"
            jump part11_3
        if savepeopleorkillallkill:
            #Symbiont
            "Kronos""{i}Du wolltest niemanden mehr retten. Dein Freund, Kloth, starb und keinen interessierte es. Es machte dich glücklich, zu denken, dass dies die richtige Entscheidung sei. {/i}"
            jump part11_3

label part9_3:

    if lookaroundklothsoffice:
        if lookaroundklothsofficewatchedatleastonethensearchedkloth:
            #Symbiont
            "Kronos""{i}In seinem Büro bist du letztendlich fündig geworden. {/i}"
            if lookaroundklothsofficeletter:
                #Symbiont
                "Kronos""{i}Du hattest einen Brief von Kloth gefunden, adressiert an dich und Chesis. Darin verabschiedete er sich von euch, seinen besten Freunden. {/i}"
            if lookaroundklothsofficedocument:
                #Symbiont
                "Kronos""{i}Du hattest dir ein Dokument angesehen, das verriet, wie wichtig die Server im Gebäude wirklich waren. {/i}"
            if lookaroundklothsofficepcpasswordcorrect:
                #Symbiont
                "Kronos""{i}Am Computer hattest du das richtige Passwort eingegeben und eine Nachricht von Kloth gefunden. Er war es, der die Bombe gelegt hatte. {/i}"
            if lookaroundklothsofficepcpasswordwrong:
                #Symbiont
                "Kronos""{i}Am Computer konntest du nicht das richtige Passwort eingeben. Hättest du dort vielleicht mehr herausfinden könnten? {/i}"

                #Symbiont
                "Kronos""{i}Trotzdem bist du auf einen Blog gestoßen. In diesem wurde davon berichtet, dass sich eine Bombe im Gebäude befindet. {/i}"

            #Symbiont
            "Kronos""{i}Vielleicht hättest du mehr herausgefunden, wenn du dir noch mehr angesehen hättest?"
            if saneorseek:
                jump part13_3
            if part14_3before and confrontananno:
                jump part15_3
            if part14_3before and confrontananyes:
                jump part13_3
            if pilltakenyes:
                jump part7_3

        else:
            if lookaroundklothsofficewatchedeverything:

                #Symbiont
                "Kronos""{i}Nur nicht, wo er war. {/i}"
                if saneorseek:
                    jump part13_3
                if part14_3before and confrontananno:
                    jump part15_3
                if part14_3before and confrontananyes:
                    jump part13_3
                if pilltakenyes:
                    jump part7_3

            else:
                if lookaroundklothsofficewatcheddontsearchkloth:
                    #Symbiont
                    "Kronos""{i}Was du gefunden hattest, hatte dich beängstigt. Es hatte dich nicht glücklich gemacht, Atropos. Du hattest entschieden, zurück an die Arbeit zu gehen. {/i}"

                    #Symbiont
                    "Kronos""{i}Hätte es dich noch mehr in das Unglück getrieben, wenn du mehr herausgefunden hättest? {/i}"
                    jump part10_3

label part10_3:
    if takeerawithyoutobomb:
        if takeerawithyoutobombyes:
            #Symbiont
            "Kronos""{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Gemeinsam mit Era bist du zum Serverraum gegangen. {/i}"

            #Symbiont
            "Kronos""{i}Era hielt die Bombe in ihren Händen, als sie explodierte. {/i}"

            #Symbiont
            "Kronos""{i}Hattest du sie geliebt? Hat sie dich glücklich gemacht? {/i}"
            jump partend_3
        else:
            if takeerawithyoutobombno:
                #Symbiont
                "Kronos""{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Also bist du zum Serverraum gegangen. {/i}"

                #Symbiont
                "Kronos""{i}Dein Schicksal wurde besiegelt, bevor du wirklich realisieren konntest, was geschah. {/i}"

                #Symbiont
                "Kronos""{i}Du warst allein. Und jetzt wird dir bewusst, dass es anders hätte sein können. {/i}"
                jump partend_3

label part11_3:
    if whatwithbomb:
        if whatwithbombtrydefuse:
            #Symbiont
            "Kronos""{i}Du fandest die Bombe im Serverraum und wolltest sie entschärfen. Aber wie hättest du es ohne Erfahrung schaffen können? {/i}"

            #Symbiont
            "Kronos""{i}Die Bombe explodierte, während du nur versuchen wolltest, das zu retten, was dir wichtig war. {/i}"
            jump partend_3
        else:
            if whatwithbombexplode:
                #Symbiont
                "Kronos""{i}Der Gedanke, Kloths Werk zu vollenden, machte dich jedoch glücklich. Du fandest die Bombe im Serverraum und hattest dort darauf gewartet, dass die Zeit abläuft. {/i}"

                #Symbiont
                "Kronos""{i}Warst du auch glücklich, als du in den letzten Momenten an deine Freunde gedacht hattest? {/i}"

                #Symbiont
                "Kronos""{i}Wäre es anders gekommen, wenn du sie gerettet hättest? {/i}"
                jump partend_3
            else:
                if whatwithbombsavepeoplebutexplode:
                    #Symbiont
                    "Kronos""{i}All diese Erlebnisse haben dich nicht glücklich gemacht. Du wolltest, wie Kloth, Aither ein Ende setzen. {/i}"

                    #Symbiont
                    "Kronos""{i}Doch all deine Kollegen und Freunde – in deinen Augen konnten sie nichts dafür. Du wolltest sie retten, bevor die Bombe explodierte. {/i}"

                    #Symbiont
                    "Kronos""{i}Deine Zweifel, am Ende… Ich habe sie gehört. Würdest du noch zweifeln, wenn du etwas an deinen Entscheidungen ändern könntest? {/i}"
                    jump partend_3
                else:
                    if whatwithbombkillanan:
                        #Symbiont
                        "Kronos""{i}Du hattest dir einen Plan überlegt: Anan war derjenige, der sterben musste. Dazu musstest du ihn nur in den Serverraum locken. {/i}"

                        #Symbiont
                        "Kronos""{i}Vielleicht hattest du davor zu viel Zeit verloren – vielleicht hatte der Plan auch nie eine Chance. {/i}"
                        jump partend_3

label part12_3:
    if lookaroundinanansoffice:
        if lookaroundinanansofficeyes:

            if lookaroundinanansofficeyesatleastonebutnotall:
                #Symbiont
                "Kronos""{i}Als du bei Anans Büro angekommen bist, war er noch nicht da. Also hattest du dich dazu entschieden, dich ein wenig umzusehen. {/i}"

                #Symbiont
                "Kronos""{i}Glaubst du, dass es im Nachhinein eine gute Idee war, Atropos? {/i}"
                if lookaroundinanansofficeyesatleastonebutnotallcomputer:
                    #Symbiont
                    "Kronos""{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotalldocument:
                    #Symbiont
                    "Kronos""{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotallletter:
                    "Kronos""{i}Der Brief von Atlas an Anan hat dich neugierig gemacht. Aber hat sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"

                #Symbiont
                "Kronos""{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"
                jump part14_3

            else:
                if lookaroundinanansofficeyesall:
                    #Symbiont
                    "Kronos""{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                    #Symbiont
                    "Kronos""{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                    #Symbiont
                    "Kronos""{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"

                    jump part9_3
        else:
            if lookaroundinanansofficeno:
                #Symbiont
                "Kronos""{i}Geduldig hattest du auf Anan gewartet. Vielleicht hättest du etwas rausgefunden, wenn du dich umgesehen hättest? {/i}"

                #Symbiont
                "Kronos""{i}Anan war nicht amüsiert über die Tatsache, dass du deine Pille nicht genommen hattest. {/i}"

                if lookaroundinanansofficenoangry:
                    jump part18_3

                else:
                    if lookaroundinanansofficenounderstanding:
                        #Symbiont
                        "Kronos""{i}Aber du bist nach seiner Ansprache wieder zur Vernunft gekommen. War es dein Glück, oder die Besiegelung deines Todes? {/i}"

                        #Symbiont
                        "Kronos""{i}Du kanntest dein Schicksal nicht. Also bist du zurück in das Labor, um die Pille zu nehmen und weiter zu arbeiten. {/i}"
                        jump part19_3
                    else:
                        if lookaroundinanansofficenonounderstanding:
                            #Symbiont
                            "Kronos""{i}Doch es war dir egal, was er dir zu sagen hatte. War es ein Fehler, zu denken, dass du dein Glück in deine eigene Hand nehmen könntest? {/i}"

                            #Symbiont
                            "Kronos""{i}Du konntest aber die Chance nutzen, als Anan wegmusste, um sein Büro genauer unter die Lupe zu nehmen. {/i}"

                            if lookaroundinanansofficeseenatleastone:

                                if lookaroundinanansofficeseenpcbutnoteverything:
                                    #Symbiont
                                    "Kronos""{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"
                                if lookaroundinanansofficeseendocumentbutnoteverything:
                                    #Symbiont
                                    "Kronos""{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"
                                if lookaroundinanansofficeseenletterbutnoteverything:
                                    #Symbiont
                                   "Kronos""{i}Der Brief von Atlas an Anan hatte dich neugierig gemacht. Aber hatte sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"
                                #Symbiont
                                "Kronos""{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"

                                jump part14_3
                            else:
                                if lookaroundinanansofficeseeneverything:
                                    #Symbiont
                                    "Kronos""{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                                    #Symbiont
                                    "Kronos""{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                                    #Symbiont
                                    "Kronos""{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"
                                    jump part9_3
                                else:
                                    if lookaroundinanansofficeseennothing:
                                        #Symbiont
                                        "Kronos""{i}Du wolltest die Gelegenheit nicht nutzen. Vielleicht wäre alles anders gekommen, wenn du es getan hättest? {/i}"

                                        #Symbiont
                                        "Kronos""{i} Als Anan wieder zurückkam, schickte er dich zurück in das Büro, wo du die Pille nehmen solltest. {/i}"

                                        #Symbiont
                                        "Kronos""{i}Gesagt, getan… Und zurück an die Arbeit. {/i}"
                                        jump part19_3

label part13_3:
    if seekafterklothpng:
        if seekafterklothpngyes:
            #Symbiont
            "Kronos""{i}Als du ihn fandest, war es aber schon zu spät. {/i}"

            #Symbiont
            "Kronos""{i}Hörst du mich, Atropos? {/i}"

            #Symbiont
            "Kronos""{i}Du hattest alle in deinem Wahnsinn getötet. Bist du glücklich mit diesem Wissen? {/i}"
            jump partend_3
        else:
            if seekafterklothpngenoughinfo:
                #Symbiont
                "Kronos""{i}Du wolltest ihn nicht suchen. Du glaubtest, genug gesehen zu haben. {/i}"
                jump part11_3

label part14_3:
    $ part14_3before = True
    if confrontanan:
        if confrontananyes:
            #Symbiont
            "Kronos""{i}War deine Neugier berechtigt? Du wolltest mehr herausfinden – die Wahrheit herausfinden. {/i}"

            #Symbiont
            "Kronos""{i}Deshalb hattest du Anan mit dem, was du gesehen hattest, konfrontiert. Doch das brachte dir keine weiteren hilfreichen Informationen. {/i}"

            #Symbiont
            "Kronos""{i}Nur seinen Ärger und eine Kündigung. Das hatte dich nur noch mehr dazu motiviert, in Kloths Büro weiterzusuchen. Nicht wahr? {/i}"

            if klothwatchedeverything == False:
                symb"{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                jump part16_3
            else:
                jump part9_3
        if confrontananno:
            if firmaok:
                #Symbiont
                "Kronos""{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb ein Geheimnis und du hattest dich danach zurück an deine Arbeit begeben. {/i}"
                jump part18_3
            else:
                if firmabad:
                    if klothwatchedeverything:
                        #Symbiont
                        "Kronos""{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        "Kronos""{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        "Kronos""{i}Du hast dir alles in Kloths Büro angesehen. Dadurch konntest du alles über die Bombe herausfinden. {/i}"

                        jump part9_3
                    else:
                        #Symbiont
                        "Kronos""{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        "Kronos""{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        "Kronos""{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                        jump part16_3


label part15_3:
    if savepeoplewarnoralarm:
        if savepeoplewarnoralarmbomb:
            #Symbiont
            "Kronos""{i}Allein bist du zum Serverraum gegangen… Deine Freunde, deine Kollegen, die Firma… Du wolltest sie nicht retten. {/i}"

            #Symbiont
            "Kronos""{i}Sag mir, Atropos, stehst du zu deinen Entscheidungen? {/i}"

            #Symbiont
            "Kronos""{i}Du hattest Zweifel, bis zum letzten Augenblick. Und nun hast du dein Schicksal besiegelt. {/i}"
            jump partend_3
        else:
            if savepeoplewarnoralarmfriends:
                #Symbiont
                "Kronos""{i}Trotz allem wolltest du deine Freunde warnen. Sie sollten nicht mit Aither untergehen. Aber die Zeit war begrenzt – das war dir bewusst. {/i}"
                if savepeoplewarnoralarmfriendsera:
                    #Symbiont
                    "Kronos""{i}Ich hatte schon gewusst, dass du dich für Era entscheiden würdest. Du hattest etwas für sie empfunden, nicht wahr? {/i}"
                    if savepeoplewarnoralarmfriendseralab:
                        #Symbiont
                        "Kronos""{i}Du konntest sie warnen, doch es war schon zu spät, um noch mehr zu tun. Eure beiden Lebensfäden wurden bemessen. {/i}"
                        jump partend_3
                    else:
                        if savepeoplewarnoralarmfriendseraelsewhere:
                            #Symbiont
                            "Kronos""{i}Auf der Suche nach ihr hattest du viel Zeit verloren. Sie stand gerade eben noch neben dir – im Flur. Gab es Momente, an denen du Zeit hättest sparen können? {/i}"
                            jump partend_3
                else:
                    if savepeoplewarnoralarmfriendschesis:
                        #Symbiont
                        "Kronos""{i}Du hattest dich dafür entschieden, deinen besten Freund zu warnen. Er schuldet dir jetzt sein Leben. Doch all deine anderen Freunde… hm…{/i}"
                        jump partend_3
                    else:
                        if savepeoplewarnoralarmfriendskloth:
                            #Symbiont
                            "Kronos""{i}Du wolltest Kloth suchen und fandest ihn. Für ihn war es jedoch schon zu spät… Hättest du die Zeit nutzen sollen, um jemand anderen zu retten? {/i}"
                            jump partend_3
                        else:
                            if savepeoplewarnoralarmfriendstycho:
                                #Symbiont
                                "Kronos""{i}Du wolltest Tycho retten. Auf dem Weg dahin hattest du es bereits geschafft, Armene vom Gehen zu überzeugen. Doch er schien dir nicht zuzuhören. {/i}"

                                #Symbiont
                                "Kronos""{i}Dein Versuch, den Feueralarm auszulösen, kam zu spät. {/i}"

                                #Symbiont
                                "Kronos""{i}Glaubst du, irgendwann einen Fehler gemacht zu haben, Atropos? {/i}"
                                jump partend_3
                            else:
                                if savepeoplewarnoralarmalarm:

                                    "Kronos""{i}Letztlich rettete Anan dein Glück und das Leben aller Menschen. {/i}"

                                    jump partend_3


label part16_3:
    if foundcorpse:
        if foundcorpselook:
            #Symiont
            "Kronos""{i}Dein Freund, Kloth… Es hatte dich unglücklich gemacht, ihn tot daliegen zu sehen. Die Erinnerung, die dir kam, machte es unerträglich. {/i}"
            jump part17_3
        else:
            if foundcorpsegoaway:
                #Symbiont
                "Kronos""{i}Als du deinen toten Freund daliegen gesehen hattest, wolltest du die richtige Entscheidung treffen. {/i}"

                #Symbiont
                "Kronos""{i}Du musstest glücklich werden, um keine schrecklichen Dinge mehr sehen zu können. Du brauchtest Happiness - und hattest sie eingenommen. {/i}"
                jump part20_3

label part17_3:
    if rememberklothtalk:
        if rememberklothtalkyes:
            #Symbiont
            "Kronos""{i}Kloth wollte mit dir reden, aber er sprach nur wirres Zeug. {/i}"

            #Symbiont
            "Kronos""{i}Ihr musstet es tun, Atropos. Ihr musstet glücklich sein. {/i}"
            if rememberklothtalkyeskillanan:
                #Symbiont
                "Kronos""{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend_3
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    "Kronos""{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend_3
        if rememberklothtalkno:
            #Symbiont
            "Kronos""{i}Kloth wollte mit dir reden. Er war verzweifelt. Du und Chesis – ihr beide wolltet einfach eure Glücklichkeit nicht riskieren. {/i}"

            #Symbtion
            "Kronos""{i}Siehst du es jetzt etwa anders? {/i}"

            if rememberklothtalkyeskillanan:
                #Symbiont
                "Kronos""{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend_3
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    "Kronos""{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend_3

label part18_3:
    $ part18_3before = True
    if ruffle:
        if ruffleangry:
            #Symbiont
            "Kronos""{i}Du warst wütend. Aber glaubst du, dass Anan dir die Kündigung angedroht hätte, wenn du glücklich gewesen wärst? {/i}"

            #Symbiont
            "Kronos""{i}Bist du dir immer noch sicher, dass du ohne Happiness glücklich sein konntest? Wohin hat es dich gebracht? {/i}"

            #Symbiont
            "Kronos""{i}Anans Büro konntest du nicht mehr erreichen. {/i}"
            jump partend_3
        if ruffleunderstanding:
            #Symbiont
            "Kronos""{i}Dachtest du, dass es der richtige Weg zum Glück sei, Vernunft zu zeigen? Du warst dir immer noch unsicher… {/i}"
            jump part19_3

label part19_3:
    if backtoworkpart:
        if backtoworkparttakepill:
            #Symbiont
            "Kronos""{i}Ich glaube, dass es eine gute Entscheidung von dir war, die Pille zu nehmen, als du zu deinem Arbeitsplatz zurückgekehrt bist. {/i}"

            #Symbiont
            "Kronos""{i}Aber denkst du das auch, jetzt wo wir hier sind? {/i}"
            if part18before:
                jump part12_3
            else:
                jump part20_3

        if backtoworkparttalkfriends:
            #Symbiont
            "Kronos""{i}Deine Kollegen schienen danach deine Kritik gar nicht wahrzunehmen. Hätte es sie vielleicht unglücklich gemacht? {/i}"

            #Symbiont
            "Kronos""{i}War vielleicht das auch der Grund, warum sie die Leiche nicht bemerkt hatten? {/i}"
            jump part16_3


label part20_3:
    if lategoback:
        #Symbiont
        "Kronos""{i}Deine Mittagspause hattest du dann mit Chesis verbracht. Es waren eure letzten gemeinsamen Minuten. {/i}"

        #Symbiont
        "Kronos""{i}Ihr wart gute Freunde. Vielleicht hätte er eine Chance gehabt zu überleben. {/i}"
        if datewithera:
            if datewitheratakeherwithyou:
                #Symbiont
                "Kronos""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Era im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                "Kronos""{i}Gib dir keine Schuld, Atropos. Sie ist gerne mit dir gegangen. Sie war glücklich, als sie neben dir stand und die Bombe explodierte. {/i}"
                jump partend_3
            else:
                if datewitheradonttakeherwithyou:
                    #Symbiont
                    "Kronos""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    "Kronos""{i}Du wirst nie erfahren, ob Era die Explosion überlebt hat. Vielleicht hattest du sie gerettet, vielleicht sterbt ihr beide in diesem Augenblick einsam. {/i}"
                    jump partend_3
        else:
            if takenarcaiswithyou:
                #Symbiont
                "Kronos""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Narcais im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                "Kronos""{i}Nun ist euer Schicksal besiegelt, doch Narcais war glücklich bis zum letzten Moment. {/i}"
                jump partend_3
            else:
                if donttakenarcaiswithyou:
                    #Symbiont
                    "Kronos""{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und Narcais wollte im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    "Kronos""{i}Währenddessen bist du im Labor geblieben. Die Bombe explodierte, ohne dass jemand etwas dagegen tun konnte. Hättest du das verhindern können? {/i}"
                    jump partend_3

label partend_3:
    scene atropos_falling
    #Symbiont
    "Kronos""{i}… {/i}"

    #Symbiont
    "Kronos""{i}Du hast viele Entscheidungen getroffen. Eine einzige hätte alles ändern können. {/i}"

    # Symbiont
    "Kronos""{i}Warst du glücklich, Atropos? {/i}"

    # Symbiont
    "Kronos""{i}Bist du zufrieden mit den Entscheidungen, die du getroffen hast? {/i}"

    # Symbiont
    "Kronos""{i}Dein Glück ist letztlich das Einzige, das zählt. {/i}"

    if secretending:
        # Symbiont
        "Kronos""{i}Lebe wohl. {/i}"

        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
        play music "Sound/Music/Rooms/verkaufsraum.mp3" fadeout 3 fadein 3
        scene street

        # Atropos Gedanken
        "Kronos""Heute ist ein guter Tag. Ein glücklicher Tag. Ein Tag voller Zufriedenheit und Erfüllung."

        # Atropos Gedanken
        "Kronos""Endlich fühle ich mich wirklich glücklich."

        # Atropos Gedanken
        "Kronos""Ich weiß nicht, warum ich in letzter Zeit unglücklicher gewesen war, aber jetzt bin ich glücklich und das ist das Einzige, das zählt."

        # Atropos Gedanken
        "Kronos""Da vorne ist ja auch schon Tartaros. Und nachher treffe ich mich mit meinen Freunden- besser kann der Tag gar nicht mehr werden."

        # Atropos Gedanken
        "Kronos""Ich bin froh für eine Firma wie Tartaros zu arbeiten. Es muss schrecklich für die Menschen gewesen sein, die in Aither gearbeitet hatten."

        # Atropos Gedanken
        "Kronos""Diese Bombe… einfach grauenhaft… wer könnte so etwas nur tun? All die Menschen, die gestorben sind…"

        # Atropos Gedanken
        "Kronos""Aber ich sollte mir keine Gedanken mehr darüber machen. Es liegt in der Vergangenheit und hat mich zum Glück nicht betroffen."

        # Atropos Gedanken
        "Kronos""Jetzt sollte ich mich ganz auf das Hier und Jetzt konzentrieren."

        # Atropos Gedanken
        "Kronos""Was steht heute alles an?"

        # Symbiont
        "Kronos""{i}Atropos. Bist du glücklich? {/i}"

        "Atropos" "Ja. Ja, das bin ich."
        return
    else:
        if pilltakenyes:
            # Symbiont
            "Kronos""{i}Es tut mir leid. {/i}"
            if endhappy:
                $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_gluecklich.mpg")
                return
            else:
                if endsad:
                    $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
                    return
                else:
                    if endcrazy:
                        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_crazy.mpg")
                        return



        else:
            if pilltakenno or pilltakenlater:
                # Symbiont
                "Kronos""{i}Wir sterben gemeinsam. {/i}"

                if endhappy:
                    $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_gluecklich.mpg")
                    return
                else:
                    if endsad:
                        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
                        return
                    else:
                        if endcrazy:
                            $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_crazy.mpg")
                            return

label part1:

    if pilltakenyes:
        # Symbiont
        symb"{i}Dein Glück lag in deinen Händen. Früh am Morgen hattest du dich für Happiness entschieden und die Pillen eingenommen. {/i}"
        jump part2
    else:
        if pilltakenno:
            # Symbiont
            symb"{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du der Überzeugung, selbst darüber entscheiden zu wollen und hattest die Pillen nicht eingenommen. {/i}"
            jump part2
        else:
            if pilltakenlater:
                #Symbiont
                symb"{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du dir nicht sicher, was genau das bedeutet. Du hattest dich dafür entschieden, die Pillen später zu nehmen. {/i}"
                jump part2

label part2:

    if beginnoffice:
        #Symbiont
        symb"{i}Nachdem du auf der Arbeit angekommen warst, wolltest du deine Freunde aufsuchen. Hattest du die Zeit mit ihnen genossen? {/i}"

        #Symbiont
        symb"{i}Deine Freunde waren dir schon immer wichtig. Ja, manchmal sogar wichtiger als dein eigenes Glück. {/i}"

        if pilltakenno or pilltakenlater:
            #Symbiont
            symb"{i}Doch danach bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
            jump part3

        else:
            jump part5

    else:
        if beginnlab:
            #Symbiont
            symb"{i}Nachdem du auf der Arbeit angekommen warst, wolltest du dich direkt an die Arbeit machen. Aber was war mit deinen Freunden? {/i}"

            if pilltakenyes:
                #Symbiont
                symb"{i}Es gab für dich kaum etwas Schöneres als den Gedanken, dass deine Arbeit andere Menschen glücklich machte.{/i}"
                jump part5
            else:
                if pilltakenno or pilltakenlater:
                    # Symbiont
                    symb"{i}Aber auf dem Weg dahin bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
                    jump part3

label part3:

    if pillnottakenananhall:
        if pillnottakenananhallananright:
            #Symbiont
            symb"{i}Du musstest zugeben, dass Anan mit seinen Worten recht hatte. Hattest du dein eigenes Glück damit gefährdet, die Pille nicht zu nehmen? {/i}"

            #Symbiont
            symb"{i}Das wolltest du natürlich nicht riskieren. {/i}"

            jump part12
        else:
            if pillnottakenananhallananwhy:
                #Symbiont
                symb"{i}Nachdem Anan wieder weg war, hattest du deine Zweifel. Wieso sollte man die Pille brauchen? Glücklich sein konntest du auch ohne. Das dachtest du. {/i}"
                jump part12
            else:
                if pillnottakenananhallananwrong:
                    #Symbiont
                    symb"{i}Auf Anans Worte wolltest du keinen Wert legen. Als Chef sollte er noch lange kein Recht über deine privaten Entscheidungen haben. {/i}"
                    jump part4


label part4:

    if gotoananofficeornot:
        if gotoananofficeornotyes:
            #Symbiont
            symb"{i}Trotzdem hattest du dich dafür entschieden, seiner Bitte zu folgen und zu seinem Büro zu gehen. {/i}"
            jump part12
        else:
            if gotoananofficeornotno:
                #Symbiont
                symb"{i}Deswegen hattest du dich dafür entschieden, nicht in sein Büro zu kommen. Doch Anan ließ dir keine Wahl. Oder hattest du die Wahl schon davor? {/i}"
                jump part18

label part5:

    if whotolookfor:
        if whotolookforklothimmediately:
            #Symbiont
            symb"{i}In der Pause hattest du dich auf die Suche nach Kloth begeben. {/i}"
            #Symbiont
            symb"{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
            jump part6

        else:
            if whotolookforklothlater:
                #Symbiont
                symb"{i}In der Pause hattest du dich auf die Suche nach Chesis begeben. Aus Sorge um den dritten in eurem Bunde, wolltest du aber auch nach Kloth suchen. {/i}"
                #Symbiont
                symb"{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
                jump part6

            else:
                if whotolookforchesis:
                    #Symbiont
                    symb"{i}In der Pause hattest du dich auf die Suche nach Chesis begeben und deine Zeit mit ihm verbracht. {/i}"

                    #Symbiont
                    symb"{i}Es sollten eure letzten gemeinsamen Minuten sein, ohne dass es euch bewusst war. Hättet ihr die Zeit anders nutzen können? Vielleicht mit Kloth? {/i}"

                    #Symbiont
                    symb"{i} Als eure Zeit vorbei war, bist du zurück ins Labor gegangen. {/i}"
                    jump part10

label part6:

    if whattosearchafteranansoffice:
        if whattosearchafteranansofficekloth:
            #Symbiont
            symb"{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

            #Symbiont
            symb"{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. {/i}"

            #Symbiont
            symb"{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

            #Symbiont
            symb"{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
            jump part8

        else:
            if whattosearchafteranansofficebacklab:
                #Symbiont
                symb"{i}Deine Pause neigte sich dem Ende zu und letztendlich musstest du aufgeben. War es die richtige Entscheidung, ins Labor zurückzukehren? {/i}"
                jump part10
            else:
                if whattosearchafteranansofficeklothsoffice:
                    #Symbiont
                    symb"{i}Du warst schon immer ein neugieriger Junge, Atropos, nicht wahr? Dir ließ es keine Ruhe, dass dein Freund nicht erreichbar war. Du machtest dir Sorgen. {/i}"

                    #Symbiont
                    symb"{i}Das war für dich Grund genug, um sein Büro zu durchsuchen. Dein Freund war wahnsinnig geworden. Hättest du das wirklich sehen sollen? {/i}"
                    jump part9

label part7:

    if searchklothorsolveclue:
        if searchklothorsolveclueclue:
            #Symbiont
            symb"{i}Du wolltest den Hinweisen nachgehen, die er hinterlassen hatte – was du fandest, sollte deinen Tod verantworten. {/i}"
            jump part11
        else:
            if searchklothorsolvecluekloth:
                #Symbiont
                symb"{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

                #Symbiont
                symb"{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. {/i}"

                #Symbiont
                symb"{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

                #Symbiont
                symb"{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
                jump part8
            else:
                if searchklothorsolvecluehappiness:
                    #Symbiont
                    symb"{i}Du wolltest zurück ins Labor. War das die richtige Entscheidung? {/i}"
                    jump part10

label part8:

    if savepeopleorkillall:
        if savepeopleorkillallsave:
            symb"{i}Dein Versuch, deine Freunde zu retten, blieb ohne Erfolg. Sie wollten einfach nicht verstehen. Was konntest du nur tun? {/i}"
            jump part11
        if savepeopleorkillallkill:
            #Symbiont
            symb"{i}Du wolltest niemanden mehr retten. Dein Freund, Kloth, starb und keinen interessierte es. Es machte dich glücklich, zu denken, dass dies die richtige Entscheidung sei. {/i}"
            jump part11

label part9:

    if lookaroundklothsoffice:
        if lookaroundklothsofficewatchedatleastonethensearchedkloth:
            #Symbiont
            symb"{i}In seinem Büro bist du letztendlich fündig geworden. {/i}"
            if lookaroundklothsofficeletter:
                #Symbiont
                symb"{i}Du hattest einen Brief von Kloth gefunden, adressiert an dich und Chesis. Darin verabschiedete er sich von euch, seinen besten Freunden. {/i}"
            if lookaroundklothsofficedocument:
                #Symbiont
                symb"{i}Du hattest dir ein Dokument angesehen, das verriet, wie wichtig die Server im Gebäude wirklich waren. {/i}"
            if lookaroundklothsofficepcpasswordcorrect:
                #Symbiont
                symb"{i}Am Computer hattest du das richtige Passwort eingegeben und eine Nachricht von Kloth gefunden. Er war es, der die Bombe gelegt hatte. {/i}"
            if lookaroundklothsofficepcpasswordwrong:
                #Symbiont
                symb"{i}Am Computer konntest du nicht das richtige Passwort eingeben. Hättest du dort vielleicht mehr herausfinden könnten? {/i}"

                #Symbiont
                symb"{i}Trotzdem bist du auf einen Blog gestoßen. In diesem wurde davon berichtet, dass sich eine Bombe im Gebäude befindet. {/i}"

            #Symbiont
            symb"{i}Vielleicht hättest du mehr herausgefunden, wenn du dir noch mehr angesehen hättest?"
            if saneorseek:
                jump part13
            if part14before and confrontananno:
                jump part15
            if part14before and confrontananyes:
                jump part13
            if pilltakenyes:
                jump part7

        else:
            if lookaroundklothsofficewatchedeverything:

                #Symbiont
                symb"{i}Nur nicht, wo er war. {/i}"
                if saneorseek:
                    jump part13
                if part14before and confrontananno:
                    jump part15
                if part14before and confrontananyes:
                    jump part13
                if pilltakenyes:
                    jump part7

            else:
                if lookaroundklothsofficewatcheddontsearchkloth:
                    #Symbiont
                    symb"{i}Was du gefunden hattest, hatte dich beängstigt. Es hatte dich nicht glücklich gemacht, Atropos. Du hattest entschieden, zurück an die Arbeit zu gehen. {/i}"

                    #Symbiont
                    symb"{i}Hätte es dich noch mehr in das Unglück getrieben, wenn du mehr herausgefunden hättest? {/i}"
                    jump part10

label part10:
    if takeerawithyoutobomb:
        if takeerawithyoutobombyes:
            #Symbiont
            symb"{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Gemeinsam mit Era bist du zum Serverraum gegangen. {/i}"

            #Symbiont
            symb"{i}Era hielt die Bombe in ihren Händen, als sie explodierte. {/i}"

            #Symbiont
            symb"{i}Hattest du sie geliebt? Hat sie dich glücklich gemacht? {/i}"
            jump partend
        else:
            if takeerawithyoutobombno:
                #Symbiont
                symb"{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Also bist du zum Serverraum gegangen. {/i}"

                #Symbiont
                symb"{i}Dein Schicksal wurde besiegelt, bevor du wirklich realisieren konntest, was geschah. {/i}"

                #Symbiont
                symb"{i}Du warst allein. Und jetzt wird dir bewusst, dass es anders hätte sein können. {/i}"
                jump partend

label part11:
    if whatwithbomb:
        if whatwithbombtrydefuse:
            #Symbiont
            symb"{i}Du fandest die Bombe im Serverraum und wolltest sie entschärfen. Aber wie hättest du es ohne Erfahrung schaffen können? {/i}"

            #Symbiont
            symb"{i}Die Bombe explodierte, während du nur versuchen wolltest, das zu retten, was dir wichtig war. {/i}"
            jump partend
        else:
            if whatwithbombexplode:
                #Symbiont
                symb"{i}Der Gedanke, Kloths Werk zu vollenden, machte dich jedoch glücklich. Du fandest die Bombe im Serverraum und hattest dort darauf gewartet, dass die Zeit abläuft. {/i}"

                #Symbiont
                symb"{i}Warst du auch glücklich, als du in den letzten Momenten an deine Freunde gedacht hattest? {/i}"

                #Symbiont
                symb"{i}Wäre es anders gekommen, wenn du sie gerettet hättest? {/i}"
                jump partend
            else:
                if whatwithbombsavepeoplebutexplode:
                    #Symbiont
                    symb"{i}All diese Erlebnisse haben dich nicht glücklich gemacht. Du wolltest, wie Kloth, Aither ein Ende setzen. {/i}"

                    #Symbiont
                    symb"{i}Doch all deine Kollegen und Freunde – in deinen Augen konnten sie nichts dafür. Du wolltest sie retten, bevor die Bombe explodierte. {/i}"

                    #Symbiont
                    symb"{i}Deine Zweifel, am Ende… Ich habe sie gehört. Würdest du noch zweifeln, wenn du etwas an deinen Entscheidungen ändern könntest? {/i}"
                    jump partend
                else:
                    if whatwithbombkillanan:
                        #Symbiont
                        symb"{i}Du hattest dir einen Plan überlegt: Anan war derjenige, der sterben musste. Dazu musstest du ihn nur in den Serverraum locken. {/i}"

                        #Symbiont
                        symb"{i}Vielleicht hattest du davor zu viel Zeit verloren – vielleicht hatte der Plan auch nie eine Chance. {/i}"
                        jump partend

label part12:
    if lookaroundinanansoffice:
        if lookaroundinanansofficeyes:

            if lookaroundinanansofficeyesatleastonebutnotall:
                #Symbiont
                symb"{i}Als du bei Anans Büro angekommen bist, war er noch nicht da. Also hattest du dich dazu entschieden, dich ein wenig umzusehen. {/i}"

                #Symbiont
                symb"{i}Glaubst du, dass es im Nachhinein eine gute Idee war, Atropos? {/i}"
                if lookaroundinanansofficeyesatleastonebutnotallcomputer:
                    #Symbiont
                    symb"{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotalldocument:
                    #Symbiont
                    symb"{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotallletter:
                    symb"{i}Der Brief von Atlas an Anan hat dich neugierig gemacht. Aber hat sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"

                #Symbiont
                symb"{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"
                jump part14

            else:
                if lookaroundinanansofficeyesall:
                    #Symbiont
                    symb"{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                    #Symbiont
                    symb"{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                    #Symbiont
                    symb"{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"

                    jump part9
        else:
            if lookaroundinanansofficeno:
                #Symbiont
                symb"{i}Geduldig hattest du auf Anan gewartet. Vielleicht hättest du etwas rausgefunden, wenn du dich umgesehen hättest? {/i}"

                #Symbiont
                symb"{i}Anan war nicht amüsiert über die Tatsache, dass du deine Pille nicht genommen hattest. {/i}"

                if lookaroundinanansofficenoangry:
                    jump part18

                else:
                    if lookaroundinanansofficenounderstanding:
                        #Symbiont
                        symb"{i}Aber du bist nach seiner Ansprache wieder zur Vernunft gekommen. War es dein Glück, oder die Besiegelung deines Todes? {/i}"

                        #Symbiont
                        symb"{i}Du kanntest dein Schicksal nicht. Also bist du zurück in das Labor, um die Pille zu nehmen und weiter zu arbeiten. {/i}"
                        jump part19
                    else:
                        if lookaroundinanansofficenonounderstanding:
                            #Symbiont
                            symb"{i}Doch es war dir egal, was er dir zu sagen hatte. War es ein Fehler, zu denken, dass du dein Glück in deine eigene Hand nehmen könntest? {/i}"

                            #Symbiont
                            symb"{i}Du konntest aber die Chance nutzen, als Anan wegmusste, um sein Büro genauer unter die Lupe zu nehmen. {/i}"

                            if lookaroundinanansofficeseenatleastone:

                                if lookaroundinanansofficeseenpcbutnoteverything:
                                    #Symbiont
                                    symb"{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"
                                if lookaroundinanansofficeseendocumentbutnoteverything:
                                    #Symbiont
                                    symb"{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"
                                if lookaroundinanansofficeseenletterbutnoteverything:
                                    #Symbiont
                                   symb"{i}Der Brief von Atlas an Anan hatte dich neugierig gemacht. Aber hatte sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"
                                #Symbiont
                                symb"{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"

                                jump part14
                            else:
                                if lookaroundinanansofficeseeneverything:
                                    #Symbiont
                                    symb"{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                                    #Symbiont
                                    symb"{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                                    #Symbiont
                                    symb"{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"
                                    jump part9
                                else:
                                    if lookaroundinanansofficeseennothing:
                                        #Symbiont
                                        symb"{i}Du wolltest die Gelegenheit nicht nutzen. Vielleicht wäre alles anders gekommen, wenn du es getan hättest? {/i}"

                                        #Symbiont
                                        symb"{i} Als Anan wieder zurückkam, schickte er dich zurück in das Büro, wo du die Pille nehmen solltest. {/i}"

                                        #Symbiont
                                        symb"{i}Gesagt, getan… Und zurück an die Arbeit. {/i}"
                                        jump part19

label part13:
    if seekafterklothpng:
        if seekafterklothpngyes:
            #Symbiont
            symb"{i}Als du ihn fandest, war es aber schon zu spät. {/i}"

            #Symbiont
            symb"{i}Hörst du mich, Atropos? {/i}"

            #Symbiont
            symb"{i}Du hattest alle in deinem Wahnsinn getötet. Bist du glücklich mit diesem Wissen? {/i}"
            jump partend
        else:
            if seekafterklothpngenoughinfo:
                #Symbiont
                symb"{i}Du wolltest ihn nicht suchen. Du glaubtest, genug gesehen zu haben. {/i}"
                jump part11

label part14:
    $ part14before = True
    if confrontanan:
        if confrontananyes:
            #Symbiont
            symb"{i}War deine Neugier berechtigt? Du wolltest mehr herausfinden – die Wahrheit herausfinden. {/i}"

            #Symbiont
            symb"{i}Deshalb hattest du Anan mit dem, was du gesehen hattest, konfrontiert. Doch das brachte dir keine weiteren hilfreichen Informationen. {/i}"

            #Symbiont
            symb"{i}Nur seinen Ärger und eine Kündigung. Das hatte dich nur noch mehr dazu motiviert, in Kloths Büro weiterzusuchen. Nicht wahr? {/i}"
            if klothwatchedeverything == False:
                symb"{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                jump part16
            else:
                jump part9
        if confrontananno:
            if firmaok:
                #Symbiont
                symb"{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb ein Geheimnis und du hattest dich danach zurück an deine Arbeit begeben. {/i}"
                jump part18
            else:
                if firmabad:
                    if klothwatchedeverything:
                        #Symbiont
                        symb"{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        symb"{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        symb"{i}Du hast dir alles in Kloths Büro angesehen. Dadurch konntest du alles über die Bombe herausfinden. {/i}"


                        jump part9
                    else:
                        #Symbiont
                        symb"{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        symb"{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        symb"{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                        jump part16


label part15:
    if savepeoplewarnoralarm:
        if savepeoplewarnoralarmbomb:
            #Symbiont
            symb"{i}Allein bist du zum Serverraum gegangen… Deine Freunde, deine Kollegen, die Firma… Du wolltest sie nicht retten. {/i}"

            #Symbiont
            symb"{i}Sag mir, Atropos, stehst du zu deinen Entscheidungen? {/i}"

            #Symbiont
            symb"{i}Du hattest Zweifel, bis zum letzten Augenblick. Und nun hast du dein Schicksal besiegelt. {/i}"
            jump partend
        else:
            if savepeoplewarnoralarmfriends:
                #Symbiont
                symb"{i}Trotz allem wolltest du deine Freunde warnen. Sie sollten nicht mit Aither untergehen. Aber die Zeit war begrenzt – das war dir bewusst. {/i}"
                if savepeoplewarnoralarmfriendsera:
                    #Symbiont
                    symb"{i}Ich hatte schon gewusst, dass du dich für Era entscheiden würdest. Du hattest etwas für sie empfunden, nicht wahr? {/i}"
                    if savepeoplewarnoralarmfriendseralab:
                        #Symbiont
                        symb"{i}Du konntest sie warnen, doch es war schon zu spät, um noch mehr zu tun. Eure beiden Lebensfäden wurden bemessen. {/i}"
                        jump partend
                    else:
                        if savepeoplewarnoralarmfriendseraelsewhere:
                            #Symbiont
                            symb"{i}Auf der Suche nach ihr hattest du viel Zeit verloren. Sie stand gerade eben noch neben dir – im Flur. Gab es Momente, an denen du Zeit hättest sparen können? {/i}"
                            jump partend
                else:
                    if savepeoplewarnoralarmfriendschesis:
                        #Symbiont
                        symb"{i}Du hattest dich dafür entschieden, deinen besten Freund zu warnen. Er schuldet dir jetzt sein Leben. Doch all deine anderen Freunde… hm…{/i}"
                        jump partend
                    else:
                        if savepeoplewarnoralarmfriendskloth:
                            #Symbiont
                            symb"{i}Du wolltest Kloth suchen und fandest ihn. Für ihn war es jedoch schon zu spät… Hättest du die Zeit nutzen sollen, um jemand anderen zu retten? {/i}"
                            jump partend
                        else:
                            if savepeoplewarnoralarmfriendstycho:
                                #Symbiont
                                symb"{i}Du wolltest Tycho retten. Auf dem Weg dahin hattest du es bereits geschafft, Armene vom Gehen zu überzeugen. Doch er schien dir nicht zuzuhören. {/i}"

                                #Symbiont
                                symb"{i}Dein Versuch, den Feueralarm auszulösen, kam zu spät. {/i}"

                                #Symbiont
                                symb"{i}Glaubst du, irgendwann einen Fehler gemacht zu haben, Atropos? {/i}"
                                jump partend
                            else:
                                if savepeoplewarnoralarmalarm:

                                    symb"{i}Letztlich rettete Anan dein Glück und das Leben aller Menschen. {/i}"

                                    jump partend


label part16:
    if foundcorpse:
        if foundcorpselook:
            #Symiont
            symb"{i}Dein Freund, Kloth… Es hatte dich unglücklich gemacht, ihn tot daliegen zu sehen. Die Erinnerung, die dir kam, machte es unerträglich. {/i}"
            jump part17
        else:
            if foundcorpsegoaway:
                #Symbiont
                symb"{i}Als du deinen toten Freund daliegen gesehen hattest, wolltest du die richtige Entscheidung treffen. {/i}"

                #Symbiont
                symb"{i}Du musstest glücklich werden, um keine schrecklichen Dinge mehr sehen zu können. Du brauchtest Happiness - und hattest sie eingenommen. {/i}"
                jump part20

label part17:
    if rememberklothtalk:
        if rememberklothtalkyes:
            #Symbiont
            symb"{i}Kloth wollte mit dir reden, aber er sprach nur wirres Zeug. {/i}"

            #Symbiont
            symb"{i}Ihr musstet es tun, Atropos. Ihr musstet glücklich sein. {/i}"
            if rememberklothtalkyeskillanan:
                #Symbiont
                symb"{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    symb"{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend
        if rememberklothtalkno:
            #Symbiont
            symb"{i}Kloth wollte mit dir reden. Er war verzweifelt. Du und Chesis – ihr beide wolltet einfach eure Glücklichkeit nicht riskieren. {/i}"

            #Symbtion
            symb"{i}Siehst du es jetzt etwa anders? {/i}"

            if rememberklothtalkyeskillanan:
                #Symbiont
                symb"{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    symb"{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend

label part18:
    $ part18before = True
    if ruffle:
        if ruffleangry:
            #Symbiont
            symb"{i}Du warst wütend. Aber glaubst du, dass Anan dir die Kündigung angedroht hätte, wenn du glücklich gewesen wärst? {/i}"

            #Symbiont
            symb"{i}Bist du dir immer noch sicher, dass du ohne Happiness glücklich sein konntest? Wohin hat es dich gebracht? {/i}"

            #Symbiont
            symb"{i}Anans Büro konntest du nicht mehr erreichen. {/i}"
            jump partend
        if ruffleunderstanding:
            #Symbiont
            symb"{i}Dachtest du, dass es der richtige Weg zum Glück sei, Vernunft zu zeigen? Du warst dir immer noch unsicher… {/i}"
            jump part19

label part19:

    if backtoworkpart:
        if backtoworkparttakepill:
            #Symbiont
            symb"{i}Ich glaube, dass es eine gute Entscheidung von dir war, die Pille zu nehmen, als du zu deinem Arbeitsplatz zurückgekehrt bist. {/i}"

            #Symbiont
            symb"{i}Aber denkst du das auch, jetzt wo wir hier sind? {/i}"
            if part18before:
                jump part12
            else:
                jump part20

        if backtoworkparttalkfriends:
            #Symbiont
            symb"{i}Deine Kollegen schienen danach deine Kritik gar nicht wahrzunehmen. Hätte es sie vielleicht unglücklich gemacht? {/i}"

            #Symbiont
            symb"{i}War vielleicht das auch der Grund, warum sie die Leiche nicht bemerkt hatten? {/i}"
            jump part16


label part20:
    if lategoback:
        #Symbiont
        symb"{i}Deine Mittagspause hattest du dann mit Chesis verbracht. Es waren eure letzten gemeinsamen Minuten. {/i}"

        #Symbiont
        symb"{i}Ihr wart gute Freunde. Vielleicht hätte er eine Chance gehabt zu überleben. {/i}"
        if datewithera:
            if datewitheratakeherwithyou:
                #Symbiont
                symb"{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Era im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                symb"{i}Gib dir keine Schuld, Atropos. Sie ist gerne mit dir gegangen. Sie war glücklich, als sie neben dir stand und die Bombe explodierte. {/i}"
                jump partend
            else:
                if datewitheradonttakeherwithyou:
                    #Symbiont
                    symb"{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    symb"{i}Du wirst nie erfahren, ob Era die Explosion überlebt hat. Vielleicht hattest du sie gerettet, vielleicht sterbt ihr beide in diesem Augenblick einsam. {/i}"
                    jump partend
        else:
            if takenarcaiswithyou:
                #Symbiont
                symb"{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Narcais im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                symb"{i}Nun ist euer Schicksal besiegelt, doch Narcais war glücklich bis zum letzten Moment. {/i}"
                jump partend
            else:
                if donttakenarcaiswithyou:
                    #Symbiont
                    symb"{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und Narcais wollte im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    symb"{i}Währenddessen bist du im Labor geblieben. Die Bombe explodierte, ohne dass jemand etwas dagegen tun konnte. Hättest du das verhindern können? {/i}"
                    jump partend

label partend:
    scene atropos_falling
    #Symbiont
    symb"{i}… {/i}"

    #Symbiont
    symb"{i}Du hast viele Entscheidungen getroffen. Eine einzige hätte alles ändern können. {/i}"

    # Symbiont
    symb"{i}Warst du glücklich, Atropos? {/i}"

    # Symbiont
    symb"{i}Bist du zufrieden mit den Entscheidungen, die du getroffen hast? {/i}"

    # Symbiont
    symb"{i}Dein Glück ist letztlich das Einzige, das zählt. {/i}"

    if secretending:
        # Symbiont
        symb"{i}Lebe wohl. {/i}"

        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")

        play music "Sound/Music/Rooms/verkaufsraum.mp3" fadeout 3 fadein 3

        scene street

        # Atropos Gedanken
        symb"Heute ist ein guter Tag. Ein glücklicher Tag. Ein Tag voller Zufriedenheit und Erfüllung."

        # Atropos Gedanken
        symb"Endlich fühle ich mich wirklich glücklich."

        # Atropos Gedanken
        symb"Ich weiß nicht, warum ich in letzter Zeit unglücklicher gewesen war, aber jetzt bin ich glücklich und das ist das Einzige, das zählt."

        # Atropos Gedanken
        symb"Da vorne ist ja auch schon Tartaros. Und nachher treffe ich mich mit meinen Freunden- besser kann der Tag gar nicht mehr werden."

        # Atropos Gedanken
        symb"Ich bin froh für eine Firma wie Tartaros zu arbeiten. Es muss schrecklich für die Menschen gewesen sein, die in Aither gearbeitet hatten."

        # Atropos Gedanken
        symb"Diese Bombe… einfach grauenhaft… wer könnte so etwas nur tun? All die Menschen, die gestorben sind…"

        # Atropos Gedanken
        symb"Aber ich sollte mir keine Gedanken mehr darüber machen. Es liegt in der Vergangenheit und hat mich zum Glück nicht betroffen."

        # Atropos Gedanken
        symb"Jetzt sollte ich mich ganz auf das Hier und Jetzt konzentrieren."

        # Atropos Gedanken
        symb"Was steht heute alles an?"

        # Symbiont
        symb"{i}Atropos. Bist du glücklich? {/i}"

        "Atropos" "Ja. Ja, das bin ich."
    else:
        if pilltakenyes:
            # Symbiont
            symb"{i}Es tut mir leid. {/i}"
            if endhappy:
                $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_gluecklich.mpg")
                return
            else:
                if endsad:
                    $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
                    return
                else:
                    if endcrazy:
                        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_crazy.mpg")
                        return

        else:
            if pilltakenno or pilltakenlater:
                # Symbiont
                symb"{i}Wir sterben gemeinsam. {/i}"
                if endhappy:
                    $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_gluecklich.mpg")
                    return
                else:
                    if endsad:
                        $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_traurig.mpg")
                        return
                    else:
                        if endcrazy:
                            $ renpy.movie_cutscene("Sound/cutscene_ende/cutscene_ende_crazy.mpg")
                            return

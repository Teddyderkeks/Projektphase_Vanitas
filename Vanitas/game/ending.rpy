
label ending:


    #Symbiont
    symb "{i} Du bist so gut wie tot. Nicht mal mehr Sekunden dauert es, bis du auf dem Boden ankommst. {/i}"

    #Symbiont
    symb"{i} Du wirst sterben und es scheint keinen Ausweg aus dieser Lage zu geben. {/i}"

    #Symbiont
    symb"{i} Der Tag unseres Todes. Denkst du, dass du alles getan hast, das du tun konntest, um glücklich zu sein und in Frieden gehen zu können? {/i}"

    jump part1


label part1:

    if pilltakenyes:
        # Symbiont
        "{i}Dein Glück lag in deinen Händen. Früh am Morgen hattest du dich für Happiness entschieden und die Pillen eingenommen. {/i}"
        jump part2
    else:
        if pilltakenno:
            # Symbiont
            "{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du der Überzeugung, selbst darüber entscheiden zu wollen und hattest und die Pillen nicht eingenommen. {/i}"
            jump part2
        else:
            if pilltakenlater:
                #Symbiont
                "{i}Dein Glück lag in deinen Händen. Früh am Morgen warst du dir nicht sicher, was genau das bedeutet. Du hattest dich dafür entschieden, die Pillen später zu nehmen. {/i}"
                jump part2

label part2:

    if beginnoffice:
        #Symbiont
        "{i}Nachdem du auf der Arbeit angekommen warst, wolltest du deine Freunde aufsuchen. Hattest du die Zeit mit ihnen genossen? {/i}"

        #Symbiont
        "{i}Deine Freunde waren dir schon immer wichtig. Ja, manchmal sogar wichtiger als dein eigenes Glück. {/i}"

        if pilltakenno or pilltakenlater:
            #Symbiont
            "{i}Doch danach bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
            jump part3

        else:
            jump part5

    else:
        if beginnlab:
            #Symbiont
            "{i}Nachdem du auf der Arbeit angekommen warst, wolltest du dich direkt an die Arbeit machen. Aber was war mit deinen Freunden? {/i}"

            if pilltakenyes:
                #Symbiont
                "{i}Es gab für dich kaum etwas Schöneres als den Gedanken, dass deine Arbeit andere Menschen glücklich machte{/i}"
                jump part5
            else:
                if pilltakenno or pilltakenlater:
                    # Symbiont
                    "{i}Aber auf dem Weg dahin bist du Anan begegnet. Er hatte sofort bemerkt, dass du nicht glücklich warst. Er wollte dich in der Pause in seinem Büro sehen. {/i}"
                    jump part3

label part3:

    if pillnottakenananhall:
        if pillnottakenananhallananright:
            #Symbiont
            "{i}Du musstest zugeben, dass Anan mit seinen Worten recht hatte. Hattest du dein eigenes Glück damit gefährdet, die Pille nicht zu nehmen? {/i}"

            #Symbiont
            "{i}Das wolltest du natürlich nicht riskieren. {/i}"

            jump part12
        else:
            if pillnottakenananhallananwhy:
                #Symbiont
                "{i}Nachdem Anan wieder weg war, hattest du deine Zweifel. Wieso sollte man die Pille brauchen? Glücklich sein konntest du auch ohne. Das dachtest du. {/i}"
                jump part12
            else:
                if pillnottakenananhallananwrong:
                    #Symbiont
                    "{i}Auf Anans Worte wolltest du keinen Wert legen. Als Chef sollte er noch lange kein Recht über deine privaten Entscheidungen haben. {/i}"
                    jump part4


label part4:

    if gotoananofficeornot:
        if gotoananofficeornotyes:
            #Symbiont
            "{i}Trotzdem hattest du dich dafür entschieden, seiner Bitte zu folgen und zu seinem Büro zu gehen. {/i}"
            jump part12
        else:
            if gotoananofficeornotno:
                #Symbiont
                "Deswegen hattest du dich dafür entschieden, nicht in sein Büro zu kommen. Doch Anan ließ dir keine Wahl. Oder hattest du die Wahl schon davor? {/i}"
                jump part18

label part5:

    if whotolookfor:
        if whotolookforklothimmediately:
            #Symbiont
            "{i}In der Pause hattest du dich auf die Suche nach Kloth begeben. {/i}"
            #Symbiont
            "{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
            jump part6

        else:
            if whotolookforklothlater:
                #Symbiont
                "{i}In der Pause hattest du dich auf die Suche nach Chesis begeben. Aus Sorge um den dritten in eurem Bunde, wolltest du aber auch nach Kloth suchen. {/i}"
                #Symbiont
                "{i}Nach erfolglosem Anruf begann deine Suche bei Anans Büro – keiner war da. {/i}"
                jump part6

            else:
                if whotolookforchesis:
                    #Symbiont
                    "{i}In der Pause hattest du dich auf die Suche nach Chesis begeben und deine Zeit mit ihm verbracht. {/i}"

                    #Symbiont
                    "{i}Es sollten eure letzten gemeinsamen Minuten sein, ohne dass es euch bewusst war. Hättet ihr die Zeit anders nutzen können? Vielleicht mit Kloth? {/i}"

                    #Symbiont
                    "{i} Als eure Zeit vorbei war, bist du zurück ins Büro gegangen. {/i}"
                    jump part10

label part6:

    if whattosearchafteranansoffice:
        if whattosearchafteranansofficekloth:
            #Symbiont
            "{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

            #Symbiont
            "{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. Und in dem Moment hattest du dich daran erinnert. Kloth war dem Wahnsinn verfallen. {/i}"

            #Symbiont
            "{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

            #Symbiont
            "{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
            jump part8

        else:
            if whattosearchafteranansofficebacklab:
                #Symbiont
                "{i}Deine Pause neigte sich dem Ende zu und letztendlich musstest du aufgeben. War es die richtige Entscheidung, ins Labor zurückzukehren? {/i}"
                jump part10
            else:
                if whattosearchafteranansofficeklothsoffice:
                    #Symbiont
                    "{i}Du warst schon immer ein neugieriger Junge, Atropos, nicht wahr? Dir ließ es keine Ruhe, dass dein Freund nicht erreichbar war. Du machtest dir Sorgen. {/i}"

                    #Symbiont
                    "{i}Das war für dich Grund genug, um sein Büro zu durchsuchen. Dein Freund war wahnsinnig geworden. Hättest du das wirklich sehen sollen? {/i}"
                    jump part9

label part7:

    if searchklothorsolveclue:
        if searchklothorsolveclueclue:
            #Symbiont
            "{i}Du wolltest den Hinweisen nachgehen, die er hinterlassen hatte – was du fandest, sollte deinen Tod verantworten. {/i}"
            jump part11
        else:
            if searchklothorsolvecluekloth:
                #Symbiont
                "{i}Du wolltest deinen Freund nach allem, was du gesehen hattest, weitersuchen. Anan lief dir über den Weg und erklärte sich bereit, dir dabei zu helfen. {/i}"

                #Symbiont
                "{i}Gemeinsam fandet ihr ihn - tot, am Fuße der Treppen. Und in dem Moment hattest du dich daran erinnert. Kloth war dem Wahnsinn verfallen. {/i}"

                #Symbiont
                "{i}Anan wollte dir deine Trauer nehmen, aber es war zu spät. Hatte Kloths Wahnsinn sich auf dich übertragen? {/i}"

                #Symbiont
                "{i}Es gab nur noch einen Weg, dein Glück zu finden. Oder gab es noch einen anderen, den du nicht gesehen hattest? {/i}"
                jump part8

label part8:

    if savepeopleorkillall:
        if savepeopleorkillallsave:
            "{i}Dein Versuch, deine Freunde zu retten, blieb ohne Erfolg. Sie wollten einfach nicht verstehen. Was konntest du nur tun? {/i}"
            jump part11
        if savepeopleorkillallkill:
            #Symbiont
            "{i}Du wolltest niemanden mehr retten. Dein Freund, Kloth, starb und keinen interessierte es. Es machte dich glücklich, zu denken, dass dies die richtige Entscheidung sei. {/i}"
            jump part11

label part9:

    if lookaroundklothsoffice:
        if lookaroundklothsofficewatchedatleastonethensearchedkloth:
            #Symbiont
            "{i}In seinem Büro bist du letztendlich fündig geworden. {/i}"
            if lookaroundklothsofficeletter:
                #Symbiont
                "{i}Du hattest einen Brief von Kloth gefunden, adressiert an dich und Chesis. Darin verabschiedete er sich von euch, seinen besten Freunden. {/i}"
            if lookaroundklothsofficedocument:
                #Symbiont
                "{i}Du hattest dir ein Dokument angesehen, das verriet, wie wichtig die Server im Gebäude wirklich waren. {/i}"
            if lookaroundklothsofficepcpasswordcorrect:
                #Symbiont
                "{i}Am Computer hattest du das richtige Passwort eingegeben und eine Nachricht von Kloth gefunden. Er war es, der die Bombe gelegt hatte. {/i}"
            if lookaroundklothsofficepcpasswordwrong:
                #Symbiont
                "{i}Am Computer konntest du nicht das richtige Passwort eingeben. Hättest du dort vielleicht mehr herausfinden könnten? {/i}"

                #Symbiont
                "{i}Trotzdem bist du auf einen Blog gestoßen. In diesem wurde davon berichtet, dass sich eine Bombe im Gebäude befindet. {/i}"

            #Symbiont
            "{i}Vielleicht hättest du mehr herausgefunden, wenn du dir noch mehr angesehen hättest?"
            if part14before:
                jump part15
            else:
                if pilltakenyes:
                    jump part7
                else:
                    if ppilltakenno or pilltakenlater:
                        jump part13

        else:
            if lookaroundklothsofficewatchedeverything:
                #Symbiont
                "{i}Du hattest dir alles in Kloths Büro angesehen. Dadurch konntest du alles über die Bombe herausfinden. {/i}"

                #Symbiont
                "{i}Nur nicht, wo er war. {/i}"
                if part14before:
                    jump part15
                else:
                    if pilltakenyes:
                        jump part7
                    else:
                        if ppilltakenno or pilltakenlater:
                            jump part13

            else:
                if lookaroundklothsofficewatcheddontsearchkloth:
                    #Symbiont
                    "{i}Was du gefunden hattest, hatte dich beängstigt. Es hatte dich nicht glücklich gemacht, Atropos. Du hattest entschieden, zurück an die Arbeit zu gehen. {/i}"

                    #Symbiont
                    "{i}Hätte es dich noch mehr in das Unglück getrieben, wenn du mehr herausgefunden hättest? {/i}"
                    jump part10

label part10:
    if takeerawithyoutobomb:
        if takeerawithyoutobombyes:
            #Symbiont
            "{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Gemeinsam mit Era bist du zum Serverraum gegangen. {/i}"

            #Symbiont
            "{i}Era hielt die Bombe in ihren Händen, als sie explodierte. {/i}"

            #Symbiont
            "{i}Hattest du sie geliebt? Hat sie dich glücklich gemacht? {/i}"
            jump partend
        else:
            if takeerawithyoutobombno:
                #Symbiont
                "{i}Doch du konntest nicht ohne funktionierenden Computer arbeiten. Also bist du zum Serverraum gegangen. {/i}"

                #Symbiont
                "{i}Dein Schicksal wurde besiegelt, bevor du wirklich realisieren konntest, was geschah. {/i}"

                #Symbiont
                "{i}Du warst allein. Und jetzt wird dir bewusst, dass es anders hätte sein können. {/i}"
                jump partend

label part11:
    if whatwithbomb:
        if whatwithbombtrydefuse:
            #Symbiont
            "{i}Du fandest die Bombe im Serverraum und wolltest sie entschärfen. Aber wie hättest du es ohne Erfahrung schaffen können? {/i}"

            #Symbiont
            "{i}Die Bombe explodierte, während du nur versuchen wolltest, das zu retten, was dir wichtig war. {/i}"
            jump partend
        else:
            if whatwithbombexplode:
                #Symbiont
                "{i}Der Gedanke, Kloths Werk zu vollenden, machte dich jedoch glücklich. Du fandest die Bombe im Serverraum und hattest dort darauf gewartet, dass die Zeit abläuft. {/i}"

                #Symbiont
                "{i}Warst du auch glücklich, als du in den letzten Momenten an deine Freunde gedacht hattest? {/i}"

                #Symbiont
                "{i}Wäre es anders gekommen, wenn du sie gerettet hättest? {/i}"
                jump partend
            else:
                if whatwithbombsavepeoplebutexplode:
                    #Symbiont
                    "{i}All diese Erlebnisse haben dich nicht glücklich gemacht. Du wolltest, wie Kloth, Aither ein Ende setzen. {/i}"

                    #Symbiont
                    "{i}Doch all deine Kollegen und Freunde – in deinen Augen konnten sie nichts dafür. Du wolltest sie retten, bevor die Bombe explodierte. {/i}"

                    #Symbiont
                    "{i}Deine Zweifel, am Ende… Ich habe sie gehört. Würdest du noch zweifeln, wenn du etwas an deinen Entscheidungen ändern könntest? {/i}"
                    jump partend
                else:
                    if whatwithbombkillanan:
                        #Symbiont
                        "{i}Du hattest dir einen Plan überlegt: Anan war derjenige, der sterben musste. Dazu musstest du ihn nur in den Serverraum locken. {/i}"

                        #Symbiont
                        "{i}Vielleicht hattest du davor zu viel Zeit verloren – vielleicht hatte der Plan auch nie eine Chance. {/i}"
                        jump partend

label part12:
    if lookaroundinanansoffice:
        if lookaroundinanansofficeyes:

            if lookaroundinanansofficeyesatleastonebutnotall:
                #Symbiont
                "{i}Als du bei Anans Büro angekommen bist, war er noch nicht da. Also hattest du dich dazu entschieden, dich ein wenig umzusehen. {/i}"

                #Symbiont
                "{i}Glaubst du, dass es im Nachhinein eine gute Idee war, Atropos? {/i}"
                if lookaroundinanansofficeyesatleastonebutnotallcomputer:
                    #Symbiont
                    "{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotalldocument:
                    #Symbiont
                    "{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"

                if lookaroundinanansofficeyesatleastonebutnotallletter:
                    "{i}Der Brief von Atlas an Anan hat dich neugierig gemacht. Aber hat sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"

                #Symbiont
                "{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"
                jump part14

            else:
                if lookaroundinanansofficeyesall:
                    #Symbiont
                    "{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                    #Symbiont
                    "{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                    #Symbiont
                    "{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"

                    jump part9
        else:
            if lookaroundinanansofficeno:
                #Symbiont
                "{i}Geduldig hattest du auf Anan gewartet. Vielleicht hättest du etwas rausgefunden, wenn du dich umgesehen hättest? {/i}"

                #Symbiont
                "{i}Anan war nicht amüsiert über die Tatsache, dass du deine Pille nicht genommen hattest. {/i}"

                if lookaroundinanansofficenoangry:
                    jump part18

                else:
                    if lookaroundinanansofficenounderstanding:
                        #Symbiont
                        "{i}Aber du bist nach seiner Ansprache wieder zur Vernunft gekommen. War es dein Glück, oder die Besiegelung deines Todes? {/i}"

                        #Symbiont
                        "{i}Du kanntest dein Schicksal nicht. Also bist du zurück in das Labor, um die Pille zu nehmen und weiter zu arbeiten. {/i}"
                        jump part19
                    else:
                        if lookaroundinanansofficenonounderstanding:
                            #Symbiont
                            "{i}Doch es war dir egal, was er dir zu sagen hatte. War es ein Fehler, zu denken, dass du dein Glück in deine eigene Hand nehmen könntest? {/i}"

                            #Symbiont
                            "{i}Du konntest aber die Chance nutzen, als Anan wegmusste, um sein Büro genauer unter die Lupe zu nehmen. {/i}"

                            if lookaroundinanansofficeseenatleastone:

                                if lookaroundinanansofficeseenpcbutnoteverything:
                                    #Symbiont
                                    "{i}Du hattest einen Blick auf seinen Computer gewagt. Dort fandest du eine Liste, mit deinem Namen an erster Stelle. {/i}"
                                if lookaroundinanansofficeseendocumentbutnoteverything:
                                    #Symbiont
                                    "{i}Die Dokumente – Die Wirkungsweisen der Happiness-Pillen auf das menschliche Gehirn. Obwohl du nicht solltest, hattest du sie dir angesehen. {/i}"
                                if lookaroundinanansofficeseenletterbutnoteverything:
                                    #Symbiont
                                   "{i}Der Brief von Atlas an Anan hatte dich neugierig gemacht. Aber hatte sich für die Information darin das Risiko, erwischt zu werden, gelohnt? {/i}"
                                #Symbiont
                                "{i}Warst du glücklich, oder würdest du dich anders entscheiden, wenn du eine weitere Chance kriegen könntest? {/i}"

                                jump part14
                            else:
                                if lookaroundinanansofficeseeneverything:
                                    #Symbiont
                                    "{i}Du hattest dir alles angesehen, das du dort vorfinden konntest – zu kosten deines Arbeitsplatzes. {/i}"

                                    #Symbiont
                                    "{i}Anan erwischte dich. Vielleicht wäre es nicht so weit gekommen, wenn du dich anders entschieden hättest? {/i}"

                                    #Symbiont
                                    "{i}Du warst auf der Suche nach noch mehr Informationen. Du wusstest, dass du sie bei Kloth finden würdest. {/i}"
                                    jump part9
                                else:
                                    if lookaroundinanansofficeseennothing:
                                        #Symbiont
                                        "{i}Du wolltest die Gelegenheit nicht nutzen. Vielleicht wäre alles anders gekommen, wenn du es getan hättest? {/i}"

                                        #Symbiont
                                        "{i} Als Anan wieder zurückkam, schickte er dich zurück in das Büro, wo du die Pille nehmen solltest. {/i}"

                                        #Symbiont
                                        "{i}Gesagt, getan… Und zurück an die Arbeit. {/i}"
                                        jump part19

label part13:
    if seekafterklothpng:
        if seekafterklothpngyes:
            #Symbiont
            "{i}Als du ihn fandest, war es aber schon zu spät. {/i}"

            #Symbiont
            "{i}Hörst du mich, Atropos? {/i}"

            #Symbiont
            "{i}Du hattest alle in deinem Wahnsinn getötet. Bist du glücklich mit diesem Wissen? {/i}"
            jump partend
        else:
            if seekafterklothpngenoughinfo:
                #Symbiont
                "{i}Du wolltest ihn nicht suchen. Du glaubtest, genug gesehen zu haben. {/i}"
                jump part11

label part14:
    if confrontanan:
        if confrontananyes:
            #Symbiont
            "{i}War deine Neugier berechtigt? Du wolltest mehr herausfinden – die Wahrheit herausfinden. {/i}"

            #Symbiont
            "{i}Deshalb hattest du Anan mit dem, was du gesehen hattest, konfrontiert. Doch das brachte dir keine weiteren hilfreichen Informationen. {/i}"

            #Symbiont
            "{i}Nur seinen Ärger und eine Kündigung. Das hatte dich nur noch mehr dazu motiviert, in Kloths Büro weiterzusuchen. Nicht wahr? {/i}"
            jump part9
        if confrontananno:
            if firmaok:
                #Symbiont
                "{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb ein Geheimnis und du hattest dich danach zurück an deine Arbeit begeben. {/i}"
                jump part18
            else:
                if firmabad:
                    if klothwatchedeverything:
                        #Symbiont
                        "{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        "{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        "{i}Du hast dir alles in Kloths Büro angesehen. Dadurch konntest du alles über die Bombe herausfinden. {/i}"

                        #Symbiont
                        "{i}Macht es dich glücklich zu wissen, dass du die Explosion nicht aufgehalten hattest? {/i}"
                        jump part11
                    else:
                        #Symbiont
                        "{i}Du wolltest kein Risiko eingehen. Dein Durchsuchen blieb zwar ein Geheimnis, aber du warst der Ansicht, dass das nicht genug war. {/i}"

                        #Symbiont
                        "{i}Du musstest unbedingt Kloth suchen – beginnend in seinem Büro. {/i}"

                        #Symbiont
                        "{i}Du wolltest nicht zu viel Zeit dort verschwenden. Nach kurzem Umsehen bist du direkt weiter. Hättest du mehr herausfinden können? {/i}"
                        jump part15


label part15:
    if savepeoplewarnoralarm:
        if savepeoplewarnoralarmbomb:
            #Symbiont
            "{i}Allein bist du zum Serverraum gegangen… Deine Freunde, deine Kollegen, die Firma… Du wolltest sie nicht retten. {/i}"

            #Symbiont
            "{i}Sag mir, Atropos, stehst du zu deinen Entscheidungen? {/i}"

            #Symbiont
            "{i}Du hattest Zweifel, bis zum letzten Augenblick. Und nun hasst du dein Schicksal besiegelt. {/i}"
            jump partend
        else:
            if savepeoplewarnoralarmfriends:
                #Symbiont
                "{i}Trotz allem wolltest du deine Freunde warnen. Sie sollten nicht mit Aither untergehen. Aber die Zeit war begrenzt – das war dir bewusst. {/i}"
                if savepeoplewarnoralarmfriendsera:
                    #Symbiont
                    "{i}Ich hatte schon gewusst, dass du dich für Era entscheiden würdest. Du hattest etwas für sie empfunden, nicht wahr? {/i}"
                    if savepeoplewarnoralarmfriendseralab:
                        #Symbiont
                        "{i}Du konntest sie warnen, doch es war schon zu spät, um noch mehr zu tun. Eure beiden Lebensfäden wurden bemessen. {/i}"
                        jump partend
                    else:
                        if savepeoplewarnoralarmfriendseraelsewhere:
                            #Symbiont
                            "{i}Auf der Suche nach ihr hattest du viel Zeit verloren. Sie stand gerade eben noch neben dir – im Flur. Gab es Momente, an denen du Zeit hättest sparen können? {/i}"
                            jump partend
                else:
                    if savepeoplewarnoralarmfriendschesis:
                        #Symbiont
                        "{i}Du hattest dich dafür entschieden, deinen besten Freund zu warnen. Er schuldet dir jetzt sein Leben. Doch all deine anderen Freunde… hm…{/i}"
                        jump partend
                    else:
                        if savepeoplewarnoralarmfriendskloth:
                            #Symbiont
                            "{i}Du wolltest Kloth suchen und fandest ihn. Für ihn war es jedoch schon zu spät… Hättest du die Zeit nutzen sollen, um jemand anderen zu retten? {/i}"
                            jump partend
                        else:
                            if savepeoplewarnoralarmfriendstycho:
                                #Symbiont
                                "{i}Du wolltest Tycho retten. Auf dem Weg dahin hattest du es bereits geschafft, Armene vom Gehen zu überzeugen. Doch er schien dir nicht zuzuhören. {/i}"

                                #Symbiont
                                "{i}Dein Versuch, den Feueralarm auszulösen, kam zu spät. {/i}"

                                #Symbiont
                                "{i}Glaubst du, irgendwann einen Fehler gemacht zu haben, Atropos? {/i}"
                                jump partend
            else:
                if savepeoplewarnoralarmalarm:
                    #Symbiont
                    #"{i}Dein Versuch, den Feueralarm auszulösen, war vergebens. Keiner wollte die Situation realisieren. Oder konnten sie es nicht? {/i}"

                    #Symbiont
                    #"{i}Vielleicht hättest du mehr Informationen gebraucht, um einen Weg zu finden, deine Freunde zu retten. {/i}"

                    #Symbiont
                    #"{i}Vielleicht hättest du sie aber auch nie retten können. Das Schicksal kann nicht geändert werden, sagt man doch. {/i}"

                    #Übergangstext:
                    #Symbiont
                    "{i}Letztlich rettete Anan dein Glück und das Leben aller Menschen. {/i}"

                    jump partend


label part16:
    if foundcorpse:
        if foundcorpselook:
            #Symiont
            "{i}Dein Freund, Kloth… Es hatte dich unglücklich gemacht, ihn tot daliegen zu sehen. Die Erinnerung, die dir kam, machte es unerträglich. {/i}"
            jump part17
        else:
            if foundcorpsegoaway:
                #Symbiont
                "{i}Als du deinen toten Freund daliegen gesehen hattest, wolltest du die richtige Entscheidung treffen. {/i}"

                #Symbiont
                "{i}Du musstest glücklich werden, um keine schrecklichen Dinge mehr sehen zu können. Du brauchtest Happiness - und hattest sie eingenommen. {/i}"
                jump part20

label part17:
    if rememberklothtalk:
        if rememberklothtalkyes:
            #Symbiont
            "{i}Kloth wollte mit dir reden, aber er sprach nur wirres Zeug. {/i}"

            #Symbiont
            "{i}Ihr musstet es tun, Atropos. Ihr musstet glücklich sein. {/i}"
            if rememberklothtalkyeskillanan:
                #Symbiont
                "{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    "{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend
        if rememberklothtalkno:
            #Symbiont
            "{i}Kloth wollte mit dir reden. Er war verzweifelt. Du und Chesis – ihr beide wolltet einfach eure Glücklichkeit nicht riskieren. {/i}"

            #Symbtion
            "{i}Siehst du es jetzt etwa anders? {/i}"

            if rememberklothtalkyeskillanan:
                #Symbiont
                "{i}Du dachtest, es wäre Anans schuld. Aber war es wirklich so? Denkst du das immer noch? Du wolltest mit dieser Entscheidung glücklich sein. {/i}"
                jump partend
            else:
                if rememberklothtalkyeskillanannot:
                    #Symbiont
                    "{i}Etwas in dir war unglücklich – hatte dich glauben lassen, dass du verantwortlich bist. Wie ist es jetzt? {/i}"
                    jump partend

label part18:
    if ruffle:
        if ruffleangry:
            #Symbiont
            "{i}Du warst wütend. Aber glaubst du, dass Anan dir die Kündigung angedroht hätte, wenn du glücklich gewesen wärst? {/i}"

            #Symbiont
            "{i}Bist du dir immer noch sicher, dass du ohne Happiness glücklich sein konntest? Wohin hat es dich gebracht? {/i}"

            #Symbiont
            "{i}Anans Büro konntest du nicht mehr erreichen. {/i}"
            jump partend
        if ruffleunderstanding:
            #Symbiont
            "{i}Dachtest du, dass es der richtige Weg zum Glück sei, Vernunft zu zeigen? Du warst dir immer noch unsicher… {/i}"
            jump part19

label part19:
    if backtoworkpart:
        if backtoworkparttakepill:
            #Symbiont
            "{i}Ich glaube, dass es eine gute Entscheidung von dir war, die Pille zu nehmen, als du zu deinem Arbeitsplatz zurückgekehrt bist. {/i}"

            #Symbiont
            "{i}Aber denkst du das auch, jetzt wo wir hier sind? {/i}"
            if part19before:
                jump part12
            else:
                jump part20

        if backtoworkparttalkfriends:
            #Symbiont
            "{i}Deine Kollegen schienen danach deine Kritik gar nicht wahrzunehmen. Hätte es sie vielleicht unglücklich gemacht? {/i}"

            #Symbiont
            "{i}War vielleicht das auch der Grund, warum sie die Leiche nicht bemerkt hatten? {/i}"
            jump part16


label part20:
    if lategoback:
        #Symbiont
        "{i}Deine Mittagspause hattest du dann mit Chesis verbracht. Es waren eure letzten gemeinsamen Minuten. {/i}"

        #Symbiont
        "{i}Ihr wart gute Freunde. Vielleicht hätte er eine Chance gehabt zu überleben. {/i}"
        if datewithera:
            if datewitheratakeherwithyou:
                #Symbiont
                "{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Era im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                "{i}Gib dir keine Schuld, Atropos. Sie ist gerne mit dir gegangen. Sie war glücklich, als sie neben dir stand und die Bombe explodierte. {/i}"
                jump partend
            else:
                if datewitheradonttakeherwithyou:
                    #Symbiont
                    "{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    "{i}Du wirst nie erfahren, ob Era die Explosion überlebt hat. Vielleicht hattest du sie gerettet, vielleicht sterbt ihr beide in diesem Augenblick einsam. {/i}"
                    jump partend
        else:
            if takenarcaiswithyou:
                #Symbiont
                "{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und du wolltest mit Narcais im Serverraum nach dem Rechten sehen. {/i}"

                #Symbiont
                "{i}Nun ist euer Schicksal besiegelt, doch Narcais war glücklich bis zum letzten Moment. {/i}"
                jump partend
            else:
                if donttakenarcaiswithyou:
                    #Symbiont
                    "{i}Zurück im Labor wolltest du dich wieder an die Arbeit machen. Euer Computer ging nicht und Narcais wollte im Serverraum nach dem Rechten sehen. {/i}"

                    #Symbiont
                    "{i}Währenddessen bist du im Labor geblieben. Die Bombe explodierte, ohne dass jemand etwas dagegen tun konnte. Hättest du das verhindern können? {/i}"
                    jump partend

label partend:
    #Symbiont
    "{i}… {/i}"

    #Symbiont
    "{i}Du hast viele Entscheidungen getroffen. Eine einzige hätte alles ändern können. {/i}"

    # Symbiont
    "{i}Warst du glücklich, Atropos? {/i}"

    # Symbiont
    "{i}Bist du zufrieden mit den Entscheidungen, die du getroffen hast? {/i}"

    # Symbiont
    "{i}Dein Glück ist letztlich das Einzige, das zählt. {/i}"

    if secretending:
        # Symbiont
        "{i}Lebe wohl. {/i}"
    else:
        if pilltakenyesbutnosecret:
            # Symbiont
            "{i}Es tut mir leid. {/i}"
        else:
            if pilltakenno or pilltakenlater:
                # Symbiont
                "{i}Wir sterben gemeinsam. {/i}"

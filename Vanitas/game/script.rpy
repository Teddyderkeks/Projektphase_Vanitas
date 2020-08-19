default pill_taken = False
default straight_office = False
default neiro_unterhalten= False
define startfade=Fade(0.5,0.5,0.5)

label start:
    stop music
    $ renpy.movie_cutscene("cutscene_introsound.mpg")
    play music "Sound_freeze.mp3" fadeout 2000

    scene atropos_falling

    # Symbiont
    "{i}Du bist so gut wie tot. Nicht mal mehr Sekunden dauert es bis du auf dem Boden aufkommst. {/i}"

    # Symbiont
    "{i}Du wirst sterben und es scheint keinen Ausweg aus der Lage zu geben. {/i}"

    # Symbiont
    "{i}Warst du glücklich, Atropos? {/i}"

    # Symbiont
    "{i}Bist du zufrieden mit den Entscheidungen, die du getroffen hast? {/i}"

    # Symbiont
    "{i}Dein Glück ist letztlich das Einzige, das zählt. {/i}"

    # Symbiont
    "{i}Lebe wohl. {/i}"

    jump change


label change:
    scene street
    with startfade
    stop music fadeout 2000
    play music "Sound_verkehrsraum_demo.mp3" fadeout 1

    # Symbiont
    "{i}Heute ist ein guter Tag. Ein glücklicher Tag. Ein Tag voller Zufriedenheit und Erfüllung. {/i}"

    # Symbiont
    "{i} Atropos, du solltest den Tag nutzen, um dich und alle anderen Menschen glücklich zu machen. {/i}"

    # Atropos Gedanken
    "Ich freue mich schon auf heute. Nach der Arbeit grillen Kloth, Chesis und ich endlich. Ich kann es schon seit Wochen kaum noch erwarten!"

    # Atropos Gedanken
    "Hoffentlich hat es Kloth nicht vergessen. Er wirkte in letzter Zeit manchmal etwas abwesend."

    # Atropos Gedanken
    "Ob ihn wohl etwas bedrückt? Ich kann mir vorstellen, dass ziemlich viel Verantwortung auf ihm lastet."

    # Atropos Gedanken
    "Für seinen Job wäre ich wohl wirklich nicht geeignet. Da kann ich echt froh sein im Labor zu arbeiten."

    # Symbiont
    "{i}Jeder bekommt von Aither geeignete Arbeit zugeteilt. Arbeit, die ihn glücklich macht.{/i}"

    # Atropos Gedanken
    "Ich kann mir nicht vorstellen, direkt unter Anan zu arbeiten. Als rechte Hand von einem der 'Großen Drei' trägt man bestimmt viel Verantwortung. Das merkt man Kloth auch an."

    # Symbiont
    "{i}Anan hat in dieser Welt wirklich einiges verändert. Deswegen ist es eine Ehre, für ihn und Aither zu arbeiten.{/i}"

    # Atropos Gedanken
    "Und nicht nur er. Auch Atlas und Adrés. Ohne ihr Triumvirat wäre die Welt vermutlich immer noch im Krieg versunken."

    # Atropos Gedanken
    "Letztlich weiß ich es nur aus den Erzählungen meines Vaters, aber es muss schrecklich gewesen sein. Das fehlende Wasser und die unzureichende Nahrung…"

    # Symbiont
    "{i}Du kannst wirklich glücklich sein, dass du in der heutigen Zeit lebst mit einem Dach über dem Kopf und nichts, worüber du dir Sorgen machen müsstest. {/i}"

    # Atropos Gedanken
    "Außerdem habe ich Chesis und Kloth an meiner Seite. Es gibt einfach nichts Besseres als gemeinsam mit seinen besten Freunden arbeiten zu können."

    # Symbiont
    "{i}Und dann auch noch für eine Firma wie Aither, die allen Menschen ihre Glücklichkeit schenkt. {/i}"

    # Atropos Gedanken
    "Alle Menschen haben es verdient glücklich zu sein, genau aus diesem Grund bringen wir ihnen ja Happiness. Manchmal frage ich mich nur…"


    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"


    "Durchsage" "{i} Nimm Happiness ein und lebe dein Leben so, wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit.{/i}"

    scene detail_pillbox

    # Atropos Gedanken
    "Happiness…"

    # Atropos Gedanken
    "Stimmt…"

    # Atropos Gedanken
    "Ich habe es schon wieder vergessen."

    # Atropos Gedanken
    "Ob es wohl Konsequenzen hat, dass ich sie nicht täglich genommen habe?"

    # Atropos Gedanken
    "Immerhin ist es das, was sie uns stets einprägen: Vergiss niemals - auch nicht einmal - deine Pille zu nehmen."

    "Atropos" "…"

    # Atropos Gedanken
    "Aber war ich in den letzten Tagen deswegen wirklich weniger glücklich?"

    # Symbiont
    "{i}Nimm die Pille, Atropos. Du brauchst sie, um glücklich zu sein. {/i}"

    # Atropos Gedanken
    "Ich habe aber nicht den Eindruck, dass sich viel verändert hat…"

    # Atropos Gedanken
    "Oder?"

    # Atropos Gedanken
    "Was soll ich jetzt machen? Soll ich sie nehmen?"

    menu:
        "Ich sollte die Pille besser jetzt sofort nehmen.":
            jump take_pill
        "Ich nehme die Pille nicht- ich brauche sie nicht!":
            jump not_take_pill
        "Ich nehme die Pille, sobald ich auf der Arbeit bin.":
            jump later_take_pill



label take_pill:
    $ pill_taken = True

    # Atropos Gedanken
    "Ich sollte die Pille besser jetzt sofort nehmen."

    scene detail_pill

    # Atropos Gedanken
    "So… schnell runter damit, ehe ich es schon wieder vergesse."

    scene street

    # Atropos Gedanken
    "Es war ein großer Fehler gewesen in letzter Zeit nicht auf die regelmäßige Einnahme zu achten."

    # Atropos Gedanken
    "Wenn ich genauer darüber nachdenke… Vermutlich war ich nicht so glücklich, wie ich hätte sein können."

    # Atropos Gedanken
    "Aber ich möchte glücklich sein. Ich möchte genauso glücklich sein wie alle anderen."

    # Atropos Gedanken
    "Ohne die Pille habe ich mich irgendwie so… leer gefühlt. Da waren Gedanken gewesen, die ich nicht haben wollte."

    # Atropos Gedanken
    "Aber ich beginne mich langsam wieder besser zu fühlen. Ich fühle mich gut. Zufrieden."

    # Atropos Gedanken
    "Die Happiness-Pille ist das, was ich brauche, um glücklich zu sein. Um ein glückliches Leben zu führen."

    # Atropos Gedanken
    "Sie ist wichtig und zukünftig werde ich sie nicht mehr vergessen! Dann kann ich endlich wieder das Leben führen, das ich führen will."

    # Atropos Gedanken
    "Ein gutes Leben."

    # Atropos Gedanken
    "Ein glückliches Leben."

    # Symbiont
    "{i}Gut gemacht, Atropos. Das ist es was wichtig ist: Ein glückliches Leben und genau dieses Leben führst du nun wieder. {/i}"

    # Symbiont
    "{i}Vergiss niemals, glücklich zu sein und immer deinem Glück zu folgen. {/i}"

    # Symbiont
    "{i}In jeder einzelnen Entscheidung. {/i}"

    # Atropos Gedanken
    "Ja, ich werde es nicht vergessen."


    jump shop

label not_take_pill:
    # Atropos Gedanken
    "Ich nehme die Pille nicht- ich brauche sie nicht!"

    # Atropos Gedanken
    "Nicht mehr zumindest."

    # Atropos Gedanken
    "Warum auch? Ich bin auch ohne sie glücklich. Sie ist komplett überflüssig."

    # Atropos Gedanken
    "Obwohl ich sie die letzten Tage so unregelmäßig genommen habe, habe ich keinen Unterschied zu sonst bemerkt."

    # Atropos Gedanken
    "Ich war glücklich und ich bin glücklich. Dafür brauche ich die Pille nicht. Sie scheint fast nur ein Placebo zu sein."

    # Atropos Gedanken
    "Die Hauptsache ist doch, dass ich glücklich bin und nicht, wie ich dieses Glück erreiche."

    # Atropos Gedanken
    "Ich werde die Tablette einfach weiterhin nicht nehmen. Das wird schon keinem auffallen. Und wenn doch, fange ich einfach an, sie wieder zu nehmen."

    # Atropos Gedanken
    "Schaden wird sie mir auf keinen Fall."

    scene street


    jump shop

label later_take_pill:
    # Atropos Gedanken
    "Ich nehme die Pille, sobald ich auf der Arbeit bin. Das sollte ausreichen."

    # Atropos Gedanken
    "Ich weiß ja, dass die Tablette wichtig ist. Nur durch sie kann ich wirklich glücklich sein…"

    # Atropos Gedanken
    "Dennoch… Ich habe die letzten Tage keinen großen Unterschied bemerkt, obwohl ich sie unregelmäßig eingenommen hatte."

    # Atropos Gedanken
    "Es wird schon keine Auswirkungen haben, dass ich sie die paar Mal vergessen habe."

    # Atropos Gedanken
    "Sicherheitshalber werde ich sie heute trotzdem wieder einnehmen. Ich möchte mein Glück nicht riskieren."

    # Atropos Gedanken
    "Bei allen anderen wirkt sie immerhin auch. Alle Menschen sind glücklich seit Anan und die anderen sie uns zum Geschenk gemacht haben."

    # Atropos Gedanken
    "Das ist kein Vergleich zu dem, wie kaputt und zerstört die Welt zuvor war."

    # Atropos Gedanken
    "Ich sollte dankbarer für diese Chance sein und mein Glück nicht riskieren."

    scene street


    jump shop

label shop:
    scene street

    # Atropos Gedanken
    "Ich bin heute echt früh dran. Da ist schon Aither und ich habe noch reichlich Zeit, bis ich mit der Arbeit anfangen muss."

    # Atropos Gedanken
    "Zum Glück wohne ich nicht so weit von der Filiale entfernt. Ich könnte es echt schlimmer treffen."

    # Atropos Gedanken
    "Ich verstehe nicht, wie Kloth so weit außerhalb vom Zentrum Astoas leben kann. Er hat ein großes Haus, aber dafür fährt er immer Ewigkeiten bis zur Arbeit."

    # Atropos Gedanken
    #"Egal… was muss ich heute nochmal tun?"

    # Atropos Gedanken
    #"Ach stimmt ja. Die neuen Proben, die gestern von Adrés Filiale eingetroffen sind, müssen analysiert und ausgewertet werden."

    # Atropos Gedanken
    #"Dann kümmere ich mich am besten als Allererstes darum."


    scene shop_1

    show zelos normal

    "Zelos" "Guten Morgen und einen wunderschönen Tag, was…? Ach, du bist es Atropos- heute extra überpünktlich?"

    "Atropos" "Hey, Zelos. Ja, ich bin heute etwas zu früh aufgewacht und dachte mir, dass ich den Tag besser nutze, als noch weiter liegen zu bleiben."

    "Zelos" "Eifrig und strebsam, das lobe ich mir. Aber man kann auch gar nicht anders als seine Arbeit hier zu lieben, natürlich ist man da gerne bereit mehr Zeit zu investieren."

    "Atropos" "Spaß macht die Arbeit hier auf jeden Fall und wir dienen der Menschheit. Das kann wohl nicht jeder von sich behaupten. (lacht)"

    "Zelos" "Ich hoffe es stört dich nicht, wenn ich nebenbei weiterarbeite? Die neuste Lieferung der Happiness-Pille kam eben an und ich muss sie noch in die Regale einsortieren."

    "Atropos" "Alles gut, lass dich von mir nicht stören."

    # Atropos Gedanken
    "Zelos ist ja wirklich nett, aber sein Übereifer kann manchmal auch etwas anstrengend sein. Wie kann er nur immer so voller Energie sein?"

    menu:
        "Ich wollte ohnehin mal bei meinen Freunden im Büro vorbeischauen.":
            jump conversation_with_seller
        "Ich wollte ohnehin erstmal ins Labor gehen.":
            jump work

label conversation_with_seller:

    show zelos normal
    "Atropos" "Ich wollte ohnehin mal bei Tycho und den anderen im Büro vorbeischauen. Wir sehen uns später."

    "Zelos" "Richte den Anderen schöne Grüße von mir aus!"

    "Atropos" "Klar, mache ich."

    "Zelos" "Wir machen heute um 12:15 Uhr Mittagspause. Du kommst doch mit uns in die Mensa, oder?"

    "Atropos" "Ich weiß noch nicht, ob ich es zeitlich schaffe. Es türmt sich heute ein Berg an Arbeit, aber ich versuche es auf alle Fälle."

    "Zelos" "(murmelt) Happiness- Glück für alle. Oh, tut mir leid, was hast du gesagt?"

    "Atropos" "(lacht) Nichts… alles gut, lass dich von mir nicht länger aufhalten. Wir sehen uns."

    "Zelos" "Bis dann und einen wunderschön glücklichen Tag in der besten Firma der Welt!"



    if pill_taken:

        scene hall

        # Atropos Gedanken
        "Da vorne liegt das Büro- ich frage mich, ob die anderen wohl schon da sind? Ich bin heute ziemlich früh dran."

        stop music fadeout 1
        play music "Sound_Buro.mp3" fadeout 2

        scene office_1

        # Atropos Gedanken
        "Hmm, es scheint noch keiner hier zu sein."

        # Atropos Gedanken
        "{i}Dann bin ich wohl wirklich zu früh dran."

        #Atropos Gedanken
        "Ich könnte mich noch ein wenig umsehen."

# klickbar => fehlt noch!!!!!
        # Wenn Spieler direkt auf den PC im Raum klickt
        # Detailansicht PC
        # Atropos Gedanken
        #"Seltsam. Da hat wohl jemand etwas nachlesen wollen und vergessen den Bildschirm zu sperren."
        # Bevor der Spieler mehr erfahren kann, schaltet sich der Bildschirm des PCs von allein aus.
        # Atropos Gedanken
        #"Hm? Der Bildschirm ist einfach ausgegangen."
        # Atropos Gedanken
        #"Wieso sollte jemand über die Moiren forschen?"

        menu:
            "Ich schaue mir den Kalender an.":
                jump watchofficecalendar

            "Da ist ein interessantes Foto.":
                jump watchofficephoto

            "Neben der Sanduhr liegt etwas.":
                jump watchofficehourglass

            "Oder nein, besser nicht. Ich sollte nicht in fremden Sachen herumstöbern.":
                jump watchnothingoffice

        label watchofficecalendar:
            scene detail_calendar
            # Atropos Gedanken
            "September 2256."
            # Atropos Gedanken
            "Der Todestag meiner Mutter jährt sich bald wieder. Ich war noch so klein… Ich kann mich gar nicht mehr an sie erinnern."
            # Atropos Gedanken
            "Vielleicht kommt Mora dann mal wieder zu Besuch, um gemeinsam zu feiern."
            # nach Button-Klick
            scene office_1
            jump watchnothingoffice

        label watchofficephoto:
            scene detail_photo_neiro
            # Atropos Gedanken
            "Oh, Neiro! Das daneben muss dann wohl sein Bruder sein. Die beiden scheinen allen Anschein nach gut miteinander auszukommen."
            # Atropos Gedanken
            "Was sein Bruder wohl jetzt so macht?"
            scene office_1
            jump watchnothingoffice

        label watchofficehourglass:
            scene detail_hourglass
            # normalerweise nach Button-Klick!!
            # Atropos Gedanken
            "Was steht da?"
            show detail_hourglass_overlay
            # normalerweise nach Button-Klick!!
            # Atropos Gedanken
            "Ein Gedicht. Wohl von Neiro."
            scene office_1
            jump watchnothingoffice

        label watchnothingoffice:

            # Atropos Gedanken
            "Ich höre Stimmen, könnten sie das sein?"

            # Atropos Gedanken
            "Tatsächlich, sie sind es und sie scheinen sich eh noch zu unterhalten bevor sie den Tag starten. Ich sollte mich zu ihnen gesellen."

            scene office_2

            "Atropos" "Hey Leute."

            show ireia normal:
                xalign 0.5

            "Ireia" "Atropos, wie schön dich hier mal wieder anzutreffen! Du hast dich schon seit einer Weile nicht mehr im Büro blicken lassen. Vermisst hast du uns wohl nicht sonderlich!"

            "Atropos" "Nun, ist ja auch nicht so ganz mein Arbeitsplatz. (lacht) Und keine Sorge, ich habe euch alle vermisst."

            show tycho normal:
                xalign 0.75

            "Tycho" "Das will ich dir aber auch geraten haben. (lacht) Uns kann man doch gar nicht {b}nicht{/b} mögen, nicht wahr? Und dementsprechend musst du uns auch vermisst haben."

            show armene normal:
                xalign 1

            "Armene" "Ja. Ja, das stimmt! Hallo Atropos."

            "Atropos" "Hi Armene, wie geht es dir?"

            "Armene" "Ich bin glücklich wie immer!"

            "Ireia" "Jetzt überfall die Arme doch nicht, du kennst sie doch."

            "Ireia" "Und Armene, du solltest weiter deine Präsentation über das firmeninterne Kommunikationssystem vorbereiten- ich erwarte bessere Arbeit von dir als letztes Mal."

            "Armene" "Natürlich Ireia, tut mir leid."

            hide armene normal

            "Tycho" "Neiro, gesell dich doch zu uns, was sitzt du so einsam und verlassen an deinem Platz? Deine Arbeitszeit hat doch noch nicht angefangen."

            show neiro normal:
                xalign 0.25

            "Neiro" "Oh… ich habe euch gar nicht bemerkt, tut mir leid. Atropos? Was machst du hier? Arbeitest du nicht in einer anderen Abteilung? Verkauf oder so?"

            "Atropos" "Neiro wie er leibt und lebt. (lacht)"

            "Ireia" "Du solltest definitiv an deinem Gedächtnis arbeiten, Neiro. Es wird in letzter Zeit immer kritischer. Ich möchte von dir keine schlechteren Ergebnisse deswegen sehen."

            "Neiro" "Natürlich Ireia, ich gebe weiterhin mein Bestes, du musst dir keine Sorgen machen."

            # Atropos Gedanken
            "Neiro hatte schon immer eine seltsame Art mit Kritik umzugehen. Aber immerhin verträgt er dadurch Ireias direkte Art gut."

            "Tycho" "Habt ihr es eigentlich schon gehört? Anan will anlässlich des diesjährigen 37. Gründungstages wieder eine riesige Feier veranstalten!"

            "Ireia" "Dann sollten wir noch härter arbeiten, damit wir auch einen Anlass zu feiern haben. Das Glück der Menschen entsteht nicht von selbst."

            "Tycho" "Natürlich arbeiten wir hart! Aber das tut man für Aither doch auch gerne."

            "Tycho" "Zurück zum Thema… diese Party wird gigantisch. Erinnert ihr euch noch an die anlässlich des 30. Gründungstages?"

            "Atropos" "Damals hatte ich noch nicht hier gearbeitet. So alt bin ich nun auch nicht. (lacht)"

            "Tycho" "Ach stimmt, du bist ja ein paar Jahre jünger als ich, oder? 24?"

            "Atropos" "Fast… 25. (grinst)"

            "Tycho" "Jedenfalls… wo war ich stehen geblieben?"

            "Tycho" "Ach ja, der 30. Gründungstag… eine bessere Feier habe ich noch nie erlebt! Und ich war schon auf vielen Feiern gewesen, das könnt ihr mir glauben."

            "Tycho" "Damals hatte ich gerade erst hier angefangen. Ich war nur ein einfacher Praktikant gewesen, aber dennoch hatte Anan mir eine Einladung geschenkt."

            "Tycho" "Ich hatte mein Glück kaum fassen können. Und es war berauschend gewesen. All das Essen im Überfluss und dann die Musik, der Tanz…"

            "Ireia" "Tycho, fass dich kürzer. Wir haben noch Arbeit zu erledigen. Und jetzt erzähl schon, was hast du vom diesjährigen Gründungstag gehört?"

            "Atropos" "Ja… du kannst doch nicht die Information anteasern und dann damit hinter dem Berg halten."

            show armene normal:
                xalign 1

            "Tycho" "Sorry, sorry… also, ich weiß nicht viel, aber angeblich sollen Atlas und Adrés höchstpersönlich vorbeikommen, um gemeinsam mit Anan diesen Tag zu feiern."

            "Atropos" "Habe ich dich gerade richtig verstanden? Die großen Drei alle hier in Astoa?"

            "Ireia" "Das sind ja unglaubliche Neuigkeiten. Wieso hast du uns nicht schon früher davon erzählt?"

            "Tycho" "Weil ich davor selbst nur ganz vage Gerüchte gehört hatte, aber mittlerweile verstärkt sich der Eindruck immer mehr, dass an den Gerüchten etwas Wahres dran sein könnte."

            "Atropos" "Ich frage mich, wie die beiden wohl sind. Natürlich kennt man ihre Namen… immerhin sind Anan, Atlas und Adrés die Gründer von Aither und diejenigen, die den Krieg beendet haben…"

            "Atropos" "Dennoch kenne ich Atlas und Adrés nur von Fotos und nicht von Videoaufzeichnungen oder anderen Quellen. Es wird ein ziemliches Geheimnis um ihre Existenz gemacht."

            "Ireia" "Das ist aber auch gut so. Die drei sind immerhin dafür verantwortlich, dass alle Menschen glücklich sind."

            "Ireia" "Da haben sie Wichtigeres zu tun als sich darum zu kümmern, dass wir Informationen über sie bekommen."

            "Armene" "Ich frage mich, ob Atlas und Adrés wohl auch so unglaublich charmant und gutaussehend sind wie Anan… (seufzt verträumt)"

            "Ireia" "Armene? Wie lange stehst du schon hier? Bist du fertig mit deiner Präsentation?"

            "Armene" "Nein… ich wollte mich nur am Gespräch beteiligen…"

            "Neiro" "Um was geht es? Tut mir leid, ich war mit den Gedanken kurz abgeschweift…"

            "Neiro" "Mein Bruder ist gestern gestorben und wir müssen noch die Feier ihm zu Ehren vorbereiten…"

            "Tycho" "(lacht) Und wieder das übliche Chaos. Es macht echt zu viel Spaß mit euch Zeit zu verbringen!"

            "Ireia" "Armene, los an die Arbeit!"

            "Armene" "Ja natürlich Ireia, mache ich!"

            hide armene normal

            # Atropos Gedanken
            "Was mich gerade interessieren würde…"

            menu:
                "Ich hätte gerne mehr Informationen über die Gründungsfeier.":
                    jump entscheidung4_1
                "Ich würde mich gerne noch etwas mehr über die großen Drei unterhalten.":
                    jump entscheidung4_2
                "Ich will mich bei Neiro nach seinem verstorbenen Bruder erkundigen.":
                    jump entscheidung4_3

            label entscheidung4_1:
                $ neiro_unterhalten = True

                "Atropos" "Tycho, hast du noch mehr Informationen über die diesjährige Gründungsfeier?"

                "Tycho" "Hmm, gute Frage- lass mich einen Moment überlegen…"

                "Neiro" "Ihr sprecht über die Gründungsfeier?"

                "Ireia" "Ja, darum ging es schon die ganzen letzten Minuten."

                "Neiro" "Oh. Jedenfalls, ich weiß ein bisschen was…"

                "Tycho" "Worauf wartest du noch? Erzähl schon!"

                "Neiro" "Atlas und Adrés werden hierher nach Astoa kommen, um der Gründungsfeier beizuwohnen!"

                "Atropos" "Neiro, das wissen wir bereits. (lacht) Immerhin haben wir dadurch noch einmal die Bestätigung."

                "Ireia" "Weißt du sonst noch etwas? Irgendwelche Neuigkeiten?"

                "Neiro" "Es hieß, dass heute im Laufe des Tages noch eine offizielle Ankündigung des Ganzen erfolgen soll."

                "Atropos" "Eine offizielle Ankündigung? Also einfach eine Durchsage von Anan?"

                "Neiro" "Nein, soweit ich das weiß, werden alle drei live geschaltet."

                "Ireia" "Das gab es ja noch nie. Normalerweise kommunizieren wir nicht mit dem Rest der Welt… warum sollten wir auch?"

                "Tycho" "Das sind wirklich unglaubliche Neuigkeiten! Ich freue mich schon darauf. Die diesjährige Gründungsfeier wird unbeschreiblich und unvergesslich werden!"

                "Neiro" "Und es gibt noch etwas: Angeblich soll mit der Gründungsfeier eine neue Happiness-Pille vorgestellt werden."

                "Ireia" "Eine neue Pille? Sag nicht, dass es eine Pille sein wird, die uns noch glücklicher macht?"

                "Tycho" "Ich wüsste nicht, was es sonst sein könnte… der Tag wird ja immer besser!"

                "Ireia" "Atropos, müsstest du darüber nicht eigentlich mehr wissen?"

                jump nachentscheidung4

            label entscheidung4_2:

                "Atropos" "Ich bin wirklich gespannt auf Atlas und Adrés."

                "Ireia" "Sie wollen das Beste für die Welt, genauso wie Anan. Ist das nicht das Einzige, das zählt?"

                "Tycho" "Ihnen ist unser Wohl am aller Wichtigsten. Stellt euch nur vor, wie die Welt ohne sie wäre. Ich wage es gar nicht mir das vorzustellen!"

                "Ireia" "Wir wären immer noch im Krieg versunken. Ohne die Happiness-Pille, ohne glückliche Menschen würde es nur weiter Streit und Zwietracht geben."

                "Atropos" "Ich frage mich immer noch wie ausgerechnet diese drei Männer es damals geschafft haben uns den Frieden zu schenken…"

                "Tycho" "Natürlich durch unsere Glücklichkeit: Happiness. Das ist das Einzige, was wirklich zählt. Spielen andere Gründe oder genauere Erläuterungen eine Rolle?"

                "Ireia" "Nein, das ist nun wirklich nichts, worüber wir uns Gedanken machen müssten."

                "Ireia" "Sie schenkten uns Happiness und beendeten damit den 50-jährigen Krieg. Darum sind wir heute glücklich. Darum dürfen wir das Leben unserer Träume leben!"

                # Symbiont
                "{i}Sie haben Recht. Warum solltest du dir weiter darüber Gedanken machen? Es spielt keine Rolle. Die Hauptsache ist ein glückliches Leben und das besitzt du. {/i}"

                "Atropos" "Ihr habt Recht. (lacht) Also, andere Frage: Durftet ihr schon einmal persönlich mit Anan sprechen?"

                "Neiro" "Es geht gerade um Anan? Was ist mit ihm? Ist er nicht toll? So zuvorkommend und aufmerksam- einen besseren Chef kann man sich nicht wünschen."

                "Ireia" "Ich hatte Dank ein paar weniger Meetings mal mit ihm zu tun. Er ist die beeindruckendste Persönlichkeit, die ich jemals getroffen habe."

                "Ireia" "Und obwohl er fast schon gottgleichen Status hat, ist er trotzdem auf dem Boden geblieben und kümmert sich um jeden einzelnen von uns."

                "Tycho" "Ich hatte ein einziges Mal mit ihm gesprochen. Damals hatte ich meine Pille vergessen zu nehmen, weil ich eine Zeit lang krank gewesen war."

                "Atropos" "Das hattest du ja noch nie erwähnt… wie ist er damit umgegangen?"

                "Tycho" "Er war unglaublich verständnisvoll gewesen und hatte mir klar gemacht, dass er nur um mein Wohlergehen und mein Glück besorgt ist."

                "Tycho" "Durch dieses Ereignis ist mir noch einmal bewusst geworden, wie wichtig die Happiness-Pille eigentlich ist."

                "Tycho" "Ich bin froh, dass Anan mir die Augen geöffnet hat. Ihr wisst gar nicht wie sehr ich es damals bereut hatte."

                "Tycho" "Anan gibt alles, damit es uns gut geht und wir glücklich sind. Wie hatte ich es ihm nur so danken können?"

                "Atropos" "Tycho… wie…"

                "Tycho" "Ich… Ich bin so glücklich, dass ich eine zweite Chance erhalten habe. Jetzt kann ich dabei helfen allen Menschen ihr Glück zu geben!"

                jump nachentscheidung4

            label entscheidung4_3:

                "Atropos" "Neiro, dein Bruder ist gestorben?"

                "Neiro" "Achso… ja. Er ist von einem der Busse erwischt worden, der eine technische Fehlfunktion hatte."

                "Ireia" "Möge er nun in Frieden glücklich sein."

                "Atropos" "Wann findet seine Ehrung statt?"

                "Neiro" "Genau steht es noch nicht fest, aber voraussichtlich kommenden Sonntag. Ihr seid alle herzlich eingeladen, wenn ihr wollt. Es wird ein riesiges Fest geben."

                "Tycho" "Habe ich da Fest gehört? Da kann man doch gar nicht nein sagen, ich bin so was von dabei! Atropos, wie sieht es bei dir aus?"

                "Atropos" "Ich muss später nochmal in meinen Terminkalender schauen, aber ansonsten bin ich natürlich auch gerne dabei."

                "Atropos" "Die Totenehrungen sind jedes Mal ein unvergessliches Ereignis. Ich freue mich schon darauf!"

                "Ireia" "Ich komme natürlich ebenfalls. Dein Bruder war ein guter Mensch, Neiro, dem das Glück aller Menschen sehr am Herzen lag. Er verdient es angemessen geehrt und gefeiert zu werden."

                "Neiro" "Danke, das freut mich sehr zu hören. Gebt die Einladung gerne an alle weiter. Ich freue mich, wenn viele Leute kommen!"

                "Tycho" "Du kannst dich auf uns verlassen. Das wird die beste Totenehrung dieses Jahres, versprochen."

                "Neiro" "Das ohnehin. Immerhin findet sie in meiner Familie statt. Das passiert auch nicht alle Tage. Meine Eltern sind schon seit Tagen am planen was es alles zu Essen geben soll."

                "Atropos" "Kann ich mir vorstellen. Als letztes Jahr mein Vater starb war die Planung seiner Ehrung auch ein großes Ereignis für meinen Bruder und mich gewesen."

                "Tycho" "Es war dafür aber auch eine wunderschöne Ehrung gewesen, die deinem Vater würdig gewesen war."

                "Atropos" "Das stimmt."

                jump nachentscheidung4


            label nachentscheidung4:
                "Atropos" "Also dann, ich muss leider langsam los. Heute wartet ein Berg an Arbeit auf mich."

                "Tycho" "Mach´s gut, bis zur Mittagspause."

                "Ireia" "Auf Wiedersehen."

                scene hall

                # Atropos Gedanken
                "Es war schön, mal wieder eine Runde mit ihnen zu reden."

                # Atropos Gedanken
                "Ich sollte öfter mal bei ihnen vorbeischauen."


                show chesis smiling:
                    xalign 0.5

                "Chesis" "Guten Morgen!"

                "Atropos" "Hey Chesis, wie schön dir über den Weg zu laufen!"

                "Atropos" "Hast du Kloth heute schon gesehen?"

                show chesis confused

                "Chesis" "Nein. Ich…"

                "Atropos" "Ach, auch egal. Die Hauptsache ist, dass er später beim Grillen auftaucht."

                "Atropos" "Erinnerst du dich noch daran, wie wir früher immer noch Ewigkeiten hier im Flur gestanden hatten?"

                show chesis grinning

                "Chesis" "Klar, wie könnte ich das vergessen. Es ist schade, dass Kloth uns keine Gesellschaft mehr leistet, aber es ist auch so schön. Und wir sehen ihn ja nach der Arbeit."

                "Atropos" "Alleine das eine Mal, als Kloth zu uns gelaufen kam, um uns zu erzählen, dass er Anans Chefsekretär werden soll!"

                show chesis grinning2

                "Chesis" "Stimmt, das war unvergesslich! Kloth kam zu uns gelaufen und…"

    # hier fehlt noch sepiafilter
                show sepia

                show chesis smiling behind sepia:
                    xalign 0.75

                show kloth grinning behind sepia:
                    xalign 0.25

                "Kloth" "Atropos… Chesis… hier seid ihr…"

                "Atropos" "Du bist ja völlig außer Atem und strahlst über das ganze Gesicht. Was hat dir dieses unglaubliche Glück bereitet?"

                "Kloth" "Ihr werdet mir diese Neuigkeiten nicht glauben… ich hätte niemals damit gerechnet, dass mir so etwas jemals passieren würde!"

                "Chesis" "Erzähl schon."

                "Kloth" "Ihr wisst doch, dass ich gestern zu Anan gerufen wurde. Ich hatte mich ja da schon gefragt, wie ich zu dieser Ehre kam…"

                "Atropos" "Und? Was war der Grund?"

                "Kloth" "Es ist so unglaublich! Ich wurde zu seinem Chefsekretär befördert. Ich kann es immer noch nicht richtig fassen…"

                show chesis grinning

                "Chesis" "Herzlichen Glückwunsch, du hast es verdient!"

                "Atropos" "Kloth, das sind ja fantastische Neuigkeiten. Ich freue mich riesig für dich!"

                "Kloth" "Es war schon immer mein Traum, der Menschheit dienen zu können und als Anans Chefsekretär ist mir das nun wirklich möglich!"

                "Chesis" "Wenn jemand von uns so etwas erreichen konnte, dann du."

                "Kloth" "Du bist aber ebenfalls unglaublich, Chesis. Du bist der beste Verkäufer, den Aither besitzt!"

                "Kloth" "Und Atropos, bei dir geht ja auch schon länger das Gerücht um, dass du zum Leiter des Labors befördert werden sollst!"

                "Atropos" "Wir erklimmen wohl alle gerade die Leiter. Aber ich könnte mir auch nichts anderes für mein Leben vorstellen."

                "Atropos" "Wir helfen den Menschen dabei ein glückliches Leben zu führen."

                show chesis confused

                "Chesis" "Kloth, was sind dann eigentlich deine Tätigkeiten?"

                show kloth unsuresmiling

                "Kloth" "Sorry, aber das muss mein kleines Geheimnis bleiben. Ihr wisst, dass ich euch sonst alles sage, aber darüber darf ich nicht reden."

                "Atropos" "Ja klar, verstehe ich. Letztlich spielt es ja auch keine Rolle. Wichtig ist nur, dass wir für Aither arbeiten."

                hide kloth
                hide sepia

    # Ende Sepiafilter

                show chesis smiling

                "Atropos" "An solche Momente erinnere ich mich immer wieder gerne. Ich schätze jede Sekunde, die ich mit Kloth und dir verbringen darf."

                "Chesis" "Geht mir genauso. Ihr seid meine besten Freunde seit der Kindheit."

                show chesis grinning

                "Chesis" "Damals, ohne euch und ohne die Happinesspille, war ich einsam und verloren gewesen. Alles hatte sich geändert, nachdem ich euch kennenlernen durfte."

                "Atropos" "Du hast uns damals auch sehr geholfen. Es ist gut jemanden in der Gruppe zu haben, der etwas ruhiger und bedachter ist. (lacht)"

                show chesis smiling

                "Chesis" "Da vorne ist Anan. Wie soll ich ihn nur begrüßen?"

                show anan 1:
                    xalign 0.25

                "Anan" "Guten Morgen und Glück für die Welt."

                "Atropos" "Glück für die Welt."

                hide anan

                show chesis confused

                "Chesis" "Jetzt habe ich meine Chance verpasst. Aber ist er nicht einfach nur unglaublich? Seine Präsenz nimmt den ganzen Raum ein, ohne dass er dafür etwas tun müsste."

                "Atropos" "Da kann ich dir nur zustimmen. Er ist wirklich beeindruckend."

                show chesis smiling

                "Chesis" "Also dann, ich muss jetzt hier weiter. Man sieht sich."

                "Atropos" "Mach´s gut. Wir sehen uns dann ja spätestens beim Grillen."

                "Atropos" "Oder in der Mittagspause, wenn wir sie gleichzeitig machen sollten."

                show chesis grinning2

                "Chesis" "Gerne."

                hide chesis

                "Atropos" "Ich sollte dann nun wirklich ins Labor."

                scene lab
                stop music fadeout 2
                play music "Sound_labor_sorglos.mp3" fadeout 3

                "Atropos" "Hey Era."

                show era normal:
                    xalign 0.5

                "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

                "Era" "…"

                "Atropos" "…"

                "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

                "Atropos" "Ja, natürlich… sorry…"

                "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

                "Era" "Ich… ahhhh…"

                # Atropos Gedanken
                "Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

                # Atropos Gedanken
                "Zum Glück bekommt sie sich immer relativ rasch wieder in den Griff."

                "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen musst."

                "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

                "Atropos" "Was wolltest du?"

                "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

                "Era" "…"

                "Era" "Was ich dich jedenfalls fragen wollte: Hast du nächste Woche Zeit? Ich dachte mir, wir könnten uns vielleicht mal treffen?"

                # Atropos Gedanken
                "Das war bei ihr mal wieder eine 180 Grad Wendung. Manchmal frage ich mich…"


                # Symbiont
                "{i}Sie ist einfach ein wenig unsicher. Es wirkt, als würde sie sich für dich interessieren. Darum ist sie nervös und weiß nicht, wie sie sich dir gegenüber verhalten soll. {/i}"


                # Symbiont
                "{i}Du solltest sie ein wenig beruhigen. Du magst sie doch auch, gestehe es dir ein. {/i}"

                "Atropos" "Gerne, warum nicht? Passt dir Donnerstag? Wir könnten Bowlen gehen."

                "Era" "Wirklich? Ich… ja… ja… Donnerstag passt super!"

                show era normal:
                    xalign 0.25

                show narcais normal:
                    xalign 0.75

                "Narcais" "Einen glücklichen guten Morgen zusammen. Habt ihr schon meine letzten Forschungsergebnisse gesehen? Ich kann mich selbst nur loben, sie sind hervorragend ausgefallen."

                "Era" "G-Guten Morgen…"

                "Atropos" "Morgen… hattest du dich nicht mit dem Einfluss der Impfung auf Kinder und Jugendliche beschäftigt?"

                "Narcais" "Ja, genau. Und ich bin zu dem Schluss gekommen, dass wir es mit Glycohexatenol versuchen sollten."

                "Narcais" "Die Jugendlichen vertragen den alten Wirkstoff ebenfalls gut, aber nachweislich können wir keine Kinder damit impfen."

                "Narcais" "Dies birgt allerdings bekannter Weise hohe Risiken, weil die Umweltverschmutzungen durch den Krieg auch Kinder betreffen können."

                "Narcais" "Auch ist die Impfung eine Grundvoraussetzung für die Einnahme der Happiness-Pille. Bereits jetzt leiden viel zu viele Kinder unter der späten Einnahme."

                "Narcais" "Die Kinder sollten ebenfalls in der Lage sein eine glückliche Kindheit führen zu dürfen! Wenn ich an meine eigene Kindheit denke…"

                "Atropos" "Narcais- du zählst nur Fakten auf, die bereits bekannt sind. Was ist jetzt mit dem Glycohexatenol?"

                # Atropos Gedanken
                "Er nutzt wirklich jede Chance, um mit seinem Wissen zu prahlen…"

                "Narcais" "Ich habe die Erkenntnis gewonnen, dass der Wirkstoff die Durchführung der Impfung um einige Jahre vorverlegen dürfte."

                "Narcais" "Diesbezüglich hatte ich einige Forschungen durchgeführt, welche meine Erkenntnis belegt hatten."

                "Narcais" "Ich habe bereits einen umfassenden Bericht dazu verfasst und dir geschickt. Aber du musst vermutlich nur einen kurzen Blick darauf werfen…"

                "Narcais" "Du weißt, dass ich immer beste Arbeit abliefere und keine Fehler mache."

                "Atropos" "Danke, ich beschäftige mich später damit."

                "Narcais" "Ja, natürlich. Lass dir Zeit. Nicht jeder kann so schnell und effizient arbeiten wie ich…"

                hide narcais

                "Atropos" "Sorry für die Unterbrechung, Era. Also, wir schreiben dann einfach die Tage, okay?"

                "Era" "J-Ja… natürlich. Danke Atropos!"



                jump good_mood

    else:

        scene hall

        # Atropos Gedanken
        "Da vorne liegt das Büro- ich frage mich, ob die anderen wohl schon da sind? Ich bin heute ziemlich früh dran."

        stop music fadeout 1
        play music "Sound_Buro.mp3" fadeout 2

        scene office_1

        # Atropos Gedanken
        "Hmm, es scheint noch keiner hier zu sein."

        # Atropos Gedanken
        "{i}Dann bin ich wohl wirklich zu früh dran."

        menu:
            "Ich schaue mir den Kalender an.":
                jump watchofficecalendar

            "Da ist ein interessantes Foto.":
                jump watchofficephoto

            "Neben der Sanduhr liegt etwas.":
                jump watchofficehourglass

            "Oder nein, besser nicht. Ich sollte nicht in fremden Sachen herumstöbern.":
                jump watchnothingoffice

        label watchofficecalendar:
            scene detail_calendar
            # Atropos Gedanken
            "September 2256."
            # Atropos Gedanken
            "Der Todestag meiner Mutter jährt sich bald wieder. Ich war noch so klein… Ich kann mich gar nicht mehr an sie erinnern."
            # Atropos Gedanken
            "Vielleicht kommt Mora dann mal wieder zu Besuch, um gemeinsam zu feiern."
            # nach Button-Klick
            scene office_1
            jump watchnothingoffice

        label watchofficephoto:
            scene detail_photo_neiro
            # Atropos Gedanken
            "Oh, Neiro! Das daneben muss dann wohl sein Bruder sein. Die beiden scheinen allen Anschein nach gut miteinander auszukommen."
            # Atropos Gedanken
            "Was sein Bruder wohl jetzt so macht?"
            scene office_1
            jump watchnothingoffice

        label watchofficehourglass:
            scene detail_hourglass
            # normalerweise nach Button-Klick!!
            # Atropos Gedanken
            "Was steht da?"
            show detail_hourglass_overlay
            # normalerweise nach Button-Klick!!
            # Atropos Gedanken
            "Ein Gedicht. Wohl von Neiro."
            scene office_1
            jump watchnothingoffice

        label watchnothingoffice:

            # Atropos Gedanken
            "Ich höre Stimmen, könnten sie das sein?"

            # Atropos Gedanken
            "Tatsächlich, sie sind es und sie scheinen sich eh noch zu unterhalten bevor sie den Tag starten. Ich sollte mich zu ihnen gesellen."

            scene office_2

            "Atropos" "Hey Leute."

            show ireia normal:
                xalign 0.5

            "Ireia" "Atropos, wie schön dich hier mal wieder anzutreffen. Du hast dich schon seit einer Weile nicht mehr im Büro blicken lassen. Vermisst hast du uns wohl nicht sonderlich."

            "Atropos" "Nun, ist ja auch nicht so ganz mein Arbeitsplatz. (lacht) Und keine Sorge, ich habe euch alle vermisst."

            show tycho normal:
                xalign 0.75

            "Tycho" "Das will ich dir aber auch geraten haben. (lacht) Uns kann man doch gar nicht {b}nicht{/b} mögen, nicht wahr? Und dementsprechend musst du uns auch vermisst haben."

            show armene normal:
                xalign 1

            "Armene" "Ja. Ja, das stimmt! Hallo Atropos."

            "Atropos" "Hi Armene, wie geht es dir?"

            "Armene" "Ich bin glücklich wie immer!"

            "Ireia" "Jetzt überfall die Arme doch nicht, du kennst sie doch."

            "Ireia" "Und Armene, du solltest weiter deine Präsentation über das firmeninterne Kommunikationssystem vorbereiten- ich erwarte bessere Arbeit von dir als letztes Mal."

            "Armene" "Natürlich Ireia, tut mir leid."

            hide armene normal

            "Tycho" "Neiro, gesell dich doch zu uns, was sitzt du so einsam und verlassen an deinem Platz? Deine Arbeitszeit hat doch noch nicht angefangen."

            show neiro normal:
                xalign 0.25

            "Neiro" "Oh… ich hatte euch gar nicht bemerkt, tut mir leid. Atropos? Was machst du hier? Arbeitest du nicht in einer anderen Abteilung? Verkauf oder so?"

            "Atropos" "Neiro wie er leibt und lebt. (lacht)"

            "Ireia" "Du solltest definitiv an deinem Gedächtnis arbeiten, Neiro. Es wird in letzter Zeit immer kritischer. Ich möchte deswegen von dir keine schlechteren Ergebnisse sehen."

            "Neiro" "Natürlich Ireia, ich gebe weiterhin mein Bestes, du musst dir keine Sorgen machen."

            # Atropos Gedanken
            "Neiro hatte schon immer eine seltsame Art mit Kritik umzugehen. Aber immerhin verträgt er dadurch Ireias direkte Art gut."

            "Tycho" "Habt ihr es eigentlich schon gehört? Anan will anlässlich des diesjährigen 37. Gründungstages wieder eine riesige Feier veranstalten!"

            "Ireia" "Dann sollten wir noch härter arbeiten, damit wir auch einen Anlass zum Feiern haben. Das Glück der Menschen entsteht nicht von selbst."

            "Tycho" "Natürlich arbeiten wir hart! Aber das tut man für Aither doch auch gerne."

            "Tycho" "Zurück zum Thema… diese Party wird gigantisch. Erinnert ihr euch noch an die anlässlich des 30. Gründungstages?"

            "Atropos" "Damals hatte ich noch nicht hier gearbeitet. So alt bin ich nun auch nicht. (lacht)"

            "Tycho" "Ach stimmt, du bist ja ein paar Jahre jünger als ich, oder? 24?"

            "Atropos" "Fast… 25. (grinst)"

            "Tycho" "Jedenfalls… wo war ich stehen geblieben?"

            "Tycho" "Ach ja, der 30. Gründungstag… eine bessere Feier habe ich noch nie erlebt! Und ich war schon auf vielen Feiern gewesen, das könnt ihr mir glauben."

            "Tycho" "Damals hatte ich gerade erst hier angefangen. Ich war nur ein einfacher Praktikant gewesen, aber dennoch schenkte Anan mir eine Einladung."

            "Tycho" "Ich konnte mein Glück kaum fassen. Es war berauschend! All das Essen im Überfluss und dann die Musik, der Tanz…"

            "Ireia" "Tycho, fass dich kürzer. Wir haben noch Arbeit zu erledigen. Und jetzt erzähl schon, was hast du vom diesjährigen Gründungstag gehört?"

            "Atropos" "Ja… du kannst doch nicht die Information anteasern und dann damit hinter dem Berg halten."

            show armene normal:
                xalign 1

            "Tycho" "Sorry, sorry… also, ich weiß nicht viel, aber angeblich sollen Atlas und Adrés höchstpersönlich vorbeikommen, um gemeinsam mit Anan diesen Tag zu feiern."

            "Atropos" "Habe ich dich gerade richtig verstanden? Die großen Drei, alle hier in Astoa?"

            "Ireia" "Das sind ja unglaubliche Neuigkeiten! Wieso hast du uns nicht schon früher davon erzählt?"

            "Tycho" "Weil ich davor selbst nur ganz vage Gerüchte gehört habe, aber mittlerweile verstärkt sich der Eindruck immer mehr, dass an den Gerüchten etwas Wahres dran sein könnte."

            "Atropos" "Ich frage mich, wie die beiden wohl sind. Natürlich kennt man ihre Namen… immerhin sind Anan, Atlas und Adrés die Gründer von Aither und diejenigen, die den Krieg beendet haben…"

            "Atropos" "Dennoch kenne ich Atlas und Adrés nur von Fotos und nicht von Videoaufzeichnungen oder anderen Quellen. Es wird ein ziemliches Geheimnis um ihre Existenz gemacht."

            "Ireia" "Das ist aber auch gut so. Die drei sind immerhin dafür verantwortlich, dass alle Menschen glücklich sind."

            "Ireia" "Da haben sie Wichtigeres zu tun, als sich darum zu kümmern, dass wir Informationen über sie bekommen."

            "Armene" "Ich frage mich, ob Atlas und Adrés wohl auch so unglaublich charmant und gutaussehend sind wie Anan… (seufzt verträumt)"

            "Ireia" "Armene? Wie lange stehst du schon hier? Bist du fertig mit deiner Präsentation?"

            "Armene" "Nein… Ich wollte mich nur am Gespräch beteiligen…"

            "Neiro" "Um was geht es? Tut mir leid, ich bin mit den Gedanken kurz abgeschweift…"

            "Neiro" "Mein Bruder ist gestern gestorben und wir müssen noch die Feier ihm zu Ehren vorbereiten…"

            "Tycho" "(lacht) Und wieder das übliche Chaos. Es macht echt zu viel Spaß mit euch Zeit zu verbringen!"

            "Ireia" "Armene, los an die Arbeit!"

            "Armene" "Ja natürlich Ireia, mache ich!"

            hide armene normal

            # Atropos Gedanken
            "Was mich gerade interessieren würde…"

            menu:
                "Ich hätte gerne mehr Informationen über die Gründungsfeier.":
                    jump entscheidung4_1V2
                "Ich würde mich gerne noch etwas mehr über die Großen Drei unterhalten.":
                    jump entscheidung4_2V2
                "Ich will mich bei Neiro nach seinem verstorbenen Bruder erkundigen.":
                    jump entscheidung4_3V2

            label entscheidung4_1V2:

                $ neiro_unterhalten = True

                "Atropos" "Tycho, hast du noch mehr Informationen über die diesjährige Gründungsfeier?"

                "Tycho" "Hmm, gute Frage- lass mich einen Moment überlegen…"

                "Neiro" "Ihr sprecht über die Gründungsfeier?"

                "Ireia" "Ja, darum ging es schon die ganzen letzten Minuten."

                "Neiro" "Oh. Jedenfalls, ich weiß ein bisschen was…"

                "Tycho" "Worauf wartest du noch? Erzähl schon!"

                "Neiro" "Atlas und Adrés werden hierher nach Astoa kommen, um der Gründungsfeier beizuwohnen!"

                "Atropos" "Neiro, das wissen wir bereits. (lacht) Immerhin haben wir dadurch noch einmal die Bestätigung."

                "Ireia" "Weißt du sonst noch etwas? Irgendwelche Neuigkeiten?"

                "Neiro" "Es hieß, dass heute im Laufe des Tages noch eine offizielle Ankündigung des Ganzen erfolgen soll."

                "Atropos" "Eine offizielle Ankündigung? Also einfach eine Durchsage von Anan?"

                "Neiro" "Nein, soweit ich das weiß, werden alle drei live geschaltet."

                "Ireia" "Das gab es ja noch nie! Normalerweise kommunizieren wir nicht mit den Menschen außerhalb von Astoa… warum sollten wir auch?"

                "Tycho" "Das sind wirklich unglaubliche Neuigkeiten! Ich freue mich schon darauf. Die diesjährige Gründungsfeier wird unbeschreiblich und unvergesslich werden!"

                "Neiro" "Und es gibt noch etwas: Angeblich soll mit der Gründungsfeier eine neue Happiness-Pille vorgestellt werden."

                "Ireia" "Eine neue Pille? Sag nicht, dass es eine Pille sein wird, die uns noch glücklicher macht?"

                "Tycho" "Ich wüsste nicht, was es sonst sein könnte… der Tag wird ja immer besser!"

                "Ireia" "Atropos, müsstest du darüber nicht eigentlich mehr wissen?"

                # Atropos Gedanken
                "Eine neue Pille? Ob sie dann wohl besser wirkt als die aktuelle? Immerhin scheine ich sie momentan nicht wirklich für mein Glück zu brauchen."

                # Symbiont
                "{i}Doch, du brauchst sie. Merkst du nicht, dass du immer mehr zu zweifeln beginnst? Zweifel säen Unmut und Unzufriedenheit. Du gefährdest dein Glück. {/i}"

                jump nachentscheidung4V2

            label entscheidung4_2V2:

                "Atropos" "Ich bin wirklich gespannt auf Atlas und Adrés."

                "Ireia" "Sie wollen das Beste für die Welt, genauso wie Anan. Ist das nicht das Einzige, das zählt?"

                "Tycho" "Ihnen ist unser Wohl am aller Wichtigsten. Stellt euch nur vor, wie die Welt ohne sie wäre. Ich wage es gar nicht, mir das vorzustellen!"

                "Ireia" "Wir wären immer noch im Krieg versunken. Ohne die Happiness-Pille, ohne glückliche Menschen würde es nur weiter Streit und Zwietracht geben."

                "Atropos" "Ich frage mich immer noch, wie ausgerechnet diese drei Männer es damals geschafft haben uns den Frieden zu schenken…"

                "Tycho" "Natürlich durch unsere Glücklichkeit: Happiness. Das ist das Einzige, was wirklich zählt. Spielen andere Gründe oder genauere Erläuterungen eine Rolle?"

                "Ireia" "Nein, das ist nun wirklich nichts, worüber wir uns Gedanken machen müssten."

                "Ireia" "Sie schenkten uns Happiness und beendeten damit den 50-jährigen Krieg. Darum sind wir heute glücklich. Darum dürfen wir das Leben unserer Träume leben!"

                # Symbiont
                "{i} Sie haben Recht. Warum solltest du dir weiter darüber Gedanken machen? Es spielt keine Rolle. Die Hauptsache ist ein glückliches Leben und das besitzt du. {/i}"

                # Atropos Gedanken
                "Ja, ich besitze ein glückliches Leben. Aber sollte man aus diesem Grund dennoch nichts hinterfragen?"

                "Atropos" "Sollten wir nicht mehr erfahren dürfen? Wieso machen Anan und die anderen beiden so ein großes Geheimnis aus der Vergangenheit?"

                "Atropos" "Wir wissen, dass sie den Krieg beendet haben und dass das mit Hilfe der Happiness-Pille passiert ist… aber wie?"

                "Ireia" "Habt ihr schon Mal die Ehre gehabt mit Anan zu sprechen?"

                # Atropos Gedanken
                "Sie übergehen mich. Ist das in letzter Zeit nicht irgendwie häufiger vorgekommen? Als würden sie die Wahrheit einfach nicht hören wollen."

                # Atropos Gedanken
                "Naja, egal, ich will mir gerade keine Gedanken mehr darum machen. Heute ist so ein schöner Tag. Ich sollte aufhören über so unnötiges Zeug nachzudenken."

                "Ireia" "Ich hatte Dank ein paar weniger Meetings mal mit ihm zu tun. Er ist die beeindruckendste Persönlichkeit, die ich jemals getroffen habe."

                "Ireia" "Und obwohl er fast schon gottgleichen Status hat, ist er trotzdem auf dem Boden geblieben und kümmert sich um jeden einzelnen von uns."

                "Neiro" "Es geht gerade um Anan? Was ist mit ihm? Ist er nicht toll? So zuvorkommend und aufmerksam- einen besseren Chef kann man sich nicht wünschen."

                "Tycho" "Ich hatte ein einziges Mal mit ihm gesprochen. Damals hatte ich vergessen meine Pille zu nehmen, weil ich eine Zeit lang krank war."

                "Atropos" "Das hattest du ja noch nie erwähnt… wie ist er damit umgegangen?"

                "Tycho" "Er war unglaublich verständnisvoll und hatte mir klar gemacht, dass er nur um mein Wohlergehen und mein Glück besorgt ist."

                # Atropos Gedanken
                "Ob Anan wohl auch bei mir so verständnisvoll reagieren würde, wenn er mitbekommen würde, dass ich die Pille nicht genommen habe?"

                "Tycho" "Durch dieses Ereignis ist mir noch einmal bewusst geworden, wie wichtig die Happiness-Pille eigentlich ist."

                "Tycho" "Ich bin froh, dass Anan mir die Augen geöffnet hat. Ihr wisst gar nicht, wie sehr ich es damals bereut hatte."

                "Tycho" "Anan gibt alles, damit es uns gut geht und wir glücklich sind. Wie hatte ich es ihm nur so danken können?"

                "Atropos" "Tycho… wie…"

                "Tycho" "Ich… Ich bin so glücklich, dass ich eine zweite Chance erhalten habe. Jetzt kann ich dabei helfen allen Menschen ihr Glück zu geben!"

                jump nachentscheidung4V2

            label entscheidung4_3V2:

                "Atropos" "Neiro, dein Bruder ist gestorben?"

                "Neiro" "Achso… ja. Er ist von einem der Busse erwischt worden, der eine technische Fehlfunktion hatte."

                "Ireia" "Möge er nun in Frieden glücklich sein."

                "Atropos" "Wann findet seine Ehrung statt?"

                "Neiro" "Genau steht es noch nicht fest, aber voraussichtlich kommenden Sonntag. Ihr seid alle herzlich eingeladen, wenn ihr wollt. Es wird ein riesiges Fest geben."

                "Tycho" "Habe ich da Fest gehört? Da kann man doch gar nicht nein sagen, ich bin so was von dabei! Atropos, wie sieht es bei dir aus?"

                "Atropos" "Ich muss später nochmal in meinen Terminkalender schauen, aber ansonsten bin ich natürlich auch gerne dabei."

                "Atropos" "Die Totenehrungen sind jedes Mal ein unvergessliches Ereignis. Ich freue mich schon darauf!"

                "Ireia" "Ich komme natürlich ebenfalls. Dein Bruder war ein guter Mensch, Neiro, dem das Glück aller Menschen sehr am Herzen lag. Er verdient es angemessen geehrt und gefeiert zu werden."

                "Neiro" "Danke, das freut mich sehr zu hören. Gebt die Einladung gerne an alle weiter. Ich freue mich, wenn viele Leute kommen!"

                "Tycho" "Du kannst dich auf uns verlassen. Das wird die beste Totenehrung dieses Jahres, versprochen."

                "Neiro" "Das ohnehin. Immerhin findet sie in meiner Familie statt. Das passiert auch nicht alle Tage. Meine Eltern sind schon seit Tagen dabei zu planen, was es alles zu Essen geben soll."

                "Atropos" "Kann ich mir vorstellen. Als letztes Jahr mein Vater starb, war die Planung seiner Ehrung auch ein großes Ereignis für meinen Bruder und mich gewesen."

                "Tycho" "Es war dafür aber auch eine wunderschöne Ehrung gewesen, die deinem Vater würdig gewesen war."

                "Atropos" "Das stimmt."


                jump nachentscheidung4V2


            label nachentscheidung4V2:
                "Atropos" "Also dann, ich muss leider langsam los. Heute wartet ein Berg an Arbeit auf mich."

                "Tycho" "Mach´s gut, bis zur Mittagspause!"

                "Ireia" "Auf Wiedersehen."

                scene hall

                jump worknachzelos

label work:
    show zelos normal

    "Atropos" "Ich wollte ohnehin erstmal ins Labor gehen."

    "Zelos" "Dann lass dich von mir nicht aufhalten. Ich bin der Letzte, der etwas gegen Arbeit sagen würde."

    "Atropos" "(lacht) Das ist mir durchaus bewusst. So gewissenhaft wie du ist wohl kaum einer, abgesehen von Chesis und Kloth. Die beiden haben es wirklich weit gebracht."

    "Zelos" "Ich be…"

    "Zelos" "(räuspert sich) Ich freue mich unglaublich für die beiden. Sie sind so weit gekommen und vor allem Kloth wird noch so viel mehr erreichen."

    "Atropos" "Als Kind hätte er sich vermutlich auch niemals vorstellen können eines Tages Chefsekretär von Anan zu werden."

    "Zelos" "Also dann, ich muss nun wirklich weitermachen. Aither öffnet bald und die Pillen lagern sich weder von selbst ein, noch verkaufen sie sich von allein."

    "Atropos" "Mach´s gut, wir sehen uns!"

    "Zelos" "Ach Atropos, ich vergaß: Bist du um 12:15 Uhr in der Mensa dabei?"

    "Atropos" "Ich denke, ich müsste es schaffen. Bis dann, man sieht sich."

    "Zelos" "Bis nachher und einen wunderschön glücklichen Tag in der besten Firma der Welt!"

    label worknachzelos:

        if pill_taken:

            scene hall

            # Atropos Gedanken
            "Was muss ich heute noch alles erledigen? Narcais wollte mir seinen Bericht über seine letzten Forschungen schicken und sonst…"

            # Atropos Gedanken
            "Ach ja, stimmt. Ich muss noch einmal die Wirkstoffliste der Tabletten durchgehen. Anan wollte, dass ich alle erfasse, weil er Änderungen vornehmen möchte."

            # Atropos Gedanken
            "Ich bin gespannt, was die neuen Wirkstoffe alles bewirken…"

            # Atropos Gedanken
            "Letztlich werde ich es wohl erst erfahren, wenn die Pille im Verkauf ist, immerhin arbeitet jeder nur an einem winzigen Teil des großen Ganzen."

            show anan 1:
                xalign 0.5

            "Anan" "Guten Morgen und Glück für die Welt."

            "Atropos" "Guten Morgen."

            "Anan" "Atropos Laiotas- richtig? Kann ich die Liste heute noch von dir erwarten? Sie wird von meinen anderen Forschern benötigt."
            # Atropos Gedanken
            "Anan kennt meinen Namen? Das werden die anderen niemals glauben, wenn ich es ihnen erzähle…"

            "Atropos" "Ja, natürlich, ich stelle sie dir heute fertig."

            "Anan" "Vielen Dank! Wir alle schätzen deine Arbeit sehr. Denk immer daran: Den Glücklichen gehört die Welt. Kein Mensch sollte unglücklich sein."

            "Atropos" "Ich werde es nicht vergessen!"

            "Anan" "Ich erwarte den Bericht um 16 Uhr in meinem Postfach."

            "Atropos" "Natürlich, ich werde dich nicht enttäuschen!"

            "Anan" "Du könntest mich niemals enttäuschen. Ich wünsche dir einen Tag voller Glücklichkeit."

            hide anan

            # Atropos Gedanken
            "Anan hat tatsächlich mit mir gesprochen? Ich muss träumen…"

            # Atropos Gedanken
            "Er war höflich gewesen, aber gleichzeitig so einnehmend. Man kann ihm keinen Wunsch abschlagen."

            # Atropos Gedanken
            "Und dass er sich die Zeit genommen hat, mit mir zu sprechen, obwohl er Anan ist… Er kümmert sich wirklich um das Glück aller Menschen. Es ist nicht nur leeres Gerede."


            # Atropos Gedanken
            "Jetzt sollte ich aber weiter ins Labor. Ich will Anan nicht enttäuschen."

            stop music fadeout 1
            play music "Sound_labor_sorglos.mp3" fadeout 2
            scene lab

            "Atropos" "Hey Era."

            show era normal:
                xalign 0.5

            "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

            "Era" "…"

            "Atropos" "…"

            "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

            "Atropos" "Ja, natürlich… sorry…"

            "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

            "Era" "Ich… ahhhh…"

            # Atropos Gedanken
            "Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

            # Atropos Gedanken
            "Zum Glück bekommt sie sich immer relativ rasch wieder in den Griff."

            "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen müsstest."

            "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

            "Atropos" "Was wolltest du?"

            "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

            "Era" "…"

            "Era" "Was ich dich jedenfalls fragen wollte: Hast du nächste Woche Zeit? Ich dachte mir wir könnten uns vielleicht mal treffen?"

            # Atropos Gedanken
            "Das war bei ihr mal wieder eine 180 Grad Wendung. Manchmal frage ich mich…"


            # Symbiont
            "{i}Sie ist einfach ein wenig unsicher. Es wirkt, als würde sie sich für dich interessieren. Darum ist sie nervös und weiß nicht, wie sie sich dir gegenüber verhalten soll. {/i}"

            # Symbiont
            "{i}Du solltest sie ein wenig beruhigen. Du magst sie doch auch, gestehe es dir ein. {/i}"

            "Atropos" "Gerne, warum nicht? Passt dir Donnerstag? Wir könnten Bowlen gehen."

            "Era" "Wirklich? Ich… ja… ja… Donnerstag passt super!"

            "Atropos" "Dann ist es abgemacht."

            "Era" "Kommen… kommen Chesis und Kloth dann auch mit? Ihr drei seid wirklich unzertrennlich, seit ihr hier angefangen habt…"

            "Atropos" "Möchtest du denn, dass sie mitkommen?"

            "Era" "Also… Ich… Ich… Nein, ehrlich gesagt, würde ich lieber Zeit mit dir alleine verbringen."

            show narcais normal:
                xalign 0.25

            show era normal:
                xalign 0.75


            "Narcais" "Einen glücklichen guten Morgen zusammen. Was habe ich verpasst? Redet ihr über mich?"

            "Atropos" "Morgen… Und nein, nicht jedes Gespräch dreht sich gleich um dich, Narcais. (lacht)"

            "Era" "G-Guten Morgen… es ging gerade um Kloth und Chesis."

            "Narcais" "Ach die drei unzertrennlichen Freunde. Ihr wart schon damals in der Schule berühmt berüchtigt. Keiner konnte euch das Wasser reichen."

            "Narcais" "Abgesehen von mir natürlich, aber das haben alle verkannt."

            "Era" "Hattet ihr damals eigentlich alle gleichzeitig angefangen hier zu arbeiten, Atropos?"

            "Atropos" "Nein, Kloth hatte ein paar Jahre vor uns angefangen. Er wurde damals von Anan höchstpersönlich rekrutiert."

            "Era" "Von Anan?"

            "Atropos" "Kloth hatte bei einer Feier eine Rede über Aither und die Bedeutung des Glücks gehalten und konnte so Anan von sich überzeugen."

            "Era" "Kloth ist wirklich mitreißend. Er ist Anan sehr ähnlich. Fast schon wie Vater und Sohn."

            "Atropos" "Das stimmt wohl. (lacht)"

            "Era" "Und… und was war mit Chesis und dir gewesen?"

            "Atropos" "Kloth hatte mich zu einem Praktikum überredet und es war die beste Entscheidung meines Lebens, es zu machen."

            "Atropos" "Und dann hatten Kloth und ich Chesis überzeugt doch ebenfalls hier anzufangen, weil er hier gute Chancen hat trotz seiner introvertierten Art."

            "Era" "Stimmt… es ist wirklich schwer mit ihm zu reden… ich hatte es ein paar Mal versucht und dann musste ich aufgegeben. Dir gegenüber ist er dagegen so offen."

            "Atropos" "Wir sind immerhin auch schon seit Ewigkeiten befreundet. Ich bin mir sicher, mit der Zeit wird er sich auch dir gegenüber mehr öffnen."

            "Era" "Das… das wäre sehr schön."

            "Narcais" "Seid ihr fertig mit eurem Gespräch über nicht anwesende Personen? Ich bin auch noch da."

            "Atropos" "Wer könnte dich vergessen? (lacht)"

            "Narcais" "Niemand, das ist mir bewusst!"

            "Narcais" "Jedenfalls: Ich habe einen Bericht verfasst, den du noch durcharbeiten müsstest."

            "Narcais" "Ich bin mir sicher, dass er keine Fehler hat, immerhin habe ich ihn erstellt, aber so ist nun mal die Vorschrift."

            "Atropos" "Es ging um den Einfluss der Impfung auf Kinder und Jugendliche, richtig?"

            "Narcais" "Ja, genau. Und diesbezüglich: Ich habe einige…"

            "Atropos" "Können wir deinen Vortrag auf später verschieben? Ich muss noch etwas für Anan fertig zusammenstellen. Ich beschäftige mich später mit deinem Bericht."

            "Narcais" "Ich bin froh zu hören, dass wenigstens eine Person hier meine Arbeit wertschätzt. Ich arbeite nun weiter."

            jump good_mood

        else:
            scene hall

            # Atropos Gedanken
            "Da vorne ist Anan… ich hoffe er bemerkt nichts."

            # Symbiont
            "{i}Du hättest die Pille sofort heute Morgen nehmen sollen. Dann müsstest du dir jetzt keine Gedanken mehr darüber machen. {/i}"

            # Symbiont
            "{i}Diese Sorgen sind doch nichts Anderes als unnötiger Stress, die dein Glück verhindern. {/i}"

            # Symbiont
            "{i}Nimm die Pille jetzt ein. Werde wieder glücklich. Du hast es verdient ein sorgenfreies Leben zu haben. {/i}"

            show anan 1:
                xalign 0.5

            "Anan" "Guten Morgen und Glück für die Welt."

            "Atropos" "Guten Morgen."

            "Anan" "Atropos Laiotas- richtig? Kann ich die Liste heute noch von dir erwarten? Sie wird von meinen anderen Forschern benötigt."

            # Atropos Gedanken
            "Lass ihn nichts bemerken… bitte… ich darf nicht auffallen. Nicht vor ihm. Er gibt so viel für uns, ich darf ihn nicht enttäuschen."

            "Atropos" "Ja, natürlich, ich stelle sie dir heute fertig."

            "Anan" "Vielen Dank."

            "Anan" "…"

            "Anan" "Atropos. Du wirkst nicht glücklich, betrübt dich etwas?"

            # Atropos Gedanken
            "Hat er etwas gemerkt? Oder erkundigt er sich einfach nur höflichkeitshalber? Was soll ich tun? Verdammt…"

            # Symbiont
            "{i}Sag die Wahrheit und entschuldige dich. Nimm einfach die Happiness-Pille sofort wieder ein und alles kommt in Ordnung. {/i}"

            # Symbiont
            "{i} Vielleicht bist du ohne die Tablette ja doch nicht so glücklich wie du dachtest, wenn es Anan sofort aufgefallen ist. {/i}"

            "Atropos" "Ja, nein… ich…"

            "Anan" "Du hast Happiness in letzter Zeit nicht regelmäßig eingenommen."

            "Atropos" "Nein… ich habe es vergessen…"

            "Anan" "Ich erwarte dich in meinem Büro. Punkt elf und keine Sekunde zu spät."

            "Anan" "Du gefährdest mit solchen Aktionen nicht nur dein eigenes Glück, sondern auch das Glück der Menschen, die dir am Wichtigsten sind."

            "Anan" "Möchtest du das etwa?"

            "Atropos" "Nein… ich…"

            "Anan" "Die Menschheit braucht Happiness, sonst würde die Welt zurück ins Chaos fallen."

            "Anan" "Ich möchte nie wieder so etwas wie im Krieg damals erleben müssen. Kein Mensch sollte so etwas jemals wieder erleiden müssen."

            "Anan" "Ich habe jetzt zu tun, aber ich will dich später in meinem Büro sehen. Vergiss es nicht. Ich wünsche dir einen Tag voller Glücklichkeit."

            hide anan

            # Symbiont
            "{i}Anan hat Recht. Du solltest die Pille nehmen. Regelmäßig. Du willst doch glücklich sein. {/i}"

            # Atropos Gedanken
            "Ich… ah… ich weiß nicht was ich tun soll…"

            # Atropos Gedanken
            "Verdammt…"


            menu:
                "Anan hat ja recht...":
                    jump anan_is_right
                "Ich bin doch auch ohne Pille glücklich...":
                    jump why_important
                "Was erlaubt sich Anan bitte? Ich lasse mir doch nichts vorschreiben…":
                    jump be_against

label anan_is_right:
    $ straight_office = True

    # Atropos Gedanken
    "Anan hat ja recht. Ich sehe es ein. Es war ein Fehler gewesen…"

    # Atropos Gedanken
    "Happiness hat es geschafft die Welt aus den Fängen des Krieges zu befreien. Ohne die Pille hätte der Krieg noch viel Jahre mehr angedauert."

    # Atropos Gedanken
    "Ich wäre im Krieg geboren worden oder meine Eltern hätten mich vielleicht gar nicht erst bekommen."

    # Atropos Gedanken
    "Und wie Anan gesagt hat. Ohne die Tablette würde vermutlich auch jetzt die Welt wieder zurück ins Chaos fallen."

    # Atropos Gedanken
    "Was hatte ich mir nur dabei gedacht jemals zu zweifeln und zu zögern? Alle Menschen nehmen Happiness und alle, die Happiness nehmen, sind glücklich."

    # Atropos Gedanken
    "Ich werde diesen Fehler nicht noch einmal begehen. Zukünftig werde ich die Pille wieder regelmäßig einnehmen."

    # Atropos Gedanken
    "Ich werde nachher zu Anan gehen und mich für mein rücksichtloses Verhalten entschuldigen."

    # Atropos Gedanken
    "Aber jetzt erstmal zurück ins Labor. Ich habe noch einiges zu tun. Ich darf Anan nicht erneut enttäuschen."


    scene lab

    "Atropos" "Hey Era."

    show era normal:
        xalign 0.5

    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

    "Era" "…"

    "Atropos" "…"

    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

    "Atropos" "Ja, natürlich… sorry…"

    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

    "Era" "Ich… ahhhh…"

    # Atropos Gedanken
    "Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

    # Atropos Gedanken
    "Zum Glück bekommt sie sich immer relativ rasch wieder in den Griff."

    "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen müsstest."

    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

    "Atropos" "Was wolltest du?"

    "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

    "Era" "…"

    "Era" "Was ich dich jedenfalls fragen wollte: Hast du nächste Woche Zeit? Ich dachte mir wir könnten uns vielleicht mal treffen?"

    # Atropos Gedanken
    "Das war bei ihr mal wieder eine 180 Grad Wendung. Manchmal frage ich mich…"


    # Symbiont
    "{i}Sie ist einfach ein wenig unsicher. Es wirkt, als würde sie sich für dich interessieren. Darum ist sie nervös und weiß nicht, wie sie sich dir gegenüber verhalten soll. {/i}"


    # Symbiont
    "{i}Du solltest sie ein wenig beruhigen. Du magst sie doch auch, gestehe es dir ein. {/i}"

    "Atropos" "Gerne, warum nicht? Passt dir Donnerstag? Wir könnten Bowlen gehen."

    "Era" "Wirklich? Ich… ja… ja… Donnerstag passt super!"

    show narcais normal:
        xalign 0.25
    show era normal:
        xalign 0.75

    "Narcais" "Einen glücklichen guten Morgen zusammen. Habt ihr schon meine letzten Forschungsergebnisse gesehen? Ich kann mich selbst nur loben, sie sind hervorragend ausgefallen."

    "Era" "G-Guten Morgen…"

    "Atropos" "Morgen… hattest du dich nicht mit dem Einfluss der Impfung auf Kinder und Jugendliche beschäftigt?"

    "Narcais" "Ja, genau. Und ich bin zu dem Schluss gekommen, dass wir es mit Glycohexatenol versuchen sollten."

    "Narcais" "Die Jugendlichen vertragen den alten Wirkstoff ebenfalls gut, aber nachweislich können wir keine Kinder damit impfen."

    "Narcais" "Dies birgt allerdings bekannter Weise hohe Risiken, weil die Umweltverschmutzungen durch den Krieg auch Kinder betreffen können."

    "Narcais" "Auch ist die Impfung eine Grundvoraussetzung für die Einnahme der Happinesspille. Bereits jetzt leiden viel zu viele Kinder unter der späten Einnahme."

    "Narcais" "Die Kinder sollten ebenfalls in der Lage sein eine glückliche Kindheit führen zu dürfen! Wenn ich an meine eigene Kindheit denke…"

    "Atropos" "Narcais- du zählst nur Fakten auf, die bereits bekannt sind. Was ist jetzt mit dem Glycohexatenol?"

    # Atropos Gedanken
    "Er nutzt wirklich jede Chance, um mit seinem Wissen zu prahlen…"

    "Narcais" "Ich habe die Erkenntnis gewonnen, dass der Wirkstoff die Durchführung der Impfung um einige Jahre vorverlegen dürfte."

    "Narcais" "Diesbezüglich hatte ich einige Forschungen durchgeführt, welche meine Erkenntnis belegt hatten."

    "Narcais" "Ich habe bereits einen umfassenden Bericht dazu verfasst und dir geschickt. Aber du musst vermutlich nur einen kurzen Blick darauf werfen…"

    "Narcais" "Du weißt, dass ich immer beste Arbeit abliefere und keine Fehler mache."

    "Atropos" "Danke, ich beschäftige mich später damit."

    "Narcais" "Ja, natürlich. Lass dir Zeit. Nicht jeder kann so schnell und effizient arbeiten wie ich…"

    hide narcais

    "Atropos" "Sorry für die Unterbrechung, Era. Also, wir schreiben dann einfach die Tage, okay?"

    "Era" "J-Ja… natürlich. Danke Atropos!"
    hide era

    # Atropos Gedanken
    "Zurück an die Arbeit."

    "Atropos" "…"


    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"

    "Durchsage" "{i}Nimm Happiness ein und lebe dein Leben so wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit. {/i}"

    "Durchsage" "{i}In wenigen Minuten erfolgt eine Übertragung von Anan. Bitte schaltet die entsprechenden Bildschirme ein. {/i}"

    "Era" "Ich… ich kümmere mich darum!"

    # für den Fall, dass Atropos sich davor mit Neiro darüber unterhalten hat

    if neiro_unterhalten:
        "Das muss die Übertragung sein, die Neiro vorhin erwähnt hatte."

        # Atropos Gedanken
        "Ob er wohl mit allen Informationen Recht hatte?"

    # ab hier wieder alle
    scene triumvirate
    show anan 1:
        xalign 0.5
    show atlas normal:
        xalign 0
    show adres normal:
        xalign 0.99


    "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag gehabt."

    "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

    "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

    "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

    "Anan" "Der Gründungstag von Aither."

    "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

    "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

    "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

    "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

    "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

    "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

    "Anan" "Ich bin bereit alles dafür zu geben und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

    "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

    "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

    "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

    "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

    "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

    "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

    "Anan" "Weil ihr uns dabei helft das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die ersten, die die neue Happiness erhalten. "

    "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

    "Anan" "Vergesst niemals: Happiness. Dein Leben. Deine Entscheidung. Deine Glücklichkeit. "

    "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

    "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns überlassen haben."

    "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

    scene lab
    show era normal:
        xalign 0.25
    show narcais normal:
        xalign 0.75

    "Era" "Wow…"

    "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

    # Atropos Gedanken
    "Und das von jemandem, der sich selbst am liebsten den ganzen Tag zuhört."

    # Atropos Gedanken
    "Aber ich muss ihnen schon Recht geben. Seine Rede war beeindruckend wie immer."

    # Atropos Gedanken
    "Und Anan hat vermutlich ebenfalls Recht. Ich weiß ja, dass er nur das Beste für uns will…"

    "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

    "Atropos" "Ja, das ist er wohl. "

    "Atropos" "Jetzt sollten wir aber zurück an die Arbeit, wir müssen heute noch einiges schaffen."

    "Atropos" "…"

    # Atropos Gedanken
    "Oh, es ist schon spät. Ich muss langsam los, damit ich pünktlich bei Anans Büro bin."

    "Atropos" "Bin gleich wieder da."

    "Era" "Bis… bis später."


    jump go_office

label why_important:
    $ straight_office = True

    # Atropos Gedanken
    "Ich bin doch auch ohne Pille glücklich…"

    # Atropos Gedanken
    "Oder? Irre ich mich etwa? Denke ich nur selbst, dass ich glücklich bin, aber alle anderen erkennen die Wahrheit?"

    # Atropos Gedanken
    "Mache ich mir nur etwas vor?"

    # Atropos Gedanken
    "Bin ich wirklich glücklich?"

    # Atropos Gedanken
    "Was ist, wenn Anan Recht hat? Gefährde ich durch meine Aktionen auch das Glück der anderen?"

    # Atropos Gedanken
    "Ist Kloth deswegen in letzter Zeit so seltsam drauf?"

    # Atropos Gedanken
    "Ist alles etwa meine Schuld?"

    # Symbiont
    "{i}Nein, mache dir darüber jetzt keine Gedanken oder Vorwürfe. Jeder macht mal Fehler, aber du hast eine Chance erhalten diesen Fehler auszubessern. {/i}"

    # Symbiont
    "{i}Nutze diese Chance und mache jetzt alles richtig. {/i}"

    # Symbiont
    "{i}Nimm die Pille und zeige der Welt wie glücklich du bist. Beweise allen, dass auch du vollkommen glücklich sein kannst. {/i}"

    # Atropos Gedanken
    "Ich weiß nicht… das alles ist so… schwierig… Was soll ich nur denken? Was soll ich nur tun?"

    # Atropos Gedanken
    "Vermutlich sollte ich jetzt erstmal ins Labor zurück, damit ich Anan nicht erneut enttäusche… dann sehe ich weiter…"


    scene lab

    "Atropos" "Hey Era."

    show era normal:
        xalign 0.5

    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

    "Era" "…"

    "Atropos" "…"

    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

    "Atropos" "Ja, natürlich… sorry…"

    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

    "Era" "Ich… ahhhh…"

    # Atropos Gedanken
    "Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

    # Atropos Gedanken
    "Ich habe gerade vor allem andere Sorgen."

    "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen müsstest."

    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

    "Atropos" "Was wolltest du?"

    "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

    "Era" "…"

    "Era" "Was ich dich jedenfalls fragen wollte…"

    "Era" "…"

    "Atropos" "Was? Tut mir leid… ich war gerade etwas in Gedanken gewesen."

    "Era" "Ich… ach… egal, vergiss es. Es war nicht so wichtig."

    "Atropos" "Okay."

    "Era" "Aber sag mal Atropos… I-Ist alles in Ordnung? Dich scheint etwas zu beschäftigen…"

    # Narcais taucht auf
    show narcais normal:
        xalign 0.25
    show era normal:
        xalign 0.75

    "Narcais" "Einen glücklichen guten Morgen zusammen. Was habe ich verpasst? Redet ihr über mich?"

    "Era" "G-Guten Morgen… Nein… es ging um Atropos. Ihn scheint etwas zu beschäftigen. Er wirkt nicht glücklich…"

    "Narcais" "Ach, mich beschäftigen auch immer tausend Dinge. Das ist doch nichts ungewöhnliches."

    "Narcais" "Jedenfalls: Ich habe einen Bericht verfasst, den du noch durcharbeiten müsstest, Atropos."

    "Narcais" "Ich bin mir sicher, dass er keine Fehler hat, immerhin habe ich ihn erstellt, aber so ist nun mal die Vorschrift."

    "Atropos" "Ich kümmere mich darum."

    "Era" "Können… können wir dir irgendwie helfen? Was ist vorgefallen?"

    "Atropos" "Ich hatte in letzter Zeit ein paar Mal meine Pille vergessen und war vorhin Anan über den Weg gelaufen."

    "Atropos" "Er hatte es sofort bemerkt und mir einen Vortrag über die Wichtigkeit der Happiness-Pille gehalten und ich muss nachher noch in sein Büro…"

    "Atropos" "Aber ich bin doch auch ohne sie glücklich… warum muss ich sie um jeden Preis einnehmen?"

    "Atropos" "Außerdem… muss Anan wirklich so einen Aufstand darum machen, dass ich sie Mal vergessen habe oder keine Lust hatte sie zu nehmen?"

    "Atropos" "Und eigentlich wollte ich Anan niemals enttäuschen… nicht nach allem, was er für uns getan hat…"

    "Atropos" "Ich weiß einfach nicht, was ich tun soll."

    "Narcais" "Ich kann Anan verstehen. Happiness ist nun mal unglaublich wichtig. Wie kannst du so etwas wichtiges nur vergessen?"

    "Narcais" "Wie kannst du so egoistisch sein? Damit gefährdest du nicht nur dein Glück, sondern unser aller Glück."

    "Era" "Atropos… mache dir bitte keine Vorwürfe, okay?"

    "Era" "Aber ich muss Narcais zustimmen. Happiness ist wichtig… du solltest die Pille nehmen und dich bei Anan dafür entschuldigen."

    "Era" "Und… und… denk bitte an dein eigenes Glück. Ich will, dass du glücklich bist… du… du bedeutest mir…"

    "Era" "…"

    "Era" "Bitte pass gut auf dich auf, Atropos."

    "Atropos" "Danke. Ihr habt ja Recht. Ich werde nachher zu Anan gehen und das Ganze klären."

    "Atropos" "Jetzt sollten wir aber erst einmal mit der Arbeit anfangen."

    "Narcais" "Vergiss meinen Bericht nicht!"

    "Atropos" "(lacht) Keine Sorge, das könnte ich niemals."

    hide era
    hide narcais

    # Atropos Gedanken
    "Zurück an die Arbeit."

    "Atropos" "…"


    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"

    "Durchsage" "{i}Nimm Happiness ein und lebe dein Leben so, wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit. {/i}"

    "Durchsage" "{i}In wenigen Minuten erfolgt eine Übertragung von Anan. Bitte schaltet die entsprechenden Bildschirme ein. {/i}"

    show era normal:
        xalign 0.5

    "Era" "Ich… ich kümmere mich darum!"

    hide era

    if neiro_unterhalten:

        # Atropos Gedanken
        "Das muss die Übertragung sein, die Neiro vorhin erwähnt hatte."

        # Atropos Gedanken
        "Ob er wohl mit allen Informationen Recht hatte?"

    # ab hier wieder alle
    scene triumvirate
    show anan 1:
        xalign 0.5
    show atlas normal:
        xalign 0
    show adres normal:
        xalign 0.99

    "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag gehabt."

    "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

    "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

    "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

    "Anan" "Der Gründungstag von Aither."

    "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

    "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

    "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

    "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

    "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

    "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

    "Anan" "Ich bin bereit alles dafür zu geben und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

    "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

    "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

    "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

    "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

    "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

    "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

    "Anan" "Weil ihr uns dabei helft das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die ersten, die die neue Happiness erhalten. "

    "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

    "Anan" "Vergesst niemals: Happiness. Dein Leben. Deine Entscheidung. Deine Glücklichkeit. "

    "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

    "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns überlassen haben."

    "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

    scene lab
    show era normal:
        xalign 0.25
    show narcais normal:
        xalign 0.75

    "Era" "Wow…"

    "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

    # Atropos Gedanken
    "Und das von jemandem, der sich selbst am liebsten den ganzen Tag zuhört."

    # Atropos Gedanken
    "Aber ich muss ihnen schon Recht geben. Seine Rede war beeindruckend wie immer."

    # Atropos Gedanken
    "Ich frage mich, ob Anan mit seiner Rede wirklich Recht hat? Es wirkt alles so plausibel und klar, wenn er es erzählt…"

    # Atropos Gedanken
    "Und dennoch… ich wüsste zu gerne was die Tablette tatsächlich bewirkt. Wie sie uns überhaupt unser Glück bringt."

    # Atropos Gedanken
    "Vielleicht würde es mir dann leichter fallen sie zu nehmen. Vielleicht würde ich dann weniger zweifeln."

    "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

    "Atropos" "Ja, das ist er wohl. "

    "Atropos" "Jetzt sollten wir aber zurück an die Arbeit, wir müssen heute noch einiges schaffen."

    # Bildschirm wird schwarz und blendet dann wieder auf. Erneut ins Labor.

    "Atropos" "…"

    # Atropos Gedanken
    "Oh, es ist schon spät. Ich müsste langsam los, wenn ich pünktlich in Anans Büro sein will…"

    # Atropos Gedanken
    "Ich sollte besser gehen. Vielleicht hilft es mir ja Mal mit Anan über meine Zweifel und Sorgen zu sprechen."

    # Atropos Gedanken
    "Ich möchte nicht Zweifeln… ich möchte einfach nur glücklich sein…"

    "Atropos" "Bin gleich wieder da."

    "Era" "Bis… bis später."


    jump go_office

label be_against:
    $ straight_office = False

    # Atropos Gedanken
    "Was erlaubt sich Anan bitte? Ich lasse mir doch nicht vorschreiben ob und wie oft ich die Happiness-Pille einnehmen soll!"

    # Atropos Gedanken
    "Ich weiß ja, dass er die Welt vom Krieg erlöst hat, aber das ist ganz allein meine Entscheidung! Ich sollte über mein eigenes Glück bestimmen können."

    # Atropos Gedanken
    "Keiner sollte mir vorgeben dürfen, wie ich zu meinem Glück kommen soll!"

    # Symbiont
    "{i}Nimm die Pille. Merkst du denn nicht, dass du mit jeder Sekunde unglücklicher wirst? {/i}"

    # Symbiont
    "{i}Denk nochmal nach, was du gerade alles gedacht hast. Bist das wirklich du? {/i}"

    # Symbiont
    "{i}Das ist nicht mehr der Atropos, der du sein willst, oder? {/i}"

    # Symbiont
    "{i}Du warst mal glücklich gewesen, aber gerade stößt du dich selbst und die, die du liebst ins Unglück. {/i}"

    # Symbiont
    "{i}Bist du gerade, ohne die Happiness-Pille, wirklich glücklich? {/i}"

    # Atropos Gedanken
    "Ja! Ja, ich bin glücklich!"

    # Symbiont
    "{i}Das nennst du Glück? Du bist gerade wirklich glücklich? Es gibt nichts, dass dir Sorgen oder Kopfzerbrechen bereitet? {/i}"

    "Atropos" "Ich bin glücklich."

    "Atropos" "Ich bin glücklich."

    "Atropos" "Ich bin glücklich!"

    "Atropos" "Und Anan kann mir das nicht nehmen! Er kann mich nicht zwingen. Ich werde nicht zu ihm gehen, das kann er vergessen!"

    # Atropos Gedanken
    "Aber jetzt erstmal zurück ins Labor…"


    scene lab

    show era normal:
        xalign 0.5

    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

    "Era" "…"

    "Atropos" "…"

    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

    "Atropos" "Ja, sorry …"

    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

    "Era" "Ich… ahhhh…"

    # Atropos Gedanken
    "Musste das jetzt sein? Ich mag Era echt gerne, aber ihre Tollpatschigkeit kann wirklich nerven."

    "Atropos" "Mir geht es gut."

    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

    "Atropos" "Era, sorry, aber mir ist gerade nicht nach einem Gespräch. Können wir das auf später verschieben?"

    # erst niedergeschlagen, dann freudestrahlend

    "Era" "Ja, natürlich. Gerne!"

    "Era" "Ich arbeite dann mal weiter."

    # Era verschwindet, Narcais taucht auf
    hide era
    show narcais normal:
        xalign 0.5

    "Narcais" "Atropos, ich habe den Bericht…"

    # fällt ihm ins Wort

    "Atropos" "Jetzt nicht… ich habe zu tun, siehst du das nicht?"

    # irritiert

    "Narcais" "Was? Aber… du wolltest doch den Bericht durchlesen, den ich geschrieben habe."

    "Atropos" "Jetzt nicht!"

    "Narcais" "Klar, kein Problem. Lies ihn dir durch sobald du dazu kommst."

    "Narcais" "Du solltest ohnehin nicht viel damit zu tun haben. Ich weiß, dass ich perfekte Arbeit liefere- das ist eine allgemein bekannte Tatsache."

    # Atropos Gedanken
    "Er ist echt stark von sich eingenommen. Ich kann weder ihn noch Era gerade ertragen…"

    # Atropos Gedanken
    "Kann ich nicht mal eine Sekunde für mich haben, damit ich in Ruhe nachdenken kann?"

    # Atropos Gedanken
    "Natürlich kann ich so nicht vollkommen glücklich sein…"

    "Atropos" "Ich kümmere mich darum."

    # Narcais verschwindet.
    hide narcais

    # Atropos Gedanken
    "Endlich ein wenig Ruhe."

    # Atropos Gedanken
    "Ich werde mich nachher mit allem beschäftigen. Jetzt sollte ich erst einmal mit der Arbeit anfangen."

    "Atropos" "…"

    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"

    "Durchsage" "{i}Nimm Happiness ein und lebe dein Leben so wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit. {/i}"

    "Durchsage" "{i}In wenigen Minuten erfolgt eine Übertragung von Anan. Bitte schaltet die entsprechenden Bildschirme ein. {/i}"

    show era normal:
        xalign 0.5

    "Era" "Ich… ich kümmere mich darum!"
    hide era

    scene triumvirate

    show anan 1:
        xalign 0.5
    show atlas normal:
        xalign 0
    show adres normal:
        xalign 0.99

    # Bild wechselt von Laborhintergrund in Nahansicht des Bildschirms. Atlas, Anan und Adrés tauchen nebeneinander auf

    "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag gehabt."

    "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

    "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

    "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

    "Anan" "Der Gründungstag von Aither."

    "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

    "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

    "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

    "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

    "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

    "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

    "Anan" "Ich bin bereit alles dafür zu geben und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

    "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

    "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

    "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

    "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

    "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

    "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

    "Anan" "Weil ihr uns dabei helft das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die ersten, die die neue Happiness erhalten. "

    "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

    "Anan" "Vergesst niemals: Happiness. Dein Leben. Deine Entscheidung. Deine Glücklichkeit. "

    "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

    "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns überlassen haben."

    "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

    scene lab
    show era normal:
        xalign 0.25
    show narcais normal:
        xalign 0.75

    # Übertragung wird beendet und der Labor ist wieder im Hintergrund.

    "Era" "Wow…"

    "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

    # Atropos Gedanken
    "Schöne Worte und nichts dahinter…"

    # Atropos Gedanken
    "Wieso mussten wir uns diesen Unsinn anhören?"

    # Atropos Gedanken
    "Warum überlässt Anan nicht uns die Wahl, ob wir die Pille nehmen wollen oder nicht?"

    # Atropos Gedanken
    "Vielleicht würde es mir dann leichter fallen sie zu nehmen. Vielleicht würde ich dann weniger zweifeln."

    # Symbiont
    "{i} Diese Gedanken hast du nur, weil du nicht glücklich bist. Nimm die Pille und werde wieder glücklich. {/i}"

    # Symbiont
    "{i} Merkst du nicht wie deine Zweifel dich innerlich zerfressen? {/i}"

    # Symbiont
    "{i}Ist es das, was du willst? Du bist unglücklich, Atropos. Kein Mensch sollte unglücklich sein. {/i}"

    "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

    "Atropos" "Wir sollten zurück an die Arbeit, wir müssen heute noch einiges schaffen."

    "Atropos" "…"

    # Atropos Gedanken
    "Es ist schon spät. Ich müsste jetzt los, um pünktlich bei Anan zu sein."

    # Atropos Gedanken
    "Aber will ich das überhaupt?"

    # Symbiont
    "{i}Du willst pünktlich sein. Anan war noch nett und verständnisvoll gewesen, aber das wird sich ändern, wenn du weiterhin dein Glück und das Glück aller gefährdest. {/i}"

    # Symbiont
    "{i}Wieso wehrst du dich so verzweifelt gegen dein Glück? Niemand will dir Leid zufügen. Alle wollen nur dein Bestes. {/i}"

    # Symbiont
    "{i}Besänftige deinen Zorn. Anan sorgt sich um dich. Geh zu ihm und entschuldige dein Verhalten. {/i}"

    # Symbiont
    "{i}Alles kann gut werden, wenn du es nur willst. {/i}"

    jump go_office

label go_office:

    if straight_office:
        jump office

    else:

        menu:
            "Ich sollte besser zu Anans Büro gehen.":
                # Atropos Gedanken
                "Vermutlich ist es besser, wenn ich zu Anan gehe. Ich will keinen Ärger bekommen. Nicht auch noch dafür."

                # Atropos Gedanken
                "Vielleicht kann er mir ja auch ein paar Antworten geben… warum es so wichtig ist die Pille zu nehmen. Was passiert, wenn ich sie ein paar Tage nicht nehme…"

                # Atropos Gedanken
                "Ich denke ich habe vorhin vielleicht etwas überreagiert… Ich sollte mir davon nicht die Laune verderben lassen."

                # Atropos Gedanken
                "Immerhin treffe ich nachher noch Kloth und Chesis zum Grillen. Für den Moment sollte ich mich darauf fokussieren."

                # Atropos Gedanken
                "Und jetzt sollte ich wirklich los. Sonst komme ich noch zu spät. Ich sollte Anan nicht warten lassen."

                "Atropos" "Bin gleich wieder da."

                "Era" "Bis… bis später."

                jump office
            "Ich werde auf keinen Fall zu Anans Büro gehen.":
                jump no_office

label good_mood:
    # Atropos Gedanken

    hide era
    hide narcais
    "Zurück an die Arbeit."

    "Atropos" "…"


    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"

    "Durchsage" "{i}Nimm Happiness ein und lebe dein Leben so wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit. {/i}"


    "Durchsage" "{i}In wenigen Minuten erfolgt eine Übertragung von Anan. Bitte schaltet die entsprechenden Bildschirme ein. {/i}"

    show era normal:
        xalign 0.5

    "Era" "Ich… ich kümmere mich darum!"

    hide era

    if neiro_unterhalten:

        # Atropos Gedanken
        "Das muss die Übertragung sein, die Neiro vorhin erwähnt hatte."

        # Atropos Gedanken
        "Ob er wohl mit allen Informationen Recht hatte?"


    scene triumvirate
    show anan 1:
        xalign 0.5
    show adres normal:
        xalign 0.99
    show atlas normal:
        xalign 0

    "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag gehabt."

    "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

    "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

    "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

    "Anan" "Der Gründungstag von Aither."

    "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

    "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

    "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

    "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

    "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

    "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

    "Anan" "Ich bin bereit alles dafür zu geben und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

    "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

    "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

    "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

    "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

    "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

    "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

    "Anan" "Weil ihr uns dabei helft das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die ersten, die die neue Happiness erhalten. "

    "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

    "Anan" "Vergesst niemals: Happiness. Dein Leben. Deine Entscheidung. Deine Glücklichkeit. "

    "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

    "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns überlassen haben."

    "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

    scene lab

    show era normal:
        xalign 0.25
    show narcais normal:
        xalign 0.75

    "Era" "Wow…"

    "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

    # Atropos Gedanken
    "Und das von jemandem, der sich selbst am liebsten den ganzen Tag zuhört."

    "Atropos" "Dieser Mann ist wirklich unglaublich… Man spürt mit jeder Faser seines Körpers, wie wichtig ihm das Wohl aller Menschen ist."

    "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

    "Atropos" "Ich frage mich, welchen Preis er wohl dafür bezahlen muss?"

    "Narcais" "Egal wie hoch er auch sein mag. Ich bin mir sicher, dass Anan nicht eine Sekunde zögert, diesen zu bezahlen."

    "Atropos" "Jetzt sollten wir aber zurück an die Arbeit, wir müssen heute noch einiges schaffen."


    jump pill

label no_office:

    # Atropos Gedanken
    "Nein! Auf keinen Fall, ich werde nicht nachgeben, nur weil Anan eine gute Rede gehalten hat."

    # Atropos Gedanken
    "Mir ist es egal was die Konsequenzen sind, ich werde mich nicht weiter dazu zwingen lassen Happiness zu nehmen."

    # Atropos Gedanken
    "Es ist meine freie Entscheidung wie ich zu meinem eigenen Glück gelangen will. Keiner kann mich zwingen dieses Glück über Happiness zu erreichen."

    # Symbiont
    "{i}Letztlich wirst du das Glück nur über Happiness erreichen können. {/i}"

    # Atropos Gedanken
    "Ich nehme die Pille wann und wenn ich will!"

    # Symbiont
    "{i}Du solltest sie jetzt und hier nehmen. {/i}"

    # Atropos Gedanken
    "Und jetzt zurück an die Arbeit. Zumindest der Bericht für Anan sollte heute fertig werden."

    "Atropos" "…"

    "Durchsage" "{i}Atropos Laitos. Dein Glück erwartet dich. Finde dich umgehend im Büro von Anan ein. {/i}"

    # Atropos Gedanken
    "Ich werde die Durchsage einfach überhören."

    "Narcais" "Atropos, deine Anwesenheit wird verlangt. Wieso reagierst du nicht? Du solltest dich geehrt fühlen in Anans Beruf gerufen zu werden!"

    "Era" "Was will er von dir, Atropos?"

    "Durchsage" "{i}Atropos Laitos. Dein Glück erwartet dich. Finde dich umgehend im Büro von Anan ein. Er erwartet dich.{/i}"

    # Atropos Gedanken
    "Sieht so aus als würde mir keine andere Wahl bleiben… Ich möchte auch nicht unter meinen Kollegen deswegen seltsam auffallen."

    # Atropos Gedanken
    "Ich hoffe die anderen denken jetzt nicht schlecht von mir… und muss Anan das gleich über die Lautsprecher durchsagen lassen?"

    # Atropos Gedanken
    "Das muss echt nicht jeder mitbekommen…"

    # Atropos Gedanken
    "Aber ich kann mir ja mal anhören, was er zu sagen hat und dann weitersehen…"

    "Narcais" "Atropos?"

    "Atropos" "Schon gut, schon gut."

    "Atropos" "Ich geh ja schon."

    jump rueffel

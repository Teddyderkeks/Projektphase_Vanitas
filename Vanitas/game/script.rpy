default pill_taken = False
default straight_office = False
default neiro_unterhalten= False
default badmood= False
default okaymood=False
define startfade=Fade(1,0.5,3)
define fadestart=Fade(1,0.5,3)
define startfade2=Fade(1,0.5,0.5)
default datewithera= False
default dialgoueoffice= False
default talkchesismorning= False
default loudspeaker = False
define symb= Character(None,window_background="gui/textbox_withoutname.png")

#xalign=0.5, yalign=1.0
$ symb= Character (None, window_xalign=0.5, window_yalign=1.0, who_posy=500)

label start:
    stop music
    $ renpy.movie_cutscene("Sound/cutscene_intro/cutscene_intro.mpg")
    play music "Sound/cutscene_intro/cutscene_intro_loopsound.mp3" fadeout 1

    window hide

    scene atropos_falling

    # Symbiont
    symb "{i}Du bist so gut wie tot. Nicht mal mehr Sekunden dauert es bis du auf dem Boden aufkommst. {/i}"

    # Symbiont
    symb"{i}Du wirst sterben und es scheint keinen Ausweg aus der Lage zu geben. {/i}"

    # Symbiont
    symb"{i}Warst du glücklich, Atropos? {/i}"

    # Symbiont
    symb"{i}Bist du zufrieden mit den Entscheidungen, die du getroffen hast? {/i}"

    # Symbiont
    symb"{i}Dein Glück ist letztlich das Einzige, das zählt. {/i}"

    # Symbiont
    symb"{i}Lebe wohl. {/i}"

    jump change


label change:
    scene 5hours
    with startfade
    scene street
    with startfade2
    play music "Sound/Music/Rooms/verkaufsraum.mp3" fadeout 3 fadein 3

    # Symbiont
    symb"{i}Heute ist ein guter Tag. Ein glücklicher Tag. Ein Tag voller Zufriedenheit und Erfüllung. {/i}"

    # Symbiont
    symb"{i} Atropos, du solltest den Tag nutzen, um dich und alle anderen Menschen glücklich zu machen. {/i}"

    # Atropos Gedanken
    symb"Ich freue mich schon auf heute. Nach der Arbeit grillen Kloth, Chesis und ich endlich. Ich kann es schon seit Wochen kaum noch erwarten!"

    scene detail_phone_unlockstreet
    with fadeshort

    # Atropos Gedanken
    symb"Oh, ich habe einige verpasste Nachrichten. Mal sehen, ob mir Kloth endlich geantwortet hat."

    scene detail_phone_chats
    with fadeshort

    # Atropos Gedanken
    symb"Immer noch nicht? Er hat sie ja noch nicht mal gelesen... dabei ist er doch sonst so gewissenhaft und antwortet innerhalb von Minuten."

    # Atropos Gedanken
    symb"Man trifft ihn eigentlich nie ohne sein Handy an. Das ist seltsam... es klingt nicht nach ihm. Ob etwas vorgefallen ist?"


    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"


    "Durchsage" "{i} Nimm Happiness ein und lebe dein Leben so, wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit.{/i}"

    scene detail_pillbox
    with fadeshort

    # Atropos Gedanken
    symb"Happiness…"

    # Atropos Gedanken
    symb"Ich habe es schon wieder vergessen."

    # Atropos Gedanken
    symb"Ob es wohl Konsequenzen hat, dass ich sie nicht täglich genommen habe?"

    # Atropos Gedanken
    symb"Immerhin ist es das, was sie uns stets einprägen: Vergiss niemals - auch nicht einmal - deine Pille zu nehmen."

    "Atropos" "…"

    # Atropos Gedanken
    symb"Aber war ich in den letzten Tagen deswegen wirklich weniger glücklich?"

    # Symbiont
    symb"{i}Nimm die Pille, Atropos. Du brauchst sie, um glücklich zu sein. {/i}"

    # Atropos Gedanken
    symb"Ich habe aber nicht den Eindruck, dass sich viel verändert hat…"

    # Atropos Gedanken
    symb"Oder?"

    # Atropos Gedanken
    symb"Was soll ich jetzt machen? Soll ich sie nehmen?"
    show screen force_mouse_move_threeoptions

    menu:
        "Ich sollte die Pille besser jetzt sofort nehmen.":
            $ pilltakenyes = True
            hide screen force_mouse_move_threeoptions
            jump take_pill
        "Ich nehme die Pille nicht- ich brauche sie nicht!":
            $ pilltakenno = True
            hide screen force_mouse_move_threeoptions
            jump not_take_pill
        "Ich nehme die Pille, sobald ich sie brauche.":
            $ pilltakenlater = True
            hide screen force_mouse_move_threeoptions
            jump later_take_pill



label take_pill:
    $ pill_taken = True

    # Atropos Gedanken
    symb"Ich sollte die Pille besser jetzt sofort nehmen."

    play sound "Sound/Sounds/pille.mp3" fadeout 1

    scene detail_pill
    with fadeshort

    # Atropos Gedanken
    symb"So… schnell runter damit, ehe ich es schon wieder vergesse."

    scene street
    with fadeshort

    # Atropos Gedanken
    symb"Es war ein großer Fehler gewesen in letzter Zeit nicht auf die regelmäßige Einnahme zu achten."

    # Atropos Gedanken
    symb"Ich möchte glücklich sein. Ich möchte genauso glücklich sein wie alle anderen."

    # Atropos Gedanken
    symb"Ohne die Pille habe ich mich irgendwie so… leer gefühlt."

    # Atropos Gedanken
    symb"Aber ich beginne mich langsam wieder besser zu fühlen. Ich fühle mich gut. Zufrieden."

    # Atropos Gedanken
    symb"Die Happiness-Pille ist das, was ich brauche, um glücklich zu sein. Um ein glückliches Leben zu führen."

    # Atropos Gedanken
    #symb"Sie ist wichtig und zukünftig werde ich sie nicht mehr vergessen! Dann kann ich endlich wieder das Leben führen, das ich führen will."

    # Atropos Gedanken
    symb"Ein gutes Leben."

    # Atropos Gedanken
    #symb"Ein glückliches Leben."

    # Symbiont
    symb"{i}Gut gemacht, Atropos. Das ist es was wichtig ist: Ein glückliches Leben und genau dieses Leben führst du nun wieder. {/i}"

    # Symbiont
    symb"{i}Vergiss niemals, glücklich zu sein und immer deinem Glück zu folgen. {/i}"

    # Symbiont
    symb"{i}In jeder einzelnen Entscheidung. {/i}"

    # Atropos Gedanken
    symb"Ja, ich werde es nicht vergessen."


    jump shop

label not_take_pill:
    # Atropos Gedanken
    symb"Ich nehme die Pille nicht- ich brauche sie nicht!"

    # Atropos Gedanken
    symb"Nicht mehr zumindest."

    # Atropos Gedanken
    symb"Warum auch? Ich bin auch ohne sie glücklich. Sie ist komplett überflüssig."

    # Atropos Gedanken
    symb"Obwohl ich sie die letzten Tage so unregelmäßig genommen habe, habe ich keinen Unterschied zu sonst bemerkt."

    # Atropos Gedanken
    symb"Ich war glücklich und ich bin glücklich. Dafür brauche ich die Pille nicht. Sie scheint fast nur ein Placebo zu sein."

    # Atropos Gedanken
    symb"Die Hauptsache ist doch, dass ich glücklich bin und nicht, wie ich dieses Glück erreiche."

    # Atropos Gedanken
    symb"Ich werde die Tablette einfach weiterhin nicht nehmen. Das wird schon keinem auffallen. Und wenn doch, fange ich einfach an, sie wieder zu nehmen."

    # Atropos Gedanken
    symb"Schaden wird sie mir auf keinen Fall."

    scene street
    with fadeshort


    jump shop

label later_take_pill:
    # Atropos Gedanken
    symb"Ich nehme die Pille, sobald ich sie brauche. Das sollte ausreichen."

    # Atropos Gedanken
    symb"Ich weiß ja, dass die Tablette wichtig ist. Nur durch sie kann ich wirklich glücklich sein…"

    # Atropos Gedanken
    symb"Dennoch… Ich habe die letzten Tage keinen großen Unterschied bemerkt, obwohl ich sie unregelmäßig eingenommen hatte."

    # Atropos Gedanken
    symb"Es wird schon keine Auswirkungen haben, dass ich sie die paar Mal vergessen habe."

    # Atropos Gedanken
    symb"Sicherheitshalber werde ich sie irgendwann heute trotzdem wieder einnehmen. Ich möchte mein Glück nicht riskieren."

    # Atropos Gedanken
    symb"Bei allen anderen wirkt sie immerhin auch. Alle Menschen sind glücklich seit Anan und die anderen sie uns zum Geschenk gemacht haben."

    # Atropos Gedanken
    symb"Das ist kein Vergleich zu dem, wie kaputt und zerstört die Welt zuvor war."

    # Atropos Gedanken
    symb"Ich sollte dankbarer für diese Chance sein und mein Glück nicht riskieren."

    scene street
    with fadeshort


    jump shop

label shop:

    # Atropos Gedanken
    symb"Da ist ja schon Aither."


    scene shop_1
    with fadeshort

    play sound "Sound/Sounds/gloeckchen.mp3"

    show zelos normal

    "Zelos" "Guten Morgen und einen wunderschönen Tag, was…? Ach, du bist es Atropos- heute extra überpünktlich?"

    "Atropos" "Hey, Zelos. Ja, ich bin heute etwas zu früh aufgewacht und dachte mir, dass ich den Tag besser nutze, als noch weiter liegen zu bleiben."

    show zelos happy

    "Zelos" "Eifrig und strebsam, das lobe ich mir. Aber man kann auch gar nicht anders als seine Arbeit hier zu lieben, natürlich ist man da gerne bereit mehr Zeit zu investieren."

    "Atropos" "Spaß macht die Arbeit hier auf jeden Fall und wir dienen der Menschheit. Das kann wohl nicht jeder von sich behaupten. (lacht)"

    "Zelos" "Ach ja, hast du meine Nachrichten bekommen? Meine Schwester erstellt eine Dokumentation über den Krieg und wie Happiness uns gerettet hat, und sucht noch alte Artikel dafür."

    "Atropos" "Bekommen ja, aber noch nicht gelesen. Über den Krieg sagst du?"

    "Zelos" "Ja, genau. Sie hofft mehr Insiderwissen zu bekommen, weil wir doch alle für Aither unter Anan arbeiten."

    "Zelos" "Er, Adrés und Atlas haben wirklich die Welt gerettet, indem sie Happiness erschufen."

    "Zelos" "Nicht auszudenken, wie lange der Krieg sonst noch angedauert hätte und wie viele Menschen ihm zum Opfer gefallen wären."

    "Atropos" "Ich weiß nur ein paar Sachen aus den Erzählungen meines Vaters, aber der 50-jährige Krieg muss wirklich schrecklich gewesen sein. Das fehlende Wasser und die unzureichende Nahrung..."

    "Zelos" "Und dann tauchten die Großen Drei als unsere Erlöser auf. Ihr Triumvirat hat uns alle gerettet!"

    "Atropos" "Ich schaue heute Abend Mal nach und gebe dir Bescheid, falls ich noch weiteres Material dazu finde."

    "Zelos" "Super, danke! Du kannst ja auch Chesis und Kloth Mal Bescheid geben- als Anans Chefsekretär hat Kloth bestimmt teiferreichende Informationen."

    "Atropos" "Ich bezweifle sehr, dass er die rausgeben darf. (lacht)"

    "Zelos" "Einen Versuch ist es doch wert, nicht wahr? Als dein bester Freund ist er bestimmt dazu bereit. (Lacht)"

    "Atropos" "Ich sehe, was ich machen kann."

    "Zelos" "Danke!"

    show zelos normal

    "Zelos" "Ich hoffe es stört dich nicht, wenn ich nebenbei weiterarbeite? Die neuste Lieferung der Happiness-Pille kam eben an und ich muss sie noch in die Regale einsortieren."

    "Atropos" "Alles gut, lass dich von mir nicht stören."

    menu:
        "Ich wollte ohnehin mal bei meinen Freunden im Büro vorbeischauen.":
            $ beginnoffice = True
            jump conversation_with_seller
        "Ich wollte ohnehin zur Arbeit los.":
            $ beginnlab = True
            jump work

label conversation_with_seller:

    show zelos normal
    "Atropos" "Ich wollte ohnehin mal bei Tycho und den anderen im Büro vorbeischauen. Wir sehen uns später."

    show zelos happy

    "Zelos" "Richte den Anderen schöne Grüße von mir aus!"

    "Atropos" "Klar, mache ich."

    "Zelos" "Wir machen heute um 12:15 Uhr Mittagspause. Du kommst doch mit uns in die Mensa, oder?"

    "Atropos" "Ich weiß noch nicht, ob ich es zeitlich schaffe. Es türmt sich heute ein Berg an Arbeit, aber ich versuche es auf alle Fälle."

    show zelos normal

    "Zelos" "(murmelt) Happiness- Glück für alle. Oh, tut mir leid, was hast du gesagt?"

    "Atropos" "(lacht) Nichts… alles gut, lass dich von mir nicht länger aufhalten. Wir sehen uns."

    show zelos happy

    "Zelos" "Bis dann und einen wunderschön glücklichen Tag in der besten Firma der Welt!"



    if pill_taken:

        scene hall
        with fadeshort

        # Atropos Gedanken
        symb"Da vorne liegt das Büro- ich frage mich, ob die anderen wohl schon da sind? Ich bin heute ziemlich früh dran."

        play music "Sound/Music/Rooms/buero_normal.mp3" fadeout 3 fadein 3
        scene office_1
        with fadeshort

        # Atropos Gedanken
        symb"Hmm, es scheint noch keiner hier zu sein."

        # Atropos Gedanken
        symb"Dann bin ich wohl wirklich zu früh dran."

        #Atropos Gedanken
        symb"Der eine Computer ist an. Ob wohl doch schon jemand hier ist? Wem gehört der Computer?"

        #Atropos Gedanken
        symb"Ich könnte mich noch ein wenig umsehen."

        show screen computer

        menu:
            "Ich schaue mir den Kalender an.":
                hide screen computer
                "Ich schaue mir den Kalender an."
                jump watchofficecalendar

            "Da ist ein interessantes Foto.":
                hide screen computer
                "Da ist ein interessantes Foto."
                jump watchofficephoto

            "Neben der Sanduhr liegt etwas.":
                hide screen computer
                "Neben der Sanduhr liegt etwas."
                jump watchofficehourglass

            "Oder nein, besser nicht. Ich sollte nicht in fremden Sachen herumstöbern.":
                hide screen computer
                "Oder nein, besser nicht. Ich sollte nicht in fremden Sachen herumstöbern."
                jump watchnothingoffice

        label computermoira:
            hide screen computer
            # Wenn Spieler direkt auf den PC im Raum klickt
            scene detail_pc_moira
            # Atropos Gedanken
            symb"Seltsam. Da hat wohl jemand etwas nachlesen wollen und vergessen den Bildschirm zu sperren."
            call screen arrowcomputer
            label afteromputermoira:
                scene office_1
                # Atropos Gedanken
                symb"Hm? Der Bildschirm ist einfach ausgegangen."
                # Atropos Gedanken
                symb"Wieso sollte jemand über die Moiren forschen?"
                jump watchnothingoffice


        label watchofficecalendar:
            scene detail_calendar
            with fadeshort
            # Atropos Gedanken
            symb"September 2256."
            # Atropos Gedanken
            symb"Der Todestag meiner Mutter jährt sich bald wieder. Ich war noch so klein… Ich kann mich gar nicht mehr an sie erinnern."
            # Atropos Gedanken
            symb"Vielleicht kommt Mora dann mal wieder zu Besuch, um gemeinsam zu feiern."
            call screen arrow_watchoffice()


        label watchofficephoto:
            scene detail_photo_neiro
            with fadeshort
            # Atropos Gedanken
            symb"Oh, Neiro! Das daneben muss dann wohl sein Bruder sein. Die beiden scheinen allen Anschein nach gut miteinander auszukommen."
            # Atropos Gedanken
            symb"Was sein Bruder wohl jetzt so macht?"
            call screen arrow_watchoffice()

        label watchofficehourglass:
            scene detail_hourglass
            with fadeshort
            # Atropos Gedanken
            symb"Was steht da?"
            show detail_hourglass_overlay
            call screen arrow_watchoffice()

        label watchnothingoffice:

            scene office_1
            with fadeshort
            $ dialgoueoffice=True

            # Atropos Gedanken
            symb"Ich höre Stimmen, könnten sie das sein?"

            # Atropos Gedanken
            symb"Tatsächlich, sie sind es, und sie scheinen sich eh noch zu unterhalten, bevor sie den Tag starten. Ich sollte mich zu ihnen gesellen."
            scene office_2
            with fadeshort

            "Atropos" "Hey Leute."

            show ireia normal:
                xalign 0.35

            "Ireia" "Atropos, wie schön dich hier mal wieder anzutreffen! Du hast dich schon seit einer Weile nicht mehr im Büro blicken lassen. Vermisst hast du uns wohl nicht sonderlich!"

            "Atropos" "Nun, ist ja auch nicht so ganz mein Arbeitsplatz. (lacht) Und keine Sorge, ich habe euch alle vermisst."

            show ireia normal_gray
            show tycho really_happy:
                xalign 0.85

            "Tycho" "Das will ich dir aber auch geraten haben. (lacht) Uns kann man doch gar nicht {b}nicht{/b} mögen, nicht wahr? Und dementsprechend musst du uns auch vermisst haben."

            show tycho really_happy_gray
            show armene normal behind neiro:
                xalign 0.0

            "Armene" "Ja. Ja, das stimmt! Hallo Atropos."

            "Atropos" "Hi Armene, wie geht es dir?"

            show armene happy

            "Armene" "Ich bin glücklich wie immer!"

            show armene happy_gray
            show ireia happy

            "Ireia" "Jetzt überfall die Arme doch nicht, du kennst sie doch."

            show ireia strict

            "Ireia" "Und Armene, du solltest weiter deine Präsentation über das firmeninterne Kommunikationssystem vorbereiten- ich erwarte bessere Arbeit von dir als letztes Mal."

            show ireia strict_gray
            show armene normal

            "Armene" "Natürlich Ireia, tut mir leid!"

            hide armene
            show tycho normal

            "Tycho" "Neiro, gesell dich doch zu uns, was sitzt du so einsam und verlassen an deinem Platz? Deine Arbeitszeit hat doch noch nicht angefangen."

            show tycho normal_gray
            show neiro nervous_laugh:
                xalign 0.6

            "Neiro" "Oh… ich habe euch gar nicht bemerkt, tut mir leid. Atropos? Was machst du hier? Arbeitest du nicht in einer anderen Abteilung? Verkauf oder so?"

            "Atropos" "Neiro, wie er leibt und lebt. (lacht)"

            show neiro nervous_laugh_gray
            show ireia strict

            "Ireia" "Du solltest definitiv an deinem Gedächtnis arbeiten, Neiro. Es wird in letzter Zeit immer kritischer. Ich möchte von dir keine schlechteren Ergebnisse deswegen sehen."

            show ireia strict_gray
            show neiro happy

            "Neiro" "Natürlich Ireia, ich gebe weiterhin mein Bestes, du musst dir keine Sorgen machen."

            # Atropos Gedanken
            symb"Neiro hatte schon immer eine seltsame Art mit Kritik umzugehen. Aber immerhin verträgt er dadurch Ireias direkte Art gut."

            show neiro happy_gray
            show tycho normal

            "Tycho" "Habt ihr es eigentlich schon gehört? Anan will anlässlich des diesjährigen 37. Gründungstages wieder eine riesige Feier veranstalten!"

            show tycho normal_gray
            show ireia happy

            "Ireia" "Dann sollten wir noch härter arbeiten, damit wir auch einen Anlass zu feiern haben. Das Glück der Menschen entsteht nicht von selbst."

            show ireia happy_gray
            show tycho happy

            "Tycho" "Natürlich arbeiten wir hart! Aber das tut man für Aither doch auch gerne."

            show tycho normal

            "Tycho" "Zurück zum Thema… diese Party wird gigantisch. Erinnert ihr euch noch an die anlässlich des 30. Gründungstages?"

            "Atropos" "Damals hatte ich noch nicht hier gearbeitet. So alt bin ich nun auch nicht. (lacht)"

            "Tycho" "Ach stimmt, du bist ja ein paar Jahre jünger als ich, oder? 24?"

            "Atropos" "Fast… 25. (grinst)"

            "Tycho" "Jedenfalls… wo war ich stehen geblieben?"

            "Tycho" "Ach ja, der 30. Gründungstag… eine bessere Feier habe ich noch nie erlebt! Und ich war schon auf vielen Feiern gewesen, das könnt ihr mir glauben."

            "Tycho" "Damals hatte ich gerade erst hier angefangen. Ich war nur ein einfacher Praktikant gewesen, aber dennoch gab Anan mir eine Einladung."

            show tycho really_happy

            "Tycho" "Ich konnte mein Glück kaum fassen. Es war berauschend! All das Essen im Überfluss und dann die Musik, der Tanz…"

            show tycho really_happy_gray
            show ireia strict

            "Ireia" "Tycho, fass dich kürzer. Wir haben noch Arbeit zu erledigen. Und jetzt erzähl schon, was hast du vom diesjährigen Gründungstag gehört?"

            "Atropos" "Ja… du kannst doch nicht die Information anteasern und dann damit hinter dem Berg halten."

            show ireia strict_gray
            show tycho happy
            show armene normal_gray:
                xalign 0.0

            "Tycho" "Sorry, sorry… also, ich weiß nicht viel, aber angeblich sollen Atlas und Adrés höchstpersönlich vorbeikommen, um gemeinsam mit Anan diesen Tag zu feiern."

            "Atropos" "Habe ich dich gerade richtig verstanden? Die Großen Drei, alle hier in Astoa?"

            show tycho happy_gray
            show ireia happy

            "Ireia" "Das sind ja unglaubliche Neuigkeiten. Wieso hast du uns nicht schon früher davon erzählt?"

            show ireia happy_gray
            show tycho normal

            "Tycho" "Weil ich davor selbst nur ganz vage Gerüchte gehört habe, aber mittlerweile verstärkt sich der Eindruck immer mehr, dass an den Gerüchten etwas Wahres dran sein könnte."

            "Atropos" "Ich frage mich, wie die beiden wohl sind. Natürlich kennt man ihre Namen… immerhin sind Anan, Atlas und Adrés die Gründer von Aither und diejenigen, die den Krieg beendet haben…"

            "Atropos" "Dennoch kenne ich Atlas und Adrés nur von Fotos und nicht von Videoaufzeichnungen oder anderen Quellen. Es wird ein ziemliches Geheimnis um ihre Existenz gemacht."

            show tycho normal_gray
            show ireia normal

            "Ireia" "Das ist aber auch gut so. Die drei sind immerhin dafür verantwortlich, dass alle Menschen glücklich sind."

            "Ireia" "Da haben sie Wichtigeres zu tun, als sich darum zu kümmern, dass wir Informationen über sie bekommen."

            show ireia normal_gray
            show armene shy

            "Armene" "Ich frage mich, ob Atlas und Adrés wohl auch so unglaublich charmant und gutaussehend sind wie Anan… (seufzt verträumt)"

            show armene shy_gray
            show ireia strict

            "Ireia" "Armene? Wie lange stehst du schon hier? Bist du fertig mit deiner Präsentation?"

            show ireia strict_gray
            show armene shy

            "Armene" "Nein… ich wollte mich nur am Gespräch beteiligen…"

            show armene shy_gray
            show neiro normal

            "Neiro" "Um was geht es? Tut mir leid, ich war mit den Gedanken kurz abgeschweift…"

            "Neiro" "Mein Bruder ist gestern gestorben und wir müssen noch die Feier ihm zu Ehren vorbereiten…"

            show neiro normal_gray
            show tycho happy

            "Tycho" "(lacht) Und wieder das übliche Chaos. Es macht echt zu viel Spaß mit euch Zeit zu verbringen!"

            show tycho happy_gray
            show ireia strict

            "Ireia" "Armene, los an die Arbeit!"

            show ireia strict_gray
            show armene normal

            "Armene" "Ja natürlich Ireia, mache ich!"

            hide armene

            # Atropos Gedanken
            symb"Was mich gerade interessieren würde…"

            menu:
                "Ich hätte gerne mehr Informationen über die Gründungsfeier.":
                    jump entscheidung4_1
                "Ich würde mich gerne noch etwas mehr über die großen Drei unterhalten.":
                    jump entscheidung4_2
                "Ich will mich bei Neiro nach seinem verstorbenen Bruder erkundigen.":
                    jump entscheidung4_3
                "Oh, es ist schon spät. Ich sollte ins Labor.":
                    symb "Oh, es ist schon spät. Ich sollte ins Labor."
                    jump nachentscheidung4

            label entscheidung4_1:
                $ neiro_unterhalten = True

                "Atropos" "Tycho, hast du noch mehr Informationen über die diesjährige Gründungsfeier?"

                show tycho normal

                "Tycho" "Hmm, gute Frage- lass mich einen Moment überlegen…"

                show tycho normal_gray
                show neiro normal

                "Neiro" "Ihr sprecht über die Gründungsfeier?"

                show neiro normal_gray
                show ireia normal

                "Ireia" "Ja, darum ging es schon die ganzen letzten Minuten."

                show ireia normal_gray
                show neiro happy

                "Neiro" "Oh. Jedenfalls, ich weiß ein bisschen was…"

                show neiro happy_gray
                show tycho happy

                "Tycho" "Worauf wartest du noch? Erzähl schon!"

                show tycho happy_gray
                show neiro normal

                "Neiro" "Atlas und Adrés werden hierher nach Astoa kommen, um der Gründungsfeier beizuwohnen!"

                "Atropos" "Neiro, das wissen wir bereits. (lacht) Immerhin haben wir dadurch noch einmal die Bestätigung."

                show neiro normal_gray
                show irea confused

                "Ireia" "Weißt du sonst noch etwas? Irgendwelche Neuigkeiten?"

                show ireia confused_gray
                show neiro nervous_laugh

                "Neiro" "Es hieß, dass heute im Laufe des Tages noch eine offizielle Ankündigung des Ganzen erfolgen soll."

                "Atropos" "Eine offizielle Ankündigung? Also einfach eine Durchsage von Anan?"

                show neiro normal

                "Neiro" "Nein, soweit ich das weiß, werden alle drei live geschaltet."

                show neiro normal_gray
                show ireia happy

                "Ireia" "Das gab es ja noch nie. Normalerweise kommunizieren wir nicht mit dem Rest der Welt… warum sollten wir auch?"

                show ireia happy_gray
                show tycho really_happy

                "Tycho" "Das sind wirklich unglaubliche Neuigkeiten! Ich freue mich schon darauf. Die diesjährige Gründungsfeier wird unbeschreiblich und unvergesslich werden!"

                show tycho really_happy_gray
                show neiro happy

                "Neiro" "Und es gibt noch etwas: Angeblich soll mit der Gründungsfeier eine neue Happiness-Pille vorgestellt werden."

                show neiro happy_gray
                show ireia confused

                "Ireia" "Eine neue Pille? Sag nicht, dass es eine Pille sein wird, die uns noch glücklicher macht?"

                show ireia confused_gray
                show tycho normal

                "Tycho" "Ich wüsste nicht, was es sonst sein könnte… der Tag wird ja immer besser!"

                show tycho normal_gray
                show ireia confused

                "Ireia" "Atropos, müsstest du darüber nicht eigentlich mehr wissen?"

                jump nachentscheidung4

            label entscheidung4_2:

                "Atropos" "Ich bin wirklich gespannt auf Atlas und Adrés."

                show ireia happy

                "Ireia" "Sie wollen das Beste für die Welt, genauso wie Anan. Ist das nicht das Einzige, das zählt?"

                show ireia happy_gray
                show tycho happy

                "Tycho" "Ihnen ist unser Wohl am aller wichtigsten. Stellt euch nur vor, wie die Welt ohne sie wäre. Ich wage es gar nicht mir das vorzustellen!"

                show tycho happy_gray
                show ireia normal

                "Ireia" "Wir wären immer noch im Krieg versunken. Ohne die Happiness-Pille, ohne glückliche Menschen würde es nur weiter Streit und Zwietracht geben."

                "Atropos" "Ich frage mich immer noch, wie ausgerechnet diese drei Männer es damals geschafft haben uns den Frieden zu schenken…"

                show ireia normal_gray
                show tycho really_happy

                "Tycho" "Natürlich durch unsere Glücklichkeit: Happiness. Das ist das Einzige, was wirklich zählt. Spielen andere Gründe oder genauere Erläuterungen eine Rolle?"

                show tycho really_happy_gray
                show ireia strict

                "Ireia" "Nein, das ist nun wirklich nichts, worüber wir uns Gedanken machen müssten."

                "Ireia" "Sie schenkten uns Happiness und beendeten damit den 50-jährigen Krieg. Darum sind wir heute glücklich. Darum dürfen wir das Leben unserer Träume leben!"

                # Symbiont
                symb"{i}Sie haben Recht. Warum solltest du dir weiter darüber Gedanken machen? Es spielt keine Rolle. Die Hauptsache ist ein glückliches Leben und das besitzt du. {/i}"

                "Atropos" "Ihr habt Recht. (lacht) Also, andere Frage: Durftet ihr schon einmal persönlich mit Anan sprechen?"

                show ireia strict_gray
                show neiro happy

                "Neiro" "Es geht gerade um Anan? Was ist mit ihm? Ist er nicht toll? So zuvorkommend und aufmerksam- einen besseren Chef kann man sich nicht wünschen."

                show neiro happy_gray
                show ireia happy

                "Ireia" "Ich hatte Dank ein paar weniger Meetings mal mit ihm zu tun. Er ist die beeindruckendste Persönlichkeit, die ich jemals getroffen habe."

                "Ireia" "Und obwohl er fast schon gottgleichen Status hat, ist er trotzdem auf dem Boden geblieben und kümmert sich um jeden einzelnen von uns."

                show ireia happy_gray
                show tycho normal

                "Tycho" "Ich hatte ein einziges Mal mit ihm gesprochen. Damals hatte ich vergessen meine Pille zu nehmen, weil ich eine Zeit lang krank war."

                "Atropos" "Das hattest du ja noch nie erwähnt… wie ist er damit umgegangen?"

                "Tycho" "Er war unglaublich verständnisvoll und hatte mir klar gemacht, dass er nur um mein Wohlergehen und mein Glück besorgt ist."

                show tycho happy

                "Tycho" "Durch dieses Ereignis ist mir noch einmal bewusst geworden, wie wichtig die Happiness-Pille eigentlich ist."

                "Tycho" "Ich bin froh, dass Anan mir die Augen geöffnet hat. Ihr wisst gar nicht, wie sehr ich es damals bereut hatte."

                show tycho really_happy

                "Tycho" "Anan gibt alles, damit es uns gut geht und wir glücklich sind. Wie hatte ich es ihm nur so danken können?"

                "Atropos" "Tycho… wie…"

                show tycho happy

                "Tycho" "Ich… Ich bin so glücklich, dass ich eine zweite Chance erhalten habe. Jetzt kann ich dabei helfen allen Menschen ihr Glück zu geben!"

                jump nachentscheidung4

            label entscheidung4_3:

                "Atropos" "Neiro, dein Bruder ist gestorben?"

                show neiro nervous_laugh

                "Neiro" "Achso… ja. Er ist von einem der Busse erwischt worden, der eine technische Fehlfunktion hatte."

                show neiro nervous_laugh_gray
                show ireia normal

                "Ireia" "Möge er nun in Frieden glücklich sein."

                "Atropos" "Wann findet seine Ehrung statt?"

                show ireia normal_gray
                show neiro normal

                "Neiro" "Genau steht es noch nicht fest, aber voraussichtlich kommenden Sonntag. Ihr seid alle herzlich eingeladen, wenn ihr wollt. Es wird ein riesiges Fest geben."

                show neiro normal_gray
                show tycho happy

                "Tycho" "Habe ich da Fest gehört? Da kann man doch gar nicht nein sagen, ich bin so was von dabei! Atropos, wie sieht es bei dir aus?"

                "Atropos" "Ich muss später nochmal in meinen Terminkalender schauen, aber ansonsten bin ich natürlich auch gerne dabei."

                "Atropos" "Die Totenehrungen sind jedes Mal ein unvergessliches Ereignis. Ich freue mich schon darauf!"

                show tycho happy_gray
                show ireia happy

                "Ireia" "Ich komme natürlich ebenfalls. Dein Bruder war ein guter Mensch, Neiro, dem das Glück aller Menschen sehr am Herzen lag. Er verdient es angemessen geehrt und gefeiert zu werden."

                show ireia happy_gray
                show neiro happy

                "Neiro" "Danke, das freut mich sehr zu hören. Gebt die Einladung gerne an alle weiter. Ich freue mich, wenn viele Leute kommen!"

                show neiro happy_gray
                show tycho really_happy

                "Tycho" "Du kannst dich auf uns verlassen. Das wird die beste Totenehrung dieses Jahres, versprochen."

                show tycho really_happy_gray
                show neiro happy

                "Neiro" "Das ohnehin. Immerhin findet sie in meiner Familie statt. Das passiert auch nicht alle Tage. Meine Eltern sind schon seit Tagen am planen, was es alles zu Essen geben soll."

                "Atropos" "Kann ich mir vorstellen. Als letztes Jahr mein Vater starb, war die Planung seiner Ehrung auch ein großes Ereignis für meinen Bruder und mich gewesen."

                show neiro happy_gray
                show tycho normal

                "Tycho" "Es war dafür aber auch eine wunderschöne Ehrung gewesen, die deinem Vater würdig gewesen war."

                "Atropos" "Das stimmt."

                jump nachentscheidung4


            label nachentscheidung4:
                "Atropos" "Also dann, ich muss leider langsam los. Heute wartet ein Berg an Arbeit auf mich."

                show tycho happy

                "Tycho" "Mach's gut, bis zur Mittagspause."

                show tycho happy_gray
                show ireia happy

                "Ireia" "Auf Wiedersehen!"

                hide ireia
                scene hall
                with fadeshort

                # Atropos Gedanken
                symb"Es war schön, mal wieder eine Runde mit ihnen zu reden."

                # Atropos Gedanken
                symb"Ich sollte öfter mal bei ihnen vorbeischauen."

                $ talkchesismorning= True


                show chesis normal:
                    xalign 0.5

                "Chesis" "Guten Morgen!"

                "Atropos" "Hey Chesis, wie schön dir über den Weg zu laufen!"

                "Atropos" "Hast du Kloth heute schon gesehen?"

                show chesis confused

                "Chesis" "Nein. Ich…"

                "Atropos" "Ach, auch egal. Die Hauptsache ist, dass er später beim Grillen auftaucht."

                "Atropos" "Erinnerst du dich noch daran, wie wir früher immer noch Ewigkeiten hier im Flur gestanden hatten?"

                show chesis happy

                "Chesis" "Klar, wie könnte ich das vergessen. Es ist schade, dass Kloth uns keine Gesellschaft mehr leistet, aber es ist auch so schön. Und wir sehen ihn ja nach der Arbeit."

                "Atropos" "Alleine das eine Mal, als Kloth zu uns gelaufen kam, um uns zu erzählen, dass er Anans Chefsekretär werden soll!"

                show chesis happy_alt

                "Chesis" "Stimmt, das war unvergesslich! 2 Jahre ist es mittlerweile her, oder? Kloth kam zu uns gelaufen und…"

    # hier fehlt noch sepiafilter
                show sepia

                show chesis normal_gray behind sepia:
                    xalign 0.75

                show kloth grinning behind sepia:
                    xalign 0.25

                "Kloth" "Atropos… Chesis… hier seid ihr…"

                "Atropos" "Du bist ja völlig außer Atem und strahlst über das ganze Gesicht. Was hat dir dieses unglaubliche Glück bereitet?"

                "Kloth" "Ihr werdet mir diese Neuigkeiten nicht glauben… ich hätte niemals damit gerechnet, dass mir so etwas jemals passieren würde!"

                show kloth grinning_gray
                show chesis normal

                "Chesis" "Erzähl schon."

                show chesis normal_gray
                show kloth smiling

                "Kloth" "Ihr wisst doch, dass ich gestern zu Anan gerufen wurde. Ich hatte mich ja da schon gefragt, wie ich zu dieser Ehre kam…"

                "Atropos" "Und? Was war der Grund?"

                show kloth grinning

                "Kloth" "Es ist so unglaublich! Ich wurde zu seinem Chefsekretär befördert. Ich kann es immer noch nicht richtig fassen…"

                show kloth grinning_gray
                show chesis happy

                "Chesis" "Herzlichen Glückwunsch, du hast es verdient!"

                "Atropos" "Kloth, das sind ja fantastische Neuigkeiten. Ich freue mich riesig für dich!"

                show chesis happy_gray
                show kloth grinning

                "Kloth" "Es war schon immer mein Traum, der Menschheit dienen zu können und als Anans Chefsekretär ist mir das nun wirklich möglich!"

                show kloth grinning_gray
                show chesis happy

                "Chesis" "Wenn jemand von uns so etwas erreichen konnte, dann du."

                show chesis happy_gray
                show kloth smiling

                "Kloth" "Du bist aber ebenfalls unglaublich, Chesis. Du bist der beste Verkäufer, den Aither besitzt!"

                "Kloth" "Und Atropos, bei dir geht ja auch schon länger das Gerücht um, dass du zum Leiter des Labors befördert werden sollst!"

                "Atropos" "Wir erklimmen wohl alle gerade die Leiter. Aber ich könnte mir auch nichts anderes für mein Leben vorstellen."

                "Atropos" "Wir helfen den Menschen dabei ein glückliches Leben zu führen."

                show kloth smiling_gray
                show chesis confused

                "Chesis" "Kloth, was sind dann eigentlich deine Tätigkeiten?"

                show chesis confused_gray
                show kloth unsuresmiling

                "Kloth" "Sorry, aber das muss mein kleines Geheimnis bleiben. Ihr wisst, dass ich euch sonst alles sage, aber darüber darf ich nicht reden."

                "Atropos" "Ja klar, verstehe ich. Letztlich spielt es ja auch keine Rolle. Wichtig ist nur, dass wir für Aither arbeiten."

                hide kloth
                hide sepia

    # Ende Sepiafilter

                show chesis normal:
                    xalign 0.5

                "Atropos" "An solche Momente erinnere ich mich immer wieder gerne. Ich schätze jede Sekunde, die ich mit Kloth und dir verbringen darf."

                "Chesis" "Geht mir genauso. Ihr seid meine besten Freunde seit der Kindheit."

                show chesis happy

                "Chesis" "Damals, ohne euch und ohne die Happiness-Pille, war ich einsam und verloren gewesen. Alles hatte sich geändert, nachdem ich euch kennenlernen durfte."

                "Atropos" "Du hast uns damals auch sehr geholfen. Es ist gut jemanden in der Gruppe zu haben, der etwas ruhiger und bedachter ist. (lacht)"

                show chesis normal

                "Chesis" "Da vorne ist Anan. Wie soll ich ihn nur begrüßen?"

                show chesis normal_gray:
                    xalign 0.75
                show anan normal_mid:
                    xalign 0.25

                "Anan" "Guten Morgen und Glück für die Welt!"

                "Atropos" "Glück für die Welt."

                hide anan

                show chesis confused:
                    xalign 0.5

                "Chesis" "Jetzt habe ich meine Chance verpasst. Aber ist er nicht einfach nur unglaublich? Seine Präsenz nimmt den ganzen Raum ein, ohne dass er dafür etwas tun müsste."

                "Atropos" "Da kann ich dir nur zustimmen. Er ist wirklich beeindruckend."

                show chesis normal

                "Chesis" "Also dann, ich muss jetzt hier weiter. Man sieht sich."

                "Atropos" "Mach's gut. Wir sehen uns dann ja spätestens beim Grillen."

                "Atropos" "Oder in der Mittagspause, wenn wir sie gleichzeitig machen sollten."

                show chesis happy_alt

                "Chesis" "Gerne."

                hide chesis

                #Atropos Gedanken
                symb"Ich könnte mich noch einmal umsehen..."
                show screen nightshade1

                menu:
                    "Wieso ist hier ein Schmetterling?":
                        hide screen nightshade
                        symb "Wieso ist hier ein Schmetterling?"
                        jump watchhallbutterfly

                    "Ich will mir die Bilder ansehen.":
                        hide screen nightshade
                        symb"Ich will mir die Bilder ansehen."
                        jump watchhallpictures

                    "Ein Druckknopfmelder?":
                        symb"Ein Druckknopfmelder?"
                        hide screen nightshade
                        jump watchhallalarm

                    "Ich sollte dann wirklich ins Labor.":
                        hide screen nightshade
                        jump watchnothinghall

                label afternightshade1:
                    hide screen nightshade1
                    # Atropos Gedanken
                    symb"Nachtschatten. Die Blumen sind wunderschön."
                    # Atropos Gedanken
                    symb"Ich glaube, ein Entwicklerteam von Visual Novels heißt so."
                    "Atropos""…"
                    # Atropos Gedanken
                    symb"Nicht, dass ich mich mit sowas beschäftigt hätte."
                    jump watchnothinghall

                label watchhallbutterfly:
                    # Atropos
                    "Atropos""Woher kommst du denn, kleiner Flattermann? Anscheinend hast du dich irgendwie hierher verirrt."
                    # Atropos
                    "Atropos""So wunderschön. Und doch haben kleine Wesen wie du nur ein kurzes Leben."
                    # Atropos
                    "Atropos""Wenn ich dich jetzt hinauslasse, könntest du mir nicht versprechen, dich nicht beim nächsten offenen Fenster wieder hinein zu verirren."
                    # Atropos
                    "Atropos""Ich würde das Gefühl haben, dich zu retten. Aber in Wahrheit würde ich dein Schicksal nur hinauszögern. Entkommen wirst du ihm nie."
                    jump watchnothinghall

                label watchhallpictures:
                    scene detail_pictureshall
                    with fadeshort
                    # Atropos Gedanken
                    symb"Anan, Atlas und Adrés. Die drei Gründer von Aither. Gemeinsam haben sie die Welt vorangebracht."
                    # Atropos Gedanken
                    symb"Dank Ihnen konnte der Krieg ein Ende finden. Die Menschheit kann sich jetzt erholen."
                    # Atropos Gedanken
                    symb"Atlas hat seinen Sitz weiter im Westen und Adrés im Osten. Gemeinsam teilen sie sich drei gleiche Bereiche der Welt."
                    call screen arrow_watchhall()
                label watchhallalarm:
                    scene detail_alarm
                    with fadeshort
                    # Atropos Gedanken
                    symb"Damit kann man den Alarm auslösen, sollte es mal brennen oder wenn irgendwelche Gase entstehen."
                    # Atropos Gedanken
                    symb"Vor allem im Labor kann schnell etwas schiefgehen. Aber wir arbeiten fleißig und passen gut auf. Seit ich hier arbeite, ist noch kein Notfall vorgekommen."
                    # Atropos Gedanken
                    symb"Trotzdem ist es gut zu wissen, wo sich der Knopf befindet. Man weiß ja nie."
                    call screen arrow_watchhall()

                label watchnothinghall:

                    $ datewithera= True

                    "Atropos" "Ich sollte dann wirklich ins Labor."

                    play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

                    scene lab
                    with fadeshort

                    "Atropos" "Hey Era."

                    show era normal:
                        xalign 0.5

                    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

                    "Era" "…"

                    "Atropos" "…"

                    show era shy

                    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

                    "Atropos" "Ja, natürlich… sorry…"

                    play sound("Sound/Sounds/bump.mp3")

                    show era confused

                    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

                    "Era" "Ich… ahhhh…"

                    # Atropos Gedanken
                    symb"Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

                    # Atropos Gedanken
                    symb"Zum Glück bekommt sie sich immer relativ rasch wieder in den Griff."

                    "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen musst."

                    show era normal

                    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

                    "Atropos" "Was wolltest du?"

                    "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

                    show era shy

                    "Era" "…"

                    show era normal

                    "Era" "Was ich dich jedenfalls fragen wollte: Hast du nächste Woche Zeit? Ich dachte mir, wir könnten uns vielleicht mal treffen?"

                    # Atropos Gedanken
                    symb"Das war bei ihr mal wieder eine 180 Grad Wendung. Manchmal frage ich mich…"


                    # Symbiont
                    symb"{i}Sie ist einfach ein wenig unsicher. Es wirkt, als würde sie sich für dich interessieren. Darum ist sie nervös und weiß nicht, wie sie sich dir gegenüber verhalten soll. {/i}"


                    # Symbiont
                    symb"{i}Du solltest sie ein wenig beruhigen. Du magst sie doch auch, gestehe es dir ein. {/i}"

                    "Atropos" "Gerne, warum nicht? Passt dir Donnerstag? Wir könnten Bowlen gehen."

                    show era happy

                    "Era" "Wirklich? Ich… ja… ja… Donnerstag passt super!"

                    show era happy_gray:
                        xalign 0.25

                    show narcais normal:
                        xalign 0.75

                    "Narcais" "Einen glücklichen guten Morgen zusammen! Habt ihr schon meine letzten Forschungsergebnisse gesehen? Ich kann mich selbst nur loben, sie sind hervorragend ausgefallen."

                    show narcais normal_gray
                    show era shy

                    "Era" "G-Guten Morgen…"

                    "Atropos" "Morgen… hattest du dich nicht mit dem Einfluss der Impfung auf Kinder und Jugendliche beschäftigt?"

                    show era shy_gray
                    show narcais normal

                    "Narcais" "Ja, genau. Und ich bin zu dem Schluss gekommen, dass wir es mit Glycohexatenol versuchen sollten."

                    "Narcais" "Die Jugendlichen vertragen den alten Wirkstoff ebenfalls gut, aber nachweislich können wir keine Kinder damit impfen."

                    show narcais cocky

                    "Narcais" "Dies birgt allerdings bekannter Weise hohe Risiken, weil die Umweltverschmutzungen durch den Krieg auch Kinder betreffen können."

                    "Narcais" "Auch ist die Impfung eine Grundvoraussetzung für die Einnahme der Happiness-Pille. Bereits jetzt leiden viel zu viele Kinder unter der späten Einnahme."

                    show narcais normal

                    "Narcais" "Die Kinder sollten ebenfalls in der Lage sein eine glückliche Kindheit führen zu dürfen! Wenn ich an meine eigene Kindheit denke…"

                    "Atropos" "Narcais- du zählst nur Fakten auf, die bereits bekannt sind. Was ist jetzt mit dem Glycohexatenol?"

                    # Atropos Gedanken
                    symb"Er nutzt wirklich jede Chance, um mit seinem Wissen zu prahlen…"

                    show narcais cocky

                    "Narcais" "Ich habe die Erkenntnis gewonnen, dass der Wirkstoff die Durchführung der Impfung um einige Jahre vorverlegen dürfte."

                    "Narcais" "Diesbezüglich hatte ich einige Forschungen durchgeführt, welche meine Erkenntnis belegt hatten."

                    "Narcais" "Ich habe bereits einen umfassenden Bericht dazu verfasst und dir geschickt. Aber du musst vermutlich nur einen kurzen Blick darauf werfen…"

                    "Narcais" "Du weißt, dass ich immer beste Arbeit abliefere und keine Fehler mache."

                    "Atropos" "Danke, ich beschäftige mich später damit."

                    show narcais normal

                    "Narcais" "Ja, natürlich. Lass dir Zeit. Nicht jeder kann so schnell und effizient arbeiten wie ich…"

                    hide narcais

                    "Atropos" "Sorry für die Unterbrechung, Era. Also, wir schreiben dann einfach die Tage, okay?"

                    show era normal:
                        xalign 0.5


                    "Era" "J-Ja… natürlich. Danke Atropos!"



                    jump good_mood

    else:

        scene hall
        with fadeshort

        # Atropos Gedanken
        symb"Da vorne liegt das Büro- ich frage mich, ob die anderen wohl schon da sind? Ich bin heute ziemlich früh dran."

        play music "Sound/Music/Rooms/buero_normal.mp3" fadeout 3 fadein 3

        scene office_1
        with fadeshort

        # Atropos Gedanken
        symb"Hmm, es scheint noch keiner hier zu sein."

        # Atropos Gedanken
        symb"Dann bin ich wohl wirklich zu früh dran."

        #Atropos Gedanken
        symb"Ich könnte mich noch ein wenig umsehen."

        show screen computer2
        menu:
            "Ich schaue mir den Kalender an.":
                hide screen computer2
                symb"Ich schaue mir den Kalender an."
                jump watchofficecalendar2

            "Da ist ein interessantes Foto.":
                hide screen computer2
                symb"Da ist ein interessantes Foto."
                jump watchofficephoto2

            "Neben der Sanduhr liegt etwas.":
                hide screen computer2
                symb"Neben der Sanduhr liegt etwas."
                jump watchofficehourglass2

            "Oder nein, besser nicht. Ich sollte nicht in fremden Sachen herumstöbern.":
                hide screen computer2
                symb"Oder nein, besser nicht. Ich sollte nicht in fremden Sachen herumstöbern."
                jump watchnothingoffice2

        label computermoira2:
            hide screen computer2
            # Wenn Spieler direkt auf den PC im Raum klickt
            scene detail_pc_moira
            # Atropos Gedanken
            symb"Seltsam. Da hat wohl jemand etwas nachlesen wollen und vergessen den Bildschirm zu sperren."
            call screen arrowcomputer2
            label afteromputermoira2:
                scene office_1
                # Atropos Gedanken
                symb"Hm? Der Bildschirm ist einfach ausgegangen."
                # Atropos Gedanken
                symb"Wieso sollte jemand über die Moiren forschen?"
                jump watchnothingoffice2

        label watchofficecalendar2:
            scene detail_calendar
            with fadeshort
            # Atropos Gedanken
            symb"September 2256."
            # Atropos Gedanken
            symb"Der Todestag meiner Mutter jährt sich bald wieder. Ich war noch so klein… Ich kann mich gar nicht mehr an sie erinnern."
            # Atropos Gedanken
            symb"Vielleicht kommt Mora dann mal wieder zu Besuch, um gemeinsam zu feiern."
            call screen arrow_watchoffice2()


        label watchofficephoto2:
            scene detail_photo_neiro
            with fadeshort
            # Atropos Gedanken
            symb"Oh, Neiro! Das daneben muss dann wohl sein Bruder sein. Die beiden scheinen allen Anschein nach gut miteinander auszukommen."
            # Atropos Gedanken
            symb"Was sein Bruder wohl jetzt so macht?"
            call screen arrow_watchoffice2()

        label watchofficehourglass2:
            scene detail_hourglass
            with fadeshort
            # Atropos Gedanken
            symb"Was steht da?"
            show detail_hourglass_overlay
            call screen arrow_watchoffice2()

        label watchnothingoffice2:

            $ dialgoueoffice=True

            # Atropos Gedanken
            symb"Ich höre Stimmen, könnten sie das sein?"

            # Atropos Gedanken
            symb"Tatsächlich, sie sind es, und sie scheinen sich eh noch zu unterhalten, bevor sie den Tag starten. Ich sollte mich zu ihnen gesellen."

            scene office_2
            with fadeshort

            "Atropos" "Hey Leute."

            show ireia normal:
                xalign 0.35

            "Ireia" "Atropos, wie schön dich hier mal wieder anzutreffen. Du hast dich schon seit einer Weile nicht mehr im Büro blicken lassen. Vermisst hast du uns wohl nicht sonderlich."

            "Atropos" "Nun, ist ja auch nicht so ganz mein Arbeitsplatz. (lacht) Und keine Sorge, ich habe euch alle vermisst."

            show ireia normal_gray
            show tycho normal:
                xalign 0.85

            "Tycho" "Das will ich dir aber auch geraten haben. (lacht) Uns kann man doch gar nicht {b}nicht{/b} mögen, nicht wahr? Und dementsprechend musst du uns auch vermisst haben."

            show tycho normal_gray
            show armene normal:
                xalign 0.0

            "Armene" "Ja. Ja, das stimmt! Hallo Atropos."

            "Atropos" "Hi Armene, wie geht es dir?"

            "Armene" "Ich bin glücklich wie immer!"

            show armene normal_gray
            show ireia happy

            "Ireia" "Jetzt überfall die Arme doch nicht, du kennst sie doch."

            show ireia strict

            "Ireia" "Und Armene, du solltest weiter deine Präsentation über das firmeninterne Kommunikationssystem vorbereiten- ich erwarte bessere Arbeit von dir als letztes Mal."

            show ireia strict_gray
            show armene shy

            "Armene" "Natürlich Ireia, tut mir leid!"

            hide armene
            show tycho normal

            "Tycho" "Neiro, gesell dich doch zu uns, was sitzt du so einsam und verlassen an deinem Platz? Deine Arbeitszeit hat doch noch nicht angefangen."

            show tycho normal_gray
            show neiro normal:
                xalign 0.6

            "Neiro" "Oh… ich hatte euch gar nicht bemerkt, tut mir leid. Atropos? Was machst du hier? Arbeitest du nicht in einer anderen Abteilung? Verkauf oder so?"

            "Atropos" "Neiro, wie er leibt und lebt. (lacht)"

            show neiro normal_gray
            show ireia strict

            "Ireia" "Du solltest definitiv an deinem Gedächtnis arbeiten, Neiro. Es wird in letzter Zeit immer kritischer. Ich möchte deswegen von dir keine schlechteren Ergebnisse sehen."

            show ireia strict_gray
            show neiro happy

            "Neiro" "Natürlich Ireia, ich gebe weiterhin mein Bestes, du musst dir keine Sorgen machen."

            # Atropos Gedanken
            symb"Neiro hatte schon immer eine seltsame Art mit Kritik umzugehen. Aber immerhin verträgt er dadurch Ireias direkte Art gut."

            show neiro happy_gray
            show tycho normal

            "Tycho" "Habt ihr es eigentlich schon gehört? Anan will anlässlich des diesjährigen 37. Gründungstages wieder eine riesige Feier veranstalten!"

            show tycho normal_gray
            show ireia happy

            "Ireia" "Dann sollten wir noch härter arbeiten, damit wir auch einen Anlass zum Feiern haben. Das Glück der Menschen entsteht nicht von selbst."

            show ireia happy_gray
            show tycho happy

            "Tycho" "Natürlich arbeiten wir hart! Aber das tut man für Aither doch auch gerne."

            show tycho normal

            "Tycho" "Zurück zum Thema… diese Party wird gigantisch. Erinnert ihr euch noch an die anlässlich des 30. Gründungstages?"

            "Atropos" "Damals hatte ich noch nicht hier gearbeitet. So alt bin ich nun auch nicht. (lacht)"

            "Tycho" "Ach stimmt, du bist ja ein paar Jahre jünger als ich, oder? 24?"

            "Atropos" "Fast… 25. (grinst)"

            "Tycho" "Jedenfalls… wo war ich stehen geblieben?"

            "Tycho" "Ach ja, der 30. Gründungstag… eine bessere Feier habe ich noch nie erlebt! Und ich war schon auf vielen Feiern gewesen, das könnt ihr mir glauben."

            "Tycho" "Damals hatte ich gerade erst hier angefangen. Ich war nur ein einfacher Praktikant gewesen, aber dennoch gab Anan mir eine Einladung."

            show tycho really_happy

            "Tycho" "Ich konnte mein Glück kaum fassen. Es war berauschend! All das Essen im Überfluss und dann die Musik, der Tanz…"

            show tycho really_happy_gray
            show ireia strict

            "Ireia" "Tycho, fass dich kürzer. Wir haben noch Arbeit zu erledigen. Und jetzt erzähl schon, was hast du vom diesjährigen Gründungstag gehört?"

            "Atropos" "Ja… du kannst doch nicht die Information anteasern und dann damit hinter dem Berg halten."

            show armene normal_gray:
                xalign 0.0
            show ireia strict_gray
            show tycho normal

            "Tycho" "Sorry, sorry… also, ich weiß nicht viel, aber angeblich sollen Atlas und Adrés höchstpersönlich vorbeikommen, um gemeinsam mit Anan diesen Tag zu feiern."

            "Atropos" "Habe ich dich gerade richtig verstanden? Die Großen Drei, alle hier in Astoa?"

            show tycho normal_gray
            show ireia happy

            "Ireia" "Das sind ja unglaubliche Neuigkeiten! Wieso hast du uns nicht schon früher davon erzählt?"

            show ireia happy_gray
            show tycho normal

            "Tycho" "Weil ich davor selbst nur ganz vage Gerüchte gehört habe, aber mittlerweile verstärkt sich der Eindruck immer mehr, dass an den Gerüchten etwas Wahres dran sein könnte."

            "Atropos" "Ich frage mich, wie die beiden wohl sind. Natürlich kennt man ihre Namen… immerhin sind Anan, Atlas und Adrés die Gründer von Aither und diejenigen, die den Krieg beendet haben…"

            "Atropos" "Dennoch kenne ich Atlas und Adrés nur von Fotos und nicht von Videoaufzeichnungen oder anderen Quellen. Es wird ein ziemliches Geheimnis um ihre Existenz gemacht."

            show tycho normal_gray
            show ireia normal

            "Ireia" "Das ist aber auch gut so. Die drei sind immerhin dafür verantwortlich, dass alle Menschen glücklich sind."

            "Ireia" "Da haben sie Wichtigeres zu tun, als sich darum zu kümmern, dass wir Informationen über sie bekommen."

            show ireia normal_gray
            show armene shy

            "Armene" "Ich frage mich, ob Atlas und Adrés wohl auch so unglaublich charmant und gutaussehend sind wie Anan… (seufzt verträumt)"

            show armene shy_gray
            show ireia strict

            "Ireia" "Armene? Wie lange stehst du schon hier? Bist du fertig mit deiner Präsentation?"

            show ireia strict_gray
            show armene shy

            "Armene" "Nein… Ich wollte mich nur am Gespräch beteiligen…"

            show armene shy_gray
            show neiro nervous_laugh

            "Neiro" "Um was geht es? Tut mir leid, ich bin mit den Gedanken kurz abgeschweift…"

            show neiro normal

            "Neiro" "Mein Bruder ist gestern gestorben und wir müssen noch die Feier ihm zu Ehren vorbereiten…"

            show neiro normal_gray
            show tycho happy

            "Tycho" "(lacht) Und wieder das übliche Chaos. Es macht echt zu viel Spaß mit euch Zeit zu verbringen!"

            show tycho happy_gray
            show ireia strict

            "Ireia" "Armene, los an die Arbeit!"

            show ireia strict_gray
            show armene normal

            "Armene" "Ja natürlich Ireia, mache ich!"

            hide armene

            # Atropos Gedanken
            symb"Was mich gerade interessieren würde…"

            menu:
                "Ich hätte gerne mehr Informationen über die Gründungsfeier.":
                    jump entscheidung4_1V2
                "Ich würde mich gerne noch etwas mehr über die Großen Drei unterhalten.":
                    jump entscheidung4_2V2
                "Ich will mich bei Neiro nach seinem verstorbenen Bruder erkundigen.":
                    jump entscheidung4_3V2
                "Oh, es ist schon spät. Ich sollte ins Labor.":
                    symb "Oh, es ist schon spät. Ich sollte ins Labor."
                    jump nachentscheidung4V2

            label entscheidung4_1V2:

                $ neiro_unterhalten = True

                "Atropos" "Tycho, hast du noch mehr Informationen über die diesjährige Gründungsfeier?"

                show tycho normal

                "Tycho" "Hmm, gute Frage- lass mich einen Moment überlegen…"

                show tycho normal_gray
                show neiro nervous_laugh

                "Neiro" "Ihr sprecht über die Gründungsfeier?"

                show neiro nervous_laugh_gray
                show ireia normal

                "Ireia" "Ja, darum ging es schon die ganzen letzten Minuten."

                show ireia normal_gray
                show neiro normal

                "Neiro" "Oh. Jedenfalls, ich weiß ein bisschen was…"

                show neiro normal_gray
                show tycho happy

                "Tycho" "Worauf wartest du noch? Erzähl schon!"

                show tycho happy_gray
                show neiro normal

                "Neiro" "Atlas und Adrés werden hierher nach Astoa kommen, um der Gründungsfeier beizuwohnen!"

                "Atropos" "Neiro, das wissen wir bereits. (lacht) Immerhin haben wir dadurch noch einmal die Bestätigung."

                show neiro normal_gray
                show ireia confused

                "Ireia" "Weißt du sonst noch etwas? Irgendwelche Neuigkeiten?"

                show ireia confused_gray
                show neiro normal

                "Neiro" "Es hieß, dass heute im Laufe des Tages noch eine offizielle Ankündigung des Ganzen erfolgen soll."

                "Atropos" "Eine offizielle Ankündigung? Also einfach eine Durchsage von Anan?"

                "Neiro" "Nein, soweit ich das weiß, werden alle drei live geschaltet."

                show neiro normal_gray
                show ireia happy

                "Ireia" "Das gab es ja noch nie! Normalerweise kommunizieren wir nicht mit den Menschen außerhalb von Astoa… warum sollten wir auch?"

                show ireia happy_gray
                show tycho really_happy

                "Tycho" "Das sind wirklich unglaubliche Neuigkeiten! Ich freue mich schon darauf. Die diesjährige Gründungsfeier wird unbeschreiblich und unvergesslich werden!"

                show tycho really_happy_gray
                show neiro happy

                "Neiro" "Und es gibt noch etwas: Angeblich soll mit der Gründungsfeier eine neue Happiness-Pille vorgestellt werden."

                show neiro happy_gray
                show ireia normal

                "Ireia" "Eine neue Pille? Sag nicht, dass es eine Pille sein wird, die uns noch glücklicher macht?"

                show ireia normal_gray
                show tycho normal

                "Tycho" "Ich wüsste nicht, was es sonst sein könnte… der Tag wird ja immer besser!"

                show tycho normal_gray
                show ireia confused

                "Ireia" "Atropos, müsstest du darüber nicht eigentlich mehr wissen?"

                # Atropos Gedanken
                symb"Eine neue Pille? Ob sie dann wohl besser wirkt als die aktuelle? Immerhin scheine ich sie momentan nicht wirklich für mein Glück zu brauchen."

                # Symbiont
                symb"{i}Doch, du brauchst sie. Merkst du nicht, dass du immer mehr zu zweifeln beginnst? Zweifel säen Unmut und Unzufriedenheit. Du gefährdest dein Glück. {/i}"

                jump nachentscheidung4V2

            label entscheidung4_2V2:

                "Atropos" "Ich bin wirklich gespannt auf Atlas und Adrés."

                show ireia happy

                "Ireia" "Sie wollen das Beste für die Welt, genauso wie Anan. Ist das nicht das Einzige, das zählt?"

                show ireia happy_gray
                show tycho happy

                "Tycho" "Ihnen ist unser Wohl am aller Wichtigsten. Stellt euch nur vor, wie die Welt ohne sie wäre. Ich wage es gar nicht, mir das vorzustellen!"

                show tycho happy_gray
                show ireia normal

                "Ireia" "Wir wären immer noch im Krieg versunken. Ohne die Happiness-Pille, ohne glückliche Menschen würde es nur weiter Streit und Zwietracht geben."

                "Atropos" "Ich frage mich immer noch, wie ausgerechnet diese drei Männer es damals geschafft haben uns den Frieden zu schenken…"

                show ireia normal_gray
                show tycho happy

                "Tycho" "Natürlich durch unsere Glücklichkeit: Happiness. Das ist das Einzige, was wirklich zählt. Spielen andere Gründe oder genauere Erläuterungen eine Rolle?"

                show tycho happy_gray
                show ireia normal

                "Ireia" "Nein, das ist nun wirklich nichts, worüber wir uns Gedanken machen müssten."

                "Ireia" "Sie schenkten uns Happiness und beendeten damit den 50-jährigen Krieg. Darum sind wir heute glücklich. Darum dürfen wir das Leben unserer Träume leben!"

                # Symbiont
                symb"{i} Sie haben Recht. Warum solltest du dir weiter darüber Gedanken machen? Es spielt keine Rolle. Die Hauptsache ist ein glückliches Leben und das besitzt du. {/i}"

                # Atropos Gedanken
                symb"Ja, ich besitze ein glückliches Leben. Aber sollte man aus diesem Grund dennoch nichts hinterfragen?"

                "Atropos" "Sollten wir nicht mehr erfahren dürfen? Wieso machen Anan und die anderen beiden so ein großes Geheimnis aus der Vergangenheit?"

                "Atropos" "Wir wissen, dass sie den Krieg beendet haben und dass das mit Hilfe der Happiness-Pille passiert ist… aber wie?"

                show ireia confused

                "Ireia" "Habt ihr schon Mal die Ehre gehabt mit Anan zu sprechen?"

                # Atropos Gedanken
                symb"Sie übergehen mich. Ist das in letzter Zeit nicht irgendwie häufiger vorgekommen? Als würden sie die Wahrheit einfach nicht hören wollen."

                # Atropos Gedanken
                symb"Naja, egal, ich will mir gerade keine Gedanken mehr darum machen. Heute ist so ein schöner Tag. Ich sollte aufhören über so unnötiges Zeug nachzudenken."

                show ireia normal

                "Ireia" "Ich hatte Dank ein paar weniger Meetings mal mit ihm zu tun. Er ist die beeindruckendste Persönlichkeit, die ich jemals getroffen habe."

                "Ireia" "Und obwohl er fast schon gottgleichen Status hat, ist er trotzdem auf dem Boden geblieben und kümmert sich um jeden einzelnen von uns."

                show ireia normal_gray
                show neiro happy

                "Neiro" "Es geht gerade um Anan? Was ist mit ihm? Ist er nicht toll? So zuvorkommend und aufmerksam- einen besseren Chef kann man sich nicht wünschen."

                show neiro happy_gray
                show tycho normal

                "Tycho" "Ich hatte ein einziges Mal mit ihm gesprochen. Damals hatte ich vergessen meine Pille zu nehmen, weil ich eine Zeit lang krank war."

                "Atropos" "Das hattest du ja noch nie erwähnt… wie ist er damit umgegangen?"

                show tycho happy

                "Tycho" "Er war unglaublich verständnisvoll und hatte mir klar gemacht, dass er nur um mein Wohlergehen und mein Glück besorgt ist."

                # Atropos Gedanken
                symb"Ob Anan wohl auch bei mir so verständnisvoll reagieren würde, wenn er mitbekommen würde, dass ich die Pille nicht genommen habe?"

                "Tycho" "Durch dieses Ereignis ist mir noch einmal bewusst geworden, wie wichtig die Happiness-Pille eigentlich ist."

                show tycho really_happy

                "Tycho" "Ich bin froh, dass Anan mir die Augen geöffnet hat. Ihr wisst gar nicht, wie sehr ich es damals bereut hatte."

                "Tycho" "Anan gibt alles, damit es uns gut geht und wir glücklich sind. Wie hatte ich es ihm nur so danken können?"

                "Atropos" "Tycho… wie…"

                "Tycho" "Ich… Ich bin so glücklich, dass ich eine zweite Chance erhalten habe. Jetzt kann ich dabei helfen allen Menschen ihr Glück zu geben!"

                jump nachentscheidung4V2

            label entscheidung4_3V2:

                "Atropos" "Neiro, dein Bruder ist gestorben?"

                show neiro nervous_laugh

                "Neiro" "Achso… ja. Er ist von einem der Busse erwischt worden, der eine technische Fehlfunktion hatte."

                show neiro nervous_laugh_gray
                show ireia normal

                "Ireia" "Möge er nun in Frieden glücklich sein."

                "Atropos" "Wann findet seine Ehrung statt?"

                show ireia normal_gray
                show neiro normal

                "Neiro" "Genau steht es noch nicht fest, aber voraussichtlich kommenden Sonntag. Ihr seid alle herzlich eingeladen, wenn ihr wollt. Es wird ein riesiges Fest geben."

                show neiro normal_gray
                show tycho happy

                "Tycho" "Habe ich da Fest gehört? Da kann man doch gar nicht nein sagen, ich bin so was von dabei! Atropos, wie sieht es bei dir aus?"

                "Atropos" "Ich muss später nochmal in meinen Terminkalender schauen, aber ansonsten bin ich natürlich auch gerne dabei."

                "Atropos" "Die Totenehrungen sind jedes Mal ein unvergessliches Ereignis. Ich freue mich schon darauf!"

                show tycho happy_gray
                show ireia happy

                "Ireia" "Ich komme natürlich ebenfalls. Dein Bruder war ein guter Mensch, Neiro, dem das Glück aller Menschen sehr am Herzen lag. Er verdient es angemessen geehrt und gefeiert zu werden."

                show ireia happy_gray
                show neiro happy

                "Neiro" "Danke, das freut mich sehr zu hören. Gebt die Einladung gerne an alle weiter. Ich freue mich, wenn viele Leute kommen!"

                show neiro happy_gray
                show tycho really_happy

                "Tycho" "Du kannst dich auf uns verlassen. Das wird die beste Totenehrung dieses Jahres, versprochen."

                show tycho really_happy_gray
                show neiro happy

                "Neiro" "Das ohnehin. Immerhin findet sie in meiner Familie statt. Das passiert auch nicht alle Tage. Meine Eltern sind schon seit Tagen am planen, was es alles zu Essen geben soll."

                "Atropos" "Kann ich mir vorstellen. Als letztes Jahr mein Vater starb, war die Planung seiner Ehrung auch ein großes Ereignis für meinen Bruder und mich gewesen."

                show neiro happy_gray
                show tycho normal

                "Tycho" "Es war dafür aber auch eine wunderschöne Ehrung gewesen, die deinem Vater würdig gewesen war."

                "Atropos" "Das stimmt."


                jump nachentscheidung4V2


            label nachentscheidung4V2:
                "Atropos" "Also dann, ich muss leider langsam los. Heute wartet ein Berg an Arbeit auf mich."

                show tycho happy

                "Tycho" "Mach's gut, bis zur Mittagspause!"

                show tycho happy_gray
                show ireia happy

                "Ireia" "Auf Wiedersehen!"

                scene hall
                with fadeshort

                # Atropos Gedanken
                symb"So… dann mal auf ins Labor."

                $ talkchesismorning= True

                show chesis normal

                "Chesis" "Guten Morgen!"

                "Atropos" "Hey Chesis, wie schön dir über den Weg zu laufen."

                "Atropos" "Hast du Kloth heute schon gesehen?"

                show chesis confused

                "Chesis" "Nein. Ich…"

                "Atropos" "Was ist? Aber ich frage mich wirklich, wo er ist…"

                "Atropos" "Ich habe schon seit gestern nichts mehr von ihm gehört und wir wollten heute eigentlich noch besprechen, was wir fürs Grillen besorgen wollen."

                "Atropos" "Mir fällt auf, dass er auch auf meine Nachrichten nicht mehr geantwortet hat… seltsam…"

                # Symbiont
                symb"{i}Vermutlich ist er einfach viel beschäftigt. Die anderen meinten doch, dass bald die Gründungsfeier sein wird. Da wird Kloth viel zu organisieren haben. {/i}"

                show chesis normal

                "Chesis" "Ich… mein Kopf tut so weh. Tut mir leid, ich muss los…"

                "Atropos" "Alles in Ordnung, Chesis? Kann ich irgendetwas für dich tun?"

                "Chesis" "Schon okay, es wird gerade wieder besser. Worüber hatten wir nochmal gesprochen?"

                "Atropos" "Über Kloth und dass er seit gestern fast schon spurlos verschwunden ist."

                show chesis confused

                "Chesis" "Ich bin mir sicher, er wird schon wieder auftauchen…"

                show chesis happy

                "Chesis" "Mach dir keinen Kopf! Du musst dir wirklich keine Gedanken machen. Es geht ihm bestimmt gut."

                "Chesis" "Ja ganz bestimmt. Es geht ihm gut. Alles ist in Ordnung. "

                "Chesis" "Er wird nachher wieder bei uns sein und wir werden alle zusammen grillen. So wie wir es schon seit Wochen geplant haben. "

                # Atropos Gedanken
                symb"Was ist denn nur los mit ihm? Er wirkt so anders. Normalerweise redet er nie so viel…"

                "Atropos" "Chesis, bist du dir sicher, dass alles in Ordnung ist?"

                # vollkommen ruhig und gelassen.

                show chesis happy_alt

                "Chesis" "Ja natürlich ist alles in Ordnung. Warum fragst du? "

                # Symbiont
                symb"{i}Du hast es dir bestimmt nur eingebildet. Er ist glücklich, was sollte also nicht stimmen? {/i}"

                "Atropos" "Alles gut… passt schon…"

                # Atropos Gedanken
                symb"Vielleicht gab es ja einen Vorfall zwischen ihm und seiner Freundin?"

                show chesis normal

                "Chesis" "Also dann, ich muss los. Wir sehen uns später."

                "Atropos" "Wenn es etwas gibt, worüber du mit mir reden möchtest, kannst du jederzeit zu mir kommen. Ich hoffe das weißt du."

                show chesis happy

                "Chesis" "Danke Atropos, du bist ein wahrer Freund. Aber mach dir keine Sorgen, es ist alles in Ordnung. Ich bin glücklich."

                "Atropos" "(leise) Das ist alles, was zählt."

                show chesis happy_alt

                "Chesis" "Bis später!"

                "Atropos" "Mach's gut…"

                hide chesis

                #Atropos Gedanken
                symb"… Das war ein wenig seltsam. Ich glaube, ich sollte mich ein wenig auf andere Gedanken bringen."

                #Atropos Gedanken
                symb"Ich könnte mich vielleicht noch einmal umsehen, bevor ich gehe..."

                show screen nightshade3

                menu:
                    "Wieso ist hier ein Schmetterling?":
                        hide screen nightshade3
                        "Wieso ist hier ein Schmetterling?"
                        jump watchhallbutterfly3

                    "Ich will mir die Bilder ansehen.":
                        hide screen nightshade3
                        "Ich will mir die Bilder ansehen."
                        jump watchhallpictures3

                    "Ein Druckknopfmelder?":
                        hide screen nightshade3
                        "Ein Druckknopfmelder?"
                        jump watchhallalarm3

                    "Ich habe vermutlich lange genug herumgetrödelt.":
                        hide screen nightshade3
                        jump watchnothinghall3

                label afternightshade3:
                    hide screen nightshade3
                    # Atropos Gedanken
                    symb"Nachtschatten. Die Blumen sind wunderschön."
                    # Atropos Gedanken
                    symb"Ich glaube, ein Entwicklerteam von Visual Novels heißt so."
                    "Atropos""…"
                    # Atropos Gedanken
                    symb"Nicht, dass ich mich mit sowas beschäftigt hätte."
                    jump watchnothinghall3

                label watchhallbutterfly3:
                    # Atropos
                    symb"Woher kommst du denn, kleiner Flattermann? Anscheinend hast du dich irgendwie hierher verirrt."
                    # Atropos
                    symb"So wunderschön. Und doch haben kleine Wesen wie du nur ein kurzes Leben."
                    # Atropos
                    symb"Wenn ich dich jetzt hinauslasse, könntest du mir nicht versprechen, dich nicht beim nächsten offenen Fenster wieder hinein zu verirren."
                    # Atropos
                    symb"Ich würde das Gefühl haben, dich zu retten. Aber in Wahrheit würde ich dein Schicksal nur hinauszögern. Entkommen wirst du ihm nie."
                    jump watchnothinghall3

                label watchhallpictures3:
                    scene detail_pictureshall
                    with fadeshort
                    # Atropos Gedanken
                    symb"Anan, Atlas und Adrés. Die drei Gründer von Aither. Gemeinsam haben sie die Welt vorangebracht."
                    # Atropos Gedanken
                    symb"Dank Ihnen konnte der Krieg ein Ende finden. Die Menschheit kann sich jetzt erholen."
                    # Atropos Gedanken
                    symb"Atlas hat seinen Sitz weiter im Westen und Adrés im Osten. Gemeinsam teilen sie sich drei gleiche Bereiche der Welt."
                    call screen arrow_watchhall3()

                label watchhallalarm3:
                    scene detail_alarm
                    with fadeshort
                    # Atropos Gedanken
                    symb"Damit kann man den Alarm auslösen, sollte es mal brennen oder wenn irgendwelche Gase entstehen."
                    # Atropos Gedanken
                    symb"Vor allem im Labor kann schnell etwas schiefgehen. Aber wir arbeiten fleißig und passen gut auf. Seit ich hier arbeite, ist noch kein Notfall vorgekommen."
                    # Atropos Gedanken
                    symb"Trotzdem ist es gut zu wissen, wo sich der Knopf befindet. Man weiß ja nie."
                    call screen arrow_watchhall3()

                label watchnothinghall3:
                    #Atropos Gedanken
                    symb"Ich habe vermutlich lange genug herumgetrödelt. Wird Zeit, dass ich mich langsam an die Arbeit mache."
                    jump worknachzelos

label work:
    show zelos normal

    "Atropos" "Ich wollte ohnehin zur Arbeit los."

    "Zelos" "Dann lass dich von mir nicht aufhalten. Ich bin der Letzte, der etwas gegen Arbeit sagen würde."

    "Atropos" "(lacht) Das ist mir durchaus bewusst. So gewissenhaft wie du ist wohl kaum einer, abgesehen von Chesis und Kloth. Die beiden haben es wirklich weit gebracht."

    "Zelos" "Ich be…"

    show zelos happy

    "Zelos" "(räuspert sich) Ich freue mich unglaublich für die beiden. Sie sind so weit gekommen und vor allem Kloth wird noch so viel mehr erreichen."

    "Atropos" "Als Kind hätte er sich vermutlich auch niemals vorstellen können eines Tages Chefsekretär von Anan zu werden."

    show zelos normal

    "Zelos" "Also dann, ich muss nun wirklich weitermachen. Aither öffnet bald und die Pillen lagern sich weder von selbst ein, noch verkaufen sie sich von allein."

    "Atropos" "Mach's gut, wir sehen uns!"

    "Zelos" "Ach Atropos, ich vergaß: Bist du um 12:15 Uhr in der Mensa dabei?"

    "Atropos" "Ich denke, ich müsste es schaffen. Bis dann, man sieht sich."

    show zelos happy

    "Zelos" "Bis nachher und einen wunderschön glücklichen Tag in der besten Firma der Welt!"

    hide zelos

    label worknachzelos:

        if pill_taken:

            scene hall
            with fadeshort

            # Atropos Gedanken
            symb"Was muss ich heute noch alles erledigen? Narcais wollte mir seinen Bericht über seine letzten Forschungen schicken und sonst…"

            # Atropos Gedanken
            symb"Ach ja, stimmt. Ich muss noch einmal die Wirkstoffliste der Tabletten durchgehen. Anan wollte, dass ich alle erfasse, weil er Änderungen vornehmen möchte."

            # Atropos Gedanken
            symb"Ich bin gespannt, was die neuen Wirkstoffe alles bewirken…"

            # Atropos Gedanken
            symb"Letztlich werde ich es wohl erst erfahren, wenn die Pille im Verkauf ist, immerhin arbeitet jeder nur an einem winzigen Teil des großen Ganzen."

            show anan normal_mid :
                xalign 0.5

            "Anan" "Guten Morgen und Glück für die Welt!"

            "Atropos" "Guten Morgen!"

            "Anan" "Atropos Laiotas- richtig? Kann ich die Liste heute noch von dir erwarten? Sie wird von meinen anderen Forschern benötigt."
            # Atropos Gedanken
            symb"Anan kennt meinen Namen? Das werden die anderen niemals glauben, wenn ich es ihnen erzähle…"

            "Atropos" "Ja, natürlich, ich stelle sie dir heute fertig."

            show anan happy_mid

            "Anan" "Vielen Dank! Wir alle schätzen deine Arbeit sehr. Denk immer daran: Den Glücklichen gehört die Welt. Kein Mensch sollte unglücklich sein."

            "Atropos" "Ich werde es nicht vergessen!"

            show anan normal_mid

            "Anan" "Ich erwarte den Bericht um 16 Uhr in meinem Postfach."

            "Atropos" "Natürlich, ich werde dich nicht enttäuschen!"

            show anan happy_mid

            "Anan" "Du könntest mich niemals enttäuschen. Ich wünsche dir einen Tag voller Glücklichkeit."

            hide anan

            # Atropos Gedanken
            symb"Anan hat tatsächlich mit mir gesprochen? Ich muss träumen…"

            # Atropos Gedanken
            symb"Er war höflich gewesen, aber gleichzeitig so einnehmend. Man kann ihm keinen Wunsch abschlagen."

            # Atropos Gedanken
            symb"Und dass er sich die Zeit genommen hat, mit mir zu sprechen, obwohl er Anan ist… Er kümmert sich wirklich um das Glück aller Menschen. Es ist nicht nur leeres Gerede."

            # Atropos Gedanken
            symb"Aber bevor ich mich um den Bericht für ihn kümmere, könnte ich mich noch kurz umsehen."

            show screen nightshade2

            menu:
                "Wieso ist hier ein Schmetterling?":
                    hide screen nightshade2
                    "Wieso ist hier ein Schmetterling?"
                    jump watchhallbutterfly2

                "Ich will mir die Bilder ansehen.":
                    hide screen nightshade2
                    "Ich will mir die Bilder ansehen."
                    jump watchhallpictures2

                "Ein Druckknopfmelder?":
                    hide screen nightshade2
                    "Ein Druckknopfmelder?"
                    jump watchhallalarm2

                "Ich sollte dann wirklich ins Labor. Ich will Anan nicht enttäuschen":
                    hide screen nightshade2
                    jump watchnothinghall2

            label afternightshade2:
                hide screen nightshade2
                # Atropos Gedanken
                "Nachtschatten. Die Blumen sind wunderschön."
                # Atropos Gedanken
                "Ich glaube, ein Entwicklerteam von Visual Novels heißt so."
                # Atropos Gedanken
                "…"
                # Atropos Gedanken
                "Nicht, dass ich mich mit sowas beschäftigt hätte."
                jump watchnothinghall2

            label watchhallbutterfly2:
                # Atropos
                symb"Woher kommst du denn, kleiner Flattermann? Anscheinend hast du dich irgendwie hierher verirrt."
                # Atropos
                symb"So wunderschön. Und doch haben kleine Wesen wie du nur ein kurzes Leben."
                # Atropos
                symb"Wenn ich dich jetzt hinauslasse, könntest du mir nicht versprechen, dich nicht beim nächsten offenen Fenster wieder hinein zu verirren."
                # Atropos
                symb"Ich würde das Gefühl haben, dich zu retten. Aber in Wahrheit würde ich dein Schicksal nur hinauszögern. Entkommen wirst du ihm nie."
                jump watchnothinghall2

            label watchhallpictures2:
                scene detail_pictureshall
                with fadeshort
                # Atropos Gedanken
                symb"Anan, Atlas und Adrés. Die drei Gründer von Aither. Gemeinsam haben sie die Welt vorangebracht."
                # Atropos Gedanken
                symb"Dank Ihnen konnte der Krieg ein Ende finden. Die Menschheit kann sich jetzt erholen."
                # Atropos Gedanken
                symb"Atlas hat seinen Sitz weiter im Westen und Adrés im Osten. Gemeinsam teilen sie sich drei gleiche Bereiche der Welt."
                call screen arrow_watchhall()

            label watchhallalarm2:
                scene detail_alarm
                with fadeshort
                # Atropos Gedanken
                symb"Damit kann man den Alarm auslösen, sollte es mal brennen oder wenn irgendwelche Gase entstehen."
                # Atropos Gedanken
                symb"Vor allem im Labor kann schnell etwas schiefgehen. Aber wir arbeiten fleißig und passen gut auf. Seit ich hier arbeite, ist noch kein Notfall vorgekommen."
                # Atropos Gedanken
                symb"Trotzdem ist es gut zu wissen, wo sich der Knopf befindet. Man weiß ja nie."
                call screen arrow_watchhall()

            label watchnothinghall2:

                $ datewithera= True


                # Atropos Gedanken
                symb"Jetzt sollte ich aber weiter ins Labor. Ich will Anan nicht enttäuschen."

                play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3
                scene lab
                with fadeshort

                "Atropos" "Hey Era."

                show era normal:
                    xalign 0.5

                "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

                "Era" "…"

                "Atropos" "…"

                show era shy

                "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

                "Atropos" "Ja, natürlich… sorry…"

                play sound("Sound/Sounds/bump.mp3")

                show era confused

                "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

                show era shy

                "Era" "Ich… ahhhh…"

                # Atropos Gedanken
                symb"Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

                # Atropos Gedanken
                symb"Zum Glück bekommt sie sich immer relativ rasch wieder in den Griff."

                "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen müsstest."

                show era confused

                "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

                "Atropos" "Was wolltest du?"

                "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

                show era shy

                "Era" "…"

                show era normal

                "Era" "Was ich dich jedenfalls fragen wollte: Hast du nächste Woche Zeit? Ich dachte mir wir könnten uns vielleicht mal treffen?"

                # Atropos Gedanken
                symb"Das war bei ihr mal wieder eine 180 Grad Wendung. Manchmal frage ich mich…"


                # Symbiont
                symb"{i}Sie ist einfach ein wenig unsicher. Es wirkt, als würde sie sich für dich interessieren. Darum ist sie nervös und weiß nicht, wie sie sich dir gegenüber verhalten soll. {/i}"

                # Symbiont
                symb"{i}Du solltest sie ein wenig beruhigen. Du magst sie doch auch, gestehe es dir ein. {/i}"

                "Atropos" "Gerne, warum nicht? Passt dir Donnerstag? Wir könnten Bowlen gehen."

                show era happy

                "Era" "Wirklich? Ich… ja… ja… Donnerstag passt super!"

                "Atropos" "Dann ist es abgemacht."

                show era normal

                "Era" "Kommen… kommen Chesis und Kloth dann auch mit? Ihr drei seid wirklich unzertrennlich, seit ihr hier angefangen habt…"

                "Atropos" "Möchtest du denn, dass sie mitkommen?"

                show era shy

                "Era" "Also… Ich… Ich… Nein, ehrlich gesagt, würde ich lieber Zeit mit dir alleine verbringen."

                show narcais normal:
                    xalign 0.25

                show era shy_gray:
                    xalign 0.75


                "Narcais" "Einen glücklichen guten Morgen zusammen. Was habe ich verpasst? Redet ihr über mich?"

                "Atropos" "Morgen… Und nein, nicht jedes Gespräch dreht sich gleich um dich, Narcais. (lacht)"

                show narcais normal_gray
                show era normal

                "Era" "G-Guten Morgen… es ging gerade um Kloth und Chesis."

                show era normal_gray
                show narcais cocky

                "Narcais" "Ach die drei unzertrennlichen Freunde. Ihr wart schon damals in der Schule berühmt berüchtigt. Keiner konnte euch das Wasser reichen."

                show narcais annoyed

                "Narcais" "Abgesehen von mir natürlich, aber das haben alle verkannt."

                show narcais annoyed_gray
                show era normal

                "Era" "Hattet ihr damals eigentlich alle gleichzeitig angefangen hier zu arbeiten, Atropos?"

                "Atropos" "Nein, Kloth hatte ein paar Jahre vor uns angefangen. Er wurde damals von Anan höchstpersönlich rekrutiert."

                show era confused

                "Era" "Von Anan?"

                "Atropos" "Kloth hatte bei einer Feier eine Rede über Aither und die Bedeutung des Glücks gehalten und konnte so Anan von sich überzeugen."

                show era normal

                "Era" "Kloth ist wirklich mitreißend. Er ist Anan sehr ähnlich. Fast schon wie Vater und Sohn."

                "Atropos" "Das stimmt wohl. (lacht)"

                show era confused

                "Era" "Und… und was war mit Chesis und dir gewesen?"

                "Atropos" "Kloth hatte mich zu einem Praktikum überredet und es war die beste Entscheidung meines Lebens, es zu machen."

                "Atropos" "Und dann hatten Kloth und ich Chesis überzeugt doch ebenfalls hier anzufangen, weil er hier gute Chancen hat trotz seiner introvertierten Art."

                show era normal

                "Era" "Stimmt… es ist wirklich schwer mit ihm zu reden… ich hatte es ein paar Mal versucht und dann musste ich aufgegeben. Dir gegenüber ist er dagegen so offen."

                "Atropos" "Wir sind immerhin auch schon seit Ewigkeiten befreundet. Ich bin mir sicher, mit der Zeit wird er sich auch dir gegenüber mehr öffnen."

                show era shy

                "Era" "Das… das wäre sehr schön."

                show era shy_gray
                show narcais annoyed

                "Narcais" "Seid ihr fertig mit eurem Gespräch über nicht anwesende Personen? Ich bin auch noch da."

                "Atropos" "Wer könnte dich vergessen? (lacht)"

                show narcais cocky

                "Narcais" "Niemand, das ist mir bewusst!"

                show narcais normal

                "Narcais" "Jedenfalls: Ich habe einen Bericht verfasst, den du noch durcharbeiten müsstest."

                show narcais cocky

                "Narcais" "Ich bin mir sicher, dass er keine Fehler hat, immerhin habe ich ihn erstellt, aber so ist nun mal die Vorschrift."

                "Atropos" "Es ging um den Einfluss der Impfung auf Kinder und Jugendliche, richtig?"

                show narcais normal

                "Narcais" "Ja, genau. Und diesbezüglich: Ich habe einige…"

                "Atropos" "Können wir deinen Vortrag auf später verschieben? Ich muss noch etwas für Anan fertig zusammenstellen. Ich beschäftige mich später mit deinem Bericht."

                show narcais cocky

                "Narcais" "Ich bin froh zu hören, dass wenigstens eine Person hier meine Arbeit wertschätzt. Ich arbeite nun weiter."

                jump good_mood

        else:
            scene hall
            with fadeshort

            # Atropos Gedanken
            symb"Da vorne ist Anan… ich hoffe er bemerkt nichts."

            # Symbiont
            symb"{i}Du hättest die Pille sofort heute Morgen nehmen sollen. Dann müsstest du dir jetzt keine Gedanken mehr darüber machen. {/i}"

            # Symbiont
            symb"{i}Diese Sorgen sind doch nichts anderes als unnötiger Stress, der dein Glück verhindert. {/i}"

            # Symbiont
            # Symbiont
            symb"{i}Nimm die Pille jetzt ein! Werd wieder glücklich! Du hast es verdient, ein sorgenfreies Leben zu haben. {/i}"

            show anan normal_mid:
                xalign 0.5

            "Anan" "Guten Morgen und Glück für die Welt!"

            "Atropos" "Guten Morgen!"

            "Anan" "Atropos Laiotas- richtig? Kann ich die Liste heute noch von dir erwarten? Sie wird von meinen anderen Forschern benötigt."

            # Atropos Gedanken
            symb"Lass ihn nichts bemerken… bitte… ich darf nicht auffallen. Nicht vor ihm. Er gibt so viel für uns, ich darf ihn nicht enttäuschen."

            "Atropos" "Ja, natürlich, ich stelle sie dir heute fertig."

            show anan happy_mid

            "Anan" "Vielen Dank."

            show anan normal_mid

            "Anan" "…"

            show anan strict_mid

            "Anan" "Atropos. Du wirkst nicht glücklich, betrübt dich etwas?"

            # Atropos Gedanken
            symb"Hat er etwas gemerkt? Oder erkundigt er sich einfach nur höflichkeitshalber? Was soll ich tun? Verdammt…"

            # Symbiont
            symb"{i}Sag die Wahrheit und entschuldige dich. Nimm einfach die Happiness-Pille sofort wieder ein und alles kommt in Ordnung. {/i}"

            # Symbiont
            symb"{i} Vielleicht bist du ohne die Tablette ja doch nicht so glücklich wie du dachtest, wenn es Anan sofort aufgefallen ist. {/i}"

            menu:
                "Ich sollte besser lügen. Die Wahrheit würde ihm nicht gefallen.":

                    # Atropos Gedanken
                    symb"Ich sollte besser lügen. Die Wahrheit würde ihm nicht gefallen."

                    # Atropos Gedanken
                    symb"Ich will keinen Ärger dafür bekommen."

                    "Atropos" "Mir geht es gut. Ich bin glücklich dank Happiness!"

                    "Anan" "Deine Lüge ist offensichtlich."

                    "Anan" "Du hast Happiness in letzter Zeit nicht regelmäßig eingenommen."

                    jump afterlieortruthanan

                "Ich sollte die Wahrheit sagen.":

                    # Atropos Gedanken
                    symb"Ich sollte die Wahrheit sagen."

                    "Atropos" "Ich habe Happiness ein paar Mal vergessen, aber nicht weiter schlimm. Ich bin glücklich."

                    jump afterlieortruthanan

            label afterlieortruthanan:

                "Anan" "Ich erwarte dich in meinem Büro. Punkt elf und keine Sekunde zu spät!"

                "Anan" "Du gefährdest mit solchen Aktionen nicht nur dein eigenes Glück, sondern auch das Glück der Menschen, die dir am wichtigsten sind."

                show anan normal_mid

                "Anan" "Möchtest du das etwa?"

                "Atropos" "Nein… ich…"

                "Anan" "Die Menschheit braucht Happiness, sonst würde die Welt zurück ins Chaos fallen."

                show anan disappointed_mid

                "Anan" "Ich möchte nie wieder so etwas wie im Krieg damals erleben müssen. Kein Mensch sollte so etwas jemals wieder erleiden müssen."

                show anan normal_mid

                "Anan" "Ich habe jetzt zu tun, aber ich will dich später in meinem Büro sehen. Vergiss es nicht. Ich wünsche dir einen Tag voller Glücklichkeit."

                hide anan

                # Symbiont
                symb"{i}Anan hat Recht. Du solltest die Pille nehmen. Regelmäßig. Du willst doch glücklich sein. {/i}"

                # Atropos Gedanken
                symb"Ich… ah… ich weiß nicht was ich tun soll…"

                # Atropos Gedanken
                symb"Verdammt…"

                show screen force_mouse_move_threeoptions
                $ pillnottakenananhall = True
                menu:
                    "Anan hat ja recht...":
                        $ pillnottakenananhallananright = True
                        hide screen force_mouse_move_threeoptions
                        $ okaymood= True
                        jump anan_is_right
                    "Ich bin doch auch ohne Pille glücklich...":
                        $ pillnottakenananhallananwhy = True
                        hide screen force_mouse_move_threeoptions
                        jump why_important
                    "Was erlaubt sich Anan bitte? Ich lasse mir doch nichts vorschreiben…":
                        $ pillnottakenananhallananwrong = True
                        hide screen force_mouse_move_threeoptions
                        $ badmood= True
                        jump be_against

label anan_is_right:
    $ straight_office = True

    $ datewithera= True

    # Atropos Gedanken
    symb"Anan hat ja recht. Ich sehe es ein. Es war ein Fehler gewesen…"

    # Atropos Gedanken
    symb"Happiness hat es geschafft die Welt aus den Fängen des Krieges zu befreien. Ohne die Pille hätte der Krieg noch viel Jahre angedauert."
    # Atropos Gedanken
    symb"Ich wäre im Krieg geboren worden oder meine Eltern hätten mich vielleicht gar nicht erst bekommen."

    # Atropos Gedanken
    symb"Und wie Anan gesagt hat. Ohne die Tablette würde vermutlich auch jetzt die Welt wieder zurück ins Chaos fallen."

    # Atropos Gedanken
    symb"Was hatte ich mir nur dabei gedacht jemals zu zweifeln und zu zögern? Alle Menschen nehmen Happiness und alle, die Happiness nehmen, sind glücklich."

    # Atropos Gedanken
    symb"Ich werde diesen Fehler nicht noch einmal begehen. Zukünftig werde ich die Pille wieder regelmäßig einnehmen."

    # Atropos Gedanken
    symb"Ich werde nachher zu Anan gehen und mich für mein rücksichtloses Verhalten entschuldigen."

    # Atropos Gedanken
    symb"Aber jetzt erstmal zurück ins Labor. Ich habe noch einiges zu tun. Ich darf Anan nicht erneut enttäuschen."

    play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3
    scene lab
    with fadeshort

    "Atropos" "Hey Era."

    show era normal:
        xalign 0.5

    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

    "Era" "…"

    "Atropos" "…"

    show era shy

    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

    "Atropos" "Ja, natürlich… sorry…"

    play sound("Sound/Sounds/bump.mp3")

    show era confused

    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

    show era shy

    "Era" "Ich… ahhhh…"

    # Atropos Gedanken
    symb"Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

    # Atropos Gedanken
    symb"Zum Glück bekommt sie sich immer relativ rasch wieder in den Griff."

    "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen müsstest."

    show era confused

    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

    "Atropos" "Was wolltest du?"

    "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

    show era shy

    "Era" "…"

    show era normal

    "Era" "Was ich dich jedenfalls fragen wollte: Hast du nächste Woche Zeit? Ich dachte mir wir könnten uns vielleicht mal treffen?"

    # Atropos Gedanken
    symb"Das war bei ihr mal wieder eine 180 Grad Wendung. Manchmal frage ich mich…"


    # Symbiont
    symb"{i}Sie ist einfach ein wenig unsicher. Es wirkt, als würde sie sich für dich interessieren. Darum ist sie nervös und weiß nicht, wie sie sich dir gegenüber verhalten soll. {/i}"


    # Symbiont
    symb"{i}Du solltest sie ein wenig beruhigen. Du magst sie doch auch, gestehe es dir ein. {/i}"

    "Atropos" "Gerne, warum nicht? Passt dir Donnerstag? Wir könnten Bowlen gehen."

    show era happy

    "Era" "Wirklich? Ich… ja… ja… Donnerstag passt super!"

    show narcais normal:
        xalign 0.25
    show era happy_gray:
        xalign 0.75

    "Narcais" "Einen glücklichen guten Morgen zusammen! Habt ihr schon meine letzten Forschungsergebnisse gesehen? Ich kann mich selbst nur loben, sie sind hervorragend ausgefallen."

    show narcais normal_gray
    show era shy

    "Era" "G-Guten Morgen…"

    "Atropos" "Morgen… hattest du dich nicht mit dem Einfluss der Impfung auf Kinder und Jugendliche beschäftigt?"

    show era shy_gray
    show narcais cocky

    "Narcais" "Ja, genau. Und ich bin zu dem Schluss gekommen, dass wir es mit Glycohexatenol versuchen sollten."

    show narcais normal

    "Narcais" "Die Jugendlichen vertragen den alten Wirkstoff ebenfalls gut, aber nachweislich können wir keine Kinder damit impfen."

    "Narcais" "Dies birgt allerdings bekannter Weise hohe Risiken, weil die Umweltverschmutzungen durch den Krieg auch Kinder betreffen können."

    "Narcais" "Auch ist die Impfung eine Grundvoraussetzung für die Einnahme der Happiness-Pille. Bereits jetzt leiden viel zu viele Kinder unter der späten Einnahme."

    show narcais cocky

    "Narcais" "Die Kinder sollten ebenfalls in der Lage sein eine glückliche Kindheit führen zu dürfen! Wenn ich an meine eigene Kindheit denke…"

    "Atropos" "Narcais- du zählst nur Fakten auf, die bereits bekannt sind. Was ist jetzt mit dem Glycohexatenol?"

    # Atropos Gedanken
    symb"Er nutzt wirklich jede Chance, um mit seinem Wissen zu prahlen…"

    show narcais normal

    "Narcais" "Ich habe die Erkenntnis gewonnen, dass der Wirkstoff die Durchführung der Impfung um einige Jahre vorverlegen dürfte."

    "Narcais" "Diesbezüglich hatte ich einige Forschungen durchgeführt, welche meine Erkenntnis belegt hatten."

    show narcais cocky

    "Narcais" "Ich habe bereits einen umfassenden Bericht dazu verfasst und dir geschickt. Aber du musst vermutlich nur einen kurzen Blick darauf werfen…"

    show narcais normal

    "Narcais" "Du weißt, dass ich immer beste Arbeit abliefere und keine Fehler mache."

    "Atropos" "Danke, ich beschäftige mich später damit."

    show narcais cocky

    "Narcais" "Ja, natürlich. Lass dir Zeit. Nicht jeder kann so schnell und effizient arbeiten wie ich…"

    hide narcais

    "Atropos" "Sorry für die Unterbrechung, Era. Also, wir schreiben dann einfach die Tage, okay?"

    show era happy

    "Era" "J-Ja… natürlich. Danke Atropos!"

    hide era

    # Atropos Gedanken
    symb"Zurück an die Arbeit."

    "Atropos" "…"

    play sound ("<from 0 to 5>Sound/Music/Rooms/verkaufsraum.mp3") fadeout 3

    "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"

    "Durchsage" "{i}Nimm Happiness ein und lebe dein Leben so wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit. {/i}"

    "Durchsage" "{i}In wenigen Minuten erfolgt eine Übertragung von Anan. Bitte schaltet die entsprechenden Bildschirme ein. {/i}"

    show era normal

    "Era" "Ich… ich kümmere mich darum!"

    hide era

    # für den Fall, dass Atropos sich davor mit Neiro darüber unterhalten hat

    if neiro_unterhalten:
        symb"Das muss die Übertragung sein, die Neiro vorhin erwähnt hatte."

        # Atropos Gedanken
        symb"Ob er wohl mit allen Informationen Recht hatte?"

    stop music

    $ renpy.movie_cutscene("cutscenes/logodrehend.mpg")

    # ab hier wieder alle
    scene screen_background
    with fadeshort
    show screen_transparent
    show atlas normal_small behind screen_transparent:
        xalign 0.12
    show adres normal_small behind screen_transparent:
        xalign 0.8
    show anan normal_left_small behind screen_transparent:
        xalign 0.4

    play music "Sound/Music/Rooms/AnansBuero/anans_buero_normal.mp3" fadeout 3 fadein 3

    "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag."

    show anan happy_left_small

    "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

    show anan normal_left_small

    "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

    "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

    show anan happy_left_small

    "Anan" "Der Gründungstag von Aither."

    "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

    "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

    show anan normal_left_small

    "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

    show anan happy_left_small

    "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

    "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

    "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

    show anan normal_left_small

    "Anan" "Ich bin bereit, alles dafür zu geben, und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

    "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

    show anan disappointed_left_small

    "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

    show anan normal_left_small

    "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

    "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

    show anan happy_left_small

    "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

    "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

    "Anan" "Weil ihr uns dabei helft, das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die Ersten, die die neue Happiness erhalten."

    "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

    "Anan" "Vergesst niemals: Happiness. Euer Leben. Eure Entscheidung. Eure Glücklichkeit."

    show anan normal_left_small

    "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

    "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns hinterlassen haben."

    "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

    play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

    scene lab
    with fadeshort
    show era normal:
        xalign 0.25
    show narcais normal_gray:
        xalign 0.75

    "Era" "Wow…"

    show era normal_gray
    show narcais normal

    "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

    # Atropos Gedanken
    symb"Und das von jemandem, der sich selbst am liebsten den ganzen Tag zuhört."

    # Atropos Gedanken
    symb"Aber ich muss ihnen schon recht geben. Seine Rede war beeindruckend wie immer."

    # Atropos Gedanken
    symb"Und Anan hat vermutlich ebenfalls recht. Ich weiß ja, dass er nur das Beste für uns will…"

    show narcais normal_gray
    show era normal

    "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

    "Atropos" "Ja, das ist er wohl. "

    "Atropos" "Jetzt sollten wir aber zurück an die Arbeit, wir müssen heute noch einiges schaffen."

    "Atropos" "…"

    # Atropos Gedanken
    symb"Oh, es ist schon spät. Ich muss langsam los, damit ich pünktlich bei Anans Büro bin."

    "Atropos" "Bin gleich wieder da."

    show era happy

    "Era" "Bis… bis später!"


    jump go_office

label why_important:
    $ straight_office = True

    # Atropos Gedanken
    symb"Ich bin doch auch ohne Pille glücklich…"

    # Atropos Gedanken
    symb"Oder? Irre ich mich etwa? Denke ich nur selbst, dass ich glücklich bin, aber alle anderen erkennen die Wahrheit?"

    # Atropos Gedanken
    symb"Mache ich mir nur etwas vor?"

    # Atropos Gedanken
    symb"Bin ich wirklich glücklich?"

    # Atropos Gedanken
    symb"Was ist, wenn Anan recht hat? Gefährde ich durch meine Aktionen auch das Glück der anderen?"

    # Atropos Gedanken
    symb"Ist Kloth deswegen in letzter Zeit so seltsam drauf?"

    # Atropos Gedanken
    symb"Ist alles etwa meine Schuld?"

    # Symbiont
    symb"{i}Nein, mache dir darüber jetzt keine Gedanken oder Vorwürfe! Jeder macht mal Fehler, aber du hast eine Chance erhalten diesen Fehler auszubessern. {/i}"


    # Symbiont
    symb"{i}Nutze diese Chance und mache jetzt alles richtig! {/i}"

    # Symbiont
    symb"{i}Nimm die Pille und zeig der Welt wie glücklich du bist! Beweise allen, dass auch du vollkommen glücklich sein kannst. {/i}"

    # Atropos Gedanken
    symb"Ich weiß nicht… das alles ist so… schwierig… Was soll ich nur denken? Was soll ich nur tun?"

    # Atropos Gedanken
    symb"Vermutlich sollte ich jetzt erstmal ins Labor zurück, damit ich Anan nicht erneut enttäusche… dann sehe ich weiter…"

    play music "Sound/Music/Rooms/Labor/labor_duester.mp3" fadeout 3 fadein 3
    scene lab
    with fadeshort

    "Atropos" "Hey Era."

    show era normal:
        xalign 0.5

    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

    "Era" "…"

    "Atropos" "…"

    show era shy

    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

    "Atropos" "Ja, natürlich… sorry…"

    play sound("Sound/Sounds/bump.mp3")

    show era confused

    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

    show era shy

    "Era" "Ich… ahhhh…"

    # Atropos Gedanken
    symb"Era ist wirklich süß, aber ihre Mischung aus Tollpatschigkeit und Unsicherheit kann auch ziemlich anstrengend sein."

    # Atropos Gedanken
    symb"Ich habe gerade vor allem andere Sorgen."

    "Atropos" "Alles in Ordnung. Es war nur ein Missgeschick, nichts worüber du dir Gedanken machen müsstest."

    show era confused

    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

    "Atropos" "Was wolltest du?"

    "Era" "Ich… ich wollte dich fragen… Zeit… du… nächste Woche… ahhh…"

    show era shy

    "Era" "…"

    show era normal

    "Era" "Was ich dich jedenfalls fragen wollte…"

    "Era" "…"

    "Atropos" "Was? Tut mir leid… ich war gerade etwas in Gedanken versunken."

    show era shy

    "Era" "Ich… ach… egal, vergiss es. Es war nicht so wichtig."

    "Era" "D-Du wirkst als würde dich etwas beschäftigen. Ich... ich sage es dir, wenn du den Kopf dafür hast."

    "Atropos" "Okay."

    show era confused

    "Era" "Aber sag mal Atropos… I-Ist alles in Ordnung? Dich scheint etwas zu beschäftigen…"

    # Narcais taucht auf
    show narcais normal:
        xalign 0.25
    show era confused_gray:
        xalign 0.75

    "Narcais" "Einen glücklichen guten Morgen zusammen. Was habe ich verpasst? Redet ihr über mich?"

    show narcais normal_gray
    show era normal

    "Era" "G-Guten Morgen… Nein… es ging um Atropos. Ihn scheint etwas zu beschäftigen. Er wirkt nicht glücklich…"

    show era normal_gray
    show narcais cocky

    "Narcais" "Ach, mich beschäftigen auch immer tausend Dinge. Das ist doch nichts ungewöhnliches."

    show narcais normal

    "Narcais" "Jedenfalls: Ich habe einen Bericht verfasst, den du noch durcharbeiten müsstest, Atropos."

    show narcais cocky

    "Narcais" "Ich bin mir sicher, dass er keine Fehler hat, immerhin habe ich ihn erstellt, aber so ist nun mal die Vorschrift."

    "Atropos" "Ich kümmere mich darum."

    show narcais cocky_gray
    show era confused

    "Era" "Können… können wir dir irgendwie helfen? Was ist vorgefallen?"

    menu:
        "Ich sollte mich ihnen anvertrauen.":
            # Atropos Gedanken
            symb"Ich sollte mich ihnen anvertrauen."

            "Atropos" "Ich hatte in letzter Zeit ein paar Mal meine Pille vergessen und bin vorhin Anan über den Weg gelaufen."

            "Atropos" "Er hatte es sofort bemerkt und mir einen Vortrag über die Wichtigkeit der Happiness-Pille gehalten und ich muss nachher noch in sein Büro…"

            "Atropos" "Aber ich bin doch auch ohne sie glücklich… warum muss ich sie um jeden Preis einnehmen?"

            "Atropos" "Außerdem… muss Anan wirklich so einen Aufstand darum machen, dass ich sie Mal vergessen habe, oder keine Lust hatte sie zu nehmen?"

            "Atropos" "Und eigentlich wollte ich Anan niemals enttäuschen… nicht nach allem, was er für uns getan hat…"

            "Atropos" "Ich weiß einfach nicht, was ich tun soll."

            show era confused_gray
            show narcais normal

            "Narcais" "Ich kann Anan verstehen. Happiness ist nun mal unglaublich wichtig. Wie kannst du so etwas Wichtiges nur vergessen?"

            show narcais annoyed

            "Narcais" "Wie kannst du so egoistisch sein? Damit gefährdest du nicht nur dein Glück, sondern unser aller Glück."

            show narcais annoyed_gray
            show era normal

            "Era" "Atropos… mach dir bitte keine Vorwürfe, okay?"

            show era confused

            "Era" "Aber ich muss Narcais zustimmen. Happiness ist wichtig… du solltest die Pille nehmen und dich bei Anan dafür entschuldigen."

            "Era" "Und… und… denk bitte an dein eigenes Glück. Ich will, dass du glücklich bist… du… du bedeutest mir…"

            show era shy

            "Era" "…"

            "Era" "Bitte pass gut auf dich auf, Atropos."

            play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

            "Atropos" "Danke. Ihr habt ja recht. Ich werde nachher zu Anan gehen und das Ganze klären."

            "Atropos" "Jetzt sollten wir aber erst einmal mit der Arbeit anfangen."

            show era shy_gray
            show narcais normal

            "Narcais" "Vergiss meinen Bericht nicht!"

            "Atropos" "(lacht) Keine Sorge, das könnte ich niemals."

            hide era
            hide narcais

            jump openyourheartornot

        "Ich will nicht darüber sprechen.":
            # Atropos Gedanken
            symb"Ich will nicht darüber sprechen."

            "Atropos" "Ich erzähle euch ein anderes Mal davon..."

            show era shy

            "Era" "J-Ja... natürlich."

            show era shy_gray
            show narcais normal

            "Narcais" "Vergiss meinen Bericht aber nicht!"

            "Atropos" "(lacht) Keine Sorge, das könnte ich niemals."

            hide era
            hide narcais

            jump openyourheartornot



    label openyourheartornot:
        # Atropos Gedanken
        symb"Zurück an die Arbeit."

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
            symb"Das muss die Übertragung sein, die Neiro vorhin erwähnt hatte."

            # Atropos Gedanken
            symb"Ob er wohl mit allen Informationen Recht hatte?"

        stop music

        $ renpy.movie_cutscene("cutscenes/logodrehend.mpg")

        # ab hier wieder alle
        scene screen_background
        with fadeshort
        show screen_transparent
        show atlas normal_small behind screen_transparent:
            xalign 0.12
        show adres normal_small behind screen_transparent:
            xalign 0.8
        show anan normal_left_small behind screen_transparent:
            xalign 0.4

        play music "Sound/Music/Rooms/AnansBuero/anans_buero_normal.mp3" fadeout 3 fadein 3

        "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag."

        "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

        show anan disappointed_left_small

        "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

        show anan normal_left_small

        "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

        show anan happy_left_small

        "Anan" "Der Gründungstag von Aither."

        "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

        show anan normal_left_small

        "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

        show anan happy_left_small

        "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

        "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

        "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

        "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

        show anan normal_left_small

        "Anan" "Ich bin bereit, alles dafür zu geben, und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

        "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

        "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

        show anan happy_left_small

        "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

        "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

        "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

        "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

        "Anan" "Weil ihr uns dabei helft, das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die Ersten, die die neue Happiness erhalten."

        "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

        "Anan" "Vergesst niemals: Happiness. Euer Leben. Eure Entscheidung. Eure Glücklichkeit."

        show anan normal_left_small

        "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

        "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns hinterlassen haben."

        "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

        play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

        scene lab
        with fadeshort
        show era normal:
            xalign 0.25
        show narcais normal_gray:
            xalign 0.75

        "Era" "Wow…"

        show era normal_gray
        show narcais normal

        "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

        # Atropos Gedanken
        symb"Und das von jemandem, der sich selbst am liebsten den ganzen Tag zuhört."

        # Atropos Gedanken
        symb"Aber ich muss ihnen schon recht geben. Seine Rede war beeindruckend wie immer."

        # Atropos Gedanken
        symb"Ich frage mich, ob Anan mit seiner Rede wirklich recht hat? Es wirkt alles so plausibel und klar, wenn er es erzählt…"

        # Atropos Gedanken
        symb"Und dennoch… ich wüsste zu gerne was die Tablette tatsächlich bewirkt. Wie sie uns überhaupt unser Glück bringt."

        # Atropos Gedanken
        symb"Vielleicht würde es mir dann leichter fallen, sie zu nehmen. Vielleicht würde ich dann weniger zweifeln."

        show narcais normal_gray
        show era normal

        "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

        "Atropos" "Ja, das ist er wohl. "

        "Atropos" "Jetzt sollten wir aber zurück an die Arbeit, wir müssen heute noch einiges schaffen."

        # Bildschirm wird schwarz und blendet dann wieder auf. Erneut ins Labor.

        "Atropos" "…"

        # Atropos Gedanken
        symb"Oh, es ist schon spät. Ich müsste langsam los, wenn ich pünktlich in Anans Büro sein will…"

        # Atropos Gedanken
        symb"Ich sollte besser gehen. Vielleicht hilft es mir ja Mal mit Anan über meine Zweifel und Sorgen zu sprechen."

        # Atropos Gedanken
        symb"Ich möchte nicht Zweifeln… ich möchte einfach nur glücklich sein…"

        "Atropos" "Bin gleich wieder da."

        show era happy

        "Era" "Bis… bis später!"


        jump go_office

label be_against:
    $ straight_office = False

    # Atropos Gedanken
    symb"Was erlaubt sich Anan bitte? Ich lasse mir doch nicht vorschreiben, ob und wie oft ich die Happiness-Pille einnehmen soll!"

    # Atropos Gedanken
    symb"Ich weiß ja, dass er die Welt vom Krieg erlöst hat, aber das ist ganz allein meine Entscheidung! Ich sollte über mein eigenes Glück bestimmen können."

    # Atropos Gedanken
    symb"Keiner sollte mir vorgeben dürfen, wie ich zu meinem Glück kommen soll!"

    # Symbiont
    symb"{i}Nimm die Pille. Merkst du denn nicht, dass du mit jeder Sekunde unglücklicher wirst? {/i}"

    # Symbiont
    symb"{i}Denk nochmal nach, was du gerade alles gedacht hast. Bist das wirklich du? {/i}"

    # Symbiont
    symb"{i}Das ist nicht mehr der Atropos, der du sein willst, oder? {/i}"

    # Symbiont
    symb"{i}Du warst mal glücklich gewesen, aber gerade stößt du dich selbst und die, die du liebst ins Unglück. {/i}"

    # Symbiont
    symb"{i}Bist du gerade, ohne die Happiness-Pille, wirklich glücklich? {/i}"

    # Atropos Gedanken
    symb"Ja! Ja, ich bin glücklich!"

    # Symbiont
    symb"{i}Das nennst du Glück? Du bist gerade wirklich glücklich? Es gibt nichts, dass dir Sorgen oder Kopfzerbrechen bereitet? {/i}"

    "Atropos" "Ich bin glücklich."

    "Atropos" "Ich bin glücklich."

    "Atropos" "Ich bin glücklich!"

    "Atropos" "Und Anan kann mir das nicht nehmen! Er kann mich nicht zwingen!"# Ich werde nicht zu ihm gehen, das kann er vergessen!"

    # Atropos Gedanken
    symb"Aber jetzt erstmal weiter ins Labor…"

    play music "Sound/Music/Rooms/Labor/labor_duester.mp3" fadeout 3 fadein 3


    scene lab
    with fadeshort

    show era normal:
        xalign 0.5

    "Era" "Atropos? Du bist hier? Oh… ich… guten Morgen…"

    "Era" "…"

    "Atropos" "…"

    show era shy

    "Era" "Ich… darf ich kurz vorbei? Ich… ich muss zu meinem Arbeitsplatz da drüben."

    "Atropos" "Ja, sorry …"

    play sound("Sound/Sounds/bump.mp3")

    show era confused

    "Era" "Ich… oh nein, es tut mir so leid… das wollte ich nicht. Habe ich dich verletzt? Das… ich… es ist aus Versehen passiert…"

    show era shy

    "Era" "Ich… ahhhh…"

    # Atropos Gedanken
    symb"Musste das jetzt sein? Ich mag Era echt gerne, aber ihre Tollpatschigkeit kann wirklich nerven."

    "Atropos" "Mir geht es gut."

    show era confused

    "Era" "Trotzdem… das wollte ich nicht… und dabei wollte ich doch… ich wollte dich…"

    "Atropos" "Era, sorry, aber mir ist gerade nicht nach einem Gespräch. Können wir das auf später verschieben?"

    show era shy

    "Era" "..."

    show era happy

    "Era" "Ja, natürlich. Gerne! Wir reden, wenn du wieder glücklicher bist!"

    "Era" "Ich arbeite dann mal weiter."

    # Era verschwindet, Narcais taucht auf
    hide era
    show narcais normal:
        xalign 0.5

    "Narcais" "Atropos, ich habe den Bericht…"

    menu:
        "Ich unterbreche ihn, sonst redet er ewig.":

            # Atropos Gedanken
            symb"Ich unterbreche ihn, sonst redet er ewig."

            "Atropos" "Jetzt nicht… ich habe zu tun, siehst du das nicht?"

            show narcais annoyed

            "Narcais" "Was? Aber… du wolltest doch den Bericht durchlesen, den ich geschrieben habe."

            "Atropos" "Jetzt nicht!"

            show narcais normal

            jump afternarcaistalk

        "Ich lasse ihn aussprechen, aber verschiebe den Bericht auf später.":
            # Atropos Gedanken
            symb"Ich lasse ihn aussprechen, aber verschiebe den Bericht auf später."

            "Narcais" "… fertiggestellt. Schaust du ihn dir an? Es sollten keine Fehler drinnen sein, immerhin kommt er von mir."

            "Atropos" "Ich kümmere mich später darum, ich habe gerade zu tun."

            jump afternarcaistalk

    label afternarcaistalk:
        "Narcais" "Klar, kein Problem! Les ihn dir durch, sobald du dazu kommst."

        show narcais cocky

        "Narcais" "Du solltest ohnehin nicht viel damit zu tun haben. Ich weiß, dass ich perfekte Arbeit liefere- das ist eine allgemein bekannte Tatsache."

        # Atropos Gedanken
        symb"Er ist echt stark von sich eingenommen. Ich kann weder ihn noch Era gerade ertragen…"

        # Atropos Gedanken
        symb"Kann ich nicht mal eine Sekunde für mich haben, damit ich in Ruhe nachdenken kann?"

        # Atropos Gedanken
        symb"Natürlich kann ich so nicht vollkommen glücklich sein…"

        "Atropos" "Ich kümmere mich darum."

        # Narcais verschwindet.
        hide narcais

        # Atropos Gedanken
        symb"Endlich ein wenig Ruhe."

        # Atropos Gedanken
        symb"Ich werde mich nachher mit allem beschäftigen. Jetzt sollte ich erst einmal mit der Arbeit anfangen."

        "Atropos" "…"

        "Durchsage" "{i}Lebe glücklich. Erfülle deinen Traum. Dein Leben ist dein Traum. Deine Träume werden wahr. {/i}"

        "Durchsage" "{i}Nimm Happiness ein und lebe dein Leben so wie du willst. Happiness, dein Leben, deine Entscheidung, deine Glücklichkeit. {/i}"

        "Durchsage" "{i}In wenigen Minuten erfolgt eine Übertragung von Anan. Bitte schaltet die entsprechenden Bildschirme ein. {/i}"

        show era normal:
            xalign 0.5

        "Era" "Ich… ich kümmere mich darum!"
        hide era

        stop music

        $ renpy.movie_cutscene("cutscenes/logodrehend.mpg")

        scene screen_background
        with fadeshort
        show screen_transparent
        show atlas normal_small behind screen_transparent:
            xalign 0.12
        show adres normal_small behind screen_transparent:
            xalign 0.8
        show anan normal_left_small behind screen_transparent:
            xalign 0.4

        play music "Sound/Music/Rooms/AnansBuero/anans_buero_normal.mp3" fadeout 3 fadein 3

        # Bild wechselt von Laborhintergrund in Nahansicht des Bildschirms. Atlas, Anan und Adrés tauchen nebeneinander auf

        "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag."

        "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

        show anan disappointed_left_small

        "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

        show anan normal_left_small

        "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

        show anan happy_left_small

        "Anan" "Der Gründungstag von Aither."

        "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

        show anan normal_left_small

        "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

        show anan happy_left_small

        "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

        "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

        "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

        "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

        show anan normal_left_small

        "Anan" "Ich bin bereit, alles dafür zu geben, und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

        "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

        "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

        show anan happy_left_small

        "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

        "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

        "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

        "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

        "Anan" "Weil ihr uns dabei helft, das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die Ersten, die die neue Happiness erhalten."

        "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

        "Anan" "Vergesst niemals: Happiness. Euer Leben. Eure Entscheidung. Eure Glücklichkeit."

        show anan normal_left_small

        "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

        "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns hinterlassen haben."

        "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

        play music "Sound/Music/Rooms/Labor/labor_duester.mp3" fadeout 3 fadein 3


        scene lab
        with fadeshort
        show era normal:
            xalign 0.25
        show narcais normal_gray:
            xalign 0.75

        # Übertragung wird beendet und der Labor ist wieder im Hintergrund.

        "Era" "Wow…"

        show era normal_gray
        show narcais normal

        "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

        # Atropos Gedanken
        symb"Schöne Worte und nichts dahinter…"

        # Atropos Gedanken
        symb"Wieso mussten wir uns diesen Unsinn anhören?"

        # Atropos Gedanken
        symb"Warum überlässt Anan nicht uns die Wahl, ob wir die Pille nehmen wollen oder nicht?"

        # Atropos Gedanken
        symb"Vielleicht würde es mir dann leichter fallen sie zu nehmen. Vielleicht würde ich dann weniger zweifeln."

        # Symbiont
        symb"{i} Diese Gedanken hast du nur, weil du nicht glücklich bist. Nimm die Pille und werde wieder glücklich! {/i}"

        # Symbiont
        symb"{i} Merkst du nicht, wie deine Zweifel dich innerlich zerfressen? {/i}"

        # Symbiont
        symb"{i}Ist es das, was du willst? Du bist unglücklich, Atropos. Kein Mensch sollte unglücklich sein. {/i}"

        show narcais normal_gray
        show era normal

        "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf, an das Glück aller Menschen zu denken."

        "Atropos" "Wir sollten zurück an die Arbeit, wir müssen heute noch einiges schaffen."

        "Atropos" "…"

        # Atropos Gedanken
        symb"Es ist schon spät. Ich müsste jetzt los, um pünktlich bei Anan zu sein."

        # Atropos Gedanken
        symb"Aber will ich das überhaupt?"

        # Symbiont
        symb"{i}Du willst pünktlich sein. Anan war noch nett und verständnisvoll, aber das wird sich ändern, wenn du weiterhin dein Glück und das Glück aller gefährdest. {/i}"

        # Symbiont
        symb"{i}Wieso wehrst du dich so verzweifelt gegen dein Glück? Niemand will dir Leid zufügen. Alle wollen nur dein Bestes. {/i}"

        # Symbiont
        symb"{i}Besänftige deinen Zorn! Anan sorgt sich um dich. Geh zu ihm und entschuldige dein Verhalten! {/i}"

        # Symbiont
        symb"{i}Alles kann gut werden, wenn du es nur willst. {/i}"

        jump go_office

label go_office:

    if straight_office:
        jump office

    else:
        show screen force_mouse_move_twooptions
        $ gotoananofficeornot = True
        menu:
            "Ich sollte besser zu Anans Büro gehen.":
                $ gotoananofficeornotyes = True
                play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

                hide screen force_mouse_move_twooptions
                # Atropos Gedanken
                symb"Vermutlich ist es besser, wenn ich zu Anan gehe. Ich will keinen Ärger bekommen. Nicht auch noch dafür."

                # Atropos Gedanken
                symb"Vielleicht kann er mir ja auch ein paar Antworten geben… warum es so wichtig ist die Pille zu nehmen. Was passiert, wenn ich sie ein paar Tage nicht nehme…"

                # Atropos Gedanken
                symb"Ich denke, ich habe vorhin vielleicht etwas überreagiert… Ich sollte mir davon nicht die Laune verderben lassen."

                # Atropos Gedanken
                symb"Immerhin treffe ich nachher noch Kloth und Chesis zum Grillen. Für den Moment sollte ich mich darauf fokussieren."

                # Atropos Gedanken
                symb"Und jetzt sollte ich wirklich los. Sonst komme ich noch zu spät. Ich sollte Anan nicht warten lassen."

                "Atropos" "Bin gleich wieder da."

                show era happy

                "Era" "Bis… bis später!"

                jump office
            "Ich werde auf keinen Fall zu Anans Büro gehen.":
                $ gotoananofficeornotno = True
                hide screen force_mouse_move_twooptions
                jump no_office

label good_mood:

    hide era
    hide narcais
    symb"Zurück an die Arbeit."

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
        symb"Das muss die Übertragung sein, die Neiro vorhin erwähnt hatte."

        # Atropos Gedanken
        symb"Ob er wohl mit allen Informationen recht hatte?"

    stop music

    $ renpy.movie_cutscene("cutscenes/logodrehend.mpg")
    scene screen_background
    with fadeshort
    show screen_transparent
    show atlas normal_small behind screen_transparent:
        xalign 0.15
    show adres normal_small behind screen_transparent:
        xalign 0.85
    show anan normal_left_small behind screen_transparent:
        xalign 0.40

    play music "Sound/Music/Rooms/AnansBuero/anans_buero_normal.mp3" fadeout 3 fadein 3

    "Anan" "Ich hoffe, ihr alle hattet heute bisher einen glücklichen Tag."

    "Anan" "An meiner Seite befinden sich Atlas und Adrés. Zwei Namen, die euch nicht ganz unbekannt sein dürften."

    show anan disappointed_left_small

    "Anan" "Aufgrund der instabilen Verbindung werden sie nicht persönlich zu euch sprechen können, aber ich spreche heute im Namen von uns allen zu euch."

    show anan normal_left_small

    "Anan" "Ich bin mir sicher, keiner von euch hat vergessen, was sich in nicht einmal einem Monat zum 37. Mal jähren wird."

    show anan happy_left_small

    "Anan" "Der Gründungstag von Aither."

    "Anan" "Und in diesem Jahr fällt der Gründungstag mit einem ganz besonderen Ereignis zusammen."

    show anan normal_left_small

    "Anan" "Die Happiness-Pille ist noch nicht vollkommen. Sie ist in einer stetigen Weiterentwicklung, damit die Menschheit eines Tages perfektes Glück erfahren darf."

    show anan happy_left_small

    "Anan" "Und diesem perfekten Glück sind wir einen Schritt nähergekommen."

    "Anan" "Die neue Tablette wird stärker sein, besser sein, glücklicher machen. Niemand muss mehr in der Angst leben, sie einmal zu vergessen und dadurch sein Glück zu verlieren."

    "Anan" "Ich verspreche es euch. Die Menschheit wird niemals wieder das erleiden müssen, was in der Vergangenheit vorgefallen ist."

    "Anan" "Eines Tages werden wir das Glück erreichen, was jeder einzelne Mensch verdient hat. Perfekten Frieden und perfekte Glücklichkeit."

    show anan normal_left_small

    "Anan" "Ich bin bereit, alles dafür zu geben, und gemeinsam können wir diesen Traum erreichen. Diese perfekte, heile Welt."

    "Anan" "Atlas und Adrés sind meine Mitstreiter, seit sie mich im Krieg gerettet haben. Sie retteten mich, obwohl wir damals auf unterschiedlichen Seiten standen."

    "Anan" "Das öffnete mir meine Augen und ließ mich erkennen, dass all der Krieg sinnlos war. Dass das nicht die Lösung war, nach der wir streben sollten."

    show anan happy_left_small

    "Anan" "Stattdessen sollten wir nach Glück streben. Denn Glück ist es, was das höchste Ziel des Individuums ist. "

    "Anan" "Glück ist alles, was der Mensch in seinem Leben braucht. Ohne Glück verliert das Leben seinen Wert und seinen Sinn. "

    "Anan" "Um diesen Triumph in unserem langen, beschwerlichen Weg auf der Suche nach Glück zu feiern, werden Adrés und Atlas zum Gründungstag nach Astoa reisen. "

    "Anan" "Ihr seid alle herzlich eingeladen, diesen Triumph auszukosten und an dem berauschenden Fest teilzunehmen, welches Aither in gesamt Astoa ausrichten wird. "

    "Anan" "Weil ihr uns dabei helft, das Glück unter die Menschen zu bringen, werdet ihr natürlich dafür belohnt. Ihr seid die Ersten, die die neue Happiness erhalten."

    "Anan" "Verteilt das Glück. Bringt anderen Glück. Seid selbst glücklich! Lebt, sodass ihr glücklich seid! Macht die Welt zu einem besseren Ort!"

    "Anan" "Vergesst niemals: Happiness. Euer Leben. Eure Entscheidung. Eure Glücklichkeit."

    show anan normal_left_small

    "Anan" "Ich danke euch für eure wertvolle Zeit. Lasst uns für die Glücklichkeit kämpfen! Lasst uns für unser eigenes Glück kämpfen! Aither wird euch stets bei diesem Kampf unterstützen!"

    "Anan" "Ihr seid der Rest der Menschheit. Wir müssen überleben und unseren Nachkommen eine heile, gute Welt überlassen. Nicht die Trümmer, welche unsere Vorfahren uns hinterlassen haben."

    "Anan" "Also kämpft an meiner Seite und lasst uns die Welt verändern!"

    play music "Sound/Music/Rooms/Labor/labor_sorglos.mp3" fadeout 3 fadein 3

    scene lab
    with fadeshort

    show era normal:
        xalign 0.25
    show narcais normal_gray:
        xalign 0.75

    "Era" "Wow…"

    show era normal_gray
    show narcais normal

    "Narcais" "Man könnte ihm den ganzen Tag zuhören ohne müde zu werden…"

    # Atropos Gedanken
    symb"Und das von jemandem, der sich selbst am liebsten den ganzen Tag zuhört."

    "Atropos" "Dieser Mann ist wirklich unglaublich… Man spürt mit jeder Faser seines Körpers, wie wichtig ihm das Wohl aller Menschen ist."

    show narcais normal_gray
    show era normal

    "Era" "Er… er ist wirklich beeindruckend… Er hat so viel in seinem Leben erreicht und dennoch hört er nie auf an das Glück aller Menschen zu denken."

    "Atropos" "Ich frage mich, welchen Preis er wohl dafür bezahlen muss?"

    show era normal_gray
    show narcais normal

    "Narcais" "Egal wie hoch er auch sein mag. Ich bin mir sicher, dass Anan nicht eine Sekunde zögert, diesen zu bezahlen."

    "Atropos" "Jetzt sollten wir aber zurück an die Arbeit, wir müssen heute noch einiges schaffen."


    jump pill

label no_office:

    # Atropos Gedanken
    symb"Nein! Auf keinen Fall, ich werde nicht nachgeben, nur weil Anan eine gute Rede gehalten hat."

    # Atropos Gedanken
    symb"Mir ist es egal, was die Konsequenzen sind, ich werde mich nicht weiter dazu zwingen lassen, Happiness zu nehmen."
    # Atropos Gedanken
    symb"Es ist meine freie Entscheidung wie ich zu meinem eigenen Glück gelangen will. Keiner kann mich zwingen, dieses Glück über Happiness zu erreichen."
    # Symbiont
    symb"{i}Letztlich wirst du das Glück nur über Happiness erreichen können. {/i}"

    # Atropos Gedanken
    symb"Ich nehme die Pille wann und wenn ich will!"

    # Symbiont
    symb"{i}Du solltest sie jetzt und hier nehmen. {/i}"

    # Atropos Gedanken
    symb"Und jetzt zurück an die Arbeit. Zumindest der Bericht für Anan sollte heute fertig werden."

    "Atropos" "…"

    "Durchsage" "{i}Atropos Laiotas. Dein Glück erwartet dich! Finde dich umgehend im Büro von Anan ein. {/i}"

    $ loudspeaker = True

    menu:
        "Ich werde die Durchsage einfach überhören.":
            jump stillnooffice

        "Ich sollte gehen.":

            # Atropos Gedanken
            symb"Ich sollte gehen."

            # Atropos Gedanken
            symb"Ich kann mir ja mal anhören, was er zu sagen hat und dann weitersehen…"

            scene hall
            with fadeshort

            jump rueffel


    label stillnooffice:

        # Atropos Gedanken
        symb"Ich werde die Durchsage einfach überhören."

        show narcais normal

        "Narcais" "Atropos, deine Anwesenheit wird verlangt. Wieso reagierst du nicht? Du solltest dich geehrt fühlen, in Anans Büro gerufen zu werden!"

        show narcais normal_gray
        show era confused

        "Era" "Was will er von dir, Atropos?"

        "Durchsage" "{i}Atropos Laiotas. Dein Glück erwartet dich! Finde dich umgehend im Büro von Anan ein. Er erwartet dich.{/i}"

        # Atropos Gedanken
        symb"Sieht so aus, als würde mir keine andere Wahl bleiben… Ich möchte auch nicht unter meinen Kollegen deswegen seltsam auffallen."

        # Atropos Gedanken
        symb"Ich hoffe die anderen denken jetzt nicht schlecht von mir… und muss Anan das gleich über die Lautsprecher durchsagen lassen?"

        # Atropos Gedanken
        symb"Das muss echt nicht jeder mitbekommen…"

        # Atropos Gedanken
        symb"Aber ich kann mir ja mal anhören, was er zu sagen hat und dann weitersehen…"

        show era confused_gray
        show narcais confused

        "Narcais" "Atropos?"

        "Atropos" "Schon gut, schon gut."

        "Atropos" "Ich geh ja schon."

        scene hall
        with fadeshort

        jump rueffel

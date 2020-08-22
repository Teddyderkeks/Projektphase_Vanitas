default back_to_work_bevore = False

label back_to_work:
    $ back_to_work_bevore = True
    # Atropos Gedanken
    symb"So… zurück an die Arbeit. Ich muss die Pille nehmen."

    # Atropos Gedanken
    symb"Auch wenn ich mich immer noch frage, wie sie überhaupt wirkt…"


    scene stairs_up
    with fadeshort

    # Atropos Gedanken
    symb"Aber apropos Pille. Sind die Werbeplakate für diese neu?"
    scene detail_posterpills
    with fadeshort

    # Atropos Gedanken
    symb"Sie stellen sie genauso wie immer dar. Ein perfektes glückliches Leben für jeden."

    call screen arrow_detail_posterpills

label after_detail_posterpills:

    scene stairs_up
    with fadeshort

    # Atropos Gedanken
    symb"Oh, da vorne sind Tycho und die anderen. Soll ich mit ihnen sprechen, bevor ich ins Labor zurückgehe?"

    # Symbiont
    symb"{i}Nimm die Pille jetzt. Willst du noch länger unglücklich sein? Sei dankbar, dass Anan dir eine zweite Chance gab. Verspiele diese nicht. Mit deinen Freunden kannst du auch nachher noch reden. {/i}"


    menu:
        "Ja, natürlich. Ich sollte sofort zurück ins Labor.":
            jump take_pill_back_work
        "Ich denke, ich werde mich erst mit meinen Freunden unterhalten.":
            jump talk_with_colleagues

label take_pill_back_work:
    # Atropos Gedanken
    symb"Ja, natürlich. Ich sollte sofort zurück ins Labor. Ich muss die Pille nehmen."

    # Atropos Gedanken
    symb"Ich hoffe nur, sie wirkt rasch. Ich will wieder glücklich sein, wie alle anderen auch."

    # Atropos Gedanken
    symb"Aber jetzt sollte ich nicht weiter darüber nachdenken, Hauptsache ich bin bald glücklich."

    jump takepillnow

label talk_with_colleagues:
    # Atropos Gedanken
    symb"Ich denke ich werde mich erst mit meinen Freunden unterhalten. Für alles andere ist auch nachher noch Zeit."

    show tycho normal:
        xalign 0.85
    show ireia normal:
        xalign 0.35
    show neiro normal:
        xalign 0.6
    show armene normal:
        xalign 0.0

    "Atropos" "Hey- schön euch zu sehen. Macht ihr gerade eine kleine Pause?"

    show tycho happy
    show ireia normal_gray
    show neiro normal_gray
    show armene normal_gray


    "Tycho" "Jap. Wir waren unten in der Mensa und haben uns einen kleinen Snack geholt. Jetzt sind wir auf dem Rückweg ins Labor."

    "Tycho" "Was treibt dich hierher?"

    "Atropos" "Ach, ich bin auf dem Rückweg zum Labor."

    show tycho happy_gray
    show ireia normal

    "Ireia" "Auf dem Rückweg? Meinst du auf dem Rückweg von Anans Büro? Ich hatte dich vorher aus diesem kommen sehen. Auch wenn mittlerweile etwas Zeit seit diesem Zeitpunkt vergangen ist."

    show ireia confused

    "Ireia" "Wieso bist du nicht direkt zurück?"

    "Atropos" "Ich…"

    show ireia confused_gray
    show tycho really_happy

    "Tycho" "Ach, verkehrst du mittlerweile in höheren Kreisen? Sind wir dir nicht mehr gut genug? (lacht)"

    "Atropos" "Ich war bei ihm, aber…"

    show tycho really_happy_gray
    show neiro normal

    "Neiro" "Es geht um Anan? Du durftest Zeit mit ihm verbringen? Das muss traumhaft sein… (seufzt)"

    show neiro normal _gray
    show armene shy

    "Armene" "Ich wünschte, ich hätte einmal das Glück mit ihm persönlich zu sprechen! Es gibt wirklich keine größere Ehre als für Anan zu arbeiten!"

    show armene shy_gray
    show neiro happy

    "Neiro"  "Und es gibt definitiv auch keinen besseren Chef. Ich kenne niemanden, der sich so sehr um das Wohl der Menschheit sorgt und sich für alle einsetzt."

    show neiro happy_gray
    show armene shy

    "Armene" "Und er ist so charmant und gut aussehend…"

    show armene shy_gray
    show ireia strict

    "Ireia" "Armene, Anan ist unfassbar toll, aber es ist immer noch dein Chef über den du hier redest."

    show ireia strict_gray
    show armene normal

    "Armene" "Tut mir leid, Ireia…"

    show armene normal_gray
    show tycho happy

    "Tycho" "Also, erzähl schon. Was hatte dich zu Anan verschlagen?"

    # Atropos Gedanken
    symb"Ich sollte besser nichts von der Pille erwähnen. Sie würden mich nur dafür verurteilen."

    "Atropos"  "Ach, es ging um ein paar persönliche Sachen. Nichts weiter Wichtiges."

    "Tycho" "Es ist schon unglaublich, dass sich so eine bedeutende Person wie Anan Zeit für persönliche Gespräche nimmt. Und dabei ist er auch immer so locker und entspannt drauf."

    show tycho really_happy

    "Tycho" "Ich hatte neulich auch mal ein Gespräch mit ihm und…"

    show tycho really happy_gray
    show ireia strict

    "Ireia" "Die Geschichte hast du schon tausend Mal erzählt."

    # Atropos Gedanken
    symb"Anan wirkte heute irgendwie anders, als ich ihn in Erinnerung hatte."

    # Atropos Gedanken
    symb"Aber vermutlich hatte er einen stressigen Tag, er trägt immerhin nicht wenig Verantwortung und dann kam auch noch ich zu seinen Problemen hinzu."

    "Atropos"  " Heute beim Gespräch wirkte er nicht unbedingt entspannt…"

    show ireia strict_gray
    show neiro nervous_laugh

    "Neiro"  "Nun, wenn man so hart und voller Freude arbeitet wie Anan, kann man sich wohl nicht entspannen. Er hat immer etwas zu tun."

    show neiro nervous_laugh_gray
    show ireia happy

    "Ireia" "Es muss viel Arbeit machen das Glück aller zu erhalten. Wir sind ihm wirklich viel schuldig."

    # Atropos Gedanken
    symb"Warum haben sie meine Aussage so sehr verdreht?"

    "Atropos"  " Nein, so meinte ich das nicht. Es geht mehr darum wie Anan sich verh…"

    show ireia normal

    "Ireia" "Wir können alle noch viel von Anan lernen. Sein Enthusiasmus ist unglaublich. Aber hier zu arbeiten und das Glück in die Welt zu bringen- es gibt einfach keinen besseren Job."

    show ireia normal_gray
    show armene happy

    "Armene" "Und wir haben das Glück, dass wir unsere Happiness dafür auch noch umsonst bekommen. Kostenloses Glück, besser geht es nicht."

    # Atropos Gedanken
    symb"Sie verehren Anan wirklich wie einen Gott. Ob ich mich in ihm getäuscht habe? Aber irgendwie… warum ignorieren sie meine Aussagen, als wäre ich gar nicht da?"

    show armene happy_gray
    show ireia strict

    "Ireia" "Wir müssen langsam zurück an die Arbeit. Es ist noch eine ganze Menge zu tun."

    show ireia strict_gray
    show armene happy

    "Armene" "Wir organisieren gerade die Gründungsfeier, weißt du? Es wird ein riesiges Fest."

    show armene happy_gray
    show ireia happy

    "Ireia" "Na los, sonst kommen wir zu nichts. (lacht)"

    show ireia happy_gray
    show tycho really_happy

    "Tycho" "Mach’s gut. Wir sehen uns."

    "Atropos"  " Bis dann."

    hide tycho
    hide ireia
    hide armene
    hide neiro

    # Atropos Gedanken
    symb"Irgendetwas war an dem Gespräch seltsam. Aber irgendwie bekomme ich es nicht wirklich zu fassen… ich…"

    # Atropos Gedanken
    symb"Naja, egal. Ich sollte jetzt zurück ins Labor…"

    scene stairs_down
    with fadeshort

    # Atropos Gedanken
    symb"Warte… was ist das?"

    # Atropos Gedankens
    symb"Das… das…"

    # Symbiont
    symb"{i}Vergiss die Pille nicht, Atropos! Du fängst schon an dir Sachen einzubilden. Hier ist nichts zu sehen. {/i}"

    # Symbiont
    symb"{i}Langsam wirst du ja schon fast wahnsinnig. Nimm die Pille und werde wieder glücklich, so wie alle deine Kollegen es sind! {/i}"

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

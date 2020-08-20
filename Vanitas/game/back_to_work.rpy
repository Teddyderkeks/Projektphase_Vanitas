default back_to_work_bevore = False

label back_to_work:
    $ back_to_work_bevore = True
    # Atropos Gedanken
    "So… zurück an die Arbeit. Ich muss die Pille nehmen."

    # Atropos Gedanken
    "Auch wenn ich mich immer noch frage, wie sie überhaupt wirkt…"


    scene stairs_up

    # Atropos Gedanken
    "Aber apropos Pille. Sind die Werbeplakate für diese neu?"
    scene detail_posterpills

    # Atropos Gedanken
    "Sie stellen sie genauso wie immer dar. Ein perfektes glückliches Leben für jeden."

    call screen arrow_detail_posterpills

label after_detail_posterpills:

    scene stairs_up

    # Atropos Gedanken
    "Oh, da vorne sind Tycho und die anderen. Soll ich mit ihnen sprechen, bevor ich ins Labor zurückgehe?"

    # Symbiont
    "{i}Nimm die Pille jetzt. Willst du noch länger unglücklich sein? Sei dankbar, dass Anan dir eine zweite Chance gab. Verspiele diese nicht. Mit deinen Freunden kannst du auch nachher noch reden. {/i}"


    menu:
        "Ja, natürlich. Ich sollte sofort zurück ins Labor.":
            jump take_pill_back_work
        "Ich denke, ich werde mich erst mit meinen Freunden unterhalten.":
            jump talk_with_colleagues

label take_pill_back_work:
    # Atropos Gedanken
    "Ja, natürlich. Ich sollte sofort zurück ins Labor. Ich muss die Pille nehmen."

    # Atropos Gedanken
    "Ich hoffe nur, sie wirkt rasch. Ich will wieder glücklich sein, wie alle anderen auch."

    # Atropos Gedanken
    "Aber jetzt sollte ich nicht weiter darüber nachdenken, Hauptsache ich bin bald glücklich."

    jump takepillnow

label talk_with_colleagues:
    # Atropos Gedanken
    "Ich denke ich werde mich erst mit meinen Freunden unterhalten. Für alles andere ist auch nachher noch Zeit."

    "Atropos" "Hey- schön euch zu sehen. Macht ihr gerade eine kleine Pause?"

    show tycho normal
    show ireia normal
    show neiro normal
    show armene normal


    "Tycho" "Jap. Wir waren unten in der Mensa und hatten uns einen kleinen Snack geholt. Jetzt sind wir auf dem Rückweg ins Labor."

    "Tycho" "Was treibt dich hierher?"

    "Atropos" "Ach, ich bin auf dem Rückweg zum Labor."

    "Ireia" "Auf dem Rückweg? Meinst du auf dem Rückweg von Anans Büro? Ich hatte dich vorher aus diesem kommen sehen. Auch wenn mittlerweile etwas Zeit seit diesem Zeitpunkt vergangen ist."

    "Ireia" "Wieso bist du nicht direkt zurück?"

    "Atropos" "Ich…"

    "Tycho" "Ach, verkehrst du mittlerweile in höheren Kreisen? Sind wir dir nicht mehr gut genug? (lacht)"

    "Atropos" "Ich war bei ihm, aber…"

    "Neiro" "Es geht um Anan? Du durftest Zeit mit ihm verbringen? Das muss traumhaft sein… (seufzt)"

    "Armene" "Ich wünschte, ich hätte einmal das Glück mit ihm persönlich zu sprechen! Es gibt wirklich keine größere Ehre als für Anan zu arbeiten!"

    "Neiro"  "Und es gibt definitiv auch keinen besseren Chef. Ich kenne niemanden, der sich so sehr um das Wohl der Menschheit sorgt und sich für alle einsetzt."

    "Armene" "Und er ist so charmant und gut aussehend…"

    "Ireia" "Armene, Anan ist unfassbar toll, aber es ist immer noch dein Chef über den du hier redest."

    "Armene" "Tut mir leid, Ireia…"


    "Tycho" "Also, erzähl schon. Was hatte dich zu Anan verschlagen?"

    # Atropos Gedanken
    "Ich sollte besser nichts von der Pille erwähnen. Sie würden mich nur dafür verurteilen."

    "Atropos"  "Ach, es ging um ein paar persönliche Sachen. Nichts weiter Wichtiges."

    "Tycho" "Es ist schon unglaublich, dass sich so eine bedeutende Person wie Anan Zeit für persönliche Gespräche nimmt. Und dabei ist er auch immer so locker und entspannt drauf."

    "Tycho" "Ich hatte neulich auch mal ein Gespräch mit ihm und…"

    "Ireia" "Die Geschichte hast du schon tausend Mal erzählt."

    # Atropos Gedanken
    "Anan wirkte heute irgendwie anders, als ich ihn in Erinnerung hatte."

    # Atropos Gedanken
    "Aber vermutlich hatte er einen stressigen Tag, er trägt immerhin nicht wenig Verantwortung und dann kam auch noch ich zu seinen Problemen hinzu."

    "Atropos"  " Heute beim Gespräch wirkte er nicht unbedingt entspannt…"
    "Neiro"  "Nun, wenn man so hart und voller Freude arbeitet wie Anan, kann man sich wohl nicht entspannen. Er hat immer etwas zu tun."

    "Ireia" "Es muss viel Arbeit machen das Glück aller zu erhalten. Wir sind ihm wirklich viel schuldig."

    # Atropos Gedanken
    "Warum haben sie meine Aussage so sehr verdreht?"

    "Atropos"  " Nein, so meinte ich das nicht. Es geht mehr darum wie Anan sich verh…"

    "Ireia" "Wir können alle noch viel von Anan lernen. Sein Enthusiasmus ist unglaublich. Aber hier zu arbeiten und das Glück in die Welt zu bringen- es gibt einfach keinen besseren Job."

    "Armene" "Und wir haben das Glück, dass wir unsere Happiness dafür auch noch umsonst bekommen. Kostenloses Glück, besser geht es nicht."

    # Atropos Gedanken
    "Sie verehren Anan wirklich wie einen Gott. Ob ich mich in ihm getäuscht habe? Aber irgendwie… warum ignorieren sie meine Aussagen, als wäre ich gar nicht da?"

    "Ireia" "Wir müssen langsam zurück an die Arbeit. Es ist noch eine ganze Menge zu tun."

    "Armene" "Wir organisieren gerade die Gründungsfeier, weißt du? Es wird ein riesiges Fest."

    "Ireia" "Na los, sonst kommen wir zu nichts. (lacht)"

    "Tycho" "Mach’s gut. Wir sehen uns."

    "Atropos"  " Bis dann."

    hide tycho
    hide ireia
    hide armene
    hide neiro

    # Atropos Gedanken
    "Irgendetwas war an dem Gespräch seltsam. Aber irgendwie bekomme ich es nicht wirklich zu fassen… ich…"

    # Atropos Gedanken
    "Naja, egal. Ich sollte jetzt zurück ins Labor…"

    scene stairs_down

    # Atropos Gedanken
    "Warte… was ist das?"

    # Atropos Gedankens
    "Das… das…"

    # Symbiont
    "{i}Vergiss die Pille nicht, Atropos! Du fängst schon an dir Sachen einzubilden. Hier ist nichts zu sehen. {/i}"

    # Symbiont
    "{i}Langsam wirst du ja schon fast wahnsinnig. Nimm die Pille und werde wieder glücklich, so wie alle deine Kollegen es sind! {/i}"

    # Symbiont
    "{i}Du hast dein Glück verdient. So wie alle Menschen Glück verdient haben. {/i}"

    # Symbiont
    "{i}Du willst das hier nicht sehen. Es würde dich unglücklich machen. Hier ist nichts. Vergiss, was du zu sehen glaubtest. {/i}"

    # Symbiont
    "{i}Brich die Suche ab und kehre ins Labor zurück! Nimm die Pille! Lebe weiterhin ein glückliches Leben. {/i}"

    # Atropos Gedanken
    "Ist das… ist das eine Leiche?"

    # Atropos Gedanken
    "Aber wie? Warum? Warum ist sie noch niemandem aufgefallen?"

    # Atropos Gedanken
    "Was hat das alles zu bedeuten? Es macht mir Angst…"

    # Atropos Gedanken
    "Will ich die Wahrheit dahinter überhaupt wissen?"

    # Atropos Gedanken
    "Nein… ja… ich… ich…"

    # Atropos Gedanken
    "Was, wenn das Kloth ist?"

    # Atropos Gedanken
    "Das… das würde ich nicht ertragen…"

    # Symbiont
    "{i}Brich die Suche ab und kehre ins Labor zurück! Nimm die Pille! Lebe weiterhin ein glückliches Leben. {/i}"

    # Symbiont
    "{i}Tu es! {/i}"




    jump leave_or_corpse

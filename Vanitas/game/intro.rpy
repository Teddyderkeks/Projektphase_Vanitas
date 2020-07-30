# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"

# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define e = Character('Eileen', color="#c8ffc8")


# Hier beginnt das Spiel.
label start:
    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    scene atropos_falling

    "Will ich versuchen etwas zu ändern?"

    menu:
        "ja":
            jump change
        "nein":
            jump quick_ending

label quick_ending:
    $ renpy.movie_cutscene("atropos_lehnt_gespraech_ab.mpg")

    return

label change:
    "Hey was geht"

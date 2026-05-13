## screens.rpy
## UI screen definitions. All custom screens are written here.
## Ren'Py's default screens are used until replaced with final UI.

## ── MAIN MENU ─────────────────────────────────────────────────────────────────

screen main_menu():
    tag menu

    ## Background (replace with final UI asset)
    add "#1a1a1a"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Camp Adventure" size 48 color "#f5e6c8" xalign 0.5

        textbutton "New Game" action Start() xalign 0.5
        textbutton "Load Game" action ShowMenu("load") xalign 0.5
        textbutton "Quit" action Quit() xalign 0.5

## ── PROTAGONIST SETUP ────────────────────────────────────────────────────────
## Player creates their character before starting the game

screen protagonist_setup():
    tag menu

    ## Background (replace with final UI asset)
    add "#1a1a1a"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        ## Title
        text "Create Your Character" size 36 color "#f5e6c8" xalign 0.5

        ## Name input
        text "Name:" size 24 color "#f5e6c8"
        input:
            xalign 0.5
            ysize 40
            value VariableInput(protagonist_name, length=20)
            allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 "

        ## Species selection
        text "Species:" size 24 color "#f5e6c8"
        vbox:
            xalign 0.5
            spacing 10
            for species in ["Fox", "Wolf", "Cat", "Bear"]:
                textbutton species:
                    xsize 200
                    ysize 40
                    action SetVariable("protagonist_species", species)
                    selected (protagonist_species == species)
                    color "#a8d8a8" if protagonist_species == species else "#666666"

        ## Continue button (only enabled if both fields are filled)
        textbutton "Continue" action Return():
            xalign 0.5
            ysize 50
            xsize 150
            enabled (protagonist_name != "" and protagonist_species != "")
            color "#f5e6c8" if (protagonist_name != "" and protagonist_species != "") else "#666666"

## ── HUD / DAY DISPLAY ────────────────────────────────────────────────────────
## Shown during gameplay. Displays current day.

screen hud():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        text "Day [current_day] / [max_days]" size 20 color "#f5e6c8"

## ── ADD NEW SCREENS BELOW THIS LINE ─────────────────────────────────────────

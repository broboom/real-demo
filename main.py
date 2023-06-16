def on_a_pressed():
    global mySprite
    mySprite = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 2 2 f f f . . . . 
                    . . . f f f 2 2 2 2 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 2 2 2 2 2 2 e e f . . 
                    . . f e 2 f f f f f f 2 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.player)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_a_released():
    global mySprite
    mySprite = sprites.create(img("""
            f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f 
                    f f f f f f f f f f f f f f f f
        """),
        SpriteKind.player)
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

mySprite: Sprite = None
music.set_volume(256)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
pause(1000)
music.play(music.melody_playable(music.thump),
    music.PlaybackMode.UNTIL_DONE)
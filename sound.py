
import sys

IS_WINDOWS = sys.platform.startswith("win")

if IS_WINDOWS:
    import winsound

    def play_click():
        winsound.Beep(600, 60)

    def play_win():
        winsound.Beep(900, 120)
        winsound.Beep(1200, 150)

    def play_draw():
        winsound.Beep(400, 200)

else:
    def _bell():
        sys.stdout.write("\a")
        sys.stdout.flush()

    def play_click():
        _bell()

    def play_win():
        _bell()

    def play_draw():
        _bell()

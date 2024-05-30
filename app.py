from math import pi

from events.input import BUTTON_TYPES, Buttons

import app


class ExampleApp(app.App):
    def __init__(self):
        self.button_states = Buttons(self)

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # The button_states do not update while you are in the background.
            # Calling clear() ensures the next time you open the app, it stays open.
            # Without it the app would close again immediately.
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        # ctx.save()
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        ctx.rgba(255, 255, 255, 1)
        ctx.translate(-50, -50)
        # ctx.arc(0, 0, 100, 0, 3, 0)
        # ctx.close_path()
        self._draw_logo(ctx)
        ctx.stroke()

        # ctx.rgb(1, 0, 0).move_to(-80, 0).text("Hello world")
        # ctx.restore()

    def _draw_logo(self, ctx):
        ctx.move_to(30, 0)
        ctx.line_to(40, ctx.y)
        ctx.line_to(ctx.x, 50)
        ctx.line_to(30, ctx.y)
        ctx.line_to(ctx.x, 30)
        ctx.line_to(15, ctx.y)
        ctx.arc(15, 35, 5, pi * 1.5, pi, 0)  # rx ry xrot laf sf x y -- 5 5 0 0 0 10 35
        ctx.line_to(ctx.x, 75)
        # ctx.arc( 5 5 0 0 0 15 80
        ctx.line_to(30, ctx.y)
        ctx.line_to(ctx.x, 60)
        ctx.line_to(40, ctx.y)
        ctx.line_to(ctx.x, 110)
        ctx.line_to(30, ctx.y)
        ctx.line_to(ctx.x, 90)
        ctx.line_to(15, ctx.y)
        # ctx.arc( 15 15 0 0 1 0 75
        ctx.line_to(ctx.x, 35)
        # ctx.arc( 15 15 0 0 1 15 20
        ctx.line_to(30, ctx.y)
        ctx.close_path()

        ctx.move_to(70, 0)
        ctx.line_to(80, ctx.y)
        ctx.line_to(ctx.x, 20)
        ctx.line_to(95, ctx.y)
        # ctx.arc( 15 15 0 0 1 110 35
        ctx.line_to(ctx.x, 75)
        # ctx.arc( 15 15 0 0 1 95 90
        ctx.line_to(80, ctx.y)
        ctx.line_to(ctx.x, 110)
        ctx.line_to(70, ctx.y)
        ctx.line_to(ctx.x, 60)
        ctx.line_to(80, ctx.y)
        ctx.line_to(ctx.x, 80)
        ctx.line_to(95, ctx.y)
        # ctx.arc( 5 5 0 0 0 100 75
        ctx.line_to(ctx.x, 35)
        # ctx.arc( 5 5 0 0 0 95 30
        ctx.line_to(80, ctx.y)
        ctx.line_to(ctx.x, 50)
        ctx.line_to(70, ctx.y)
        ctx.line_to(ctx.x, 40)
        ctx.line_to(50, ctx.y)
        ctx.line_to(ctx.x, 30)
        ctx.line_to(70, ctx.y)
        ctx.line_to(ctx.x, 20)
        ctx.line_to(50, ctx.y)
        ctx.line_to(ctx.x, 10)
        ctx.line_to(70, ctx.y)
        ctx.close_path()

        ctx.move_to(50, 60)
        ctx.line_to(60, ctx.y)
        ctx.line_to(ctx.x, 80)
        ctx.line_to(50, ctx.y)
        ctx.close_path()

        ctx.move_to(50, 90)
        ctx.line_to(60, ctx.y)
        ctx.line_to(ctx.x, 110)
        ctx.line_to(50, ctx.y)
        ctx.close_path()

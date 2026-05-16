from manim import *


class SmokeScene(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        title = Text("Manim Master Skill", font_size=44, color=WHITE)
        circle = Circle(radius=1.2, color=BLUE_B).next_to(title, DOWN, buff=0.6)
        dot = Dot(circle.get_top(), color=YELLOW)

        self.play(Write(title))
        self.play(Create(circle), FadeIn(dot))
        self.wait(1)

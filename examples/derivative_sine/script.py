from manim import *
import numpy as np


class Scene1_UnitCircle(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        title = Text("A point on the unit circle", font_size=42)
        title.to_edge(UP)

        circle = Circle(radius=1.6, color=BLUE_B)
        dot = Dot(circle.point_at_angle(45 * DEGREES), color=YELLOW)
        radius = Line(circle.get_center(), dot.get_center(), color=YELLOW)

        self.play(Write(title))
        self.play(Create(circle))
        self.play(Create(radius), FadeIn(dot))
        self.wait(1)


class Scene2_SlopeIdea(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=3.5,
        )
        graph = axes.plot(lambda x: np.sin(x), color=BLUE_B)
        dot = Dot(axes.c2p(PI / 4, np.sin(PI / 4)), color=YELLOW)
        label = MathTex(r"y=\sin(x)", font_size=38).next_to(axes, UP)

        self.play(Create(axes))
        self.play(Create(graph), Write(label))
        self.play(FadeIn(dot))
        self.wait(1)


class Scene3_Takeaway(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        formula = MathTex(r"\frac{d}{dx}\sin(x)=\cos(x)", font_size=52)
        note = Text("The slope follows the cosine pattern.", font_size=30)
        note.next_to(formula, DOWN, buff=0.5)

        self.play(Write(formula))
        self.play(FadeIn(note))
        self.wait(2)

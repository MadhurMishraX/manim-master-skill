from manim import *


class Scene1_VectorAddition(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        title = Text("Vector addition", font_size=44).to_edge(UP)

        a = Arrow(ORIGIN, RIGHT * 2, color=BLUE_B)
        b = Arrow(ORIGIN, UP * 1.5, color=GREEN_B)
        b_shifted = b.copy().shift(RIGHT * 2)
        result = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, color=YELLOW)

        label_a = MathTex(r"\vec a").next_to(a, DOWN)
        label_b = MathTex(r"\vec b").next_to(b_shifted, RIGHT)
        label_r = MathTex(r"\vec a+\vec b").next_to(result, UP)

        group = VGroup(a, b, b_shifted, result, label_a, label_b, label_r).move_to(ORIGIN)

        self.play(Write(title))
        self.play(GrowArrow(a), Write(label_a))
        self.play(GrowArrow(b))
        self.play(Transform(b, b_shifted), Write(label_b))
        self.play(GrowArrow(result), Write(label_r))
        self.wait(2)

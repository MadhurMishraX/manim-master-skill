from manim import *
import numpy as np

# ============================================================
# Global style
# ============================================================

BACKGROUND = "#0B1020"
PRIMARY = BLUE_B
SECONDARY = GREEN_B
ACCENT = YELLOW
WARNING = RED_B
TEXT_COLOR = WHITE

TITLE_SIZE = 46
BODY_SIZE = 30
FORMULA_SIZE = 38
LABEL_SIZE = 24


def apply_default_style(scene: Scene) -> None:
    scene.camera.background_color = BACKGROUND


def title_text(text: str) -> Text:
    return Text(text, font_size=TITLE_SIZE, color=TEXT_COLOR)


def body_text(text: str) -> Text:
    return Text(text, font_size=BODY_SIZE, color=TEXT_COLOR)


def formula_tex(tex: str) -> MathTex:
    return MathTex(tex, font_size=FORMULA_SIZE, color=TEXT_COLOR)


def small_label(text: str) -> Text:
    return Text(text, font_size=LABEL_SIZE, color=TEXT_COLOR)


# ============================================================
# Scene 1
# ============================================================

class Scene1_Hook(Scene):
    def construct(self):
        apply_default_style(self)

        title = title_text("Why does this idea work?")
        subtitle = body_text("A visual explanation, step by step").next_to(title, DOWN, buff=0.35)

        group = VGroup(title, subtitle).move_to(ORIGIN)

        self.add_subcaption("We begin with the central question.", duration=2)
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.wait(1)

        self.play(FadeOut(group), run_time=0.8)


# ============================================================
# Scene 2
# ============================================================

class Scene2_CoreIdea(Scene):
    def construct(self):
        apply_default_style(self)

        heading = title_text("Core visual idea").to_edge(UP)

        circle = Circle(radius=1.5, color=PRIMARY)
        dot = Dot(circle.point_at_angle(45 * DEGREES), color=ACCENT)
        radius = Line(circle.get_center(), dot.get_center(), color=ACCENT)

        label = small_label("track one moving point").next_to(circle, DOWN, buff=0.4)

        visual = VGroup(circle, radius, dot, label).move_to(ORIGIN)

        self.add_subcaption("Now we build the idea using one clean visual model.", duration=3)
        self.play(Write(heading), run_time=1)
        self.play(Create(circle), run_time=1)
        self.play(Create(radius), FadeIn(dot), run_time=1)
        self.play(FadeIn(label), run_time=0.7)
        self.wait(1)

        self.play(FadeOut(VGroup(heading, visual)), run_time=0.8)


# ============================================================
# Scene 3
# ============================================================

class Scene3_Conclusion(Scene):
    def construct(self):
        apply_default_style(self)

        takeaway = title_text("Final takeaway")
        formula = formula_tex(r"\text{visual intuition} \rightarrow \text{symbolic clarity}")
        formula.next_to(takeaway, DOWN, buff=0.5)

        group = VGroup(takeaway, formula).move_to(ORIGIN)

        self.add_subcaption("The final frame should leave one clear idea in the viewer's mind.", duration=3)
        self.play(Write(takeaway), run_time=1)
        self.play(Write(formula), run_time=1.2)
        self.wait(2)

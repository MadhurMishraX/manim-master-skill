from manim import *


class Scene1_BinarySearch(Scene):
    def construct(self):
        self.camera.background_color = "#0B1020"

        title = Text("Binary search halves the problem", font_size=40).to_edge(UP)

        values = [1, 3, 5, 7, 9, 11, 13]
        boxes = VGroup()
        labels = VGroup()

        for value in values:
            box = Square(side_length=0.65, color=BLUE_B)
            label = Text(str(value), font_size=24)
            labels.add(label)
            boxes.add(VGroup(box, label))

        boxes.arrange(RIGHT, buff=0.12).move_to(ORIGIN)

        mid_box = boxes[3][0]
        left_side = VGroup(*boxes[:3])
        right_side = VGroup(*boxes[4:])

        self.play(Write(title))
        self.play(FadeIn(boxes))
        self.play(mid_box.animate.set_stroke(YELLOW, width=6))
        self.wait(0.5)
        self.play(left_side.animate.set_opacity(0.25))
        self.wait(0.5)
        self.play(right_side.animate.set_opacity(0.25))
        self.wait(2)

from typing import Any, Iterable, List, Optional
from manim import BLUE_D, RIGHT, UP, Animation, Line, Mobject, Scene, Circle, Create, DOWN, VMobject, np
from manim.animation.composition import AnimationGroup, LaggedStart
from manim.mobject.text.text_mobject import Text
from manim.utils.color import RED_D, Color
from numpy import ndarray


class CreateTrunkManual(Scene):
    def construct(self):
        c0 = Circle()
        c0.to_edge(DOWN)
        c0.z_index = 1
        c0.set_fill(RED_D, opacity=1)
        c0.set_stroke(width=0)

        c1 = Circle()
        c1.set_fill(RED_D, opacity=1)
        c1.next_to(c0, UP, buff=0.5)
        c1.z_index = 1
        c1.set_stroke(width=0)

        l0_1 = Line(c0.get_center(), c1.get_center())

        c2 = Circle()
        c2.set_fill(RED_D, opacity=1)
        c2.next_to(c1, UP, buff=0.5)
        c2.z_index = 1
        c2.set_stroke(width=0)

        l1_2 = Line(c1.get_center(), c2.get_center())

        t = Text("main")
        t.next_to(c0, RIGHT, buff=0.5)

        self.play(
            LaggedStart(
                AnimationGroup(
                    Create(t),
                    Create(c0),
                ),
                LaggedStart(
                    Create(l0_1),Create(c1),
                    lag_ratio=0.5
                ),
                LaggedStart(
                    Create(l1_2),Create(c2),
                    lag_ratio=0.5
                ),
                lag_ratio=0.5
            )
        )

class CreateTrunk(Scene):
    def construct(self):
        main = Branch("main")
        c = main.add_commit()
        dev = Branch("develop", color=BLUE_D, parent=c)
        main.add_commit()
        main.add_commit()
        dev.add_commit()
        dev.add_commit()
        self.play(main.animate())
        self.play(dev.animate())

class Commit():
    _mobj: VMobject

    def __init__(self, color: str, parent: Optional['Commit'] = None, parent_from_other_branch: bool = False) -> None:

        self._mobj = Circle()
        self._mobj.set_fill(color, opacity=1)
        self._mobj.set_stroke(width=0)
        self._mobj.z_index = 1

        if parent == None:
            self._mobj.to_edge(DOWN)
        else:
            if parent_from_other_branch:
                self._mobj.next_to(parent._mobj, RIGHT+UP, buff=1)
            else:
                self._mobj.next_to(parent._mobj, UP, buff=0.5)

    def animate(self) -> Animation:
        return Create(self._mobj)

    def get_center(self):
        return self._mobj.get_center()


class Branch():
    name: str
    name_pos: ndarray[Any, Any] = RIGHT
    color: str = RED_D
    parent: Optional[Commit] = None
    commits: List[Commit]

    def __init__(self, name: str, color: str = RED_D, parent: Optional[Commit] = None) -> None:
        self.name = name
        self.parent = parent
        self.color = color
        self.commits = list()

    def add_commit(self) -> Commit:
        parent = None
        parent_from_other_branch = False

        if len(self.commits) > 0:
            parent = self.commits[-1]
        else:
            if self.parent != None:
                parent = self.parent
                parent_from_other_branch = True

        commit = Commit(self.color, parent, parent_from_other_branch=parent_from_other_branch)
        self.commits.append(commit)
        return commit

    def animate(self) -> Animation:
        prev = None
        anims = list()

        for commit in self.commits:
            if prev == None:
                t = Text(self.name)
                t.next_to(commit._mobj, self.name_pos, buff=0.5)
                start_branch_anim = AnimationGroup(
                    commit.animate(), Create(t)
                )

                if self.parent != None:
                    line = Line(self.parent.get_center(), commit.get_center())
                    start_branch_anim = LaggedStart(Create(line), start_branch_anim, lag_ratio=0.5)

                anims.append(start_branch_anim)
            else:
                line = Line(prev.get_center(), commit.get_center())
                anims.append(
                    LaggedStart(
                        Create(line),commit.animate(),
                        lag_ratio=0.5
                    )
                )

            prev = commit

        return LaggedStart(*anims, lag_ratio=0.5)

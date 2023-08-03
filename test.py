from manimlib import *

class DesignFlow(Scene):
    def construct(self):
        
        user = Circle(fill_color=GREY,fill_opacity=0.7).move_to([-4, 0, 0]).scale(0.75)
        usertext = (Tex('USER').next_to(user, UP)).scale(0.7)
        
        frontend = Rectangle(fill_color=BLUE,fill_opacity=0.7, width = 3, height = 2).move_to([0, 0, 0])
        frontendtext = Tex('Frontend').next_to(frontend, UP).scale(0.7)

        backend = Rectangle(fill_color=GREEN,fill_opacity=0.7, width = 3, height = 2).move_to([4, 2, 0])
        backendtext = Tex('Backend').next_to(backend, UP).scale(0.7)

        model = Rectangle(fill_color=RED,fill_opacity=0.7, width = 2, height = 3).move_to([4, -2, 0])
        modeltext = Tex('Model').next_to(model, UP).scale(0.7)

        self.add(usertext, user, frontend, frontendtext, backend, backendtext,model ,modeltext)

        url = Tex('URL').scale(0.5)
        self.add(url.next_to(user, RIGHT))
        self.play(url.animate.next_to(frontend, LEFT), run_time=2)
        self.remove(url)

        arrowUser = Arrow(user, frontend, buff=0.1, stroke_width=6)
        self.play(ShowCreation(arrowUser))

        discFront = Text('Check for validity').scale(0.5)
        self.add(discFront.move_to(frontend.get_center()))

        self.add(url.next_to(frontend, RIGHT))
        self.play(url.animate.next_to(backend, LEFT), run_time=2)
        self.remove(url)

        arrowFront = Arrow(frontend, backend, buff=0.1, stroke_width=6)
        self.play(ShowCreation(arrowFront))

        discBack = Text('Extract Features').scale(0.5)
        self.add(discBack.move_to(backend.get_center()))

        self.add(url.next_to(backend, DOWN))
        self.play(url.animate.next_to(model, RIGHT), run_time=2)
        self.remove(url)

        discmodel = Text('Predict').scale(0.5)
        self.add(discmodel.move_to(model.get_center()))

        arrowBack = Arrow(backend, modeltext, buff=0.1, stroke_width=6)
        self.play(ShowCreation(arrowBack))

        resultarrowGreen = Arrow(modeltext, backend.get_corner(DR) - [0.25,0,0], buff=0.1, stroke_width=6).set_color(GREEN)
        resultarrowRED = Arrow(modeltext, backend.get_corner(DL) + [0.25,0,0], buff=0.1, stroke_width=6).set_color(RED)
        self.remove(arrowBack)
        self.play(*[ShowCreation(resultarrowRED), ShowCreation(resultarrowGreen)])
       
        resultarrowGreenBack = Arrow(backend, frontend.get_corner(UR), buff=0.1, stroke_width=6).set_color(GREEN)
        resultarrowREDBack = Arrow(backend, frontend.get_corner(UR) + [0,-1,0], buff=0.1, stroke_width=6).set_color(RED)
        self.remove(arrowFront)
        self.play(*[ShowCreation(resultarrowREDBack), ShowCreation(resultarrowGreenBack)])

        sqGood = Square(fill_color=GREEN,fill_opacity=0.7).scale(0.75).move_to(frontend.get_bottom() + [-2,-1.5,0])
        sqBad = Square(fill_color=RED,fill_opacity=0.7).scale(0.75).move_to(frontend.get_bottom() + [1,-1.5,0])
        goodText = Text('Load page').move_to(sqGood.get_center()).scale(0.5)
        badText = Text('Dont\nLoad page').move_to(sqBad.get_center()).scale(0.5)
        self.add(sqGood, sqBad, goodText, badText)

        finalGreen = Arrow(frontend, sqGood, buff=0.1, stroke_width=6).set_color(GREEN)
        finalRED = Arrow(frontend, sqBad, buff=0.1, stroke_width=6).set_color(RED)
        
        self.remove(arrowFront)
        self.play(*[ShowCreation(finalRED), ShowCreation(finalGreen)])
        self.wait(3)
        
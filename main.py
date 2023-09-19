from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivymd.theming import ThemeManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
import random
global score
score = 0
global score_1
score_1 = 0
class CommonKeypad(FloatLayout):
    pass
class MainScreen(Screen):
    pass
class AddScreen(Screen):
    pass
class SubScreen(Screen):
    pass
class MulScreen(Screen):
    pass
class DivScreen(Screen):
    pass
class MyManager(ScreenManager): 
    pass

class MathsQuizApp(MDApp):
    def build(self):
        bldr = Builder.load_file("main.kv")
        self.icon = "Icon.jpg"
        return bldr
    def score(self):
        global score
        score_3 = self.root.get_screen("mainscrn").ids.score
        score += 1
        if score + score_1 != 0:
            a = (score / (score + score_1)) * 100
            a = a*4
            score_3.text = f"Score: {a:.2f}%"
    def score_1(self):
        global score_1
        score_3 = self.root.get_screen("mainscrn").ids.score
        score_1 += 1
        if score + score_1 != 0:
            a = (score / (score + score_1)) * 100
            a = a*4
            score_3.text = f"Score: {a:.2f}%"
    def clarification_random(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.random_ques_add()
        if curren_screen=="subscrn":
            self.random_ques_sub()
        if curren_screen=="mulscrn":
            self.random_ques_mul()
        if curren_screen=="divscrn":
            self.random_ques_div()
    def clarification_check_123(self):
        right_ans = "Congrats \nYou Got Correct Answer"
        wrong_ans = "Incorrect Answer, \nThe Correct Answer Is: "
        current_screen = self.root.current
        expected_result_2 = 0
        expected_result_3 = 0
        expected_result_4 = 0
        expected_result_5 = 0
        if current_screen == "addscrn":
            quiz_input = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
            question_label = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.ques.text
            operation = "+"
        elif current_screen == "subscrn":
            quiz_input = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
            question_label = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.ques.text
            operation = "-"
        elif current_screen == "mulscrn":
            quiz_input = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
            question_label = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.ques.text
            operation = "×"
        elif current_screen == "divscrn":
            quiz_input = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
            question_label = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.ques.text
            operation = "÷"
        parts = question_label.split(operation)
        if len(parts) == 2:
            a = float(parts[0].strip())
            b = float(parts[1].strip())
            if operation == "+":
                expected_result = a + b
            elif operation == "-":
                expected_result = a - b
            elif operation == "×":
                expected_result = a * b
            elif operation == "÷" and b != 0:
                expected_result = a / b
        if len(parts) == 2 and operation=="+":
            expected_result = int(parts[0].strip())
            expected_result_1 = int(parts[1].strip())
            expected_result_2 = int(expected_result+expected_result_1)
        else:
            expected_result = ""
            expected_result_1 = ""
        if len(parts) == 2 and operation=="-":
            expected_result = int(parts[0].strip())
            expected_result_1 = int(parts[1].strip())
            expected_result_3 = int(expected_result-expected_result_1)
        else:
            expected_result = ""
            expected_result_1 = ""
        if len(parts) == 2 and operation=="×":
            expected_result = int(parts[0].strip())
            expected_result_1 = int(parts[1].strip())
            expected_result_4 = int(expected_result*expected_result_1)
        else:
            expected_result = ""
            expected_result_1 = ""
        if len(parts) == 2 and operation == "÷":
            expected_result = int(parts[0].strip())
            expected_result_1 = int(parts[1].strip())
            expected_result_5 = float(expected_result) / expected_result_1
        else:
            expected_result = ""
            expected_result_1 = ""
            expected_result_5 = ""
        user_input = quiz_input.text.strip()
        if current_screen=="divscrn" and user_input.strip()!="":
            user_input = float(user_input)
        else:
            if user_input.strip()!="":
                user_input = int(user_input)
        if user_input == expected_result_2 and current_screen=="addscrn" and str(user_input).strip()!="":
            ans_label = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.check_ans
            ans_label.text = right_ans
            self.score()
        else:
            if len(parts) == 2:
                expected_result = int(parts[0].strip())
                expected_result_1 = int(parts[1].strip())
                expected_result_2 = int(expected_result+expected_result_1)
            ans_label = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.check_ans
            ans_label.text = wrong_ans+str(expected_result_2)
            self.score_1()
        if user_input == expected_result_3 and current_screen=="subscrn":
            ans_label = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.check_ans
            ans_label.text = right_ans
            self.score()
        else:
            if len(parts) == 2:
                expected_result = int(parts[0].strip())
                expected_result_1 = int(parts[1].strip())
                expected_result_2 = int(expected_result-expected_result_1)
            ans_label = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.check_ans
            ans_label.text = wrong_ans+str(expected_result_3)
            self.score_1()
        if user_input == expected_result_4 and current_screen=="mulscrn":
            ans_label = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.check_ans
            ans_label.text = right_ans
            self.score()
        else:
            if len(parts) == 2:
                expected_result = int(parts[0].strip())
                expected_result_1 = int(parts[1].strip())
                expected_result_2 = int(expected_result-expected_result_1)
            ans_label = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.check_ans
            ans_label.text = wrong_ans+str(expected_result_4)
            self.score_1()
        if current_screen == "divscrn" and str(user_input).strip()!="":
            user_input = float(user_input)
        else:
            if str(user_input).strip()!="":
                user_input = int(user_input)
        if user_input == expected_result_5 and current_screen == "divscrn":
            ans_label = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.check_ans
            ans_label.text = right_ans
            self.score()
        else:
            ans_label = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.check_ans
            ans_label.text = wrong_ans + str(expected_result_5)
            self.score_1()
    def random_ques_add(self):
        ques_label = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.ques
        textinputadd1 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input.text
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        a = str(a)
        b = str(b)
        ques_label.text = a+"+"+b
        a = int(a)
        b = int(b)
    def random_ques_mul(self):
        ques_label = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.ques
        a = random.randint(0, 30)
        b = random.randint(0, 30)
        a = str(a)
        b = str(b)
        ques_label.text = a+"×"+b
    def random_ques_sub(self):
        ques_label = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.ques
        
        while True:
            a = random.randint(0, 100)
            b = random.randint(0, a)
            if a >= b:
                break
        a = str(a)
        b = str(b)
        ques_label.text = a + "-" + b
    def random_ques_div(self):
        ques_label = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.ques
        
        while True:
            a = random.randint(0, 1000)
            b = random.randint(1, 1000)
            if a % b == 0:
                break

        a = str(a)
        b = str(b)
        ques_label.text = a + "÷" + b
    def textinputadd(self):
        textinputadd1 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input.text
        textdata1 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata1.text = ""
    def textinputsub(self):
        textinputsub1 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input.text
        textdata2 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata2.text = ""
    def textinputmul(self):
        textinputmul1 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input.text
        textdata3 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata3.text = ""
    def textinputdiv(self):
        textinputdiv1 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input.text
        textdata4 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata4.text = ""
    def add0(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="0"
    def sub0(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="0"
    def mul0(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="0"
    def div0(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="0"
    def add1(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="1"
    def sub1(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="1"
    def mul1(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="1"
    def div1(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="1"
    def add2(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="2"
    def sub2(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="2"
    def mul2(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="2"
    def div2(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="2"
    def add3(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="3"
    def sub3(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="3"
    def mul3(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="3"
    def div3(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="3"
    def add4(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="4"
    def sub4(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="4"
    def mul4(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="4"
    def div4(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="4"
    def add5(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="5"
    def sub5(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="5"
    def mul5(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="5"
    def div5(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="5"
    def add6(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="6"
    def sub6(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="6"
    def mul6(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="6"
    def div6(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="6"
    def add7(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="7"
    def sub7(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="7"
    def mul7(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="7"
    def div7(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="7"
    def add8(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="8"
    def sub8(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="8"
    def mul8(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="8"
    def div8(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="8"
    def add9(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text+="9"
    def sub9(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text+="9"
    def mul9(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text+="9"
    def div9(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text+="9"
    def addback(self):
        textdata6 = self.root.get_screen("addscrn").ids.commonkeypadadd.ids.quiz_input
        textdata6.text = textdata6.text[:-1]
    def subback(self):
        textdata6 = self.root.get_screen("subscrn").ids.commonkeypadsub.ids.quiz_input
        textdata6.text = textdata6.text[:-1]
    def mulback(self):
        textdata6 = self.root.get_screen("mulscrn").ids.commonkeypadmul.ids.quiz_input
        textdata6.text = textdata6.text[:-1]
    def divback(self):
        textdata6 = self.root.get_screen("divscrn").ids.commonkeypaddiv.ids.quiz_input
        textdata6.text = textdata6.text[:-1]
    def clarification_0(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add0()
        if curren_screen=="subscrn":
            self.sub0()
        if curren_screen=="mulscrn":
            self.mul0()
        if curren_screen=="divscrn":
            self.div0()
    def clarification_1(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add1()
        if curren_screen=="subscrn":
            self.sub1()
        if curren_screen=="mulscrn":
            self.mul1()
        if curren_screen=="divscrn":
            self.div1()
    def clarification_2(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add2()
        if curren_screen=="subscrn":
            self.sub2()
        if curren_screen=="mulscrn":
            self.mul2()
        if curren_screen=="divscrn":
            self.div2()
    def clarification_2(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add2()
        if curren_screen=="subscrn":
            self.sub2()
        if curren_screen=="mulscrn":
            self.mul2()
        if curren_screen=="divscrn":
            self.div2()
    def clarification_3(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add3()
        if curren_screen=="subscrn":
            self.sub3()
        if curren_screen=="mulscrn":
            self.mul3()
        if curren_screen=="divscrn":
            self.div3()
    def clarification_4(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add4()
        if curren_screen=="subscrn":
            self.sub4()
        if curren_screen=="mulscrn":
            self.mul4()
        if curren_screen=="divscrn":
            self.div4()
    def clarification_5(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add5()
        if curren_screen=="subscrn":
            self.sub5()
        if curren_screen=="mulscrn":
            self.mul5()
        if curren_screen=="divscrn":
            self.div5()
    def clarification_6(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add6()
        if curren_screen=="subscrn":
            self.sub6()
        if curren_screen=="mulscrn":
            self.mul6()
        if curren_screen=="divscrn":
            self.div6()
    def clarification_7(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add7()
        if curren_screen=="subscrn":
            self.sub7()
        if curren_screen=="mulscrn":
            self.mul7()
        if curren_screen=="divscrn":
            self.div7()
    def clarification_8(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add8()
        if curren_screen=="subscrn":
            self.sub8()
        if curren_screen=="mulscrn":
            self.mul8()
        if curren_screen=="divscrn":
            self.div8()
    def clarification_9(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.add9()
        if curren_screen=="subscrn":
            self.sub9()
        if curren_screen=="mulscrn":
            self.mul9()
        if curren_screen=="divscrn":
            self.div9()
    def clarification_back(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.addback()
        if curren_screen=="subscrn":
            self.subback()
        if curren_screen=="mulscrn":
            self.mulback()
        if curren_screen=="divscrn":
            self.divback()
    def clarification(self):
        curren_screen = self.root.current
        if curren_screen=="addscrn":
            self.textinputadd()
        if curren_screen=="subscrn":
            self.textinputsub()
        if curren_screen=="mulscrn":
            self.textinputmul()
        if curren_screen=="divscrn":
            self.textinputdiv()
if __name__ == '__main__':
    MathsQuizApp().run()
import unittest
from math import sin
from hypothesis import given, strategies
from MathExpression import expression, direct_cal


class TestMathExpression(unittest.TestCase):
    def test_MathExpression(self):
        # test1
        str="a + 2 - sin(-0.3)*(b - c)"
        func_dic={"sin": lambda a: sin(a[0])}
        test1 = expression(str=str, func_dic=func_dict, a=2, b=1, c=3)
        value1 = test1.process()
        out1 = direct_cal(value1)
        self.assertEqual(2 + 2 - sin(-0.3)*(1 - 3), out1)
        # test2
        str="a*6 - sin(b)*(b - c)"
        func_dic={"sin": lambda a: sin(a[0])}
        test2 = expression(str=str, func_dic=func_dic, a=2, b=1, c=3)
        value2 = test2.process()
        out2 = direct_cal(value2)
        self.assertEqual(2*6-sin(1)*(1-3), out2)
        # test3
        str="a + 2 - f(b, c)*(b - c)"
        func_dic={"f": lambda a: sin(a[0]) + a[1]}
        test3 = expression(str=str, func_dic=func_dic, a=2, b=1, c=3)
        value3 = test3.process()
        out3 = direct_cal(value3)
        self.assertEqual(2 + 2 - (sin(1) + 3) * (1 - 3), out3)
        # test4
        str="a + 2 - f(b,c,d,e)*(b - c)"
        func_dic={"f": lambda a: sin(a[0]) + a[1]*a[2]-a[3]}
        test4 = expression(str=str, func_dic=func_dic, a=2, b=1, c=3, d=4, e=8)
        value4 = test4.process()
        out4 = direct_cal(value4)
        self.assertEqual(2 + 2 - (sin(1) + 3*4-8) * (1 - 3), out4)
        # test5
        str="a + 2 - f(b,c,d,e)*(b - c)"
        func_dic={"f": lambda a: sin(a[0])*a[1] * (a[2] - a[3])}
        test5 = expression(str=str, func_dic=func_dic, a=2, b=1, c=3, d=4, e=8)
        value5 = test5.process()
        out5 = direct_cal(value5)
        self.assertEqual(2 + 2 - (sin(1)*3 * (4 - 8)) * (1 - 3), out5)
        # test6
        str="sin(a) + 2 - f(b,c,d,e)*(b - c)"
        func_dic={"sin": lambda a: sin(a[0]), "f": lambda a: sin(a[0]) * a[1] * (a[2] - a[3])}
        test6 = expression(str=str, func_dic=func_dic, a=2, b=1, c=3, d=4, e=8)
        value6 = test6.process()
        out6 = direct_cal(value6)
        self.assertEqual(sin(2) + 2 - (sin(1) * 3 * (4 - 8)) * (1 - 3), out6)

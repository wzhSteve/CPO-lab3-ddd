import unittest
from math import sin
from hypothesis import given, settings
import hypothesis.strategies as st
from MathExpression import expression, direct_cal


min = -3.4e+38
max = 3.4e+38


class TestMathExpression(unittest.TestCase):
    def test_MathExpression(self):
        # test1
        str = "a + 2 - sin(-0.3)*(b - c)"
        test1 = expression(str=str, func_dic=lambda a: sin(a),
                           a=2, b=1, c=3)
        value1 = test1.process()
        out1 = direct_cal(value1)
        self.assertEqual(2 + 2 - sin(-0.3)*(1 - 3), out1)
        # test2
        str = "a*6 - sin(b)*(b - c)"
        test2 = expression(str=str, func_dic=lambda a: sin(a),
                           a=2, b=1, c=3)
        value2 = test2.process()
        out2 = direct_cal(value2)
        self.assertEqual(2*6-sin(1)*(1-3), out2)
        # test3
        str = "a + 2 - f(b, c)*(b - c)"
        func_dic = lambda a, b: sin(a) + b
        test3 = expression(str=str, func_dic=func_dic, a=2, b=1, c=3)
        value3 = test3.process()
        out3 = direct_cal(value3)
        self.assertEqual(2 + 2 - (sin(1) + 3) * (1 - 3), out3)
        # test4
        str = "a + 2 - f(b,c,d,e)*(b - c)"
        func_dic = lambda a, b, c, d: sin(a) + b * c - d
        test4 = expression(str=str, func_dic=func_dic,
                           a=2, b=1, c=3, d=4, e=8)
        value4 = test4.process()
        out4 = direct_cal(value4)
        self.assertEqual(2 + 2 - (sin(1) + 3*4-8) * (1 - 3), out4)
        # test5
        str = "a + 2 - f(b,c,d,e)*(b - c)"
        func_dic = lambda a, b, c, d: sin(a) * b * (c - d)
        test5 = expression(str=str, func_dic=func_dic,
                           a=2, b=1, c=3, d=4, e=8)
        value5 = test5.process()
        out5 = direct_cal(value5)
        self.assertEqual(2 + 2 - (sin(1)*3 * (4 - 8)) * (1 - 3), out5)
        # add test
        # test6
        str = "a + 2 - f(b,c)*(b - c)"
        test6 = expression(str=str, func_dic=lambda a, b: a+b,
                           a=2, b=1, c=3)
        value6 = test6.process()
        out6 = direct_cal(value6)
        self.assertEqual(2 + 2 - (1 + 3) * (1 - 3), out6)
        # test7
        str = "a + 2 - f(b,c)*(b - c)"
        test6 = expression(str=str, func_dic=lambda a, b: a - b,
                           a=2, b=1, c=3)
        value6 = test6.process()
        out6 = direct_cal(value6)
        self.assertEqual(2 + 2 - (1 - 3) * (1 - 3), out6)
        # test8
        str = "a + 2 - f(b,c)*(b - c)"
        test6 = expression(str=str, func_dic=lambda a, b: a + b,
                           a=2, b=1, c=3)
        value6 = test6.process()
        out6 = direct_cal(value6)
        self.assertEqual(2 + 2 - (1+3) * (1-3), out6)

    @settings(max_examples=10)
    @given(a=st.floats(min_value=min, max_value=max),
           b=st.floats(min_value=min, max_value=max),
           c=st.floats(min_value=min, max_value=max))
    def test_PBT1(self, a, b, c):
        str = "a + 2 - f(a,b)*(b - c)"
        test = expression(str=str, func_dic=lambda a, b: a + b,
                          a=a, b=b, c=c)
        value = test.process()
        out = direct_cal(value)
        self.assertEqual(a + 2 - (a + b) * (b - c), out)

    @settings(max_examples=10)
    @given(a=st.floats(min_value=min, max_value=max),
           b=st.floats(min_value=min, max_value=max),
           c=st.floats(min_value=min, max_value=max))
    def test_PBT2(self, a, b, c):
        str = "a + 2 - f(a,b)*(b - c)"
        test = expression(str=str, func_dic=lambda a, b: a - b,
                          a=a, b=b, c=c)
        value = test.process()
        out = direct_cal(value)
        self.assertEqual(a + 2 - (a - b) * (b - c), out)

    @settings(max_examples=10)
    @given(a=st.floats(min_value=min, max_value=max),
           b=st.floats(min_value=min, max_value=max),
           c=st.floats(min_value=min, max_value=max))
    def test_PBT3(self, a, b, c):
        str = "a + 2 - f(b, c)*(b - c)"
        test = expression(str=str, func_dic=lambda a, b: sin(a)+b,
                          a=a, b=b, c=c)
        value = test.process()
        out = direct_cal(value)
        self.assertEqual(a + 2 - (sin(b) + c) * (b - c), out)

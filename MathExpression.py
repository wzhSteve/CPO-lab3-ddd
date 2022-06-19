import re
import logging


raw = r"-*\d+\.?\d*[e][-|+]\d+\.?\d*|-*\d+\.?\d*|inf"


def types(argType):
    def check(func):
        def f(*args, **kwargs):
            length = len(args)
            for k, v in argType.items():
                if k < length:
                    p = args[k]
                    if not isinstance(p, v):
                        logging.error("The arg %s should be %s,"
                                      "but it's %s now!"
                                      % (str(p), type(v()), type(p)))
                else:
                    if isinstance(kwargs, v):
                        pass
            try:
                res = func(*args, **kwargs)
            finally:
                logging.info("{} FINISH".format(func.__name__))
            return res
        return f
    return check


class expression(object):

    @types({1: str, 2: str, 3: dict})
    def __init__(self, str, func_dic, **parameter):
        self.__str = str
        self.__func_dic = func_dic
        self.__parameter = parameter
        self.__flag = 0
        for i in self.__str:
            if i == "(":
                self.__flag = self.__flag + 1
            elif i == ")":
                self.__flag = self.__flag - 1
            if self.__flag < 0:
                logging.error("Incorrect order of brackets")
        if self.__flag != 0:
            logging.error("Incorrect number of brackets")

    def str_tolist(self):
        operate = "+-*/()"
        num = "0123456789"
        str_list = []
        i = 0
        while (i < len(self.__str)):
            if self.__str[i] == ' ':
                i = i + 1
                continue
            if self.__str[i] in operate:
                str_list.append(self.__str[i])
            if self.__str[i] in num or self.__str[i] == 'inf':
                for j in range(i + 1, len(self.__str)):
                    if self.__str[j] not in num:
                        str_list.append(self.__str[i:j])
                        i = j - 1
                        break
            if re.match(r'[a-zA-Z]', self.__str[i]) is not None:
                for j in range(i + 1, len(self.__str)):
                    if re.match(r'[a-zA-Z]', self.__str[j]) is None:
                        if self.__str[j] == '(':
                            for k in range(j + 1, len(self.__str)):
                                if self.__str[k] == ')':
                                    str_list.append(self.__str[i:k + 1])
                                    i = k
                                    break
                        else:
                            str_list.append(self.__str[i:j])
                            i = j - 1
                        break
            i = i + 1
        return str_list

    @types({1: str})
    def value_replace(self, input):
        value = []
        for i in range(len(input)):
            if input[i] in self.__parameter.keys():
                value.append(str(self.__parameter[input[i]]))
            else:
                value.append(input[i])
        if len(input) > 1:
            return "".join(value)
        else:
            return value[0]

    def process(self):
        str_list = self.str_tolist()
        value = [self.value_replace(i) for i in str_list]
        for ele in value:
            if re.match(r'[a-zA-Z]', ele) is not None:
                for i in range(len(ele)):
                    if re.match(r'[a-zA-Z]', ele[i]) is None:
                        num = re.findall(raw, ele)
                        t = value.index(ele)
                        parameter = tuple([float(i) for i in num])
                        value[t] = str(self.__func_dic(*parameter))
                        break
        return value


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


@types({1: str})
def direct_cal(infix):
    cal_class = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    list = infix
    numStack = Stack()
    opStack = Stack()
    for x in list:
        if re.match(raw, x) is not None:
            numStack.push(float(x))
        elif x == "(":
            opStack.push(x)
        elif x == ")":
            y = opStack.pop()
            while not y == "(":
                b = numStack.pop()
                a = numStack.pop()
                numStack.push(simple_cal(a, b, y))
                y = opStack.pop()
        elif x in "*/+-":
            p = cal_class[x]
            q = opStack.peek()
            while (not opStack.isEmpty()) and (cal_class[q] >= p):
                b = numStack.pop()
                a = numStack.pop()
                y = opStack.pop()
                numStack.push(simple_cal(a, b, y))
            opStack.push(x)
    while not opStack.isEmpty():
        b = numStack.pop()
        a = numStack.pop()
        y = opStack.pop()
        numStack.push(simple_cal(a, b, y))
    return numStack.pop()


@types({1: float, 2: str, 3: str})
def simple_cal(a, b, x):
    if x == "*":
        return a * b
    elif x == "/":
        return a / b
    elif x == "+":
        return a + b
    elif x == "-":
        return a - b

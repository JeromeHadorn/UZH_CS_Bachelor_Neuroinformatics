import ast, os
from unittest import TestCase
from public.script import req_steps


class PrivateTestSuite(TestCase):

    def _assert(self, n, expected):
        self.assert_recursion()
        actual = req_steps(n)
        m = "@@The calculation is not correct for {} disks.@@".format(n)
        self.assertEqual(expected, actual, m)

    def assert_recursion(self):
        # adopt working directory
        path = "public/script.py" if os.path.exists("public/script.py") else "../public/script.py"
        with open(path) as f:
            tree = ast.parse(f.read())

            v = RecursionTestVisitor()
            v.visit(tree)

            m = "@@Required function 'req_steps' not found.@@"
            self.assertTrue("req_steps" in v.calls.keys(), m)

            m = "@@No recursive call found in the function body of 'req_steps'.@@"
            self.assertTrue("req_steps" in v.calls["req_steps"], m)

    def test_1(self):
        self._assert(1, 1)

    def test_2(self):
        self._assert(2, 3)

    def test_3(self):
        self._assert(3, 7)

    def test_4(self):
        self._assert(4, 15)

    def test_5(self):
        self._assert(5, 31)

    def test_6(self):
        self._assert(6, 63)

    def test_8(self):
        self._assert(8, 255)

    def test_12(self):
        self._assert(12, 4095)



class RecursionTestVisitor(ast.NodeVisitor):

    def __init__(self):
        self.calls = {}
        self.__current = []

    def visit_FunctionDef(self, node):
        self.__current = []
        self.calls[node.name] = self.__current
        self.generic_visit(node)
        self.__current = []

    def visit_Call(self, node):
        if "id" in node.func._fields:
            self.__current.append(node.func.id)
        self.generic_visit(node)

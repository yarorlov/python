from ..ex5.cat import parser
from ..ex5.cat import output
import os


def test_cat_parser():
    args = parser.parse_args("a.txt b.txt".split())
    assert args.files == ['a.txt', 'b.txt']

def test_cat_output():
    args = parser.parse_args("tests/a.txt tests/b.txt".split())
    with open("tests/tested_output.txt", 'w') as t:
        output(args.files, file = t)
    t.close()
    expected = open("tests/expected_output.txt", 'r')
    tested = open('tests/tested_output.txt', 'r')
    assert expected.read() == tested.read()
    expected.close()
    tested.close()
    os.remove(os.path.abspath('tests/tested_output.txt'))
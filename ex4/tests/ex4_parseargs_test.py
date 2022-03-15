
from ..ex4.parseargs import parser




def test_parseargs():
    test_args = parser.parse_args("first 2 -u".split())
    print(dir(test_args))
    assert test_args.arguments == ['first', '2']
    assert test_args.up == True



from ..ex4.parseargs import parser




def test_parseargs():
    args = parser.parse_args("first 2 -u -n".split())
    print(dir(args))
    assert args.arguments == ['first', '2']
    assert args.up == True
    assert args.number == 42


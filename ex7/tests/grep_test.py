
from ex7 import grep




def test_pattern_matching():
    assert grep.pattern_matching(r'[\d+].[\d].[\d+]', './tests/test.txt') == ['WALKING ~!@#$% 123 1.2.3.']



from ex7 import grep




def test_pattern_matching():
    assert grep.pattern_matching(r'[\d+].[\d].[\d+]', './tests/test.txt') == ['WALKING ~!@#$% 123 1.2.3.\n']
    assert grep.pattern_matching(r'ab?', './tests/test.txt')[0].strip() == 'aaaaaaa'
    assert grep.pattern_matching(r'ab*', './tests/test.txt')[1].strip() == 'ab'
    

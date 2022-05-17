
from ex6 import find
import os


def test_path_finder():
    assert find.path_finder('.') == os.getcwd()
    assert find.path_finder('C:\\') == 'C:\\'

def test_search_files():
    
    assert find.search_files(os.path.join(os.getcwd(),'tests'),'nd_') == ['find_test.py']



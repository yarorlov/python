
from ex9.sed import sed 




def test_sed():
    flags = {'inplace':False}
    assert sed(r'w+', 'WW', './tests/test_doc.txt', **flags) == 'A WWhirling WWind ges through my bones' # special mistake in word 'ges'
    

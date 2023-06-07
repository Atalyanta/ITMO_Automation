
def test_homeworkA():
    a = ['home', 'work']
    b = ['home', 'work']
    assert a == b


def test_homeworkB():
    assert not 'QA' == 'QC'


def test_homeworkC():
    x = [1, 1, 2, 3, 5]
    y = [2, 3, 5]
    assert x != y

import pytest

def sum1 (N):
    result = 0 
    for x in range(1, N+1):
        result = result + x
    return result

# 3 теста

@pytest.mark.parametrize('N, res', [(10, 55), (0, 0), (1, 1),
    # негавтиная проверка
                        pytest.param(-5, -40, marks=pytest.mark.xfail),    
                        pytest.param(-1, 0, marks=pytest.mark.xfail)])    


def test_sum1(N, res):
    result = sum1(N)
    assert res == result
from unit_test import calc_md5

def test_calc_md5():
    actual = calc_md5(" This is Content ")
    print(actual)
    assert actual == "e61994e96b20e3965b61de16077e18c7", 'NG'


if __name__ == "__main__":
    test_calc_md5()
from validation import validate

class TestValidate:
    def test_valid(self):
        """検証が正しい場合
        """
        assert validate('a')
        assert validate('a' * 50)
        assert validate('a' * 100)

    def test_invalid_too_short(self):
        """検証が正しくない: 文字が短すぎる場合
        memo: assert not にしているから何も出力されなければOK
        """
        assert not validate("")

    def test_invalid_too_long(self):
        """検証が正しくない: 文字が長すぎる場合
        """
        assert not validate("a" * 101)


def main():
    test = TestValidate()
    test.test_valid()
    test.test_invalid_too_short()
    test.test_invalid_too_long()

if __name__ == "__main__":
    main()

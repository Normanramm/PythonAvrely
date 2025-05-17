from unittest import TestCase, main
from MyPrograms.alesson import qwerty


class QwertyTest(TestCase):
    def test_plus(self):
        self.assertEqual(qwerty.plus(1, 1), 1)


if __name__ == '__main__':
    main()

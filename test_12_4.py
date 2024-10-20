import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8',
    filemode='w'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Арсен", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.warning(e, exc_info=True)

    def test_run(self):
        try:
            runner = Runner(12345)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(e, exc_info=True)

if __name__ == '__main__':
    unittest.main()

# Задача "Заморозка кейсов":
# Подготовка:
# В этом задании используйте те же TestCase, что и в предыдущем: RunnerTest и TournamentTest.
# Часть 1. TestSuit.
# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
# Часть 2. Пропуск тестов.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod),
# который при значении is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
# 'Тесты в этом кейсе заморожены'.
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
# Пример результата выполнения тестов:
# Вывод на консоль:
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s OK (skipped=3)

import unittest

from runner_and_tournament import Runner
from runner_and_tournament import Tournament


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        return method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("TestRunner", 5)

    @skip_if_frozen
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 5)

    @skip_if_frozen
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 15)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner("Runner1", 5)
        self.runner2 = Runner("Runner2", 6)
        self.tournament = Tournament(100, self.runner1, self.runner2)

    @skip_if_frozen
    def test_first_tournament(self):
        results = self.tournament.start()
        self.assertEqual(results[1], self.runner2)

    @skip_if_frozen
    def test_second_tournament(self):
        results = self.tournament.start()
        self.assertEqual(results[2], self.runner1)

    @skip_if_frozen
    def test_third_tournament(self):
        results = self.tournament.start()
        self.assertEqual(results[1], self.runner2)
        self.assertEqual(results[2], self.runner1)


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())



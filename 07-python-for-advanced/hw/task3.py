"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""

import unittest
from task2 import Message
from task1 import SiamObj
import time


class TestMessage(unittest.TestCase):

    def test_creating(self):
        m = Message()
        self.assertEqual(type(m.msg), str)

    def test_reset_timer(self):
        m = Message()
        result = m.msg
        self.assertEqual(m.msg, result)
        time.sleep(1)
        self.assertEqual(m.msg, result)
        m.msg = 'test_message'
        self.assertNotEqual(m.msg, result)
        result = m.msg
        time.sleep(1)
        self.assertEqual(m.msg, result)

    def test_cache_dump(self):
        m = Message()
        result = m.msg
        self.assertEqual(m.msg, result)
        time.sleep(1)
        self.assertEqual(m.msg, result)


if __name__ == '__main__':
    unittest.main()
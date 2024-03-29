# from django.test import TestCase
from unittest import TestCase


# Create your tests here.
def sum_of_two_integers(a, b):
    return a + b


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_two_integers(1, 2), 3)
        self.assertEqual(sum_of_two_integers(2, 2), 4)

import unittest

import leapyear
#import pytest

class TestLeapYear(unittest.TestCase):
    def test_leap_year_divisible_by_4_not_by_100(self):
        self.assertTrue(leapyear.isLeapYear(2004), 'This is a leapyear')
        self.assertTrue(leapyear.isLeapYear(2008), 'This is a leapyear')
        self.assertTrue(leapyear.isLeapYear(2012), 'This is a leapyear')
        self.assertTrue(leapyear.isLeapYear(2020), 'This is a leapyear')


    def test_not_leap_year_divisible_by_100_not_by_400(self):
        self.assertFalse(leapyear.isLeapYear(1700), 'This is not a leapyear')
        self.assertFalse(leapyear.isLeapYear(1800), 'This is not a leapyear')
        self.assertFalse(leapyear.isLeapYear(1900), 'This is not a leapyear')
        self.assertFalse(leapyear.isLeapYear(2100), 'This is not a leapyear')

    def test_leap_year_divisible_by_400(self):
        self.assertTrue(leapyear.isLeapYear(1600), 'this is a leapyear')
        self.assertTrue(leapyear.isLeapYear(2000), 'this is a leapyear')
        self.assertTrue(leapyear.isLeapYear(2400), 'this is a leapyear')
    
    def test_not_leap_year(self):
        self.assertFalse(leapyear.isLeapYear(2023), 'this is not a leapyear')
        self.assertFalse(leapyear.isLeapYear(2022), 'this is not a leapyear')
        self.assertFalse(leapyear.isLeapYear(2021), 'this is not a leapyear')

import leapyear
import pytest

def test_leap_year_divisible_by_4_not_by_100():
    assert leapyear.isLeapYear(2004) == True
    assert leapyear.isLeapYear(2008) == True
    assert leapyear.isLeapYear(2012) == True
    assert leapyear.isLeapYear(2020) == True

def test_not_leap_year_divisible_by_100_not_by_400():
    assert leapyear.isLeapYear(1700) == False
    assert leapyear.isLeapYear(1800) == False
    assert leapyear.isLeapYear(1900) == False
    assert leapyear.isLeapYear(2100) == False

def test_leap_year_divisible_by_400():
    assert leapyear.isLeapYear(1600) == True
    assert leapyear.isLeapYear(2000) == True
    assert leapyear.isLeapYear(2400) == True

def test_not_leap_year():
    assert leapyear.isLeapYear(2023) == False
    assert leapyear.isLeapYear(2022) == False
    assert leapyear.isLeapYear(2021) == False

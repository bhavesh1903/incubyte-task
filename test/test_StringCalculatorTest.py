from unittest import TestCase
from calculator.StringCalculator import *
import pytest
class test_StringCalculatorTest(TestCase):
    def test_stringCalculator_return_zero_on_empty_string(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("")
        assert result==0

    def test_stringCalculator_return_value_on_single_value(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("1")
        assert result==1

    def test_stringCalculator_return_sumation_on_two_value(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("1,2")
        assert result==3

    def test_multiple_number_return_sumation(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("2,3,5")
        assert result==10

    def test_number_with_newline_return_sumation(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("1\n2,3")
        assert result==6

    def test_different_delimiter(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("//;\n11;22")
        assert result==33

    def test_greater_than_thousand(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("//;\n1005,2;3")
        assert result==5

    def test_delimiter_any_len(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("//[###]\n1###20###13")
        assert result==34

    def test_multiple_delimiter(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("//[#][$]\n1$20#13")
        assert result==34

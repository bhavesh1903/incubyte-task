from unittest import TestCase
from calculator.StringCalculator import *

class test_StringCalculatorTest(TestCase):
    def test_stringCalculator_return_zero_on_empty_string(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("")#exercise
        assert result==0#validate

    def test_stringCalculator_return_value_on_single_value(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("1")#exercise
        assert result==1#validate

    def test_stringCalculator_return_sumation_on_two_value(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("1,2")#exercise
        assert result==3#validate

    def test_multiple_number_return_sumation(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("2,3,5")#exercise
        assert result==10#validate

    def test_number_with_newline_return_sumation(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("1\n2,3")#exercise
        assert result==6#validate

    def test_different_delimiter(self):
        stringCalculatorObj=StringCalculator()
        result=stringCalculatorObj.addition("//;\n11;22")#exercise
        assert result==33#validate

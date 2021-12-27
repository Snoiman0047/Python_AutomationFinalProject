import allure
import pytest

from work_flows.desktop_flows import CalculatorFlows


@pytest.mark.usefixtures('init_desktop')
class Test_CalculatorSystem:

    @allure.title('Test01: Mathematical exercise of addition action.')
    @allure.description('Test description: test mathematical exercise of addition action.')
    @pytest.mark.order(0)
    def test_addition(self):
        CalculatorFlows.calc_it('4+2')
        CalculatorFlows.verify_calc_result('6', 'addition')

    @allure.title('Test02: Mathematical exercise of combination action.')
    @allure.description('Test description: test mathematical exercise of combination action.')
    @pytest.mark.order(1)
    def test_combination(self):
        CalculatorFlows.calc_it('10*3+5=/7')
        CalculatorFlows.verify_calc_result('5', 'combination')

    @allure.title('Test03: Mathematical exercise of division action.')
    @allure.description('Test description: test mathematical exercise of division action.')
    @pytest.mark.order(2)
    def test_division(self):
        CalculatorFlows.calc_it('22/11')
        CalculatorFlows.verify_calc_result('2', 'division')

    @allure.title('Test04: Mathematical exercise of multiplication action.')
    @allure.description('Test description: test mathematical exercise of multiplication action.')
    @pytest.mark.order(3)
    def test_multiplication(self):
        CalculatorFlows.calc_it('9*5')
        CalculatorFlows.verify_calc_result('45', 'multiplication')

    @allure.title('Test05: Mathematical exercise of subtraction action.')
    @allure.description('Test description: test mathematical exercise of subtraction action.')
    @pytest.mark.order(4)
    def test_subtraction(self):
        CalculatorFlows.calc_it('8-6')
        CalculatorFlows.verify_calc_result('2', 'subtraction')


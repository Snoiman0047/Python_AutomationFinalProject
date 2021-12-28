import allure
import pytest

from main.utilities.auxiliary_methods import get_actions
from main.work_flows.desktop_flows import CalculatorFlows


@pytest.mark.usefixtures('init_desktop')
class Test_CalculatorSystem:

    @allure.title('Test: Mathematical exercise of addition action.')
    @allure.description('Test description: test mathematical exercise of action.')
    @pytest.mark.parametrize('mathematical_exercise, expected_calc_result, action_name', get_actions())
    def test_addition(self, mathematical_exercise, expected_calc_result, action_name):
        CalculatorFlows.calc_it(mathematical_exercise)
        CalculatorFlows.verify_calc_result(expected_calc_result, action_name)



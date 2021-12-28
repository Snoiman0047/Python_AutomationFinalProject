import allure
import pytest

from main.work_flows.electron_flows import DemosFlow


@pytest.mark.usefixtures('init_electron')
class Test_Demos:

    @allure.title('Test01: Copy action.')
    @allure.description('Test description: test copy from clipboard action.')
    def test_copy_action(self):
        DemosFlow.copy_action('This is Electron App :)')
        DemosFlow.verify_copy_action()
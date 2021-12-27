import allure

from extensions.ui_actions import WebUiAction
from page_objects.appium.appium_page import appium_page


class mobile_work_flow:
    app_po = appium_page(driver)

    @allure.step("loan calculator")
    def loan_calc(self,la,ir,ly,lm,epm):
        WebUiAction.click_on(self.app_po.loan_calc)
        WebUiAction.send_keys(self.app_po.loan_amount, la)
        WebUiAction.send_keys(self.app_po.interest_rate, ir)
        WebUiAction.send_keys(self.app_po.loan_year, ly)
        WebUiAction.send_keys(self.app_po.loan_month, lm)
        WebUiAction.send_keys(self.app_po.extra_per_month, epm)
        WebUiAction.click_on(self.app_po.calc)



    def monthly_payment(self):
        WebUiAction.get_text(self.monthly_payment)

    def total_payment(self):
        WebUiAction.get_text(self.total_payment)


    def total_interest(self):
        WebUiAction.get_text(self.total_interest)

    def annual_payment(self):
        WebUiAction.get_text(self.annual_payment)

    def interest_saving(self):
        WebUiAction.get_text(self.interest_saving)







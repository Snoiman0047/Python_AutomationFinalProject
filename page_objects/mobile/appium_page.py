from selenium.webdriver.common.by import By


class appium_page:

    loan_calc = (By.XPATH, "//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Loan Calculator']]")

    loan_amount = (By.XPATH,"//*[@id='loanAmount']")

    interest_rate = (By.ID, "interestRate")

    loan_year = (By.XPATH, "//*[@id='loanYear']")

    loan_month = (By.XPATH, "//*[@id='loanMonth']")

    extra_per_month = (By.XPATH, "//*[@id='extraPerMonth']")

    calc = (By.XPATH, "//*[@id='calc']")

    #res

    monthly_payment = (By.XPATH, "//*[@id='monthlyPayment']")

    total_payment = (By.XPATH, "//*[@id='totalPayment']")

    total_interest = (By.XPATH, "//*[@id='totalInterest']")

    annual_payment = (By.XPATH, "//*[@id='annualPayment']")

    interest_saving = (By.XPATH, "//*[@id='interestSaving']")









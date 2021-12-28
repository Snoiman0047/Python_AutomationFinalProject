import allure


class Verifications:

    @staticmethod
    @allure.step("Verify the actual text is the same as expected text.")
    def verify_equals(actual_text, expected_text, massage):
        assert actual_text == expected_text, massage

    @staticmethod
    @allure.step("Verify the condition is true")
    def verify_true(condition, massage):
        assert (condition, massage)

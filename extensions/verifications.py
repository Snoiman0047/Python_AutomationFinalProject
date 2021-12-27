import allure


class Verifications:

    @staticmethod
    @allure.step("Verify the actual text is the same as expected text.")
    def string_value(actual_text, expected_text, massage):
        assert actual_text == expected_text, massage
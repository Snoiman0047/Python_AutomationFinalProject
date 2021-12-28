import xml.etree.ElementTree as ET

import allure


@allure.step('Get data from config_data.xml.')
def get_data(node_name):
    root = ET.parse('C:/Automation/Python_AutomationFinalProject/configuration/data_config.xml').getroot()
    return root.find(".//" + node_name).text


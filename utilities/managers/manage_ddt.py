import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:\Python_AutomationFinalProject\configuration\data_config.xml').getroot()
    return root.find(".//" + node_name).text
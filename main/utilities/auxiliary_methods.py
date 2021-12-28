from main.utilities.manage_ddt import get_data


def get_actions():
    math_actions_string = get_data('ACTIONS')
    math_actions = math_actions_string.split(' # ')
    for index in range(len(math_actions)):
        actions = math_actions[index].split(', ')
        math_actions[index] = tuple(actions)
    return math_actions


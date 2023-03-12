SETTINGS = {"PLAYER_COLOR" : "GREEN", "CPU_COLOR" : "BLUE", "PLAYER_MARK" : "X"}
PATH = 'settings.ini'


def get_settings():
    global SETTINGS
    return SETTINGS

def set_settings(settings):
    global SETTINGS
    SETTINGS = settings

def save_settings():
    global PATH
    settings = ''
    for key, value in SETTINGS.items():
        settings += str(key) + ":" + str(value) + "\n"
    with open(PATH, 'w') as data:
        data.write(settings)

def load_settings():
    global PATH
    global SETTINGS
    result = {}
    with open(PATH) as data:
        settings = data.readlines()
    for element in settings:
        temp = element.strip().split(':')
        result[temp[0]] = temp[1]
    SETTINGS = result

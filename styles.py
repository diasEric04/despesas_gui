import qdarktheme
import os.path
import json

# Classe[property='valor da property'](:acao) {
#   estilo qss dos elementos
# }

QSS = ''


def setupTheme(dataFolder):
    THEME_JSON_FOLDER = dataFolder / 'theme.json'
    if not os.path.exists(THEME_JSON_FOLDER):
        with open(THEME_JSON_FOLDER, 'w', encoding='utf8') as jsonFile:
            themeDict = {
                'theme': 'light'  # defalut
            }
            json.dump(themeDict, jsonFile)
    with open(THEME_JSON_FOLDER, 'r', encoding='utf8') as jsonFile:
        jsonDict = json.load(jsonFile)
        theme = jsonDict['theme']

    qdarktheme.setup_theme(
        theme=theme,
        corner_shape='rounded',
        additional_qss=QSS
    )


def setTheme(dataFolder, theme):
    THEME_JSON_FOLDER = dataFolder / 'theme.json'
    with open(THEME_JSON_FOLDER, 'w', encoding='utf8') as jsonFile:
        themeDict = {
            'theme': theme
        }
        json.dump(themeDict, jsonFile)

import qdarktheme
import os.path
import json
import data

# Classe[property='valor da property'](:acao) {
#   estilo qss dos elementos
# }
dataFolder = data.initData()
THEME_JSON_FOLDER = dataFolder / 'theme.json'
QSS = ''


def setupTheme():
    if not os.path.exists(THEME_JSON_FOLDER):
        setTheme('light')
    theme = getTheme()

    qdarktheme.setup_theme(
        theme=theme,
        corner_shape='rounded',
        additional_qss=QSS
    )


def setTheme(theme):
    with open(THEME_JSON_FOLDER, 'w', encoding='utf8') as jsonFile:
        themeDict = {
            'theme': theme
        }
        json.dump(themeDict, jsonFile)


def getTheme():
    with open(THEME_JSON_FOLDER, 'r', encoding='utf8') as jsonFile:
        jsonDict = json.load(jsonFile)
        theme = jsonDict['theme']
    return theme


BIG_FONT_SIZE = 26
MEDIUM_FONT_SIZE = 22
SMALL_FONT_SIZE = 18

TEXT_MARGIN = 15

MINIMUM_WIDTH = 350

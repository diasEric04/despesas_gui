from pathlib import Path

USER_HOME = Path.home()
APPDATA_PATH = USER_HOME / 'AppData' / 'Roaming'
DATA_PATH = APPDATA_PATH / 'despesas_data_folder'


def initData() -> Path:
    DATA_PATH.mkdir(exist_ok=True)
    return DATA_PATH

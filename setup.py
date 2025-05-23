from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon/icon.icns',
    'plist': {
        'CFBundleName': "EcoProgramBelonogov",
        'CFBundleShortVersionString': "1.0.0",
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
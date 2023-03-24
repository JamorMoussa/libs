import os

global abs_path

abs_path = os.path.abspath(__file__).split('\\__init__.py')[0]
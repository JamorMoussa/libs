import os
global css_path
from ... import abs_path

css_path = os.path.abspath(f'{abs_path}/view/style/style.css')
css_dir = css_path.split('/style.css')[0]

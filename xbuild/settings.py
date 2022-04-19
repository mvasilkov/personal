from pathlib import Path
import platform

OUR_ROOT = Path(__file__).parents[1].resolve()
NODE_MODULES = OUR_ROOT / 'node_modules'

NODE_USE_SHELL = platform.system() == 'Windows'

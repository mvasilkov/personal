from pathlib import Path
import platform

PHP_ROOT = Path(__file__).parents[1].resolve()
NODE_MODULES = PHP_ROOT / 'node_modules'

NODE_USE_SHELL = platform.system() == 'Windows'

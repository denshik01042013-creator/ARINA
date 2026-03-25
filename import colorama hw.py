import colorama
from colorama import Fore, Back, Style
import inspect

colorama.init()

print("=== Інтроспекція модуля colorama ===")
print("Атрибути модуля:")
print(dir(colorama))

print("\n=== Основні класи ===")
for name, obj in inspect.getmembers(colorama):
    if inspect.isclass(obj):
        print(name)

print("\n=== Атрибути Fore ===")
print(dir(Fore))

print("\n=== Атрибути Back ===")
print(dir(Back))

print("\n=== Атрибути Style ===")
print(dir(Style))

print("\n=== Методи colorama ===")
for name, obj in inspect.getmembers(colorama):
    if inspect.isfunction(obj):
        print(name)
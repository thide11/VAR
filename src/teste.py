import re

teste = "testando\n\ntestestando2\n\n\ntesteando3"

blocks = re.split("\n\n\n?", teste)
print(blocks);
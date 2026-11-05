# import pathlib as Path
from pathlib import Path

Path("bcit.txt").write_text("hello")
Path("bcit.txt").write_text("bcit")
data = Path("bcit.txt").read_text()
print(data)

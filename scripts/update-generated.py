"""Apply dependency metadata and urllib3 compatibility after regeneration."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "src"
requirements = (root / "requirements.txt").read_text()
(out / "requirements.txt").write_text(requirements)
setup = (out / "setup.py").read_text()
setup = re.sub(r"REQUIRES = \[.*?\]", "REQUIRES = " + repr(requirements.splitlines()), setup, count=1, flags=re.S)
setup = re.sub(r'    python_requires="[^"\n]+",\n', "", setup)
setup = setup.replace("setup(\n", 'setup(\n    python_requires=">=3.10",\n')
(out / "setup.py").write_text(setup)
(out / "pyproject.toml").write_text('[build-system]\nrequires = ["setuptools>=84.0.0"]\nbuild-backend = "setuptools.build_meta"\n')
rest = out / "wodby" / "rest.py"
source = rest.read_text().replace("self.urllib3_response.getheaders()", "self.urllib3_response.headers")
source = source.replace("self.urllib3_response.getheader(name, default)", "self.urllib3_response.headers.get(name, default)")
rest.write_text(source)
(out / "setup.py.orig").unlink(missing_ok=True)

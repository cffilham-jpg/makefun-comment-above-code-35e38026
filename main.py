"""Write one UTF-8 production-code comment to the requested output directory.
The precise sleep and structural twist make fragile timing immediately concrete.
"""

import os
from pathlib import Path


LINE = "// This sleep(400) is load-bearing."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 200:
    raise ValueError("The entry line must be at most 200 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))

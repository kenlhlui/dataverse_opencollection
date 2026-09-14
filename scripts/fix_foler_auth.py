"""Post-process vacuum's OpenCollection output so folders inherit collection auth.

vacuum's `open-collection` writes every folder.yml without a `request.auth`
block. Bruno's OpenCollection parser turns a missing folder auth into
`mode: none`, and at send time a folder whose auth mode is anything other
than `inherit` overrides the collection-level auth. The result: every
request inside a folder silently drops the X-Dataverse-Key header.
Writing an explicit `auth: inherit` into each folder.yml restores the
collection -> folder -> request inheritance chain.
"""

import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "dataverse_endpoints")


def has_auth(lines: list[str]) -> bool:
    """Return True if the folder.yml already declares a request.auth entry."""
    in_request = False
    for line in lines:
        if line.startswith("request:"):
            in_request = True
            continue
        if in_request:
            # A new top-level key ends the request block.
            if line and not line[0].isspace():
                in_request = False
                continue
            if line.strip().startswith("auth:"):
                return True
    return False


def patch_folder(path: Path) -> bool:
    """Add `request.auth: inherit` to one folder.yml; return True if changed."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if has_auth(lines):
        return False

    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if line.startswith("request:") and not inserted:
            out.append("    auth: inherit")
            inserted = True

    if not inserted:
        # No request block at all -> append one.
        out.append("request:")
        out.append("    auth: inherit")

    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return True


def main() -> None:
    """Patch every folder.yml under the collection directory."""
    changed = 0
    folders = sorted(ROOT.rglob("folder.yml"))
    for folder in folders:
        if patch_folder(folder):
            changed += 1
    print(f"Patched {changed} of {len(folders)} folder.yml files")


if __name__ == "__main__":
    main()

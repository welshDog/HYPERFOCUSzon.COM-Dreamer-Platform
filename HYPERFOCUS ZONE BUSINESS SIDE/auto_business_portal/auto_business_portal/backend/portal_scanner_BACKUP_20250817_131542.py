"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
portal_scanner.py
-------------------

Utility functions for discovering and describing business portals.  This
module scans a configurable base directory (by default ``portals``) for
HTML files that represent individual portals.  Each portal file is
converted into a simple JSON-friendly dictionary containing a user‑friendly
``name`` and the file ``path`` relative to the project root.  You could
extend this helper to parse additional metadata, such as reading
``title`` tags from the HTML or loading a manifest file.  For the
purposes of the BROski auto–business system, this scanner provides
the foundation for the master directory listing.

This scanner is deliberately lightweight and synchronous – it can be
called at start‑up or on demand.  See ``backend/app.py`` for an example
of how it is used.

Example usage::

    from portal_scanner import scan_portals
    portals = scan_portals('portals')
    for portal in portals:
        print(portal['name'], portal['path'])

"""

import os
from pathlib import Path
from typing import List, Dict


def humanize_portal_name(filename: str) -> str:
    """Convert a file name like ``admin-portal-showcase.html`` into a
    human friendly name such as ``Admin Portal Showcase``.

    Parameters
    ----------
    filename : str
        The base name of the portal file.

    Returns
    -------
    str
        A capitalized, space separated version of the file name.
    """
    name = Path(filename).stem  # remove .html extension
    # replace dashes/underscores with spaces and capitalize words
    words = name.replace('_', ' ').replace('-', ' ').split()
    return ' '.join(word.capitalize() for word in words)


def scan_portals(base_dir: str = 'portals') -> List[Dict[str, str]]:
    """Scan a directory for portal HTML files.

    This function looks for all ``.html`` files under the given
    directory and returns a list of dictionaries.  Each dictionary
    contains at least two keys: ``name`` – a human friendly title, and
    ``path`` – the relative filesystem path to the portal file.  If no
    portals are found, an empty list is returned.

    Parameters
    ----------
    base_dir : str, optional
        The directory to search (defaults to ``'portals'``).

    Returns
    -------
    List[Dict[str, str]]
        A list of portal descriptors.
    """
    portals: List[Dict[str, str]] = []
    directory = Path(base_dir)
    if not directory.exists():
        return portals

    for item in sorted(directory.iterdir()):
        # Only consider HTML files at the top level.  For a real system
        # you might recursively search or apply further filtering.
        if item.is_file() and item.suffix.lower() == '.html':
            # Convert to absolute path then get relative path from project root
            abs_path = item.resolve()
            try:
                rel_path = abs_path.relative_to(Path.cwd())
            except ValueError:
                # If we can't get relative path from cwd, use the path from base_dir
                rel_path = Path(base_dir) / item.name

            portals.append({
                'name': humanize_portal_name(item.name),
                'path': str(rel_path),
            })

    return portals


if __name__ == '__main__':
    # Allow simple CLI testing: ``python portal_scanner.py`` prints
    # discovered portals from the default ``portals`` directory.
    discovered = scan_portals()
    logger.info("🌌 Discovered portals:")
    for portal in discovered:
        print(f"- {portal['name']}: {portal['path']}")
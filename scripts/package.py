from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from os import PathLike
from typing import Union

def zip_dir(zipfile_name: str, source_dir: Union[str, PathLike]):
    src_path = Path(source_dir).expanduser().resolve(strict=True)

    with ZipFile(zipfile_name, 'w', ZIP_DEFLATED) as zf:
        for file in src_path.rglob('*'):
            # Here, we iterate recursively through the entire dir tree
            # and write each file/folder individually to the zip
            zf.write(file, file.relative_to(src_path.parent))

zip_dir("HideMySeed.mcpack", "HideMySeed")
import os
import shutil
import glob
import gzip
from pathlib import Path


def compress_log_data():
    path = glob.glob("/var/log/*")
    for item in path:
        if not Path(item).suffix == ".gz":
            with open(item, 'rb') as file_in:
                with gzip.open(f"{item}.gz", 'wb') as file_out:
                    shutil.copyfileobj(file_in, file_out)
                    os.unlink(item)


if __name__ == "__main__":
    compress_log_data()

import urllib.request
import shutil
import os


def download_file(url, dest=None, timeout=30):
    if dest is None:
        dest = os.path.basename(url)

    req = urllib.request.Request(url, headers={"User-Agent": "MyLibrary/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status != 200:
                raise RuntimeError(f"HTTP {response.status}")
            with open(dest, "wb") as f:
                shutil.copyfileobj(response, f)
    except Exception as e:
        raise RuntimeError(f"Download failed: {e}")
    return dest

import requests, re
from pathlib import Path



def download_file(url: str, dest: str, chunk_size: int = 8192, timeout: float = 10.0):
    """
    Download `url` to `dest` (file path). Overwrites if exists.
    """
    
    print(f"Downloading: {url}")
    print(f"Destination: {dest}")

    dest_path = Path(dest)
    
    with requests.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with dest_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
    


def download_if_exists(url: str, dest: str, timeout: float = 10.0):
    head = requests.head(url, allow_redirects=True, timeout=timeout)
    if head.status_code == 200:
        download_file(url, dest, timeout=timeout)
    else:
        print(f"Download error: {head.status_code}")



# ZFS Linux

zfs_linux_pattern = re.compile(r'/zfs-linux-[0-9][^/]*\.pkg\.tar\.zst?$', re.I)
zfs_utils_pattern = re.compile(r'/zfs-utils-[0-9][^/]*\.pkg\.tar\.zst?$', re.I)

zfs_linux_url = ''
zfs_utils_url = ''

headers = { 'Accept': 'application/vnd.github+json' }
url = 'https://api.github.com/repos/archzfs/archzfs/releases/tags/experimental'

r = requests.get(url, headers=headers)
r.raise_for_status()

for a in r.json().get('assets', []):
    download_url = a.get('browser_download_url')
    if zfs_linux_pattern.search(download_url.strip()):
        zfs_linux_url = download_url.strip()
    if zfs_utils_pattern.search(download_url.strip()):
        zfs_utils_url = download_url.strip()



# Packages

zfs_linux_pkg_name = ''

linux_pkg_name = ''
linux_headers_pkg_name = ''

match = re.search(r'zfs-linux-[0-9][^_]+_([^/]+)(\.pkg\.tar\.zst)$', zfs_linux_url)
if match:
    zfs_linux_version = match.group(1)
    linux_version = re.sub(r'(\.arch\d)\.\d+\b', r'\1', match.group(1))
    extension = match.group(2)

    zfs_linux_pkg_name = f"zfs-linux-{zfs_linux_version}{extension}"
    linux_pkg_name = f"linux-{linux_version}{extension}"
    linux_headers_pkg_name = f"linux-headers-{linux_version}{extension}"


match = re.search(r'(zfs-utils-[0-9][^/]*\.pkg\.tar\.zst)?$', zfs_utils_url)

zfs_utils_pkg_name = match.group(1)



# Download URLs
 
linux_pkg_url = f"https://archive.archlinux.org/packages/l/linux/{linux_pkg_name}"
linux_headers_pkg_url = f"https://archive.archlinux.org/packages/l/linux-headers/{linux_headers_pkg_name}"

linux_pkg_dest_path = f"./{linux_pkg_name}"
linux_headers_pkg_dest_path = f"./{linux_headers_pkg_name}"

zfs_linux_pkg_dest_path = f"./{zfs_linux_pkg_name}"
zfs_utils_pkg_dest_path = f"./{zfs_utils_pkg_name}"

download_if_exists(zfs_linux_url, zfs_linux_pkg_dest_path)
download_if_exists(zfs_utils_url, zfs_utils_pkg_dest_path)

download_if_exists(linux_pkg_url, linux_pkg_dest_path)
download_if_exists(linux_headers_pkg_url, linux_headers_pkg_dest_path)

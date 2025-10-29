import requests, re
from pathlib import Path



def download_file(url: str, dest: str, chunk_size: int = 8192, timeout: float = 10.0):
    """
    Download url to dest (file path). Overwrites if exists.
    """

    dest_path = Path(dest)
    
    with requests.get(url, stream=True, timeout=timeout) as r:
        r.raise_for_status()
        with dest_path.open("wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
    


def download_if_exists(url: str, dest: str, timeout: float = 10.0):
    """
    Download url to dest (file path), only if file on url exists.
    """

    print(f"Downloading: {url}")
    print(f"Destination: {dest}")

    head = requests.head(url, allow_redirects=True, timeout=timeout)
    if head.status_code == 200:
        download_file(url, dest, timeout=timeout)
    else:
        print(f"Download error: {head.status_code}")



def get_archzfs_pkg_download_urls() -> tuple[str | None, str | None]:
    """
    Query GitHub's archzfs repository for the download urls of:
    zfs-linux and zfs-utils packages.
    """

    archzfs_linux_url = None
    archzfs_utils_url = None

    archzfs_linux_pattern = re.compile(r'/zfs-linux-[0-9][^/]*\.pkg\.tar\.zst?$', re.I)
    archzfs_utils_pattern = re.compile(r'/zfs-utils-[0-9][^/]*\.pkg\.tar\.zst?$', re.I)

    headers = { 'Accept': 'application/vnd.github+json' }
    url = 'https://api.github.com/repos/archzfs/archzfs/releases/tags/experimental'

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    for a in r.json().get('assets', []):
        download_url = a.get('browser_download_url')
        if archzfs_linux_pattern.search(download_url.strip()):
            archzfs_linux_url = download_url.strip()
        if archzfs_utils_pattern.search(download_url.strip()):
            archzfs_utils_url = download_url.strip()

    return (archzfs_linux_url, archzfs_utils_url)



def get_pkg_names(archzfs_linux_url: str, archzfs_utils_url: str) -> dict:
    """
    Parse archzfs download urls to get names of corresponding packages.
    """

    pkg_names = {
        'archzfs_linux': None,
        'archzfs_utils': None,
        'arch_linux': None,
        'arch_linux_headers': None
    }

    zfs_linux_pkg_name = ''

    linux_pkg_name = ''
    linux_headers_pkg_name = ''

    match = re.search(r'zfs-linux-[0-9][^_]+_([^/]+)(\.pkg\.tar\.zst)$', archzfs_linux_url)
    if match:
        archzfs_linux_version = match.group(1)
        # Remove the '.N' (N=1,2...) suffix from archzfs package name (only difference between names)
        arch_linux_version = re.sub(r'(\.arch\d)\.\d+\b', r'\1', match.group(1))
        extension = match.group(2)

        pkg_names['archzfs_linux'] = f"zfs-linux-{archzfs_linux_version}{extension}"
        pkg_names['arch_linux'] = f"linux-{arch_linux_version}{extension}"
        pkg_names['arch_linux_headers'] = f"linux-headers-{arch_linux_version}{extension}"


    match = re.search(r'(zfs-utils-[0-9][^/]*\.pkg\.tar\.zst)?$', archzfs_utils_url)
    if match:
        pkg_names['archzfs_utils'] = match.group(1)

    return pkg_names



if __name__ == "__main__":

    """
    Goal: to download latest archzfs packages and associated Arch Linux kernel and headers.
    Later: use those packages to update system with pacman.
    How:
        1. Query the GitHub repository of archzfs for download URLs of zfs-linux and zfs-utils releases.
        2. Identify the associated Arch Linux kernel and headers package names.
        3. Finally download all packages from GitHub and the Arch Linux archive to the current directory.
    """

    # Get archzfs package download urls

    archzfs_linux_url, archzfs_utils_url = get_archzfs_pkg_download_urls()
    
    # And all package names

    if archzfs_linux_url is not None and archzfs_utils_url is not None:

        pkg_names = get_pkg_names(archzfs_linux_url, archzfs_utils_url)

        if all(name is not None for name in pkg_names.values()):
            # Construct arch linux archive download urls
 
            arch_linux_pkg_url = f"https://archive.archlinux.org/packages/l/linux/{pkg_names['arch_linux']}"
            arch_linux_headers_pkg_url = f"https://archive.archlinux.org/packages/l/linux-headers/{pkg_names['arch_linux_headers']}"

            # And destination file paths

            arch_linux_pkg_dest_path = f"./{pkg_names['arch_linux']}"
            arch_linux_headers_pkg_dest_path = f"./{pkg_names['arch_linux_headers']}"

            archzfs_linux_pkg_dest_path = f"./{pkg_names['archzfs_linux']}"
            archzfs_utils_pkg_dest_path = f"./{pkg_names['archzfs_utils']}"

            # Then, download packages

            download_if_exists(archzfs_linux_url, archzfs_linux_pkg_dest_path)
            download_if_exists(archzfs_utils_url, archzfs_utils_pkg_dest_path)

            download_if_exists(arch_linux_pkg_url, arch_linux_pkg_dest_path)
            download_if_exists(arch_linux_headers_pkg_url, arch_linux_headers_pkg_dest_path)

        else:
            print('Could not get package names!')
            print(pkg_names)

    else:
        print('Could not get archzfs package download urls!')


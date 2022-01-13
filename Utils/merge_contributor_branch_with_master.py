import logging
import subprocess
import sys

CONTENT_URL = 'https://github.com/demisto/content.git'


def main():
    try:
        subprocess.run(['git', 'remote', 'add', 'upstream_content', CONTENT_URL])
        subprocess.run(['git', 'fetch', 'upstream'])
        subprocess.run(['git', 'checkout', 'master'])
        subprocess.run(['git', 'rebase', 'upstream/master'])
        subprocess.run(['git', 'push', '-f', 'origin', 'master'])
        subprocess.run(['git', 'pull', 'origin', 'master'])
    except Exception as e:
        logging.exception(f'An error occured while trying to fetch and rebase from content master. {e}')
        sys.exit(1)
    logging.debug("fetch and rebase from content master is done.")


if __name__ == "__main__":
    main()

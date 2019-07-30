import os
import errno

def make_missing_paths(dir_path):
    if not os.path.exists(os.path.dirname(dir_path)):
        try:
            os.makedirs(os.path.dirname(dir_path + "/"))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def crawl_for_text(root_dir):
    text_lines = []
    for (dirpath, _, fnames) in os.walk(root_dir):
        for fname in fnames:
            fpath = os.path.join(dirpath, fname)
            with open(fpath) as fh:
                text_lines.extend(fh.readlines())
    return text_lines
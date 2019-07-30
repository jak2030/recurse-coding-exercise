import os
import errno

ROOT_DIR = os.getenv("BARDI_B_DATA_DIR")
SHAKESPEARE_DATA_ROOT = os.path.join(ROOT_DIR, "shakespeare/")

def write_shakespeare(work):
    cleaned_name = work["name"].replace("'", "").replace(" ", "-").replace(",", "")
    dir_path = os.path.join(SHAKESPEARE_DATA_ROOT, work["category"] + "/")
    fpath = os.path.join(dir_path, cleaned_name)
    # TODO centralized this file-making logic
    if not os.path.exists(os.path.dirname(dir_path)):
        try:
            os.makedirs(os.path.dirname(dir_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    print("Writing results to {}".format(fpath))
    with open(fpath, "w") as fh:
        fh.write(work["text"])
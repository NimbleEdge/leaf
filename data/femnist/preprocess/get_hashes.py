import hashlib
import os
import sys
import tqdm
from multiprocessing import Pool
from tqdm import tqdm

utils_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils_dir = os.path.join(utils_dir, "utils")
sys.path.append(utils_dir)

import util

parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

cfd = os.path.join(parent_path, "data", "intermediate", "class_file_dirs")
wfd = os.path.join(parent_path, "data", "intermediate", "write_file_dirs")
class_file_dirs = util.load_obj(cfd)
write_file_dirs = util.load_obj(wfd)

class_file_hashes = []
write_file_hashes = []


def create_hash(tup):

    (cclass, cfile) = tup
    file_path = os.path.join(parent_path, cfile)

    chash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
    return (cclass, cfile, chash)


def write_hashed_image(tup):
    (cclass, cfile) = tup
    file_path = os.path.join(parent_path, cfile)

    chash = hashlib.md5(open(file_path, "rb").read()).hexdigest()
    return (cclass, cfile, chash)


if __name__ == "__main__":
    p = Pool(processes=20)
    class_file_hashes = list(
        tqdm(p.imap(create_hash, class_file_dirs), total=len(class_file_dirs))
    )
    cfhd = os.path.join(parent_path, "data", "intermediate", "class_file_hashes")
    util.save_obj(class_file_hashes, cfhd)
    write_file_hashes = list(
        tqdm(p.imap(write_hashed_image, write_file_dirs), total=len(write_file_dirs))
    )
    wfhd = os.path.join(parent_path, "data", "intermediate", "write_file_hashes")
    util.save_obj(write_file_hashes, wfhd)

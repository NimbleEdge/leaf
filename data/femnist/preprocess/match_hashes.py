import os
import sys
from tqdm import tqdm
from multiprocessing import Pool

utils_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils_dir = os.path.join(utils_dir, "utils")
sys.path.append(utils_dir)

import util

parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
parent_path = "/mnt/share/femnist"


cfhd = os.path.join(parent_path, "raw", "intermediate", "class_file_hashes")
wfhd = os.path.join(parent_path, "raw", "intermediate", "write_file_hashes")
class_file_hashes = util.load_obj(cfhd)  # each elem is (class, file dir, hash)
write_file_hashes = util.load_obj(wfhd)  # each elem is (writer, file dir, hash)

class_hash_dict = {}
for i in tqdm(range(len(class_file_hashes))):
    (c, f, h) = class_file_hashes[len(class_file_hashes) - i - 1]
    class_hash_dict[h] = (c, f)

write_classes = []
for tup in tqdm(write_file_hashes):
    (w, f, h) = tup
    write_classes.append((w, f, class_hash_dict[h][0]))

wwcd = os.path.join(parent_path, "raw", "intermediate", "write_with_class")
util.save_obj(write_classes, wwcd)

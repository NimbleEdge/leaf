import os
import sys
from tqdm import tqdm

utils_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
utils_dir = os.path.join(utils_dir, "utils")
sys.path.append(utils_dir)

import util

parent_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
parent_path = "/mnt/share/femnist"

wwcd = os.path.join(parent_path, "raw", "intermediate", "write_with_class")
write_class = util.load_obj(wwcd)

writers = []  # each entry is a (writer, [list of (file, class)]) tuple
cimages = []
(cw, _, _) = write_class[0]
for (w, f, c) in tqdm(write_class):
    if w != cw:
        writers.append((cw, cimages))
        cw = w
        cimages = [(f, c)]
    cimages.append((f, c))
writers.append((cw, cimages))

ibwd = os.path.join(parent_path, "raw", "intermediate", "images_by_writer")
util.save_obj(writers, ibwd)

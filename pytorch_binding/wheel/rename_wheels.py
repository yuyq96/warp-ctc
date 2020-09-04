import glob
import os
import shutil
from subprocess import Popen, PIPE

import torch


def get_cuda_version():
    proc = Popen(['nvcc', '--version'], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    out.decode('utf-8').split('\n')[-2].split(', ')[-2].split(' ')
    return out.decode('utf-8').split()[-2][:-1].replace('.', '')


def get_torch_version():
    major_ver, minor_ver = torch.__version__.split('.')[:2]
    return major_ver + minor_ver


local_version_identifier = '+torch{}'.format(get_torch_version())
if torch.cuda.is_available() or "CUDA_HOME" in os.environ:
    enable_gpu = True
    local_version_identifier += ".cuda{}".format(get_cuda_version())
else:
    local_version_identifier = ".cpu"


for whl_path in glob.glob(os.path.join(os.getcwd(), 'dist', '*.whl')):
    whl_name = os.path.basename(whl_path)
    dist, version, python_tag, abi_tag, platform_tag = whl_name.split('-')
    version += local_version_identifier
    platform_tag = platform_tag.replace('linux', 'manylinux1')
    new_whl_name = '-'.join([dist, version, python_tag, abi_tag, platform_tag])
    new_whl_path = os.path.join(os.path.dirname(whl_path), new_whl_name)
    shutil.move(whl_path, new_whl_path)

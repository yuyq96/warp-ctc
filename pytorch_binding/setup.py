import os
import platform
import shutil
import sys
from setuptools import setup, find_packages
from subprocess import Popen, PIPE

from torch.utils.cpp_extension import BuildExtension, CppExtension
import torch

extra_compile_args = ['-std=c++11', '-fPIC']
warp_ctc_build_path = "../build"

if platform.system() == 'Darwin':
    lib_ext = ".dylib"
else:
    lib_ext = ".so"
warp_ctc_libname = 'libwarpctc{}'.format(lib_ext)

if "WARP_CTC_PATH" in os.environ:
    warp_ctc_build_path = os.environ["WARP_CTC_PATH"]
if not os.path.exists(os.path.join(warp_ctc_build_path, warp_ctc_libname)):
    print(("Could not find {libname} in {build_path}.\n"
           "Build warp-ctc and set WARP_CTC_PATH to the location of"
           " {libname} (default is '../build')").format(
               libname=warp_ctc_libname, build_path=warp_ctc_build_path))
    sys.exit(1)

include_dirs = [os.path.realpath('../include')]

warp_ctc_libpath = "./warpctc_pytorch/lib"
if not os.path.isdir(warp_ctc_libpath):
    os.mkdir(warp_ctc_libpath)
shutil.copyfile(
    '{}/{}'.format(warp_ctc_build_path, warp_ctc_libname),
    '{}/{}'.format(warp_ctc_libpath, warp_ctc_libname)
)


def get_cuda_version():
    proc = Popen(['nvcc', '--version'], stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    out.decode('utf-8').split('\n')[-2].split(', ')[-2].split(' ')
    return out.decode('utf-8').split()[-2][:-1].replace('.', '')


def get_torch_version():
    major_ver, minor_ver = torch.__version__.split('.')[:2]
    return major_ver + minor_ver


if torch.cuda.is_available() or "CUDA_HOME" in os.environ:
    enable_gpu = True
else:
    print("Torch was not built with CUDA support, not building warp-ctc GPU extensions.")
    enable_gpu = False

if enable_gpu:
    from torch.utils.cpp_extension import CUDAExtension

    build_extension = CUDAExtension
    extra_compile_args += ['-DWARPCTC_ENABLE_GPU']
    package_name = 'warpctc_pytorch{}_cuda{}'.format(
        get_torch_version(), get_cuda_version())
else:
    build_extension = CppExtension
    package_name = 'warpctc_pytorch{}_cpu'.format(get_torch_version())

ext_modules = [
    build_extension(
        name='warpctc_pytorch._warp_ctc',
        language='c++',
        sources=['src/binding.cpp'],
        include_dirs=include_dirs,
        library_dirs=[os.path.realpath(warp_ctc_libpath)],
        libraries=['warpctc'],
        extra_link_args=['-Wl,-rpath,{}'.format('$ORIGIN/lib')],
        extra_compile_args=extra_compile_args
    )
]

setup(
    name=package_name,
    version="0.1.1",
    description="Pytorch Bindings for warp-ctc maintained by ESPnet",
    url="https://github.com/espnet/warp-ctc",
    author=','.join([
        "Jared Casper",
        "Sean Naren",
        "Shinji Watanabe",
        "Jiro Nishitoba",
        "Yusuke Nishioka"
    ]),
    author_email=','.join([
        "jared.casper@baidu.com",
        "sean.narenthiran@digitalreasoning.com",
        "sw005320@gmail.com",
        "j.nshtb+github@gmail.com",
        "yusuke.nishioka.0713@gmail.com"
    ]),
    license="Apache",
    packages=find_packages(),
    package_data={'': ['lib/{}'.format(warp_ctc_libname)]},
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExtension}
)

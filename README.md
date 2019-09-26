# PyTorch bindings for Warp-ctc

|branch|status|pypi package|
|:-:|:-:|:-:|
|`pytorch_bindings`|[![Build Status](https://travis-ci.org/espnet/warp-ctc.svg?branch=pytorch_bindings)](https://github.com/espnet/warp-ctc/tree/pytorch_bindings)|-|
|`pytorch-0.4`|[![Build Status](https://travis-ci.org/espnet/warp-ctc.svg?branch=pytorch-0.4)](https://github.com/espnet/warp-ctc/tree/pytorch-0.4)|-|
|`pytorch-1.0`|[![Build Status](https://travis-ci.org/espnet/warp-ctc.svg?branch=pytorch-1.0)](https://github.com/espnet/warp-ctc/tree/pytorch-1.0)|[![PyPI version](https://badge.fury.io/py/warpctc-pytorch10-cuda101.svg)](https://badge.fury.io/py/warpctc-pytorch10-cuda101)|
|`pytorch-1.1`|[![Build Status](https://travis-ci.org/espnet/warp-ctc.svg?branch=pytorch-1.1)](https://github.com/espnet/warp-ctc/tree/pytorch-1.1)|[![PyPI version](https://badge.fury.io/py/warpctc-pytorch11-cuda101.svg)](https://badge.fury.io/py/warpctc-pytorch11-cuda101)|

This is an extension onto the original repo found [here](https://github.com/baidu-research/warp-ctc).

## Installation

Install [PyTorch](https://github.com/pytorch/pytorch#installation) first.

### for PyTorch 1.2

warp-ctc does not work with PyTorch 1.2.
Use [`torch.nn.CTCLoss`](https://pytorch.org/docs/1.2.0/nn.html#ctcloss) built in PyTorch 1.2.

### for PyTorch 1.0 or 1.1

Install `warpctc-pytorchXX-cudaYY` wheel based on PyTorch and CUDA version of your environment.

```bash
# for PyTorch 1.1 and CUDA 10.1
$ pip install warpctc-pytorch11-cuda101

# for PyTorch 1.1 and CUDA 10.0
$ pip install warpctc-pytorch11-cuda100

# for PyTorch 1.1 and CUDA 9.2
$ pip install warpctc-pytorch11-cuda92

# for PyTorch 1.1 and CUDA 9.1
$ pip install warpctc-pytorch11-cuda91

# for PyTorch 1.1 and CUDA 9.0
$ pip install warpctc-pytorch11-cuda90

# for PyTorch 1.1 and CUDA 8.0
$ pip install warpctc-pytorch11-cuda80

# for PyTorch 1.0 and CUDA 10.1
$ pip install warpctc-pytorch10-cuda101

# for PyTorch 1.0 CUDA 10.0
$ pip install warpctc-pytorch10-cuda100

# for PyTorch 1.0 CUDA 9.2
$ pip install warpctc-pytorch10-cuda92

# for PyTorch 1.0 CUDA 9.1
$ pip install warpctc-pytorch10-cuda91

# for PyTorch 1.0 CUDA 9.0
$ pip install warpctc-pytorch10-cuda90

# for PyTorch 1.0 CUDA 8.0
$ pip install warpctc-pytorch10-cuda80
```

### for PyTorch 0.4.1

Wheels for PyTorch 0.4.1 are not provided so users have to build from source manually.

`WARP_CTC_PATH` should be set to the location of a built WarpCTC
(i.e. `libwarpctc.so`).  This defaults to `../build`, so from within a
new warp-ctc clone you could build WarpCTC like this:

```bash
$ git clone https://github.com/espnet/warp-ctc.git
$ cd warp-ctc; git checkout -b pytorch-0.4 remotes/origin/pytorch-0.4
$ mkdir build; cd build
$ cmake ..
$ make
```

Now install the bindings:
```bash
$ cd ../pytorch_binding
$ pip install numpy cffi
$ python setup.py install
```

Example to use the bindings below.

```python
import torch
from warpctc_pytorch import CTCLoss
ctc_loss = CTCLoss()
# expected shape of seqLength x batchSize x alphabet_size
probs = torch.FloatTensor([[[0.1, 0.6, 0.1, 0.1, 0.1], [0.1, 0.1, 0.6, 0.1, 0.1]]]).transpose(0, 1).contiguous()
labels = torch.IntTensor([1, 2])
label_sizes = torch.IntTensor([2])
probs_sizes = torch.IntTensor([2])
probs.requires_grad_(True)  # tells autograd to compute gradients for probs
cost = ctc_loss(probs, labels, probs_sizes, label_sizes)
cost.backward()
```

## Documentation

```
CTCLoss(size_average=False, length_average=False, reduce=True)
    # size_average (bool): normalize the loss by the batch size (default: False)
    # length_average (bool): normalize the loss by the total number of frames in the batch. If True, supersedes size_average (default: False)
    # reduce (bool): average or sum over observation for each minibatch.
        If `False`, returns a loss per batch element instead and ignores `average` options.
        (default: `True`)

forward(acts, labels, act_lens, label_lens)
    # acts: Tensor of (seqLength x batch x outputDim) containing output activations from network (before softmax)
    # labels: 1 dimensional Tensor containing all the targets of the batch in one large sequence
    # act_lens: Tensor of size (batch) containing size of each output sequence from the network
    # label_lens: Tensor of (batch) containing label length of each example
```

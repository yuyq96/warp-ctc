FROM nvidia/cuda:10.1-cudnn7-devel-centos7

ENV CUDA_HOME /usr/local/cuda

RUN yum update -y
RUN yum install -y centos-release-scl \
  && yum install -y devtoolset-3-gcc-c++ \
  && echo 'source scl_source enable devtoolset-3' >> ~/.bash_profile
RUN yum install -y make cmake which
# Install miniconda
ENV PATH /root/miniconda/bin:$PATH
RUN curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh \
  && bash miniconda.sh -b -p /root/miniconda \
  && conda config --set always_yes yes --set changeps1 no \
  && conda update -q conda

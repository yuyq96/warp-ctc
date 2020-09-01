ARG base_image
FROM ${base_image}
ARG devtoolset_version

ENV CUDA_HOME /usr/local/cuda

RUN yum update -y
RUN yum install -y centos-release-scl \
  && yum install -y devtoolset-${devtoolset_version}-gcc-c++ \
  && echo "source scl_source enable devtoolset-${devtoolset_version}" >> ~/.bash_profile
RUN yum install -y make cmake which git \
  && yum install -y zlib-devel libffi-devel bzip2-devel openssl-devel readline-devel
# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git /opt/pyenv
ENV PYENV_ROOT /opt/pyenv
ENV PATH ${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
# Install Python
ENV PYTHON_VERSIONS 3.6.9 3.7.4
RUN source scl_source enable devtoolset-${devtoolset_version} \
  && for python_version in ${PYTHON_VERSIONS}; do \
       pyenv install ${python_version}; \
     done

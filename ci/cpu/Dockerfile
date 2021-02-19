FROM centos:centos7

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y centos-release-scl \
 && yum install -y devtoolset-9-gcc-c++ \
 && echo 'source scl_source enable devtoolset-9' >> ~/.bash_profile
RUN yum install -y \
    bzip2-devel \
    cmake \
    git \
    jq \
    libffi-devel \
    make \
    openssl-devel \
    readline-devel \
    sqlite-devel \
    which \
    zlib-devel
# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git /opt/pyenv
ENV PYENV_ROOT /opt/pyenv
ENV PATH ${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
# Install Python
SHELL ["/bin/bash", "-c"]
ENV PYTHON_VERSIONS 3.6.12 3.7.9 3.8.5
RUN source scl_source enable devtoolset-9 \
 && for python_version in ${PYTHON_VERSIONS}; do \
      pyenv install ${python_version}; \
    done

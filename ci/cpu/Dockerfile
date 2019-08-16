FROM centos:centos7

RUN yum update -y
RUN yum install -y centos-release-scl \
  && yum install -y devtoolset-3-gcc-c++ \
  && echo 'source scl_source enable devtoolset-3' >> ~/.bash_profile
RUN yum install -y make cmake which git \
  && yum install -y zlib-devel libffi-devel bzip2-devel openssl-devel readline-devel
# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git /opt/pyenv
ENV PYENV_ROOT /opt/pyenv
ENV PATH ${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}
# Install Python
SHELL ["/bin/bash", "-c"]
ENV PYTHON_VERSIONS 3.6.9 3.7.4
RUN source scl_source enable devtoolset-3 \
  && for python_version in ${PYTHON_VERSIONS}; do \
       pyenv install ${python_version}; \
     done

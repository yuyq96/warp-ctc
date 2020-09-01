#!/bin/sh

image_repository=espnet/warpctc_builder
cuda_versions=(9.2 10.0 10.1)
for cuda_version in ${cuda_versions[@]}; do
  # gcc version check exists in /usr/local/cuda/include/crt/host_config.h
  devtoolset_version=8
  if [ "$cuda_version" = "10.0" ] || [ "$cuda_version" = "9.2" ]; then
    devtoolset_version=7
  fi
  base_image="nvidia/cuda:$cuda_version-cudnn7-devel-centos7"
  image_tag=cuda${cuda_version/./}
  image_name=$image_repository:$image_tag
  echo "Building $image_name"
  docker build --build-arg base_image=$base_image --build-arg devtoolset_version=$devtoolset_version -t $image_name ./gpu
  echo "Done.\n"
done

image_tag=cpu
image_name=$image_repository:$image_tag
echo "Building $image_name"
docker build -t $image_name ./cpu
echo Done.

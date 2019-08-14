#!/bin/sh

image_repository=espnet/warpctc_builder
cuda_versions=(9.2 10.1)
for cuda_version in ${cuda_versions[@]}; do
  base_image="nvidia/cuda:$cuda_version-cudnn7-devel-centos7"
  image_tag=cuda${cuda_version/./}
  image_name=$image_repository:$image_tag
  echo "Building $image_name"
  docker build --build-arg base_image=$base_image -t $image_name .
  echo Done.
done

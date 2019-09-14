#!/bin/sh

image_repository=espnet/warpctc_builder
cuda_versions=(8.0 9.0 9.1 9.2 10.0 10.1)
for cuda_version in ${cuda_versions[@]}; do
  base_image="nvidia/cuda:$cuda_version-cudnn7-devel-centos7"
  image_tag=cuda${cuda_version/./}
  image_name=$image_repository:$image_tag
  echo "Building $image_name"
  docker build --build-arg base_image=$base_image -t $image_name ./gpu
  echo "Done.\n"
done

image_tag=cpu
image_name=$image_repository:$image_tag
echo "Building $image_name"
docker build -t $image_name ./cpu
echo Done.

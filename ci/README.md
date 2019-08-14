Docker image builder for Travis CI
===

This directory contains tools to build Docker images used in Travis CI.
The tools build images by CUDA versions (9.2, 10.1), whose name is `espnet/warpctc_builder:cudaXX` (`XX` is CUDA version without `.`).

## Building Docker images

Run `build.sh`.

```console
$ ./build.sh
```

## Uploading images to Dockerhub

Run `docker push`.

```console
$ docker push espnet/warpctc_builder:cudaXX
```

Note that your Dockerhub account have write access to [espnet/warpctc_builder](https://hub.docker.com/r/espnet/warpctc_builder) repository.

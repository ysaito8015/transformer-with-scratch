# ROCm-setup
- [Introduction to ROCm Installation Guide for Linux](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.4.2/page/Introduction_to_ROCm_Installation_Guide_for_Linux.html)


## deb package

```shell
$ sudo apt-get update
$ wget https://repo.radeon.com/amdgpu-install/5.4.2/ubuntu/jammy/amdgpu-install_5.4.50402-1_all.deb
$ sudo apt-get install ./amdgpu-install_5.4.50402-1_all.deb
```


## install

```shell
$ sudo amdgpu-install --list-usecase
```


```shell
$ sudo amdgpu-install --usecase=dkms,rocm
```


## Add Official Repositry

```shell
$ curl -fsSL https://repo.radeon.com/rocm/rocm.gpg.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/rocm-keyring.gpg
$ echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/amdgpu/5.4.2/ubuntu jammy main' | sudo tee /etc/apt/sources.list.d/rocm.list
$ echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600
$ sudo apt update
$ sudo amdgpu-install --usecase=dkms,rocm --rocmrelease=5.4.2
```


## Summary

> For a fresh ROCm installation using the package manager method on a Linux distribution, follow the steps below:
> 1.     Meet prerequisites – Ensure the Prerequisites are met before the ROCm installation.
> 2.     Install kernel headers and development packages – Ensure kernel headers and development packages are installed on the system.
> 3.     Select the base URLs for AMDGPU and ROCm stack repository – Ensure the base URLs for AMDGPU and ROCm stack repositories are selected.
> 4.     Add the AMDGPU stack repository – Ensure the AMDGPU stack repository is added.
> 5.     Install the kernel-mode driver and reboot the system – Ensure the kernel-mode driver is installed and the system is rebooted.
> 6.     Add ROCm stack repository – Ensure the ROCm stack repository is added.
> 7.     Install single-version or multiversion ROCm meta-packages – Install the desired meta-packages.
> 8.     Verify installation for the applicable distributions – Verify if the installation is successful.


## Check prerequires

```shell
$ sudo dpkg -l | grep linux-headers
$ sudo dpkg -l | grep linux-modules-extra
$ sudo apt install linux-headers-`uname -r` linux-modules-extra-`uname -r`
```


## Post-install Actions and Verification Process

```shell
$ export LD_LIBRARY_PATH=/opt/rocm-5.4.2/lib:/opt/rocm-5.4.2/lib64
$ export PATH=$PATH:/opt/rocm-5.4.2/bin:/opt/rocm-5.4.2/opencl/bin
$ dkms status
$ /opt/rocm-5.4.2/bin/rocminfo
```

## Error 1

```
2023-02-03 18:37:23.031595: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Netwo
rk Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Traceback (most recent call last):
  File "/home/ysaito/projects/books/transformer-with-scratch/.venv/lib/python3.10/site-packages/tensorflow/python/pywrap_tensorflow.py", line 62, 
in <module>
    from tensorflow.python._pywrap_tensorflow_internal import *
ImportError: librccl.so.1: cannot open shared object file: No such file or directory
```


```shell
$ sudo apt install rccl
```


## Error 2

```
2023-02-03 18:37:50.591638: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Netwo
rk Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-02-03 18:37:53.004582: I tensorflow/compiler/xla/stream_executor/rocm/rocm_gpu_executor.cc:843] successful NUMA node read from SysFS had nega
tive value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2023-02-03 18:37:53.004761: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'librocbla
s.so'; dlerror: librocblas.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm-5.4.2/lib:/opt/rocm-5.4.2/lib
64
2023-02-03 18:37:53.004827: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libMIOpen
.so'; dlerror: libMIOpen.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm-5.4.2/lib:/opt/rocm-5.4.2/lib64
2023-02-03 18:37:53.004891: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libhipfft
.so'; dlerror: libhipfft.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm-5.4.2/lib:/opt/rocm-5.4.2/lib64
2023-02-03 18:37:53.004947: W tensorflow/compiler/xla/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'librocran
d.so'; dlerror: librocrand.so: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/rocm-5.4.2/lib:/opt/rocm-5.4.2/lib
64
2023-02-03 18:37:53.004960: W tensorflow/core/common_runtime/gpu/gpu_device.cc:1934] Cannot dlopen some GPU libraries. Please make sure the missin
g libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for ho
w to download and setup the required libraries for your platform.
Skipping registering GPU devices...
2023-02-03 18:37:53.005262: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Netwo
rk Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE3 SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
```


```shell
$ sudo apt install rocm-libs
```

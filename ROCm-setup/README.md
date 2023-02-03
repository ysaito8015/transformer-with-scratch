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

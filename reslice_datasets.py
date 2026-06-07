"""
================
Reslice Datasets
================

Diffusion MRI data is sometimes acquired with anisotropic voxel sizes (e.g.,
different resolution in the slice direction). This example shows how to
reslice such a dataset to isotropic voxels using ``dipy.align.reslice``.

The resliced volume is saved in both NIfTI and SPM Analyze formats.
"""

import os

import nibabel as nib

from dipy.align.reslice import reslice
from dipy.data import get_fnames
from dipy.io.image import load_nifti, save_nifti


os.makedirs("reslice_datasets", exist_ok=True)

fimg = get_fnames(name="aniso_vox")

data, affine, voxel_size= load_nifti(fimg, return_voxsize=True)

print(f"Data Size: {data.shape}")
print(f"Voxel size: {voxel_size}")

new_voxel_size = (3.0, 3.0, 3.0)
print(f"New Voxel size: {new_voxel_size}")

data2, affine2 = reslice(data, affine, voxel_size, new_voxel_size)
print(f"New data size: {data2.shape}")

save_nifti("reslice_datasets/iso_vox.nii.gz", data2, affine2)

img3 = nib.Spm2AnalyzeImage(data2, affine2)
nib.save(img3, "reslice_datasets/iso_vox.img")


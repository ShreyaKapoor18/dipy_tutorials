import nibabel as nib

from dipy.align.reslice import reslice
from dipy.data import get_fnames
from dipy.io.image import load_nifti, save_nifti


fimg = get_fnames(name="aniso_vox")

data, affine, voxel_size= load_nifti(fimg, return_voxsize=True)

print(f"Data Size: {data.shape}")
print(f"Voxel size: {voxel_size}")

new_voxel_size = (3.0, 3.0, 3.0)
print(f"New Voxel size: {new_voxel_size}")

data2, affine2 = reslice(data, affine, voxel_size, new_voxel_size)
print(f"New data size: {data2.shape}")

save_nifti("reslice/iso_vox.nii.gz", data2, affine2)

img3 = nib.Spm2AnalyzeImage(data2, affine2)
nib.save(img3, "reslice/iso_vox.img")


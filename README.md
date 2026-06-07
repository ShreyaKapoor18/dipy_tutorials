# dipy_tutorials

A collection of standalone tutorial scripts demonstrating core [DIPY](https://dipy.org/) workflows for diffusion MRI analysis, tractography, and visualization.

## Structure

Each tutorial lives in its own directory alongside its outputs:

```
quick_start/
reslice_datasets/
tracking_introduction_eudx/
tracking_ptt/
parallel_transport_tractography/
bundle_group_registration/
viz_advanced/
run_gpu_streamlines/
```

## Tutorials

### `quick_start/quick_start.py` — Getting Started with DIPY
Introduces the three file types used in diffusion MRI (NIfTI data, b-values, b-vectors). Downloads the Sherbrooke 3-shell dataset, loads it with `nibabel`, builds a `GradientTable`, and visualizes axial slices with `matplotlib`. A good starting point for anyone new to DIPY.

**Outputs:** `data.png`, `HARDI193_S0.nii.gz`

### `reslice_datasets/reslice_datasets.py` — Reslice Datasets
Shows how to reslice an anisotropic voxel dataset to isotropic voxels using `dipy.align.reslice`. Saves the output in both NIfTI (`.nii.gz`) and SPM Analyze (`.img`) formats.

**Outputs:** `iso_vox.nii.gz`, `iso_vox.img`

### `tracking_introduction_eudx/tracking_introduction_eudx.py` — Introduction to Basic Tracking
Covers local fiber tracking end-to-end using the Stanford HARDI dataset:
1. Fits a Constant Solid Angle (CSA) ODF model to estimate fiber directions.
2. Applies a GFA-based `ThresholdStoppingCriterion` to constrain tracking.
3. Seeds from the corpus callosum and runs the EuDX algorithm via `LocalTracking`.

**Outputs:** `csa_direction_field.png`, `gfa_tracking_mask.png`, `tractogram_EuDX.png`, `tractogram_EuDX.trx`

### `tracking_ptt/tracking_ptt.py` — Parallel Transport Tractography (PTT)
Demonstrates the PTT algorithm using a CSD model fit to Stanford HARDI data. Seeds from the corpus callosum with a binary white-matter stopping criterion. Saves the tractogram as a `.trk` file and optionally renders it with FURY.

**Outputs:** `tractogram_ptt.trk`, `tractogram_ptt.png`

### `parallel_transport_tractography/parallel_transport_tractography.py` — Parallel Transport Tractography (variant)
A second PTT example using the same CSD + Stanford HARDI pipeline, saving output as a `.trx` file. Useful for comparing PTT parameter settings.

**Outputs:** `tractogram_ptt.trx`, `tractogram_ptt.png`

### `bundle_group_registration/bundle_group_registration.py` — Groupwise Bundle Registration
Coregisters a set of fiber bundles to a common unbiased space using Streamline Linear Registration (SLR) via `groupwise_slr`. Loads 5 left arcuate fasciculi, visualizes them before and after registration, and reports the pairwise distance reduction across iterations.

**Outputs:** `before_group_registration.png`, `after_group_registration.png`

### `viz_advanced/viz_advanced.py` — Advanced Interactive Visualization
Builds an interactive 3D scene with FURY that overlays fiber bundles on FA/T1 image slices. Adds `LineSlider2D` widgets to scroll through axial, sagittal, and coronal slices and adjust slicer opacity in real time. Optionally records the session to a video.

**Outputs:** `bundles_and_3_slices.png` (non-interactive), `viz_advanced_tutorial.mp4` (interactive + recording)

### `run_gpu_streamlines/run_gpu_streamlines.py` — GPU-Accelerated Tractography
Runs probabilistic or PTT tractography on GPU (CUDA, Metal, WebGPU) or CPU (numba) via the `cuslines` library. Accepts a DWI NIfTI file, b-values, b-vectors, mask, and ROI as arguments, or defaults to the Stanford HARDI dataset.

**Usage:**
```bash
python run_gpu_streamlines/run_gpu_streamlines.py [nifti] [bvals] [bvecs] [mask] [roi] \
  --device gpu --dg prob --output-prefix results/tractogram
```

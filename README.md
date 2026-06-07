# dipy_tutorials

A collection of standalone tutorial scripts demonstrating core [DIPY](https://dipy.org/) workflows for diffusion MRI analysis, tractography, and visualization.

## Tutorials

### `quick_start.py` — Getting Started with DIPY
Introduces the three file types used in diffusion MRI (NIfTI data, b-values, b-vectors). Downloads the Sherbrooke 3-shell dataset, loads it with `nibabel`, builds a `GradientTable`, and visualizes axial slices with `matplotlib`. A good starting point for anyone new to DIPY.

### `reslice_datasets.py` — Reslice Datasets
Shows how to reslice an anisotropic voxel dataset to isotropic voxels using `dipy.align.reslice`. Saves the output in both NIfTI (`.nii.gz`) and SPM Analyze (`.img`) formats.

### `tracking_introduction_eudx.py` — Introduction to Basic Tracking
Covers local fiber tracking end-to-end using the Stanford HARDI dataset:
1. Fits a Constant Solid Angle (CSA) ODF model to estimate fiber directions.
2. Applies a GFA-based `ThresholdStoppingCriterion` to constrain tracking.
3. Seeds from the corpus callosum and runs the EuDX algorithm via `LocalTracking`.
Saves the tractogram as a `.trx` file and renders it with FURY.

### `tracking_ptt.py` — Parallel Transport Tractography (PTT)
Demonstrates the PTT algorithm using a CSD model fit to Stanford HARDI data. Seeds from the corpus callosum with a binary white-matter stopping criterion. Saves the tractogram as a `.trk` file and optionally renders it with FURY.

### `parallel_transport_tractography.py` — Parallel Transport Tractography (variant)
A second PTT example using the same CSD + Stanford HARDI pipeline but saving output to the `parallel_transport_tractography/` directory as a `.trx` file. Useful for comparing PTT parameter settings.

### `bundle_group_registration.py` — Groupwise Bundle Registration
Coregisters a set of fiber bundles to a common unbiased space using Streamline Linear Registration (SLR) via `groupwise_slr`. Loads 5 left arcuate fasciculi, visualizes them before and after registration, and reports the pairwise distance reduction across iterations.

### `viz_advanced.py` — Advanced Interactive Visualization
Builds an interactive 3D scene with FURY that overlays fiber bundles on FA/T1 image slices. Adds `LineSlider2D` widgets to scroll through axial, sagittal, and coronal slices and adjust slicer opacity in real time.

## Output Directories

| Directory | Script |
|---|---|
| `tracking_quickstart_output/` | `quick_start.py` |
| `images_tracking_output/` | `tracking_introduction_eudx.py` |
| `tracking_ptt_output/` | `tracking_ptt.py` |
| `parallel_transport_tractography/` | `parallel_transport_tractography.py` |
| `bundle_group_registration_output/` | `bundle_group_registration.py` |
| `reslice/` | `reslice_datasets.py` |
| `viz_transport/` | `viz_advanced.py` |

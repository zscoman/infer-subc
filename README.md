# infer_subc_2d

[![codecov](https://codecov.io/gh/ergonyc/infer-subc/branch/main/graph/badge.svg?token=infer-subc_token_here)](https://codecov.io/gh/ergonyc/infer-subc)
[![CI](https://github.com/ergonyc/infer-subc/actions/workflows/main.yml/badge.svg)](https://github.com/ergonyc/infer-subc/actions/workflows/main.yml)

## About The Project
---
`infer_subc_2d` 
- aims to create a simple, extensible, and reproducible workflow to measure (or infer) the shape, position, size, and interaction of several sub-cellular components. These data can then be applied later to better understand the spatial coordination of these structures and the interactome during key biological processes.

- is part of a larger collaboration between the CZI Neurodegeneration Challenge Network [(NDCN)](https://chanzuckerberg.com/science/programs-resources/neurodegeneration-challenge/) Data Science Concierge program and the Cohen lab at UNC [(website,](https://cohenlaboratory.web.unc.edu/) [github)](https://github.com/SCohenLab) to migrate a multispectral imaging dataset of iPSCs which identifies sub-cellular components to a scalable cloud-based pipeline.  



## `infer_subc_2d` Workflow
---

The staring point of this workflow is a set of multichannel images, where each channel labels a different sub-cellular component. The workflow can then be completed in a _**suggested**_ series of steps, outlined in the notebooks below.

**Identify a single cell of interest**

1. [Infer soma](./notebooks/01_infer_soma.ipynb) (🚨 Steps 2-9 depend on establishing a good solution here)
2. [Infer nuclei ](./notebooks/02_infer_nuclei.ipynb)
3. [Infer cytosol](./notebooks/03_infer_cytosol.ipynb) 

**Segment each of the organelles**

4. [Infer lysosomes](./notebooks/04_infer_lysosome.ipynb)
5. [Infer mitochondria](./notebooks/05_infer_mitochondria.ipynb)
6. [Infer golgi complex](./notebooks/06_infer_golgi.ipynb)
7. [Infer peroxisomes](./notebooks/07_infer_peroxisome.ipynb)
8. [Infer endoplasmic reticulum](./notebooks/08_infer_endoplasmic_reticulum.ipynb)
9. [Infer lipid bodies](./notebooks/09_infer_lipid_body.ipynb) 

## Built With
---

A quick note on tools and resources used.

- [`napari-allencell-segmenter`](https://github.com/AllenCell/napari-allencell-segmenter) -- We are leveraging the framework of the `napari-allencell-segmenter` plugin, which enables powerful 3D image segmentation while taking advantage of the `napari` graphical user interface. 
- [`aicssegmentation`](https://github.com/AllenCell/aics-segmentation) -- We call the `aicssegmentation` package directly.
- [`napari`](https://napari.org/stable/) -- Used as the visualization framework, a fast, interactive, multi-domensional image viewer for Python.
- [`scipy`](https://scipy.org/install/) -- Image analysis
- [`scikit-image`](https://scikit-image.org/) -- Image analysis
- [`itk`](https://itkpythonpackage.readthedocs.io/en/master/Quick_start_guide.html) -- Image analysis
- [`numpy`](https://numpy.org/) -- Under the hood computation
- [`Alzheimer's Disease AD Workbench`](https://www.alzheimersdata.org/ad-workbench) -- We initially wanted to use the ADDI's ADWB as a method of data sharing and to serve as a computational resource.

## ADWB hints
---

Given that the github repos are not yet whitelisted, the source directory needs to be zipped and uploaded in order to make an "editable" pip install.

[uploading guide ](https://knowledgebase.aridhia.io/article/guidance-for-uploading-files/)
[uploading files via the workspace article](https://knowledgebase.aridhia.io/article/uploading-files-via-the-workspace/).
[Using BLOB storage](https://knowledgebase.aridhia.io/article/using-blob-storage/)

### Uploading files to Blobs
> The file upload to Blob storage follows the process described in [uploading files via the workspace article](https://knowledgebase.aridhia.io/article/uploading-files-via-the-workspace/). Note that due to the nature of Blob storage, folder hierarchies cannot exist without content. This means that you won't be able to create empty folders, and after refreshing the page the empty folders will be gone from your Blob storage. There is a workaround: you can create an empty folder, and without closing the window, add or upload a new file to the folder.

## Getting Started
---

### Prerequisites

The following are prerequisites and should be installed prior to using the workflow.

- `napari` 
  ```
  pip install "napari[all]"
  ```

- `scipy`
  ```
  python -m pip install scipy
  ```

- `scikit-image`
  ```
  pip install scikit-image
  ```

- `itk`
  ```
  pip install itk
  ```
- `numpy`
  ```
  pip install numpy
  ```

### Installation

`infer_subc_2d` can be installed from `PyPI` via `pip`
```
pip install infer_subc_2d
```

## Usage
---

```py
from infer_subc_2d.organelles import infer_NUCLEI

NU_object, NU_label, out_p =  infer_NUCLEI(raw_nuclei.copy(), default_params) 

```

 🚧 WIP 🚧 (🚨🚨🚨🚨 )
> NOTE: command line capabilities not implimented
```bash
$ python -m infer_subc_2d
#or
$ infer_subc_2d
```

## Roadmap
---
 - [ ] Add `infer_subc_2d` to ADWB whitelist
 - [ ] Update prerequisites
 - [ ] Create `PyPI` package
 - [ ] Update installation instructions to reflect optimal use of `conda` environments

## Development
---
Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License
---

Distributed under the Unlicense license. See `LICENSE` for more information.  

## Issues
---

If you encounter any problems, please file an issue with a detailed description.
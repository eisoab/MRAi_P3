# MRAi_P3: Magnetic Resonance processing with Artificial intelligence for Peak Probability Presentarion

## Authors
* [Amir Jahangiri](amir.jahangiri@gu.se)
* [Vladislav Orekhov](vladislav.orekhov@nmr.gu.se)

## License
This package is licensed under the MIT License. See the LICENSE file for details.

## Citation
Please cite our articles if you use this application in your research or publication. 

* [NMR spectrum reconstruction as a pattern recognition problem](https://doi.org/10.1016/j.jmr.2022.107342)
* [Beyond traditional magnetic resonance processing with artificial intelligence](https://doi.org/10.1038/s42004-024-01325-w)
* [Towards ultimate nmr resolution with deep learning](https://arxiv.org/abs/2502.20793)

---
## Installation
## Installation
1. Install [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) by following the Regular installation instructions.
2. Download MRAi_P3 pacckege from [`Code`](https://github.com/Amir-Jahangiri/MRAi_P3/archive/refs/heads/main.zip).
3. Unzip the `MRAi_P3-main.zip` file.
4. Open Terminal in `MRAi_P3-main` folder.
5. Create a conda environment with: 
```python
conda create -n mrai_p3 python=3.11
```
* Type `yes` if prompted. This may take a few minutes.
  
6. Active `mrai_p3` environment with:
```python
conda activate mrai_p3
```
7. Install `MRAi_P3` with:
```python
pip install MRAi_P3-0.0.0-py3-none-any.whl
```
* Installation may take a few minutes.
  
8. Install Jupyter with:
```python
conda install jupyter
```
* Type `yes` if prompted. This may take a few minutes.
  
9. Once completed, close the terminal.
---
## Usage

1. Open Terminal in `MRAi_P3-main` folder.
2. Active `mrai_p3` environment with:
```python
conda activate mrai_p3
```
3. Run Jupyter Notebook with:
```python
jupyter notebook
```
4. Open and run Jupyter notebook (`P3_Notebook.ipynb`), following the instructions provided in the file.

5. If necessary, restart the kernel and then shut down any open Jupyter instances before running a new notebook.
---
## Uninstallation

If it is needed to uninstall the entire environment, open a terminal in the `base` Conda environment and remove the `mrai_p3` environment with:
```python
conda remove --name mrai_p3 --all
```
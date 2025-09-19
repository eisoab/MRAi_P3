# MRAi_2D: Magnetic Resonance processing with Artificial intelligence for 2D spectra

## About
MRAi is an AI-powered tool for processing Magnetic Resonance data, specifically designed for 2D NMR spectra. With it, you can perform the following tasks:
* Non-Uniform Sampling (NUS) Reconstruction (`NUS_Rec.ipynb` [Preview](https://github.com/Amir-Jahangiri/MRAi_2D/blob/master/NUS_Rec.ipynb))
* Virtual homo-decoupling in a 2D methyl H-C—HMQC with J-coupling around 35 Hz (`VD_ID.ipynb` [Preview](https://github.com/Amir-Jahangiri/MRAi_2D/blob/master/VD_ID.ipynb))
* Echo or Anti-Echo Reconstruction with MRAi and Compressed Sensing (CS) (`Echo_Rec.ipynb` [Preview](https://github.com/Amir-Jahangiri/MRAi_2D/blob/master/Echo_Rec.ipynb))
* Uncertainty Estimation for Echo or Anti-Echo Reconstruction with MRAi and CS (`Uncertainty.ipynb` [Preview](https://github.com/Amir-Jahangiri/MRAi_2D/blob/master/Uncertainty.ipynb))
* Data generation and WNN architectures for training (`Generator.ipynb` [Preview](https://github.com/Amir-Jahangiri/MRAi_2D/blob/master/Generator.ipynb))"

## Authors
* [Amir Jahangiri](amir.jahangiri@gu.se)
* [Vladislav Orekhov](vladislav.orekhov@nmr.gu.se)

## License
This package is licensed under the MIT License. See the LICENSE file for details.

## Citation
Please cite our articles if you use this application in your research or publication. 

* [NMR spectrum reconstruction as a pattern recognition problem](https://doi.org/10.1016/j.jmr.2022.107342)
* [Beyond traditional magnetic resonance processing with artificial intelligence](https://doi.org/10.1038/s42004-024-01325-w)

---
## Installation
1. Install [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) by following the Regular installation instructions.
2. Download MRAi_2D pacckege from [`Code`](https://github.com/Amir-Jahangiri/MRAi_2D/archive/refs/heads/master.zip).
3. Unzip the `MRAi_2D-master.zip` file.
4. Open Terminal in `MRAi_2D-master/Packages` folder.
5. Create a conda environment with: 
```python
conda create -n mrai python=3.11
```
* Type `yes` if prompted.
* This may take a few minutes.
  
6. Active `mrai` environment with:
```python
conda activate mrai
```
7. Install `MRAi_2D` and `Proc_2D` with:
```python
pip install MRAi_2D-0.1.0-py3-none-any.whl
```
```python
pip install Proc_2D-0.1.0-py3-none-any.whl
```
* Installation may take a few minutes.
  
8. Install Jupyter with:
```python
conda install jupyter
```
* Type `yes` if prompted.
* This may take a few minutes.
  
9. Once completed, close the terminal.
---
## Usage

1. Open Terminal in `MRAi_2D-master` folder.
2. Active `mrai` environment with:
```python
conda activate mrai
```
3. Run Jupyter Notebook with:
```python
jupyter notebook
```
4. Open and run one of the Jupyter notebooks (`*.ipynb`), following the instructions provided in the file.

5. If necessary, restart the kernel and then shut down any open Jupyter instances before running a new notebook.
---
## Uninstallation

If it is needed to uninstall the entire environment, open a terminal in the `base` Conda environment and remove the `mrai` environment with:
```python
conda remove --name mrai --all
```
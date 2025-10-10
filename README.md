# Automating Dense GPR B-scan Simulations for C-Scan Imaging

This repository contains the Grasshopper and GhPython scripts referenced in the article *"Automating Dense GPR Simulations for C-Scan Imaging of Subsurface Infrastructure: Pipe Leakage Case Study"*, which facilitate the automation of dense GPR B-scan simulations.

The scripts demonstrate a case study involving a road pavement structure with a void cavity beneath it. A total of 11 GPR B-scans were simulated using the open-source FDTD solver **gprMax**. Modeling each B-scan directly in gprMax is challenging due to its geometric modeling limitations, which primarily support simple shapes like boxes, triangles, and cylinders.

This work proposes a **digital model-centered method** for bulk B-scan simulations, especially suitable for infrastructure with complex geometry and material properties. The approach centers around a digital model reconstructed in professional modeling software—in this case, **Rhino 3D**.

Scripts are provided to demonstrate a grid survey simulation of a multi-layer pavement containing a subsurface void. A total of 11 B-scans are generated based on geometry and material data extracted from the Rhino 3D model using **Grasshopper** (a visual programming environment within Rhino) and **GhPython** (the Python scripting component of Grasshopper).

The steps to reproduce the simulations are outlined below. This method can be adapted to other models or use cases with similar needs.


## 1. Digital modeling

The model can be created manually or via parametric modeling in Rhino 3D (`void.3dm`). In this case, a parametric model was used to construct a digital pavement with four layers:

* Wearing course
* Base course
* Road base
* Sub-base

The ground material is set as sand, and a void of 1 m diameter is embedded in it.

<img width="361" height="320" alt="image" src="https://github.com/user-attachments/assets/01f3d21b-b985-46ba-861a-9f75d8b7188d" />

---

## 2. Run the Grasshopper script for grid slicing

In a GPR grid survey, each B-scan simulation requires a corresponding 2D or 3D cross-section geometry file in HDF5 (`.h5`) format. Generating these files manually for complex geometries is not intuitive or efficient.

To automate this, use the provided **Grasshopper script** (`void.gh`). The slicing logic is explained in the pseudo-code in the manuscript. The movement of the slicing bounding box is controlled by an embedded Python script. The separate `slicing.py` file is provided for reference only.

The **step interval** (i.e., distance between slices) can be adjusted by the user. Other adjustable parameters in the Grasshopper script include:

* Slicing direction (X or Y axis)
* Voxel resolution
* Export format
* Output directory

<img width="836" height="641" alt="image" src="https://github.com/user-attachments/assets/8f6c7318-a054-4ca6-9593-c4fb310ee99a" />

---

## 3. Convert Grasshopper output to HDF5 files

The sliced cross-sections are saved as spreadsheet files, which need to be converted into `.h5` format for compatibility with gprMax.

A Python script (`gh_output_to_hdf5.py`) is provided as a reference for this conversion process.

---

## 4. Prepare simulation input files and run simulations

The simulation input files can be generated in bulk using Python or other scripting languages. This involves creating:

* Command files (`.in`)
* Material definition files (`.txt`)

This is primarily a text editing task and can be automated with minimal effort.

Example input files are included in the repository for reference.

---

## Correspondence

If you have questions or need further clarification regarding the implementation of this method, feel free to open an issue in this repository. The authors will respond as soon as possible.

---

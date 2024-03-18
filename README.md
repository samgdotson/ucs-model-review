# ucs-model-review
Data and documents related to the review of models


In order to run most of the scripts in this repository, it is recommended to use the accompanying `conda environment`.

```bash
conda create env

conda activate ucs-model-review
```

# Data preparation

In order to create a consistent test model of the Mid-continent independent system operator (MISO) for comparing energy models, the following steps and assumptions were taken/made.

1. Hourly electricity demand data from 2023 was scraped from EIA with `gridstatus`. Notebook may be found in `energy_data/eia_data.ipynb`.
2. For simplicity, the test models assume that all generating resources are connected to a single bus located at the centroid of MISO's service area. The calculation of this centroid may be found in `gis_data\miso_centroid.ipynb`. The shapefile used in that notebook was downloaded on `2024-03-15` from [this
government website hosted by ArcGIS](https://hifld-geoplatform.opendata.arcgis.com/datasets/geoplatform::independent-system-operators-1/explore?location=32.576794%2C-95.679925%2C3.74) and saved to the `gis_data` folder.

# Calliope Model

Here are the steps taken to generate the `calliope` model and results.

## Pre-requisites

1. Install a solver, such as GLPK, CBC, CPLEX, or other.
2. Install `calliope` and its `conda` environment with `mamba create -c conda-forge -n calliope calliope` (I prefer the `mamba` variant).
3. Create an isolated folder in this repository with `mkdir calliope_model`.
4. Navigate to this repository with `cd calliope_model`.
5. Activate the `conda` environment with `mamba activate calliope`.
6. The MISO demand data needs to be modified slightly. `calliope` uses a convention where energy sinks are negative and sources are positive. Therefore, we need to negate the demand data from MISO. This was achieved by running 

```bash
~\ucs-model-review\ python calliope_model\miso_model\timeseries_data\convert_miso_data.py
```

## Creating the model

Per `calliope`'s [documentation](https://calliope.readthedocs.io/en/stable/user/building.html#files-that-define-a-model) I created a new template model called `miso_model` with the command

```bash
~\ucs-model-review\calliope_model> calliope new miso_model
Copying national_scale template to target directory: miso_model
```

### Modifications from Template
*Any commands listed here assume your working directory is `calliope_model/miso_model`.*

1. In `model.yaml`
    * change `solver: cbc` to `solver: cplex`
    * change `subset_time` to `subset_time: ['2023-01-01', '2023-01-05']`
2. In `model_config/locations.yaml`
    * change the `demand_power:constraints` from `demand1.csv` to `miso_demand_calliope`
    * remove `region2`
    * remove transmission capacities


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

Per `calliope`'s [documentation](https://calliope.readthedocs.io/en/stable/user/building.html#files-that-define-a-model) I created a new template model called `calliope_model` with the command

```bash
~\ucs-model-review\calliope_model> calliope new calliope_model
Copying national_scale template to target directory: calliope_model
```

### Modifications from Template
*Any commands listed here assume your working directory is `calliope_model/`.*

1. In `model.yaml`
    * change `solver: cbc` to `solver: cplex`
    * change `subset_time` to `subset_time: ['2023-01-01', '2023-12-31']`

2. In `model_config/locations.yaml`
    * change the `demand_power:constraints` from `demand1.csv` to `miso_demand_calliope`

Ran the model again.

```bash
Error in process_timeseries_data, C:\Users\sdotson\AppData\Local\miniforge3\envs\calliope\lib\site-packages\calliope\preprocess\model_run.py:639
subset time range ['2023-01-01', '2023-12-31'] is outside the input data time range [2023-01-01, 2005-12-31]
```

2. (Continued) In `model_config/locations.yaml`
    * remove demand from `region2`

Ran the model again 

```bash
Error in process_timeseries_data, C:\Users\sdotson\AppData\Local\miniforge3\envs\calliope\lib\site-packages\calliope\preprocess\model_run.py:639
subset time range ['2023-01-01', '2023-12-31'] is outside the input data time range [2023-01-01, 2005-12-31]
```

3. In `model_config/techs.yaml`
    * remove `csp` technology.
4. In `model_confgi/locations.yaml`
    * remove subregions `region1-x`.
    * remove the links from each subregion `region1-x`.

Ran the model again

```bash
Calliope 0.6.10 starting at 2024-03-18 14:25:30

[2024-03-18 14:25:30] INFO     Model: initialising
[2024-03-18 14:25:31] INFO     Model: preprocessing stage 1 (model_run)

Error in print_warnings_and_raise_errors, C:\Users\sdotson\AppData\Local\miniforge3\envs\calliope\lib\site-packages\calliope\exceptions.py:80
Errors during model processing:
 * column `demand` not found in dataframe `miso_demand_calliope.csv`, but was requested by loc::tech `region1::demand_power`.

Calliope run aborted due to an error. Elapsed: 0.1 seconds (time at exit: 2024-03-18 14:25:31)
```
5. Edit the conversion script `convert_miso_data.py` to rename the load column to `demand`.

Ran the model again

```bash
Error in query, C:\Users\sdotson\AppData\Local\miniforge3\envs\calliope\lib\site-packages\xarray\core\indexes.py:247
"not all values found in index 'timesteps'"
```

6. Edit the conversion script to remove the timezone awareness from miso dataset.

Model ran without error.

## Adding more technology options

....
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





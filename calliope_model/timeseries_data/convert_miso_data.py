if __name__ == "__main__":
    import pandas as pd
    from pathlib import Path
    import os
    cwd = Path(os.path.dirname(__file__))
    energy_data_path = Path(list(cwd.parents)[1])/'energy_data'
    read_path = energy_data_path/"2023-miso-demand.csv"
    print(f"Reading from {read_path}")
    miso_data = pd.read_csv(read_path, 
                            index_col='Interval End', 
                            parse_dates=True)
    miso_data['Load'] = miso_data['Load']*-1
    miso_data.columns = ["demand"]
    miso_data.index = miso_data.index.tz_localize(None)

    print(miso_data.index.name)
    save_path = cwd/"miso_demand_calliope.csv"
    print(f"Saving to {save_path}")
    miso_data.to_csv(save_path)
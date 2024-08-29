import pandas as pd
import geopandas as gpd
import os
import requests

class local_data:
    def __init__(self):
        self.username = os.getenv("USERNAME", "Default User")
        self.github_base_url = rf"https://raw.githubusercontent.com/lawolf8/Satellite-Launch-Cost-Minimization-Operations-Research-/Data/sat data/"
        
    def gcat(self):
        # Replace 'username/repo/branch/path/to/data/' with the actual path in your GitHub repository
        lp_url = os.path.join(self.github_base_url, 'launch.tsv')
        lp = pd.read_table(lp_url, header=0)

        sc_url = os.path.join(self.github_base_url, 'satcat.tsv')
        sc = pd.read_table(sc_url, header=0)
        satcat = sc[sc['OpOrbit'].str.contains('Leo|LEO|LEO/I|LLEO/I', na=False)]

        ax_url = os.path.join(self.github_base_url, 'auxcat.tsv')
        ax = pd.read_table(ax_url, header=0)
        auxcat = ax[ax['OpOrbit'].str.contains('Leo|LEO|LEO/I|LLEO/I', na=False)]

        ftorbit_url = os.path.join(self.github_base_url, 'ftocat.tsv')
        ftorbit = pd.read_table(ftorbit_url, header=0)

        launchlist_url = os.path.join(self.github_base_url, 'launch.tsv')
        launchlist = pd.read_table(launchlist_url, header=0)
        launchlist = launchlist.dropna()

        orgs_url = os.path.join(self.github_base_url, 'orgs.tsv')
        orgs = pd.read_table(orgs_url, header=0)

        sites_url = os.path.join(self.github_base_url, 'sites.tsv')
        sites = pd.read_table(sites_url, header=0)

    def ourworld(self):
        leocost_url = os.path.join(self.github_base_url, 'cost-space-launches-low-earth-orbit.csv')
        leocost = pd.read_csv(leocost_url, header=0)
        leocost['Year'] = pd.to_datetime(leocost['Year'], format='%Y')

    def local_nws(self):
        nwsdata_url = os.path.join(self.github_base_url, 'z_05mr24.shp')
        nwsdata = gpd.read_file(nwsdata_url)

if __name__ == "__main__":
    data_instance = local_data()
    data_instance.gcat()
    data_instance.ourworld()
    data_instance.local_nws()

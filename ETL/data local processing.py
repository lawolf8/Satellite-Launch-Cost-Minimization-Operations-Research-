import pandas as pd
import geopandas as gpd
import os
import Optional

class local_data_preprocess:
    def __init__(self) -> None:
        self.username = os.getenv("USERNAME", "Default User")
        self.current_path = os.getcwd()

    def gcat(self) -> Optional[pd.DataFrame]:
        # Adjust paths to move up one directory
        lp_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'launch.tsv')
        print(lp_path)
        lp = pd.read_table(lp_path, header=0)

        sc_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'satcat.tsv')
        sc = pd.read_table(sc_path, header=0)
        satcat = sc[sc['OpOrbit'].str.contains('Leo|LEO|LEO/I|LLEO/I', na=False)]

        ax_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'auxcat.tsv')
        ax = pd.read_table(ax_path, header=0)
        auxcat = ax[ax['OpOrbit'].str.contains('Leo|LEO|LEO/I|LLEO/I', na=False)]

        ftorbit_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'ftocat.tsv')
        ftorbit = pd.read_table(ftorbit_path, header=0)

        launchlist_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'launch.tsv')
        launchlist = pd.read_table(launchlist_path, header=0)
        launchlist = launchlist.dropna()

        orgs_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'orgs.tsv')
        orgs = pd.read_table(orgs_path, header=0)

        sites_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'sites.tsv')
        sites = pd.read_table(sites_path, header=0)
        return lp, satcat, auxcat, ftorbit, orgs, sites
    def ourworld(self) -> Optional[pd.DataFrame]:
        # Adjust path to move up one directory
        leocost_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'cost-space-launches-low-earth-orbit.csv')
        leocost = pd.read_csv(leocost_path, header=0)
        leocost['Year'] = pd.to_datetime(leocost['Year'], format='%Y')
        return leocost
    def local_nws(self) -> Optional[pd.DataFrame]:
        # Adjust path to move up one directory
        nwsdata_path = os.path.join(self.current_path, '..', 'Data', 'sat data', 'z_05mr24.shp')
        nwsdata = gpd.read_file(nwsdata_path)
        return nwsdata
class local_processing:
    def __init__(self):
        data_instance = local_data_preprocess()

        # Get the data
        lp, satcat, auxcat, ftorbit, orgs, sites = data_instance.gcat()
        leocost = data_instance.ourworld()
        nws_local = data_instance.local_nws()

        # Processing
        self.first_processing(lp, satcat, auxcat, ftorbit, orgs, sites,leocost,nws_local)

    def first_processing(self, lp=None, satcat=None, auxcat=None, ftorbit=None,
                         orgs=None, sites=None, leocost=None, nws=None):
        #Cost Average from last 20 years Per Launch Class
        leoyear = leocost[leocost['Year'] >= '2000-01-01']
        leoavgcost = leoyear.groupby('launch_class')['cost_per_kg'].mean()
        leoavgcost = pd.DataFrame(leoavgcost).reset_index()

        #Sites only located in the Southeast US Region (Florida, Georgia, Alabama, Mississippi, Louisiana, Texas)
        locations = 'Florida|Georgia|Alabama|Mississippi|Louisiana|Texas|FL|GA|AL|MS|LA|TX|US|United States'
        filtered_sites = sites[sites['Location'].str.contains(locations, na=False)]
        filtered_sites = filtered_sites.reset_index(drop=True)
        #filtered_sites['State, Country'] = filtered_sites['Location'].str.split(',').str[1] + ", " + filtered_sites['StateCode']
        filtered_sites['State'] = filtered_sites['Location'].str.contains(locations, na=False)
        return leoavgcost, filtered_sites
    def second_processing(self, ):
        pass


if __name__ == "__main__":
    data_instance = local_data_preprocess()
    data_instance.gcat()
    data_instance.ourworld()
    data_instance.local_nws()

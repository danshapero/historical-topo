import pandas
import pathlib
import subprocess

__all__ = ["file_index"]

# See `https://www.usgs.gov/faqs/can-i-get-bulk-order-usgs-topographic-maps-pdf-format-state-or-entire-country`
# See `http://prd-tnm.s3-website-us-west-2.amazonaws.com/?prefix=StagedProducts/Maps/Metadata/`
# for all indices of USGS topo maps.
base_url = "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/Metadata/"
archive_filename = "historicaltopo.zip"
if not pathlib.Path(archive_filename).exists():
    subprocess.run(f"curl -O {base_url}{archive_filename}".split())

index_filename = "historicaltopo.csv"
if not pathlib.Path(index_filename).exists():
    subprocess.run(f"unzip {archive_filename}".split())

with open(index_filename, "r") as index_file:
    file_index = pandas.read_csv(index_file)

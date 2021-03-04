import setuptools

# Parse the version from the rasterio module.
with open("ubdc_cctvapi/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    version=version,
    author_email="nick.ves@glasgow.ac.uk",
    description="API client for UBDC CCTV data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/urbanbigdatacentre/ubdc_cctvapi",
    project_urls={
        "Bug Tracker": "https://github.com/urbanbigdatacentre/ubdc_cctvapi/issues",
    }
)

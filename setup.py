from distutils.core import setup

setup(
    name="web-plotting",
    version="0.1",
    author="SSDS",
    author_email="arn45@cornell.edu",
    description="Cislunar Explorers web plotting framework",
    install_requires=["numpy", "matplotlib", "pytest",
                      "scipy", "astropy", "pandas", "jsonschema"],
    package_dir={"": "src"},
)

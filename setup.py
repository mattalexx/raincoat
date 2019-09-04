import setuptools
import json
import os
from pathlib import Path
from subprocess import check_call
from setuptools.command.install import install

APP_NAME = "Raincoat"

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        cfg_path = f"{str(Path.home())}/.config/{APP_NAME}.json"
        if not os.path.exists(cfg_path):            
            cfg = open(cfg_path, 'x')
            j = dict(
            jackett_apikey="",
            jackett_url="",
            description_length=100,
            exclude="",
            results_limit=20,
            client_url="",
            display="grid",
            torrent_client="transmission",
            torrent_client_username="",
            torrent_client_password=""
            )
            json.dump(j, cfg, indent=4)
        install.run(self)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="raincoat",
    version="0.2",
    author="Gabisonfire",
    author_email="gabisonfire@github.com",
    description="Tool to search torrents via Jackett and send them to your client.",
    keywords="transmission qbittorrent deluge jackett torrent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.*",
    packages=setuptools.find_packages(),
    entry_points = {
        "console_scripts": ['raincoat = raincoat.raincoat:main']
        },
    url="https://github.com/Gabisonfire/raincoat",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Topic :: Communications :: File Sharing",
    ],
    install_requires=["requests", "justlog", "colorama", "tabulate", "transmission-clutch", "deluge-client", "python-qbittorrent"],
    cmdclass={
        'install': PostInstallCommand
    },

)
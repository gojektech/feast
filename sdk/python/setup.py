# Copyright 2019 The Feast Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess

from setuptools import find_packages, setup

NAME = "feast"
DESCRIPTION = "Python SDK for Feast"
URL = "https://github.com/feast-dev/feast"
AUTHOR = "Feast"
REQUIRES_PYTHON = ">=3.6.0"

REQUIRED = [
    "Click",
    "google-api-core",
    "google-auth",
    "google-cloud-bigquery",
    "google-cloud-storage",
    "google-cloud-core",
    "googleapis-common-protos",
    "google-cloud-bigquery-storage",
    "grpcio",
    "pandas",
    "pandavro",
    "protobuf",
    "PyYAML",
    "fastavro",
    "kafka-python",
    "tabulate",
    "toml",
    "tqdm",
    "pyarrow",
    "numpy",
    "google",
    "confluent_kafka",
]

# README file from Feast repo root directory
repo_root = (
    subprocess.Popen(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE)
    .communicate()[0]
    .rstrip()
    .decode("utf-8")
)
README_FILE = os.path.join(repo_root, "README.md")
with open(os.path.join(README_FILE), "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    # https://stackoverflow.com/questions/28509965/setuptools-development-requirements
    # Install dev requirements with: pip install -e .[dev]
    extras_require={"dev": ["mypy-protobuf==1.*", "grpcio-testing==1.*"]},
    include_package_data=True,
    license="Apache",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={"console_scripts": ["feast=feast.cli:cli"]},
    use_scm_version={"root": "../..", "relative_to": __file__},
    setup_requires=["setuptools_scm"],
)

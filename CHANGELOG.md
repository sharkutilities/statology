<h1 align = "center">CHANGELOG</h1>

<div align = "justify">

All notable changes to this project will be documented in this file. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [PEP0440](https://peps.python.org/pep-0440/)
styling guide. For full details, see the [commit logs](https://github.com/sharkutilities/pandas-wizard/commits).

## `PEP0440` Styling Guide

<details>
<summary>Click to open <code>PEP0440</code> Styilng Guide</summary>

Packaging for `PyPI` follows the standard PEP0440 styling guide and is implemented by the **`packaging.version.Version`** class. The other
popular versioning scheme is [`semver`](https://semver.org/), but each build has different parts/mapping.
The following table gives a mapping between these two versioning schemes:

<div align = "center">

| `PyPI` Version | `semver` Version |
| :---: | :---: |
| `epoch` | n/a |
| `major` | `major` |
| `minor` | `minor` |
| `micro` | `patch` |
| `pre` | `prerelease` |
| `dev` | `build` |
| `post` | n/a |

</div>

One can use the **`packaging`** version to convert between PyPI to semver and vice-versa. For more information, check
this [link](https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html).

</details>

## Release Note(s)

The release notes are documented, the list of changes to each different release are documented. The `major.minor` patch are indicated
under `h3` tags, while the `micro` and "version identifiers" are listed under `h4` and subsequent headlines.

<details>
<summary>Click to open <code>Legend Guidelines</code> for the Project CHANGELOG.md File</summary>

  * 🎉 - **Major Feature** : something big that was not available before.
  * ✨ - **Feature Enhancement** : a miscellaneous minor improvement of an existing feature.
  * 🛠️ - **Patch/Fix** : something that previously didn’t work as documented – or according to reasonable expectations – should now work.
  * ⚙️ - **Code Efficiency** : an existing feature now may not require as much computation or memory.
  * 💣 - **Code Refactoring** : a breakable change often associated with `major` version bump.

</details>

### Statology V1 Release

The library is designed to provide a simple interface between different modules and to perform statistical operations on an
array (`numpy.ndarray`, `pandas.Series`, etc.) by using wrapper (context manager) controls.

#### v1.2.0 | Release Date : 2026-02-24

The version brings added functionalities, and other minor patches and bug fixes as below.

  * 💣 Renamed `sum_product()` to `weighted()`, change is necessary as it reflects the function use case.
  * 🎉 Added functionality to forecast for a longer interval based on two new additional parameters.

#### v1.1.0 | Release Date : 2026-02-23

The first stable version of **`statology`** that can work as a wrapper to perform statistical operations on external modules,
or can work standalone using `numpy.ndarray`. The following features are now available:

  * 🎉 Calculate outliers (`statology.outliers`) using IQR or Z-Score and return boolean,
  * 🎉 Flexibility to control boundary for both type of outlier detection if a forward integration module works in an
    unconventional way or does not follow thumb-rules.
  * 🎉 Create a function to return weighted average sum product of a series, this method is particularly helpful in financial
    accounting.

NOTE: There were two internal releases which were deleted from PyPI due to incompatibility issues, users are requested to
migrate to the latest version.

</div>

# Release Process

This document describes the release process for the nicolas-cache package.

## Versioning

The package uses [CalVer (Calendar Versioning)](https://calver.org/) with the format `YY.MM.DD` and [setuptools-scm](https://github.com/pypa/setuptools_scm) for automatic versioning based on git tags.

### Version Format

- **Release versions**: `YY.MM.DD` (e.g., `25.07.16` for July 16, 2025)
- **Development versions**: `YY.MM.DD.devN+gHASH` (automatically generated from git history)
- **Git tags**: `vYY.MM.DD` (e.g., `v25.07.16`)

### Version Sources

1. **Git tags**: Release versions are determined by git tags in CalVer format
2. **Git commits**: Development versions include commit information
3. **Fallback**: `25.07.16-dev` if git is not available

## Release Process

### 1. Prepare Release

1. Ensure all tests pass:
   ```bash
   pytest
   ```

2. Update documentation if needed

3. Update CHANGELOG.md with release notes

### 2. Create Release Tag

1. Create and push a CalVer version tag:
   ```bash
   # For a release on July 16, 2025
   git tag v25.07.16
   git push origin v25.07.16
   ```

2. The GitHub Actions workflow will automatically:
   - Run tests on multiple Python versions
   - Build the package
   - Upload to PyPI (if configured)
   - Create a GitHub release

### 3. Manual Release (if needed)

If you need to build and release manually:

1. Install build dependencies:
   ```bash
   pip install build setuptools-scm twine
   ```

2. Build the package:
   ```bash
   python -m build
   ```

3. Check the package:
   ```bash
   twine check dist/*
   ```

4. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

## GitHub Actions Workflows

### Test Suite (`python-package.yml`)

Runs on every push and pull request:
- Tests on Python 3.9, 3.10, 3.11, 3.12
- Type checking with mypy
- Linting with ruff
- Coverage reporting
- Redis integration tests

### Build and Package (`build-package.yml`)

Runs on git tags and can be triggered manually:
- Builds source distribution and wheel
- Uploads to PyPI (on tags)
- Creates GitHub release
- Uploads build artifacts

## PyPI Configuration

To enable automatic PyPI uploads:

1. Generate a PyPI API token at https://pypi.org/manage/account/token/
2. Add the token as a GitHub secret named `PYPI_API_TOKEN`

## Local Development

### Check Current Version

```bash
python -c "import nicolas; print(nicolas.__version__)"
```

### Build Package Locally

```bash
./scripts/build.sh
```

### Test Package Installation

```bash
pip install dist/nicolas-*.whl
```

## Version Examples

- `v25.07.16` → `25.07.16` (July 16, 2025)
- `v25.12.31` → `25.12.31` (December 31, 2025)
- `v26.01.01` → `26.01.01` (January 1, 2026)
- Untagged commits → `25.07.16.dev123+g1234abc`
- Multiple releases per day → `25.07.16.1`, `25.07.16.2`, etc.
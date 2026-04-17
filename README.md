# Research Software Release Baseline

A minimal, modern Python project template for research software.
It uses `uv` with `pyproject.toml`, a `src/` layout, `pytest`, Ruff, Sphinx docs,
and small Docker and Apptainer imagea.

## Structure
```
project/
  src/project_name/         # your package
  tests/test_project_name/  # tests
  docs/                     # Sphinx documentation
  Dockerfile                # Docker container build instructions
  apptainer_container.def   # Apptainer container build instructions
  .dockerignore
  .gitignore
  .env 
  pyproject.toml            # modern packaging
  README.md
  LICENSE                   # use MIT license for example
```

## Quick start

### Prerequisites
- Install **uv** (see https://docs.astral.sh/uv/getting-started/)

### Sync environment
```bash
uv lock && uv sync --all-groups
```

### Run tests & lint
```bash
# Test
uv run pytest
# Lint
uv run ruff check
```

### Build docs
```bash
rm docs/api/*.rst
uv run sphinx-apidoc -o docs/api/ src/project_name -f --separate --module-first --tocfile index
uv run sphinx-build -M html docs docs/_build
```
Open [./docs/_build/html/index.html](./docs/_build/html/index.html) in browser

### Run locally
```bash
uv run cli 1
```

### Docker
Build a small multi-stage image that reuses the uv lock when present.
```bash
docker build -t project-name:dev .
docker run --rm project-name:dev 1 -b 3
```

### Apptainer
Build an Apptainer image from the docker container.
```bash
apptainer build --force project-name.sif apptainer_container.def
apptainer run project-name.sif 1 -b 3
```

### Releasing
1. Update the version in `pyproject.toml`
2. Tag and push
```bash
git tag -a v0.1.0 -m "First baseline"
git push origin v0.1.0
```
3. Create a GitHub Release from the tag and include brief notes

## Notes
- `uv.lock` is optional here. Generate it with `uv lock` for reproducible installations.
- Prefer reStructuredText (reST) style docstrings with Sphinx autodoc.

## Contact or support 
If you have questions, bugs, or feature requests, please [open an issue](https://github.com/jbuerman/research-software-release-baseline/issues/new/choose).

# Acknowledgments

This reposotory was developed as part of the [UKRI Centre for Doctoral Training in Machine Intelligence for Nano- Electronic Devices and Systems (MINDS)](https://www.mindscdt.southampton.ac.uk/).


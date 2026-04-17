# syntax=docker/dockerfile:1
FROM python:3.12-slim AS builder
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# Install curl and uv
RUN apt-get update && apt-get install -y --no-install-recommends curl  && curl -LsSf https://astral.sh/uv/install.sh | sh  && rm -rf /var/lib/apt/lists/*
WORKDIR /app
# Copy manifests *and* README before syncing (needed by build backend)
COPY pyproject.toml uv.lock* README.md ./
# Copy the source package now so Hatchling can find src/project_name
COPY src/ src/
# Create a local venv and install dependencies deterministically
RUN /root/.local/bin/uv sync --no-group dev --no-group docs --frozen || /root/.local/bin/uv sync --no-group dev  --no-group docs

# ---- final image ----
FROM python:3.12-slim
ENV PATH="/app/.venv/bin:${PATH}" \
    VIRTUAL_ENV="/app/.venv" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app
# Copy the resolved virtualenv and source code
COPY --from=builder /app/.venv /app/.venv
COPY src/ src/
CMD ["cli", "1"]
ENTRYPOINT ["cli"]

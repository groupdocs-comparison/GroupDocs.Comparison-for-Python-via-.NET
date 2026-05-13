FROM python:3.13-slim

# System dependencies:
#   libicu-dev  - required by the .NET runtime
#   libgdiplus  - required for image comparison code paths (System.Drawing)
#   ttf-mscorefonts-installer - provides Arial and other MS core fonts used during rendering
#   fontconfig  - font cache management
RUN echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections \
    && sed -i 's/^Components: main$/Components: main contrib/' /etc/apt/sources.list.d/debian.sources 2>/dev/null \
    || sed -i 's/main$/main contrib/' /etc/apt/sources.list \
    ; apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        libicu-dev \
        libgdiplus \
        fontconfig \
        ttf-mscorefonts-installer \
    && fc-cache -f \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]

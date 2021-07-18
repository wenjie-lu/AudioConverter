# Audio Converter

## Get Started

[ffmpeg](http://ffmpeg.org/) is required to run this package.

To install the package: `pip install .`

To install the package for dev: `pip install -e .`

Supported source format: `.m4a`, `.wav` (more to be tested)

- Convert all files in the current directory: `audioconverter`
- Convert all files in specified directory: `audioconverter -i path/to/src/directory`
- Convert a specific file: `audioconverter -i path/to/src/file.wav`

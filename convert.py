import argparse
import os
import subprocess
from pathlib import Path


SUPPORTED_FORMAT = ["wav", "m4a"]


def check_ffmpeg():
    try:
        subprocess.check_output(["which", "ffmpeg"])
    except Exception as e:
        print(e, e.output)
        print("Error: ffmpeg is not installed.")


def convert(args):
    check_ffmpeg()

    src_dir = args.input if args.input else Path(".")
    src_files = []

    # Get src files to convert
    if src_dir.is_file():
        src_files = [src_dir]
        assert (
            src_dir.suffix.lower() in SUPPORTED_FORMAT
        ), f"Source format {src_dir.suffix} not supported!"
    else:
        for format in SUPPORTED_FORMAT:
            src_files.extend(list(Path.rglob(src_dir, f"*.{format}")))

    # Conversion
    num_converted = 0
    for src_file in src_files:
        targ_file = src_file.with_suffix(f".{args.format}")
        if targ_file.exists():
            print(f"Target existed. Skip {src_file.name}")
            continue

        print(f"===== Converting {src_file.name}... =====")
        subprocess.run(["ffmpeg", "-i", src_file.as_posix(), targ_file.as_posix()],)
        num_converted += 1

        # Remove the source file
        if args.delete_src:
            os.remove(src_file)

    print(f"Done! {num_converted} files converted. 🎉")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="",
        help="Input directory or file. Default: the current directory",
    )
    parser.add_argument(
        "--format", type=str, default="mp3", help="Target format. Default: .mp3"
    )
    parser.add_argument(
        "-d",
        "--delete_src",
        action="store_true",
        help="If True, delete source files after conversion",
    )
    args = parser.parse_args()
    convert(args)


if __name__ == "__main__":
    main()

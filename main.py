#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

from PIL import ExifTags, Image


def remove_exif_data(image_path):
    print("Remove exif data from image : ", image_path)

    new_image_name = input("Enter the name of the new image without extension: ")
    output_path = Path(new_image_name).with_suffix(Path(image_path).suffix)

    print("Saving image without exif data...")
    with Image.open(image_path) as img:
        img.save(output_path, exif=b"")

    print("Image saved successfully!")


def view_exif_data(image_path):
    print("View exif data from image : ", image_path, end="\n\n")

    with Image.open(image_path) as img:
        exif_data = img.getexif()

    if len(exif_data) == 0:
        print("No EXIF data found in the image.")
        return

    for tag, value in exif_data.items():
        if tag in ExifTags.TAGS:
            print(f"{ExifTags.TAGS[tag]}: {value}")
        else:
            print(f"Tag: {tag}, value: {value}")


def main():
    parser = argparse.ArgumentParser(
        description="View or remove EXIF data from an image."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-v", "--view", metavar="IMAGE", help="view image EXIF data")
    group.add_argument(
        "-r", "--remove", metavar="IMAGE", help="remove image EXIF data"
    )
    args = parser.parse_args()

    if args.view:
        view_exif_data(args.view)
    else:
        remove_exif_data(args.remove)


if __name__ == "__main__":
    main()

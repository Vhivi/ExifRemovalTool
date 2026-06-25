#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

from PIL import ExifTags, Image


def remove_exif_data(image_path):
    """
    Removes the EXIF data from the given image.

    Args:
        image_path (str): The path to the image file.

    Returns:
        None
    """
    print("Remove exif data from image : ", image_path)

    print("Opening image...")
    img = Image.open(image_path)
    img_extension = image_path.split(".")[-1]
    # Remove the EXIF data
    print("Getting data from image...")
    data = list(img.getdata())
    print("Creating image without exif data...")
    image_without_exif = Image.new(img.mode, img.size)
    image_without_exif.putdata(data)

    # Save the image without the EXIF data
    new_image_name = input("Enter the name of the new image without extension: ")
    print("Saving image without exif data...")
    image_without_exif.save(new_image_name + "." + img_extension)
    image_without_exif.close()
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

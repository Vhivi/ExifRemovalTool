#!/usr/bin/python
# -*- coding: utf-8 -*-

# Project Description: The project aims to provide a script that removes
# the EXIF data from an image. EXIF data is information stored
# in image files. This data can contain sensitive information
# such as the location of the shot, the camera model, the date
# of the shot, etc. The script should be able to remove this
# EXIF data from an image.
# Author:
# Creation Date: 2024-02-09
# Version: 1.0.3
# Python 3.10.11

################################################################
# Importing modules
################################################################

import getopt
import sys

from PIL import ExifTags, Image

################################################################
# Function declarations
################################################################


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
    """
    Displays the EXIF data of an image.

    Args:
        image_path (str): The path to the image.

    Returns:
        None
    """
    print("View exif data from image : ", image_path, end="\n\n")

    img = Image.open(image_path)
    # Retrieve the EXIF data
    exif_data = img.getexif()
    # Display the EXIF data
    # If no EXIF data is found, display a message
    if len(exif_data) == 0:
        print("No EXIF data found in the image.")
    else:
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

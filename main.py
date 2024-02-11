#!/usr/bin/python
# -*- coding: utf-8 -*-

# Project Description: The project aims to provide a script that removes
# the EXIF data from an image. EXIF data is information stored
# in image files. This data can contain sensitive information
# such as the location of the shot, the camera model, the date
# of the shot, etc. The script should be able to remove this
# EXIF data from an image.
# Author:
# Creation Date (dd/mm/yyyy): 09/02/2024
# Version:
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
    # Remove the EXIF data
    print("Getting data from image...")
    data = list(img.getdata())
    print("Creating image without exif data...")
    image_without_exif = Image.new(img.mode, img.size)
    image_without_exif.putdata(data)

    # Save the image without the EXIF data
    new_image_name = input("Enter the name of the new image without extension: ")
    print("Saving image without exif data...")
    image_without_exif.save(new_image_name + ".jpg")
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
    print("View exif data from image : ", image_path)

    img = Image.open(image_path)
    # Retrieve the EXIF data
    exif_data = img.getexif()
    # Display the EXIF data
    if exif_data is None:
        print("No exif data found")
    else:
        for tag, value in exif_data.items():
            if tag in ExifTags.TAGS:
                print(f"{ExifTags.TAGS[tag]}: {value}")
            else:
                print(f"Tag: {tag}, value: {value}")


def main():
    """
    This function is the entry point of the ExifRemovalTool program.
    It parses the command line arguments and performs the corresponding actions based on the provided options.
    """
    argumentlist = sys.argv[1:]

    options = "hv:r:"

    long_options = ["help", "view", "remove"]

    try:
        arguments, _ = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:
            # If no argument is passed, display the help message
            if currentArgument in ("-h", "--help") or len(sys.argv) == 1:
                print("Help message:", end="\n")
                print(
                    "This program is designed to remove EXIF data from an image. It takes the following options:"
                )
                print("-h, --help: Display this help message.")
                print("-v, --view : View the EXIF data of the specified image.")
                print(
                    "-r, --remove : Remove the EXIF data from the specified image.",
                    end="\n\n",
                )
                print("Usage: python main.py [options]")
                print("Example: python main.py -v image.jpg")
            elif currentArgument in ("-v", "--view"):
                view_exif_data(currentValue)
            elif currentArgument in ("-r", "--remove"):
                remove_exif_data(currentValue)
    except getopt.GetoptError as err:
        print(str(err))
        print("Usage: python main.py [options]")
        print("Example: python main.py -v image.jpg")


if __name__ == "__main__":
    main()

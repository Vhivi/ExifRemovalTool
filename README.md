ExifRemovalTool
===============

[![Python 3.10.11](https://img.shields.io/badge/python-3.10.11-blue.svg)](https://www.python.org/downloads/release/python-31011/)
[![Pillow 10.2.0](https://img.shields.io/badge/Pillow-10.2.0-blue.svg)](https://pypi.org/project/Pillow/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
--------------------------------

About
-----

ExifRemovalTool is a Python-based script designed to remove EXIF data from images, ensuring the privacy and security of sensitive information embedded in image files.

Project Description
-------------------

This project focuses on providing a versatile script capable of removing EXIF data, which often includes sensitive information such as the location of the shot, camera model, and date of the shot. The script empowers users to enhance their privacy by eliminating this EXIF data from images.

How to use it
-------------

1. **Install dependencies**

    ```shell
    pip install -r requirements.txt
    ```

2. **Using the script**

* To view the EXIF data of an image, use the following command:

    ```shell
    python main.py -v image.jpg
    ```

* To remove the EXIF data from an image, use the following command:

    ```shell
    python main.py -r image.jpg
    ```

Project Structure
-----------------

The project is based on Python 3.10.11 and utilizes the Pillow library (version 10.2.0) to manipulate images.

Acknowledgements
----------------

Special thanks to the open-source community for their valuable contributions and support.

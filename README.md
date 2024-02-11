ExifRemovalTool
===============

[![Python 3.10.11](https://img.shields.io/badge/python-3.10.11-blue.svg)](https://www.python.org/downloads/release/python-31011/)
[![Pillow 10.2.0](https://img.shields.io/badge/Pillow-10.2.0-blue.svg)](https://pypi.org/project/Pillow/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
--------------------------------

FR - Outil de suppression des données EXIF d'une image
------------------------------------------------------

Description du projet
---------------------

Ce projet vise à fournir un script capable de supprimer les données EXIF d'une image. Les données EXIF contiennent des informations sensibles telles que l'emplacement de la prise de vue, le modèle de l'appareil photo, la date de la prise de vue, etc. Le script peut supprimer ces données EXIF d'une image.

Comment l'utiliser
------------------

Le projet est basé sur Python 3.10.11 et utilise la bibliothèque `Pillow` (10.2.0) pour manipuler les images.

1. **Installation des dépendances**

```shell
pip install -r requirements.txt
```

1. **Utilisation du script**

* Pour visualiser les données EXIF d'une image, utilisez la commande suivante :

```shell
python main.py -v image.jpg
```

* Pour supprimer les données EXIF d'une image, utilisez la commande suivante :

```shell
python main.py -r image.jpg
```

Remerciements
-------------

EN - Tool to remove EXIF data from an image
-------------------------------------------

Project description
-------------------

This project provides a script capable of removing EXIF data from an image. EXIF data contains sensitive information such as the location of the shot, camera model, date of the shot, etc. The script can remove this EXIF data from an image.

How to use it
-------------

The project is based on Python 3.10.11 and uses the `Pillow` library (10.2.0) to manipulate images.

1. **Install dependencies**

```shell
pip install -r requirements.txt
```

1. **Using the script**

* To view the EXIF data of an image, use the following command:

```shell
python main.py -v image.jpg
```

* To remove the EXIF data from an image, use the following command:

```shell
python main.py -r image.jpg
```

Acknowledgements
----------------

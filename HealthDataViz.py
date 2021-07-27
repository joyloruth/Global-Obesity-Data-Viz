{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "HealthDataViz",
      "provenance": [],
      "authorship_tag": "ABX9TyPabGsEkRhWICQDAyZUSAJL",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joyloruth/Global-Obesity-Data-Viz/blob/master/HealthDataViz.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UBrje8VuPhO4"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "36_ezc9_nfDc",
        "outputId": "93d6ca35-7164-4f09-fe5f-8416de95763b"
      },
      "source": [
        "pip install geopandas"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting geopandas\n",
            "  Downloading geopandas-0.9.0-py2.py3-none-any.whl (994 kB)\n",
            "\u001b[K     |████████████████████████████████| 994 kB 8.6 MB/s \n",
            "\u001b[?25hCollecting fiona>=1.8\n",
            "  Downloading Fiona-1.8.20-cp37-cp37m-manylinux1_x86_64.whl (15.4 MB)\n",
            "\u001b[K     |████████████████████████████████| 15.4 MB 34 kB/s \n",
            "\u001b[?25hCollecting pyproj>=2.2.0\n",
            "  Downloading pyproj-3.1.0-cp37-cp37m-manylinux2010_x86_64.whl (6.6 MB)\n",
            "\u001b[K     |████████████████████████████████| 6.6 MB 38.5 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pandas>=0.24.0 in /usr/local/lib/python3.7/dist-packages (from geopandas) (1.1.5)\n",
            "Requirement already satisfied: shapely>=1.6 in /usr/local/lib/python3.7/dist-packages (from geopandas) (1.7.1)\n",
            "Collecting click-plugins>=1.0\n",
            "  Downloading click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (57.2.0)\n",
            "Collecting munch\n",
            "  Downloading munch-2.5.0-py2.py3-none-any.whl (10 kB)\n",
            "Requirement already satisfied: attrs>=17 in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (21.2.0)\n",
            "Requirement already satisfied: six>=1.7 in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (1.15.0)\n",
            "Collecting cligj>=0.5\n",
            "  Downloading cligj-0.7.2-py3-none-any.whl (7.1 kB)\n",
            "Requirement already satisfied: click>=4.0 in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (7.1.2)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from fiona>=1.8->geopandas) (2021.5.30)\n",
            "Requirement already satisfied: numpy>=1.15.4 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.24.0->geopandas) (1.19.5)\n",
            "Requirement already satisfied: pytz>=2017.2 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.24.0->geopandas) (2018.9)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.24.0->geopandas) (2.8.1)\n",
            "Installing collected packages: munch, cligj, click-plugins, pyproj, fiona, geopandas\n",
            "Successfully installed click-plugins-1.1.1 cligj-0.7.2 fiona-1.8.20 geopandas-0.9.0 munch-2.5.0 pyproj-3.1.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xKAhjIFinmXa"
      },
      "source": [
        "import geopandas as gpd"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eLl2mEvgnzf0"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_zwkjU41n7s8"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        },
        "id": "BYuCXoJPPnUO",
        "outputId": "b774e4df-4bc6-4520-ba56-cb8b053f8010"
      },
      "source": [
        "df = pd.read_csv(\"/share-of-deaths-obesity.csv\")\n",
        "df"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Entity</th>\n",
              "      <th>Code</th>\n",
              "      <th>Year</th>\n",
              "      <th>Obesity (IHME, 2019)</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>AFG</td>\n",
              "      <td>1990</td>\n",
              "      <td>3.92</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>AFG</td>\n",
              "      <td>1991</td>\n",
              "      <td>3.87</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>AFG</td>\n",
              "      <td>1992</td>\n",
              "      <td>3.82</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>AFG</td>\n",
              "      <td>1993</td>\n",
              "      <td>3.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Afghanistan</td>\n",
              "      <td>AFG</td>\n",
              "      <td>1994</td>\n",
              "      <td>3.25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6407</th>\n",
              "      <td>Zimbabwe</td>\n",
              "      <td>ZWE</td>\n",
              "      <td>2013</td>\n",
              "      <td>3.81</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6408</th>\n",
              "      <td>Zimbabwe</td>\n",
              "      <td>ZWE</td>\n",
              "      <td>2014</td>\n",
              "      <td>4.13</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6409</th>\n",
              "      <td>Zimbabwe</td>\n",
              "      <td>ZWE</td>\n",
              "      <td>2015</td>\n",
              "      <td>4.36</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6410</th>\n",
              "      <td>Zimbabwe</td>\n",
              "      <td>ZWE</td>\n",
              "      <td>2016</td>\n",
              "      <td>4.59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6411</th>\n",
              "      <td>Zimbabwe</td>\n",
              "      <td>ZWE</td>\n",
              "      <td>2017</td>\n",
              "      <td>4.86</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>6412 rows × 4 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "           Entity Code  Year  Obesity (IHME, 2019)\n",
              "0     Afghanistan  AFG  1990                  3.92\n",
              "1     Afghanistan  AFG  1991                  3.87\n",
              "2     Afghanistan  AFG  1992                  3.82\n",
              "3     Afghanistan  AFG  1993                  3.50\n",
              "4     Afghanistan  AFG  1994                  3.25\n",
              "...           ...  ...   ...                   ...\n",
              "6407     Zimbabwe  ZWE  2013                  3.81\n",
              "6408     Zimbabwe  ZWE  2014                  4.13\n",
              "6409     Zimbabwe  ZWE  2015                  4.36\n",
              "6410     Zimbabwe  ZWE  2016                  4.59\n",
              "6411     Zimbabwe  ZWE  2017                  4.86\n",
              "\n",
              "[6412 rows x 4 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    }
  ]
}
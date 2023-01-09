{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPtXyoGpSB/EKDhr/ENd8XC",
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
        "<a href=\"https://colab.research.google.com/github/TABEYWICKRAMA/Python_series_end-to-end/blob/main/Untitled62.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5TzilxAmWxG-",
        "outputId": "2235a60b-e4af-4c58-b6ba-0b1ecc5401c0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello world\n"
          ]
        }
      ],
      "source": [
        "print('Hello world')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#multiline strings\n",
        "print(''' Hi \n",
        "            This shows \n",
        "                    the code as \n",
        "                                we write our code. \n",
        "''')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VsKI2vgeW9M_",
        "outputId": "4dfd475f-06bd-43cc-e9a2-1fc6a2f55645"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Hi \n",
            "            This shows \n",
            "                    the code as \n",
            "                                we write our code. \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('thisara\\'s python world')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YcV3iYREW94l",
        "outputId": "ad7519b5-01b3-4a6e-f4c4-a36d35fbe2fd"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "thisara's python world\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **String concatination vs String formatting**"
      ],
      "metadata": {
        "id": "APkLR969XM4d"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#String concatination\n",
        "first = 'John'\n",
        "last = 'Smith'\n",
        "message = first + ' [' + last + '] is a coder.'\n",
        "print(message)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GzgcX1frXKRW",
        "outputId": "463e6ea2-45f6-492e-8ba4-6f7fcae36b1c"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "John [Smith] is a coder.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#String formatting\n",
        "msg = f'{first} [{last}] is a coder'\n",
        "print(msg)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iNxfQ6rdXVrU",
        "outputId": "5a42a7d8-1fb9-4afa-a28c-d4c7d14835b3"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "John [Smith] is a coder\n"
          ]
        }
      ]
    }
  ]
}
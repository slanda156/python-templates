# Python templates

> A collection of python templates.

![GitHub contributors](https://img.shields.io/github/contributors/slanda156/python-templates)
![GitHub Repo stars](https://img.shields.io/github/stars/slanda156/python-templates?style=plastic)

This is a collection of diffrent templates for my most used modules.

## Installation

1. Copy the folder of the template you want to use

    ```sh
    cp template-folder your-project-name
    ```

2. Move into this new folder

    ```sh
    cd your-project-name
    ```

3. Create a virtual enviroment

    venv:

    ```sh
    venv .venv
    ```

    virtualenv (faster creation):

    ```sh
    virtualenv .venv
    ```

4. Activate the enviroment

    Linux:

    ```sh
    source .venv/bin/activate
    ```

    Windows:

    ```sh
    .venv\bin\activate.bat
    ```

5. Install pip-tools

    ```sh
    pip install pip-tools
    ```

6. Compile the requirements

    ```sh
    pip-compile
    ```

    Docs:

    ```sh
    pip-compile requirements-docs.in
    ```

7. Syncronise your virutal enviroment

    ```sh
    pip-sync
    ```

8. Install docs modules (Optional)

    ```sh
    pip install -r requirements-docs.txt
    ```

9. Serve the docs (Optional)

    ```sh
    mkdocs serve
    ```

10. Build the docs (Optional)

    ```sh
    mkdocs build
    ```

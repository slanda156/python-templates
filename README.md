# Python templates

> A collection of python templates.

![GitHub contributors](https://img.shields.io/github/contributors/slanda156/python-templates)
![GitHub Repo stars](https://img.shields.io/github/stars/slanda156/python-templates?style=plastic)

This is a collection of different templates for my most used modules.

fastapi: This template is still in development and doesn't work out of the box yet.

## Installation

1. Copy the folder of the template you want to use

    ```sh
    cp template-folder your-project-name
    ```

2. Move into this new folder

    ```sh
    cd your-project-name
    ```

3. Create a virtual environment

    venv:

    ```sh
    python -m venv .venv
    ```

    virtualenv (faster creation):

    ```sh
    virtualenv .venv
    ```

4. Activate the environment

    Linux:

    ```sh
    source .venv/bin/activate
    ```

    Windows:

    ```sh
    .venv\Scripts\activate.bat
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

7. Synchronize your virtual environment

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

## Meta

Christoph Heil – <christoph.heil156@gmail.com>

Distributed under the MIT license. See [``License``](LICENSE) for more information.

[https://github.com/slanda156/python-templates](https://github.com/slanda156/python-templates)

## Contributing

Any ideas or bug reports are welcome as issues or comments.

If you want to contribute, please fork the repository and create a pull request.

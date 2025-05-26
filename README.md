# Python templates

> A collection of python templates.

![GitHub contributors](https://img.shields.io/github/contributors/slanda156/python-templates)
![GitHub Repo stars](https://img.shields.io/github/stars/slanda156/python-templates?style=plastic)

This is a collection of different templates for my most used modules.

**fastapi**: This template is still in development and doesn't work out of the box yet.

## Installation and Usage

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

    Open your browser and go to [127.0.0.1:8000](http://127.0.0.1:8000)

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

## Deutsch

### Python-Vorlagen

> Eine Sammlung von Python-Vorlagen.

Dies ist eine Sammlung verschiedener Vorlagen für meine am häufigsten verwendeten Module.

fastapi: Diese Vorlage befindet sich noch in der Entwicklung und funktioniert noch nicht direkt.

### Installation und Verwendung

1. Kopiere den Ordner der gewünschten Vorlage

    ```sh
    cp template-folder dein-projekt-name
    ```

2. Wechsle in diesen neuen Ordner

    ```sh
    cd dein-projekt-name
    ```

3. Erstelle eine virtuelle Umgebung

    venv:

    ```sh
    python -m venv .venv
    ```

    virtualenv (schnellere Erstellung):

    ```sh
    virtualenv .venv
    ```

4. Aktiviere die Umgebung

    Linux:

    ```sh
    source .venv/bin/activate
    ```

    Windows:

    ```sh
    .venv\Scripts\activate.bat
    ```

5. Installiere pip-tools

    ```sh
    pip install pip-tools
    ```

6. Erstelle die requirements-Dateien

    ```sh
    pip-compile
    ```

    Dokumentation:

    ```sh
    pip-compile requirements-docs.in
    ```

7. Synchronisiere deine virtuelle Umgebung

    ```sh
    pip-sync
    ```

8. Installiere die Dokumentationsmodule (Optional)

    ```sh
    pip install -r requirements-docs.txt
    ```

9. Starte die Dokumentation lokal (Optional)

    ```sh
    mkdocs serve
    ```

    Öffne deinen Browser und gehe zu [127.0.0.1:8000](http://127.0.0.1:8000)

10. Baue die Dokumentation (Optional)

    ```sh
    mkdocs build
    ```

### Meta

Christoph Heil – <christoph.heil156@gmail.com>

Veröffentlicht unter der MIT-Lizenz. Siehe [``License``](LICENSE) für weitere Informationen.

[https://github.com/slanda156/python-templates](https://github.com/slanda156/python-templates)

### Mitwirken

Ideen oder Fehlerberichte sind als Issues oder Kommentare willkommen.

Wenn du beitragen möchtest, forke das Repository und erstelle einen Pull Request.

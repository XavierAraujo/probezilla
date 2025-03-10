# Setup 

The project is configured via [Poetry](https://python-poetry.org/docs/). To set it up you just need to run: 
```
poetry install
```

Currently the project was only validated using Python 3.11.6 so you can use pyenv to set that Python version up.
Or you can remove this strict dependency from Poetry 'pyproject.toml' configuration file and proceed with the Python version you have set up.

# Run
To run the project either enter on Poetry shell and execute the main script

```
poetry shell
python probezilla/probezilla.py
```

or just execute it directly

```
poetry run python probezilla/probezilla.py
```
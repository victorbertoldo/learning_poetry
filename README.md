# Learning Poetry


To install Poetry let's run this command:

```shel
curl -sSL https://install.python-poetry.org | python3 -
```

Now that poetry is installed, let's init a new project.

```shel
poetry new <project_name>
```

Here we'll use poetry_test_pack.

Now to install the project and it dependencies go to the project dir and run this:

```shel
poetry install <project_name>
```

To add external libs and packages we only do this:

```shel
poetry add httpx
```

To remove it we only do this:

```shel
poetry remove httpx
```

To do it in a dev environment:

```shel
poetry add --dev httpx
```

To remove it we only do this:

```shel
poetry remove --dev httpx
```


To access the context of the project run this:

```shel
poetry shell
```

To change the context of vs code, click in the selection of interpreters and put a path like this in it:

```shell
/home/vitao/.cache/pypoetry/virtualenvs/poetry-test-pack-6r0LYRVR-py3.10/bin/python3.10
```
> You will have to search it to get the specific path for this project.

To see what the project will be running when the call is done, go to the toml file and search it for `[tool.poetry.scripts]`

To run the project just run:

```shel
poetry run <project_name>
```

To build the project just run:


```shel
poetry build
```

To publish it into pypi:


```shel
poetry publish
```
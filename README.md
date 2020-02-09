# Snakypy Helloworld - Cookiecutter

`Snakypy Helloworld - Cookiecutter` is a template for [Cookiecutter](https://github.com/cookiecutter/cookiecutter) not creating a Hello World on the console with entry points.


## For Developers

**Download and access the template:**

```
$ ROOT="/tmp"
$ git clone https://github.com/snakypy/snakypy-helloworld.git $ROOT/snakypy-helloworld
$ cd $ROOT/snakypy-helloworld
$ git checkout cookiecutter
```

## For User final

**Compile template and install package:**

```
$ ROOT="/tmp"
$ cookiecutter --no-input -o $ROOT https://github.com/snakypy/snakypy-helloworld.git --checkout cookiecutter
$ cd snakypy_helloworld
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
$ bin/make install
$ snakypy-helloworld
```

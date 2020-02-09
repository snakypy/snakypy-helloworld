# Snakypy Helloworld - Cookiecutter

`Snakypy Helloworld - Cookiecutter` is a template for [Cookiecutter](https://github.com/cookiecutter/cookiecutter) not creating a Hello World on the console with entry points.


## Developers

```
$ ROOT="/tmp"
$ mkdir $ROOT/snakypy-helloworld-cookiecutter; cd $_
$ git clone https://github.com/snakypy/snakypy-helloworld.git; cd snakypy-helloworld
$ git checkout cookiecutter
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
```

**Compile and install:**

```
$ cookiecutter --no-input -o $ROOT https://github.com/snakypy/snakypy-helloworld.git
$ cd $ROOT/snakypy_helloworld
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
$ bin/make install
$ snakypy-helloworld
```

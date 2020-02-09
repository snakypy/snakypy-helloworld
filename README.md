# Snakypy Helloworld - Cookiecutter

`Snakypy Helloworld - Cookiecutter` is a template for [Cookiecutter](https://github.com/cookiecutter/cookiecutter) not creating a Hello World on the console with entry points.


## Developers

```
$ ROOT="/tmp"
$ git clone https://github.com/snakypy/snakypy-helloworld.git $ROOT; cd $ROOT/snakypy-helloworld
$ git checkout cookiecutter
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
```

**Compile and install:**

```
$ mkdir build; cd $_
$ cookiecutter --no-input -o build https://github.com/snakypy/snakypy-helloworld.git
$ cd build/snakypy_helloworld
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
$ bin/make install
$ snakypy-helloworld
```

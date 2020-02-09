# Snakypy Helloworld - Cookiecutter

`Snakypy Helloworld - Cookiecutter` is a template for [Cookiecutter](https://github.com/cookiecutter/cookiecutter) not creating a Hello World on the console with entry points.


## For Developers

**Download template:**

```
$ ROOT="/tmp"
$ git clone https://github.com/snakypy/snakypy-helloworld.git $ROOT/snakypy-helloworld
$ cd $ROOT/snakypy-helloworld
$ git checkout cookiecutter
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
```

**Compile template and install package:**

```
$ mkdir build; cd $_
$ cookiecutter --no-input -o build https://github.com/snakypy/snakypy-helloworld.git --checkout cookiecutter
$ cd build/snakypy_helloworld
$ git checkout master
$ deactivate
$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements-dev.txt
$ bin/make install
$ snakypy-helloworld
```

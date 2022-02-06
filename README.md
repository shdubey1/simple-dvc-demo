create env

```bash

conda create -n wineq python=3.7 -y
```

activate env

```bash

conda activate wineq
```

create a requirement file

install the req
```bash
pip install -r requirements.txt
```

download the data from

https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

one line commit
```
git add . && git commit -m "update README.md"
```
```bash
git add .
```

```bash
git commit -m "first commit"
```

```bash
git remote add origin https://github.com/shdubey1/simple-dvc-demo.git
git branch -M main
git push origin main
```

tox command

```bash
tox
```
for rebuilding

```bash
tox -r
```
pytest command
```bash
pytest -v
```

setup commands
```bash
pip install -e .
```

build your own package command

```bash
python setup.py sdist bdist wheel
```

create an artifacts folder

mlflow server command -

mlflow server \
    --backend-store-uri sqlite:///mlfolw.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1235
    




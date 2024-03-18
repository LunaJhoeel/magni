Check pyenv versions in OS and in local directory
```bash
pyenv versions
pyenv local
```
Install specific Python version to OS
```bash
pyenv install 3.12.2
```
Install local pyenv
```bash
pyenv local 3.12.2
```
Install uv
```bash
pip install uv
```
Create environment with uv
```bash
uv venv uvenv
```
Activate environment
```bash
source uvenv/bin/activate
```
List packages installed with uv
```bash
uv pip list
```
Install Chronos with pip
```bash
pip install git+https://github.com/amazon-science/chronos-forecasting.git
```
Install dependencies
```bash
pip install -r requirements.txt
```


https://github.com/pyenv/pyenv

https://delightfuldatascience.substack.com/p/the-ultimate-python-set-up-pyenv

https://realpython.com/intro-to-pyenv/#what-about-a-package-manager

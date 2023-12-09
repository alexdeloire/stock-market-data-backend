# Stock Market API

<div align='center'>

[Pre-requisites](#pre-requisites) | [Install](#installation) | [Usage](#usage) | [License](#license)

This is a backend API for stock market data. It is built with Python and FastAPI.

</div>

# Pre-requisites

You need to have python3 installed on your system. If you don't have it, you can install it from [here](https://www.python.org/downloads/).

# Installation

1. Clone the repository

```bash
git clone <repo-url>
```

2. Create a virtual environment

```bash
python3 -m venv env
```

3. Activate the virtual environment (this is for linux, for windows, see [here](https://docs.python.org/3/library/venv.html))


```bash
source env/bin/activate
```

4. Install the dependencies

```bash
pip install -r requirements.txt
```

5. Run the server

```bash
python3 main.py
```

# Usage

There is a frontend application to interact with the API. The frontend application can be found [here](https://github.com/alexdeloire/stock_market_data_frontend).

You can test uploading a csv file for new data with the files provided in the 'data_to_upload' folder.

# Credits

Made by [Alexandre Deloire](https://github.com/alexdeloire).

# License

<div align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
</div>
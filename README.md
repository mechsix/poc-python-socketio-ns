## Overview

The proof of concept project with Python SocketIO on Tornado backend with socket.io js client

## Install Launching

Install dependency

```
poetry install
```

Activate the shell

```
poetry shell
```

Launch backend

```
python -m server
# Launch on port 8888
```

Launch frontend

```
cd client
python -m http.server
# Launch on port 8000
```


## Access the page

Go to `localhost:8000` to see the concept
Check the connection status from backend console or frontend DOM
if systemctl is-active --quiet mongodb; then
    echo "MongoDB is already running."
else
    sudo service mongodb start
fi

lint_errors=$(ruff check . --exclude __init__.py)

if [ -n "$lint_errors" ]; then
    echo "Linting errors detected. Aborting the project execution."
    exit 1  
fi

python3 app.py

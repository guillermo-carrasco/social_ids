# Remove building leftovers
rm -rf build dist *egg-info htmlcov src

# Remove pyc files
find . -type f -name *pyc -exec rm {} +

# Remove __pycache__ directories
find . -type d -name __pycache__ -exec rm -rf {} +

#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

G='\033[0;32m'
Y='\033[1;33m'
NC='\033[0m'

echo "${Y}Installing deps...${NC}"
poetry install
echo "${G}Dependencies installed.${NC}"
echo "${Y}Setting Pre-Commit hooks...${NC}"
poetry run pre-commit install

poetry run pre-commit autoupdate
echo "${G}Pre-Commit hooks set.${NC}"

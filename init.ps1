echo "----------- setting venv -----------"
py -3.12 -m venv .venv

echo "----------- activate venv -----------"
.venv/Scripts/activate

echo "----------- pip install -----------"
pip install -r requirements.txt -r requirements.dev.txt
rm app.pex
pip wheel -w . .
pex --python=python3 -f $PWD click cli-passthrough cli -e app.main -o app.pex
rm cli-0.0.0-py3-none-any.whl
rm -rf ~/.pex
./app.pex

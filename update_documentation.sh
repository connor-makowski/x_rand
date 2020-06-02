# Must be installed locally to work `pip install -e .`
pdoc --html --force -o docs x_rand/
mv ./docs/x_rand/* ./docs
rm -r ./docs/x_rand

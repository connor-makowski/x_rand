# Must be installed locally to work `pip install -e .`
# Must also have pydoc3 installed locally `pip install -r dev_requirements.txt`
pdoc --html --force -o docs x_rand/
mv ./docs/x_rand/* ./docs
rm -r ./docs/x_rand

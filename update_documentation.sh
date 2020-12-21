# Must be installed locally to work `pip install -e .`
# Must also have pydoc3 installed locally `pip install -r dev_requirements.txt`
pdoc --html --force -o docs x_rand/ x_rand2/
mv ./docs/x_rand2/* ./docs
# rm -r ./docs/x_rand

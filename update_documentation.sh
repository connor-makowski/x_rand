# Must be installed locally to work `pip install -e .`
pdoc --html --html-dir docs --overwrite x_rand
mv ./docs/x_rand/* ./docs
rm -r ./docs/x_rand

# Setup
1. Install Python3.6+
2. Navigate to this directory
  ```
  cd path/to/fingerprint
  ```
3. Setup the python environment
  - First time setup on unix/osx:
  ```
  pip3 install virtualenv
  python3 -m virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  deactivate
  ```

  - First time setup on windows:
  ```
  pip3 install virtualenv
  python3 -m virtualenv venv
  venv/Scripts/activate
  pip3 install -r requirements.txt
  deactivate
  ```

# Run the code:
1. Activate your virtualenv
  - On unix/osx
  ```
  source venv/bin/activate
  ```
  - On windows
  ```
  venv/Scripts/activate
  ```

2. Copy in your current course data into `path/to/fingerprint/data`
  - Rename your downloaded anon id csv file to `aids.csv`
  - Rename your downloaded anon id csv file to `profile_info.csv`

3. Copy your edX code to `path/to/fingerprint/fingerprint.edx`

4. Copy your problem data into `path/to/fingerprint/fingerprint.py`:
  - Note: You can not copy your code exactly.
  - Note: Make sure to follow the `#` comments in `fingerprint.py`

5. Run the script:
  ```
  python3 fingerprint.py
  ```

6. Deactivate your python environment
  ```
  deactivate
  ```

7. Your output should be in `path/to/fingerprint/data/output.csv`

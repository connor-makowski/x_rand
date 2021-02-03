# Setup
1. Install [Python3.6+](https://www.python.org/downloads/) on a Unix based system
  - If on unix/macos, skip to step 2 after installing python3.6+
  - If on windows 10 use WSL (instructions below) or a VM (no instructions provided)
    - Set up WSL2 on Win 10
      - Follow the [Microsoft docs here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install WSL2
    - Install Ubuntu 20.04 from the Microsoft store
    - Open Ubuntu 20.04 and install requirements
      - Create a user and password (make sure to remember this)
      - Run the following commands in the terminal:
        - Note: You may be prompted for your password (that you created above)
        ```
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python3 python3-pip git -y
        ```

2. Clone the x_rand repository into your personal folder and navigate into it:
  ```
  cd ~
  git clone https://github.com/connor-makowski/x_rand.git
  cd ~/x_rand/examples/fingerprint
  ```

3. Setup the python fingerprint environment
  ```
  pip3 install virtualenv
  python3 -m virtualenv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  deactivate
  ```

# Run the code after initial setup:
1. Navigate into the fingerprint repository and activate your virtualenv
  ```
  cd ~/x_rand/examples/fingerprint
  source venv/bin/activate
  ```

2. Download and copy in your current course data into `path/to/fingerprint/data`
  - Download anonymous_student_ids.csv and rename the file to `aids.csv`
  - Download profile_information.csv and rename the file to `profile_info.csv`
  - Move `aids.csv` and `profile_info.csv` to `~/x_rand/examples/fingerprint/data`
    - If you are using WSL, the `~` will not be easily accessable.
      - Your Root WSL system can be found in your file explorer at `\\wsl$`
      - The `~` character represents your user data at `\\wsl$` -> `<your linux distribution>` -> `home` -> `<your username>`

3. (Optional) Copy your edX code to `~/x_rand/examples/fingerprint/fingerprint.edx`

4. Copy your problem data into `~/x_rand/examples/fingerprint/fingerprint.py`:
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

7. Your output should be in `~/x_rand/examples/fingerprint/data/output.csv`

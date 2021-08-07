# Check attendance by Face Recognition
## Install
```
# Install dependences
sudo apt install libpq-dev # for deb
sudo pacman -S postgresql-libs # for arch


# Install pacakages
pip3 install -r ./requirements.txt # for deb
pip install -r ./requirements.txt # for arch and window
```

After that, download folder Models in this [link](https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view) and add to the root of this folder.

Folder structure will look like
```
.
|
--AISrc
|
--Models
  |
  --20180402-114759.pb
  |
  --...
```

Then, you have to ensure database configuration in `AISrc/src/settings.py` is correct

```
cd AISrc

# Run migration if your database is empty
python3 manage.py migrate
```
Next step, let's create folder `Dataset/FaceData` in the root of project, add 2 subfolders `processed` and `raw`

Download dataset from [this](https://drive.google.com/drive/folders/1itJjeBTp5CEW-gFDt2cMl7AN4DeeTHR3) and put it into `raw`

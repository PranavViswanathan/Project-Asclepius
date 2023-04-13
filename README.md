# Project-Asclepius

The healthcare industry is a vital existence in any country. However, it has come to our notice that there are a few areas where improvements can be made, or maybe even completely overhauled. 
In case of any accidents, victims are handled by first responders (first aid) or if at a hospital, the emergency department. The treatment provided here is to stabilize the victim enough to proceed with further treatment, however, there are chances that said victim may have an allergic reaction to the substance being used. This further endangers the victim, instead of stabilizing them.
Patients who consult multiple doctors from different hospitals have individual files in their name at each of those hospitals. None of the visited hospitals have the patient’s complete medical history, which in cases can provide extra insight to the doctors regarding the patient’s treatment plan.

## Using the project

tarp - Contains code for RFID data collection<br>
tarpBlockchain - Contains blockchain code<br>
PDFReader - Reads data from insurance papers

## Running the project:

The project runs on flask and the dependencies can be installed via pip.

Steps to follow:

1. Create a virtual environment:
```
    virtualenv env
```
2. Create activate the virtual environment

```
source PATH/TO/FILE/activate
```
3. Install dependencies

```
pip install -r requirements.py
```

4. Run application

```
SET FLASK_APP=app
python -m flask run
```

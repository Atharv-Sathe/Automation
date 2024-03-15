# Welcome to Automatic Certificate/Letter Generation

## Folder Structure
* _Design_ : Contains all the designs for the certificates/letters.
* _Fonts_ : Contains all the fonts used in the designs.
* _Generated_ : All the generated certificates/letters will be stored here.
* _DesGen.py_ : The main script to generate certificates/letters.
* _DelGen.py_ : The main script to delete generated certificates/letters from the 'Generated' folder.

## Working
The python script `DesGen.py` reads the data from the CSV file and generates certificates/letters for each participant/member. The generated certificates/letters are stored in the 'Generated' folder.
<br>
Once the certificates/letters are generated one can use the `DelGen.py` script to delete all the generated certificates/letters from the 'Generated' folder. Before deleting the generated files can be either cut or copy pasted to another desired folder if required.

## Optimization
To optimize the generation process multithreading has been used with the help of concurrent futures module and 
ProcessPoolExecutor class which allows the script to run the generateCertificate function on multiple CPU cores making the porcess faster and efficient.

## ImpLinks
The following link can be used to accurately find the coordinates of any point on the design.
* [https://www.image-map.net/](https://www.image-map.net/)

## Dependencies
Check the requirements.txt(Automation/requirements.txt) file for the required dependencies. 
To install the dependencies run the following command in the terminal.
`pip install -r requirements.txt`


## Issues
1. Due to the uneven sizes of names, sometimes the alignment of few names may not be perfect. This can be fixed by manually adjusting the coordinates in the design for specific names. **_Fixed : ✅_**


**_For security reasons certain folders like CSVs, Designs, Generated, Attachements have not been uploaded._**

## DesGen.py Documentation

This script generates certificates for a list of names and registration numbers provided in a CSV file. It uses the Python Imaging Library (PIL) to open a certificate template, draw the name and registration number on the certificate, and save the generated certificate as a PNG file.

## Dependencies

The script requires the following Python packages:

- pandas
- PIL (Pillow)
- concurrent.futures (built-in)

You can install the required packages using pip:

```bash
pip install pandas pillow
```
### How to Use
1. Prepare a CSV file with the names and registration numbers. The CSV file should have columns named 'Name' and 'Registration Number'.

2. Update the main function in the script to read your CSV file:
```python
csv = pd.read_csv('path_to_your_csv_file.csv')
```
3. Update the coordinates to draw the name and registration number on the certificate:

4. Run the script using the command `python DesGen.py`.

The script will generate a certificate for each name in the CSV file and save it as a PNG file in the ./Generated and ../SendEmails/Attachments directories.

### Function Descriptions
`generateCertificate(name, regNo)`: This function generates a certificate for the given name and registration number. It opens the certificate template, draws the name on the certificate, and saves the certificate as a PNG file.

`main()`: This function reads the names and registration numbers from the CSV file, and uses a process pool executor to generate certificates for all names concurrently.

### Error Handling
If an error occurs while reading the CSV file or generating the certificates, the script will print the error message and continue.


#### Regards
**_TheBug_**
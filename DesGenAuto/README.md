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

### ImpLinks
The following link can be used to accurately find the coordinates of any point on the design.
* [https://www.image-map.net/](https://www.image-map.net/)

### Dependencies
* Python 3.7 or above
* Pillow
* Pandas
* Concurrent Futures

### Issues
Due to the uneven sizes of names, sometimes the alignment of few names may not be perfect. This can be fixed by manually adjusting the coordinates in the design for specific names.
However a solution to this minor issue is **being worked upon**.

**_For security reasons the details in the CSV files have been cleared, however you can use your own CSV files to generate certificates/letters._**


#### Regards
**_TheBug_**
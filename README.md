# Project Dataset for Trainings

This repository contains Python code that can be re-used by participants of trainings about coding practices. Thus the idea is to use the code as a starting point and improve it during the training.

## Contents

The script is called `script.py`:  

- It receives an arbitrary amount of `.csv` files as input.
- It plots the data of the first two columns of each file, all together in a single plot that produces as output in a `.png` file.
- It looks at the range of the first column of each file, and prints to the terminal screen the overlap range considering all input files.

## Usage

In the terminal, the script is run with the following command:

```
python script.py <list_input_files> <name_plot> <x-axis_label> <y-axis_label>
```

where:
- `<list_input_files>`: list of `.csv` input files  
- `<name_plot>`: name of the output `.png` plot file
- `<x-axis_label>`: string with the x-axis label of the plot
- `<y-axis_label>`: string with the y-axis label of the plot

### Example 

To exemplify how the code works you can use any `.csv` files that have at least 2 columns. Here we will use the following dataset from the 4TU.ResearchData archive: https://doi.org/10.4121/uuid:ad6de66a-72be-4835-b97d-7d6ab1bd378c

This is a finalized dataset that is publicly available. Once downloaded, unzip it and move the files to a `data/` directory. Take a look at the README file (called `_Readme First.txt`). The dataset corresponds to monitoring data of fatigue experiments carried out with 12 different specimens. For each specimen, acoustic emission data (`AE*.csv`) and digital image correlation data (`DIC*.csv`) are recorded against time.

Let us say the `script.py` is in `~/Desktop` and the data directory is in `~/Desktop/data/`. Then we can plot the acoustic emission data of the first 8 specimens by typing:

```
python script.py data/AE*0[1-8].csv Plot_AE_Specimen_1-8.png "Time (s)" "Cumulative Energy (J)"
```

The script will create a `Plot_AE_Specimen_1-8.png` file in the current directory, and it will print to the screen the overlap time range between the files: `(500.0, 15000.0)`.

## Requirements

You will check how to write a proper requirements.txt file during the training. Thus for now we will just specify that the `script.py` has been written with Python 3.8.5 using the following packages:

```
numpy==1.19.2
matplotlib==3.3.2
```

## License

The material found in this repository is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (CC-BY-4.0). See more in the LICENSE file.

## References

Eleftheroglou, Nikolaos; Zarouchas, D. (Dimitrios); Benedictus, R. (Rinze) (2020): Composite specimens under fatigue and impact loading conditions. 4TU.ResearchData. Dataset. https://doi.org/10.4121/uuid:ad6de66a-72be-4835-b97d-7d6ab1bd378c 
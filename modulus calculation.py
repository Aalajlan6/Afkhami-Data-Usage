import pandas as pd
import numpy as np
import glob
import re
import matplotlib.pyplot as plt

file_list = glob.glob('/*.csv')
file_list = sorted(file_list, key=lambda x: int(re.search(r'\d+', x).group()))

stress_frames = []
strain_frames = []

for idx, file in enumerate(file_list):
    print(file)
    df = pd.read_csv(file, skiprows=3)
    force = df.iloc[:, 1]
    stroke = df.iloc[:, 2]
    stress = force / (3.18 * 3.2) # surface area
    strain = stroke / 25.4 # initial height
    stress_frames.append(stress)
    strain_frames.append(strain)
    stress_strain_df = pd.DataFrame({'Stress': stress, 'Strain': strain})
    stress_strain_df.to_csv(f'/{idx+1}.csv', index=False) # save to new files



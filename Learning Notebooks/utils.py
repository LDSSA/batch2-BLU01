import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def measure_error(measurement, corect_measure):
    error = measurement-corect_measure
    print('We measured %0.2f Km, which is wrong by %0.2f Km' % 
          (measurement, error))


def measure_the_earth(std, verbose=False):
    
    corect_measure=6371
    
    measurement = np.random.normal(corect_measure, corect_measure * std)
    
    if verbose: 
        measure_error(measurement, corect_measure=corect_measure)
        
    return measurement


def plot_number_of_tries(series):
    
    # oh... you are reading my plotting code? How embarrasing
    ax = series.plot(figsize=(16, 8))
    plt.axhline(6371+10, color='g', ls=':')
    plt.axhline(6371-10, color='g', ls=':')
    plt.ylim([6371-100, 6371+100])
    plt.title('Expanding window of the measures of the radius of the Earth (+/- 10 Km in green)')
    plt.xlabel('Number of measurements')
    plt.ylabel('Mean measurement')
    plt.show()

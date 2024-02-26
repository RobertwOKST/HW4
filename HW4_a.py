#Robert's code edited by Anthony
#importsregion
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#endregion

#problemregion
"""
Step 1: Define the parameters for each normal distribution (sigma and mu)
Step 2: Create ranges for the x values (will show up on graph)
Step 3: Calculate the probability density function (pdf) for each normal distribution
Step 4: Calculate the cumulative distribution function (cdf) for each normal distribution
Step 5: Plot the pdf and cdf for each normal distribution
Step 6: Format the 4 graphs
"""

def main():
    """
    :param: mu1: mean of the 1st normal distribution
    :param: sigma1: stdv of the first normal distribution
    :param: mu2: mean of the 2nd distribution
    :param: sigma2: stdv of the 2nd distribution
    :param: x1: range for the 1st distribution
    :param: x2: range for 2nd distribution
    :param: pdf1: 1st distribution pdf
    :param: pdf2: 2nd distribution pdf
    :param: cdf1: 1st distribution cdf
    :param: cdf2: 2nd distribution cdf
    :return: figure of the four subplots
    """
    # Define parameters for the two normal distributions
    mu1 = 0
    sigma1 = 1  # Mean and standard deviation for the first normal distribution

    mu2 = 175
    sigma2 = 3  # Mean and standard deviation for the second normal distribution

    # Create a range of x values for the first normal distribution
    x1 = np.linspace(-4, 4, 1000)

    # Create a range of x values for the second normal distribution
    x2 = np.linspace(160, 190, 1000)

    # Calculate the probability density function (pdf) for each normal distribution
    pdf1 = stats.norm.pdf(x1, mu1, sigma1)
    pdf2 = stats.norm.pdf(x2, mu2, sigma2)

    # Calculate the cumulative distribution function (cdf) for each normal distributions
    cdf1 = stats.norm.cdf(x1, mu1, sigma1)
    cdf2 = stats.norm.cdf(x2, mu2, sigma2)

    # Create a figure and two subplots
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

#endregion

#plottingregion
#separate the quadrants into 4 for plotting
    #Plot the PDF of the first normal distribution on the first subplot
    #I got this format from chatgpt
    ax[0, 0].plot(x1, pdf1, label='N(0, 1)')
    ax[0, 0].set_title('PDF of N(0, 1)')
    ax[0, 0].set_xlabel('x')
    ax[0, 0].set_ylabel('Probability Density')
    ax[0, 0].legend()

    #Plot the CDF of the first normal distribution on the second subplot
    ax[0, 1].plot(x1, cdf1, label='N(0, 1)')
    ax[0, 1].set_title('CDF of N(0, 1)')
    ax[0, 1].set_xlabel('x')
    ax[0, 1].set_ylabel('Cumulative Probability')
    ax[0, 1].legend()

    #Plot the PDF of the second normal distribution on the third subplot
    ax[1, 0].plot(x2, pdf2, label='N(175, 3)')
    ax[1, 0].set_title('PDF of N(175, 3)')
    ax[1, 0].set_xlabel('x')
    ax[1, 0].set_ylabel('Probability Density')
    ax[1, 0].legend()

    #Plot the CDF of the second normal distribution on the fourth subplot
    ax[1, 1].plot(x2, cdf2, label='N(175, 3)')
    ax[1, 1].set_title('CDF of N(175, 3)')
    ax[1, 1].set_xlabel('x')
    ax[1, 1].set_ylabel('Cumulative Probability')
    ax[1, 1].legend()

    #Adjust layout and display the plot
    plt.tight_layout()
    plt.show()

#endregion

if __name__ == "__main__":
    main()


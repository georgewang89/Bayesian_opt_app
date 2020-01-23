# import modules

# GPyOpt - Cases are important, for some reason
import GPyOpt
from GPyOpt.methods import BayesianOptimization

# numpy and pandas

import streamlit as st
import pandas as pd
import numpy as np

# plotting tools

# Plotting tools
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy.random import multivariate_normal

# Define the objective function
def obj_func(x):
    out = x ** 4 + 2 * x ** 3 - 12 * x ** 2 - 2 * x + 6
    return out

# Plot the function
x = pd.Series(np.linspace(-5,4,1000))
f_x = pd.Series.apply(x, obj_func)

# create the plot
plt.plot(x, f_x, 'b-')
plt.show()

# plot previous line using streamlit
st.pyplot()

# ========== set up and run bayesian optmization ==========
# run bayesian optimization on charge
# the following 'domain' is a list of dictionaries containing the description of the inputs variables (See GPyOpt.core.space.Design_space class for details).
domain = [{'name': 'var_1', 'type': 'continuous', 'domain': (-5,4)}]

# f = objective fucntion for the Bayesian Optimization; domain = [refer to above]
myBopt_1d = BayesianOptimization(f=obj_func, domain=domain)
myBopt_1d.run_optimization(max_iter=5)
myBopt_1d.plot_acquisition()

# plot the acquisition function using streamlit
st.pyplot()

# ========== get the output of the bayesian optimization ==========

ins = myBopt_1d.get_evaluations()[1].flatten()
outs = myBopt_1d.get_evaluations()[0].flatten()
evals = pd.DataFrame({'x':ins, 'y':outs})

# plot
st.write(evals)

st.markdown("The minumum value obtained by the function was %.4f (x = %.4f)" % (myBopt_1d.fx_opt, myBopt_1d.x_opt))
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error as mse
from sklearn import metrics
from sklearn.metrics import r2_score 
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import KNNImputer
from sklearn.inspection import permutation_importance
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

import plotly.express as px

import geopandas as gpd
import folium
from folium.plugins import HeatMap

import re

from rdkit import Chem 
from rdkit.Chem import AllChem, Draw, Descriptors

from scipy.cluster.hierarchy import dendrogram, linkage

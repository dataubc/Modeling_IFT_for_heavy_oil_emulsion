# Modeling IFT and Volume Expansion for Heavy Oil Recovery by Gas Injection
![alt text](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_r_files/figure-gfm/unnamed-chunk-1-1.png)
 

In this work I am building models using data generated in our earlier paper [Modeling "Underlying Physics of Heavy Oil Recovery by Gas Injection: An Experimental Parametric Analysis When Oil Exists in the Form of Oil Based Emulsion](https://www.sciencedirect.com/science/article/abs/pii/S0263876220304561)

> Mohammedalmojtaba Salama, Lixing Lin, Georgeta Istratescu, Tayfun Babadagli
> University of Alberta

> Amin Bademchi Zadeh, Mark Anderson, Chris Patterson
> Canadian Natural Resources Limited


**Abstract**
---

In this paper, we focus on the interfacial properties, relative volume change, and PVT behavior
of CO 2 and CH 4 in (w/ho) emulsions, which is encountered in heavy oil reservoirs during
secondary recovery methods such as water or steam injection. We generated the water-in-heavy-
oil (w/ho) emulsion using steam at 150 o C for two types of oils (27,000 cP and 4,351 cP).
vol.% range from 10-70.

Machine Learning :
---
After conducting initial data exploration and visualization I explopred different models to predict IFT and volume expansion given the water content, gas type, and time. A linear model was implemented with Ridge model to control for overfitting, but the obtained score was still low. Using GradientBoostingRegressor I was able to get 99% accuracy on the test data after applying a full pipeline for preprocessing 'scaling' numerical data and 'encoding' categorical variables. Validation using GridSearchCV was performed to optimize the learning rate

- [IFT prediction model in python: Notebook](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_python.ipynb)

- [IFT prediction model in python: python script](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/gradient_boosting.py)

- [Volume Expansion model :Notebook](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_r.md)

- [lm model in R for IFT and Volume expansion](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_r.md)


Presentation:
---
My presentation at University of Alberta can be found [here](https://dataubc.github.io/Modeling_IFT_for_heavy_oil_emulsion/)


Data is available upon request:
Email : mmohamme@ualberta.ca

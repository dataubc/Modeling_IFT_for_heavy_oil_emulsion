# Modeling IFT for heavy oil emulsion
In this work I am building models using data generated in our earlier paper *Modeling "Underlying Physics of Heavy Oil Recovery by Gas Injection: An Experimental Parametric Analysis When Oil Exists in the Form of Oil Based Emulsion* paper that is accepted to be published at [Chemical Engineering Research and Design](https://www.journals.elsevier.com/chemical-engineering-research-and-design)

> Mohammed Mohammedalmojtaba, Lixing Lin, Georgeta Istratescu, Tayfun Babadagli
> University of Alberta

> Amin Bademchi Zadeh, Mark Anderson, Chris Patterson
> Canadian Natural Resources Limited


**Abstract**
---

In this paper, we focus on the interfacial properties, relative volume change, and PVT behavior
of CO 2 and CH 4 in (w/ho) emulsions, which is encountered in heavy oil reservoirs during
secondary recovery methods such as water or steam injection. We generated the water-in-heavy-
oil (w/ho) emulsion using steam at 150 o C for two types of oils (27,000 cP and 4,351 cP). Next,
the stability of our emulsion was tested using different criteria such as phase separation, viscosity
of the produced emulsion compared with that of the starting oil, and the size and number of
water droplets in the continuous medium. The influence of water content in the emulsion was
found to be critical and thus subsequent surface tension (SF) and relative volume measurements
as well as PVT analyses were conducted using emulsions of different water contents with a
vol.% range from 10-70.

Machine Learning :
---

After conducting initial data exploration and visualization I created two models to predict the IFT given the water content, gas type, and time. A linear model was implemented with Ridge model to control for overfitting, but the obtained score was still low. Using GradientBoostingRegressor I was able to get 99% accuracy on the test data after applying a full pipeline for preprocessing 'scaling' numerical data and 'encoding' categorical variables. Validation using GridSearchCV was performed to optimize the learning rate

- [IFT prediction model in python: Notebook](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_python.ipynb)

- [IFT prediction model in python: python script](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/gradient_boosting.py)

- [Volume Expansion model :Notebook](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_r.md)

- [lm model in R for IFT and Volume expansion](https://github.com/dataubc/Modeling_IFT_for_heavy_oil_emulsion/blob/master/modeling_ift_r.md)



Data is available upon request:
Email : mmohamme@ualberta.ca

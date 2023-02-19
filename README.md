# Independent Study Module (ISM): Secure ML

We studied different machine learning problems and ways to solve them in the first half of the ISM, and explored different data poisoning attacks that can be done on the ML algorithms. 

ISM Final Report: [*Final Presentation.pdf*](https://github.com/kubershahi/ashoka-secureml/blob/master/Final%20Presentation.pdf) 

## Implementation Details

**Trash Bucket Problem:**
- binary classfication: dog-vs-cat model created using CNN. Dataset used: https://www.kaggle.com/c/dogs-vs-cats/data https://www.kaggle.com/andrewmvd/animal-faces
- multiclass classfication: number recognition model created using simple NN. Dataset used: MNIST
- Notebooks: *dogvscat.ipynb* & *MNIST_Trash_Bucket.ipynb*

**One shot learning with a Siamese Network:**
- Paper: https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf
- Dataset: MNIST & Omniglot, https://github.com/brendenlake/omniglot
- Notebooks: *one_shot_learning_omniglot.ipynb* & *One_Shot_Learning_MNIST.ipynb*

**Subpopulation Data Poisoning Attack (Paper):**
- Paper: https://arxiv.org/abs/2006.14026
- Dataset: Adult Dataset, https://archive.ics.uci.edu/ml/datasets/adult
- Notebooks: subpopulation_attack_paperimplementation.ipynb
- View *Subpopulation Attack Paper Summary.pdf* for the summary of the paper.

**Subpopulation Data Poisinong Attack (real-world datasets):**
- Dataset: Credit Risk (https://www.kaggle.com/laotse/credit-risk-dataset) & Stroke Prediction (https://www.kaggle.com/fedesoriano/stroke-prediction-dataset/code)
- Notebooks: *subpopulation_attack_credit_risk.ipynb* & *Subpopulation_Stroke.ipynb* 

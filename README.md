# GQSAT 

Can Q-learning with Graph Networks learn a Generalizable Branching Heuristic for a SAT solver?

I will first go over the commands used to install all the necessary modules. 

Then I will go over how to train and test using GQSAT, and changes I made to the original code for my experiments. 

Lastly, I will describe what is included in some of the files I added to the repo.


PLEASE RUN EVERYTHING ON UBUNTU!!

## How to add metadata for evaluation
This will add a METADATA file that is necessary for your validation problems in training and your testing problems when testing
* First download your dataset from https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html
* Unzip the dataset and partition the ``*/cnf`` files into training, validation, and/or testing folders
* Run the command below once for your validation folder (if any) and once for your testing folder (if any)
```python3 add_metadata.py --eval-problems-paths <path_to_folder_with_cnf>```

## How to train
This will train GQSAT using your training problems and validate using your validation problems
* First open train.sh in a text editor
* Replace the path in ``--train-problems-paths ./data/uf20-91/train1Problem \`` with the path to your training folder
* Replace the path in ``--eval-problems-paths ./data/uf20-91/validation \`` with the path to your validation folder
```./train.sh```

## How to evaluate 

* add the path to the model to the script first
* choose the evaluation dataset
* ```./evaluate.sh```


## How to build a solver (you need this only if you changed the c++ code)

Run `make && make python-wrap` in the minisat folder.

## How to build swig code (if you changed minisat-python interface, e.g. in GymSolver.i)

Go to minisat/minisat/gym, run `swig -fastdispatch -c++ -python3 GymSolver.i` and then repeat the building procedure from the previous step.

## Individual Contributor License Agreement

Please fill out the following CLA and email to sgodil@nvidia.com:  https://www.apache.org/licenses/icla.pdf

## Cite

```
@inproceedings{kurin2019improving,
  title={Can Q-Learning with Graph Networks Learn a Generalizable Branching Heuristic for a SAT Solver?},
  author={Kurin, Vitaly and Godil, Saad and Whiteson, Shimon and Catanzaro, Bryan},
  booktitle = {Advances in Neural Information Processing Systems 32},
  year={2020}
}
```

## Acknowledgements

We would like to thank [Fei Wang](https://github.com/feiwang3311/minisat) whose initial implementation of the environment we used as a start, and the creators of [Minisat](https://github.com/niklasso/minisat) on which it is based on.
We would also like to thank the creators of [Pytorch Geometric](https://github.com/rusty1s/pytorch_geometric) whose 
MetaLayer and [Graph Nets](https://arxiv.org/abs/1806.01261) implementation we built upon. 

### Experimental Data and Parameter Settings

The experimental instances reported in Section 6.2 were randomly generated. Fixed random seeds were used to ensure the reproducibility of the experiments. The data-generation procedures, parameter settings, and result files are described below.

#### 6.2.1 Single-Machine Instances

The job sizes were randomly generated as integers in the open interval \((0,10)\), that is, from the set {1,2,...,10\}. The random seed was set to 42, and the chamber length was set to \(S=10\).

Each instance was solved using the following five methods:

- MINLP
- MILP
- MINLP-L
- MILP-L
- DP

The reported performance measures are presented in the following order:

\[ Cmax\ CPU time\ gap1 \]

where Cmax denotes the makespan, CPU time denotes the computational time, and gap1 denotes the optimality gap reported by the solver at termination.

#### 6.2.2 Medium-Scale Identical-Machine Instances

**Table 8:** Job sizes were randomly generated in the open interval (0,10) and rounded to three decimal places. The random seed was set to 42, the chamber length was set to \(S=10\), and the number of machines was set to \(m=2\). Each instance was solved using MINLP-L and MILP-L, and the corresponding makespan, CPU time, and terminal solver gap were recorded.

**Tables 9 and 10:** To compare the performance of the three approximation algorithms and the three heuristic batching rules on medium-scale instances, six groups of experiments were conducted for each method. Each group contained 50 independently generated random instances, using random seeds ranging from 101 to 150. The tables report the average results over the 50 instances in each group.

The comparison focuses on the makespan Cmax and gap2, which measures the relative deviation of the obtained makespan from the theoretical lower bound. Detailed results are provided in:

```
6.2.(2) The results of the medium-scale instances for identical machines of three algorithms and heuristic batching algorithms.xlsx
```

#### 6.2.3 Large-Scale Identical-Machine Instances

To evaluate the performance of the three approximation algorithms on large-scale instances, 15 groups of experiments were conducted for each algorithm, corresponding to different combinations of job and machine numbers. The number of machines \(m\) was set to 10, 15, and 20.

Each group contained 50 independently generated random instances, using random seeds ranging from 101 to 150. The reported values are the averages over the 50 instances in each group and are presented in the following order:

[ Cmax\ CPU time\ Splitting\ gap2 \]

where Splitting denotes the number of batch-splitting operations and gap2 denotes the relative deviation of the obtained makespan from the theoretical lower bound.

Detailed results are provided in:

```
6.2.(3) Performance analysis of three algorithms for the large-scale instances.xlsx
```



### 7.1 data-set

```
TYPE_DATA = [
    (6.2, 700, "small"),
    (8.4, 700, "small"),
    (10.6, 700, "small"),
    (12.8, 700, "small"),
    (15.1, 700, "small"),
    (17.3, 700, "small"),
    (20.0, 700, "small"),
    (23.4, 700, "small"),
    (26.7, 700, "small"),
    (29.2, 700, "small"),
    (5.0, 21000, "large"),
    (7.0, 21000, "large"),
    (9.0, 21000, "large"),
    (11.0, 21000, "large"),
    (13.0, 21000, "large"),
]
```
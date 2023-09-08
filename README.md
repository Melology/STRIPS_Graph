# STRIPS_Graph


[TOC]

## For Coding
* Python 3.9.6
* Packages:
    * matplotlib 3.7.2
    * networkx 3.1


## Definition of Graph
A **directed graph** of **digraph** is a graph in which edges have orientations with a pair $G=(V,E)$ comprising:  
* $V$, a set of vertices(also called nodes or points)  
* *E*, a set of edges(alse called directed edges,directed links and so on)  

$$
E\subseteq\{(x,y)|(x,y)\in V^{2}\,\,\text{and}\,\,x\ne y\}
$$

In this project, the nodes represent the conditions(also called status) and the edges represent the actions.   

To make it more clear, I will give an example to explain this.  

```yaml=
STRIPS:
    Initial Condition:
        hunger: true
        have an apple: true
        have a watermelon: true
    Goal: 
        hunger: false
    
    Action:
    - eat an apple:
        precondition:
        
        hunger: true
        have an apple: true
        postcondition:
        
        hunger: false
        have an apple: false
        
    - eat a watermelon:
        precondition:
        
        hunger: true
        have a watermelon: true
        
        postcondition:
        
        hunger: false
        have a watermelon: false
        
```

In the above example, The NPCs have two options. One is eating an apple and another is eating a watermelon. Therefore, the graph from the example data should looks like this:  

![graph from the example](https://hackmd.io/_uploads/SybKkYO0n.png)  
- Node_{1}: represent the initial condition:
```yaml=
hunger: true
have an apple: true
have a watermelon: true
```
- Node_{2}:represent the condition after the NPCs eating an apple:
```yaml=
hunger: false
have an apple: false
have a watermelon: true
```
- Node_{3}:represent the condition after the NPCs eating a watermelon:
```yaml=
hunger: false
have an apple: true
have a watermelon: false
```

Of course, we will know that:
- Edge_{(1,2)}:represent the action so-called eat an apple.
- Edge_{(1,3)}:represent the action so-called eat a watermelon.


## How to convert from the STRIPS to Graph

from 








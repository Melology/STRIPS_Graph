# STRIPS_Graph


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

```mermaid
graph TD;
    1-->2;
    1-->3;
```
- $Node_{1}$ : represent the initial condition:
```yaml=
hunger: true
have an apple: true
have a watermelon: true
```
- $Node_{2}$ : represent the condition after the NPCs eating an apple:
```yaml=
hunger: false
have an apple: false
have a watermelon: true
```
- $Node_{3}$ : represent the condition after the NPCs eating a watermelon:
```yaml=
hunger: false
have an apple: true
have a watermelon: false
```

Of course, we will know that:
- $Edge_{(1,2)}$ : represent the action so-called eat an apple.
- $Edge_{(1,3)}$ : represent the action so-called eat a watermelon.

## How to convert from the STRIPS to Graph


### Initialzation

In order to make the process of converting be logicl and without losing any information, Firstly, the Whole graph would contain only single node named $node_{1}$.  

**Waring: :warning:   
perhaps it should be called $node_{0}$, but because in my coding, i name it as $node_{1}$, it a little bit hard to fix it, Please forgive with this small mistake.** :smile: 

Now, in our graph, it should look like this:
```mermaid
graph TD
    1
```
### More nodes could be generated

Considering every time the NPCs do one action, the conditions of this guy could be changed by action at the same time. So Let's consider the action before adding nodes to our graph.

We observe that the there are some actions whose precondition is satisfied by the initial node($node_{1}$).i.e. ***buff_friend_attack*** & ***buff_friend_defense*** & ***buff_friend_speed***  

Naturally, our graph is updating like this:

```mermaid
graph TD
1-->2;
1-->3;
1-->4;
```
- $Node_{2}$ : represent the condition after the NPCs buff_friend_attack
- $Node_{3}$ : represent the condition after the NPCs buff_friend_defense
- $Node_{4}$ : represent the condition after the NPCs buff_friend_speed
- $Edge_{(1,2)}$ : represent the action so-called buff_friend_attack
- $Edge_{(1,3)}$ : represent the action so-called buff_friend_defense
- $Edge_{(1,4)}$ : represent the action so-called buff_friend_speed

### Traverse to complete the graph

Every time we add some new nodes to our graph, we always check if there are some actions that could be done by NPCs according to the new nodes.

Finally, we could generate the whole graph! :sunglasses: 

## For centrality

After we generated the graph representing the STRIPS. We finally could compute the centrality of each action.

Firstly, we just use a tool named [edge_betweenness_centrality](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html).

By this algorithm, we are able to compute each edge's centrality.

Considering this graph, most of actions are repeating again and again. If we want to comput each action's centrality respectively. We need another way to deal with it.

This is a easy way(Not sure it is the best way) to compute acions'centrality.

In the graph, we give the same lable to edges if they are representing the same actions.

$$
C=\sum e_{c}
$$

- $C$ : is the centrality of one action.
- $e_{c}$ : is the centrality of edges with the same labels.

The result is here:

```
Label 'buff_friend_defense': Total Betweenness Edge Centrality = 0.0009522945764556503
Label 'buff_friend_speed': Total Betweenness Edge Centrality = 0.0009522945764556503
Label 'buff_friend_attack': Total Betweenness Edge Centrality = 0.0009522945764556503
Label 'buff_my_attack': Total Betweenness Edge Centrality = 0.0009069472156720479
Label 'buff_my_defense': Total Betweenness Edge Centrality = 0.0009522945764556503
Label 'buff_my_speed': Total Betweenness Edge Centrality = 0.0009522945764556503
Label 'move_to_enemy': Total Betweenness Edge Centrality = 0.010157808815526937
Label 'fireball_enemy': Total Betweenness Edge Centrality = 0.011563576999818604
Label 'heal_friend': Total Betweenness Edge Centrality = 0.010339198258661347
Label 'debuff_enemy_attack': Total Betweenness Edge Centrality = 0.004625430799927444
Label 'debuff_enemy_defense': Total Betweenness Edge Centrality = 0.004625430799927444
Label 'debuff_enemy_speed': Total Betweenness Edge Centrality = 0.004625430799927444
Label 'melee_enemy': Total Betweenness Edge Centrality = 0.0013150734627244696
Label 'move_to_friend': Total Betweenness Edge Centrality = 0.014692544893887171
```

The higher centrality of actions means the more frequent they are.  
In this caes, we can know that the action **'move_to_friend'** might be the most freuqnet one.















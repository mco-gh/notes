Theories of Error Back-Propagation in the Brain

## Highlights

The error back-propagation algorithm can be approximated in networks of neurons, in which plasticity only depends on the activity of presynaptic and postsynaptic neurons.

These biologically plausible deep learning models include both feedforward and feedback connections, allowing the errors made by the network to propagate through the layers.

The learning rules in different biologically plausible models can be implemented with different types of spike-time-dependent plasticity.

The dynamics and plasticity of the models can be described within a common framework of energy minimisation.

This review article summarises recently proposed theories on how neural circuits in the brain could approximate the error back-propagation algorithm used by artificial neural networks. Computational models implementing these theories achieve learning as efficient as artificial neural networks, but they use simple synaptic plasticity rules based on activity of presynaptic and postsynaptic neurons. The models have similarities, such as including both feedforward and feedback connections, allowing information about error to propagate throughout the network. Furthermore, they incorporate experimental evidence on neural connectivity, responses, and plasticity. These models provide insights on how brain networks might be organised such that modification of synaptic weights on multiple levels of cortical hierarchy leads to improved performance on tasks.

## Keywords

- [deep learning](https://www.cell.com/action/doSearch?searchType=quick&occurrences=all&ltrlSrch=true&searchScope=fullSite&searchText=deep%20learning&code=cell-site)•
- [neural networks](https://www.cell.com/action/doSearch?searchType=quick&occurrences=all&ltrlSrch=true&searchScope=fullSite&searchText=neural%20networks&code=cell-site)•
- [predictive coding](https://www.cell.com/action/doSearch?searchType=quick&occurrences=all&ltrlSrch=true&searchScope=fullSite&searchText=predictive%20coding&code=cell-site)•
- [synaptic plasticity](https://www.cell.com/action/doSearch?searchType=quick&occurrences=all&ltrlSrch=true&searchScope=fullSite&searchText=synaptic%20plasticity&code=cell-site)

## Deep Learning and Neuroscience

In the past few years, computer programs using **deep learning** (see [Glossary](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#glo0005)) have achieved impressive results in complex cognitive tasks that were previously only in the reach of humans. These tasks include processing of natural images and language [

[1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], or playing arcade and board games [

[2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[3](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Since these recent deep learning applications use extended versions of classic **artificial neural networks** [

[4](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], their success has inspired studies comparing information processing in artificial neural networks and the brain. It has been demonstrated that when artificial neural networks learn to perform tasks such as image classification or navigation, the neurons in their layers develop representations similar to those seen in brain areas involved in these tasks, such as receptive fields across the visual hierarchy or grid cells in the entorhinal cortex [

[5](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[6](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[7](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. This suggests that the brain may use analogous algorithms. Furthermore, thanks to current computational advances, artificial neural networks can now provide useful insights on how complex cognitive functions are achieved in the brain [

[8](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

A key question that remains open is how the brain could implement the **error back-propagation** algorithm used in artificial neural networks. This algorithm describes how the weights of synaptic connections should be modified during learning, and its attractiveness, in part, comes from prescribing weight changes that reduce errors made by the network, according to a theoretical analysis. Although artificial neural networks were originally inspired by the brain, the modification of their synaptic connections, or weights, during learning appears biologically unrealistic [

[9](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[10](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Nevertheless, recent models have demonstrated that learning as efficient as in artificial neural networks can be achieved in distributed networks of neurons using only simple plasticity rules [

[11](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[12](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. These theoretic studies are important because they overrule the dogma, generally accepted for the past 30 years, that the error back-propagation algorithm is too complicated for the brain to implement [

[9](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[10](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Before discussing this new generation of models in detail, we first provide a brief overview of how the back-propagation algorithm is used to train artificial neural networks and discuss why it was considered biologically implausible.

## Artificial Neural Networks and Error Back-Propagation

To effectively learn from feedback, the synaptic connections often need to be appropriately adjusted in multiple hierarchical areas simultaneously. For example, when a child learns to name letters, the incorrect pronunciation may be a combined result of incorrect synaptic connections in speech, associative, and visual areas. When a multi-layer artificial neural network makes an error, the error back-propagation algorithm appropriately assigns credit to individual synapses throughout all levels of hierarchy and prescribes which synapses need to be modified and by how much.

How is the back-propagation algorithm used to train artificial neural networks? The algorithm is trained on a set of examples, each consisting of an **input pattern** and a **target pattern**. For each such pair, the network first generates its prediction based on the input pattern and then the synaptic weights are modified to minimise the difference between the target and the **predicted pattern**. To determine the appropriate modification, an error term is computed for each neuron throughout the network. This describes how the activity of the neuron should change to reduce the discrepancy between the predicted and target pattern ([Box 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0005)). Each weight is modified by an amount determined by the product between the activity of the neuron it projects from and the error term of the neuron it projects to.

[-Box 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

**Artificial Neural Networks**

A conventional artificial neural network consists of layers of neurons, with each neuron within a layer receiving a weighted input from the neurons in the previous layer ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0015)A). The input layer is first set to be the input pattern and then a prediction is made by propagating the activity through the layers, according to **Equation 1.1**, where ***x***l is a vector denoting neurons in layer *l* and ***W***l−1 is a matrix of synaptic weights from layer *l* − 1 to layer *l*. An activation function *f* is applied to each neuron to allow for nonlinear computations.

During learning, the synaptic connections are modified to minimise a cost function quantifying the discrepancy between the predicted and target patterns (typically defined as in **Equation 1.2**). In particular, the weights are modified in the direction of steepest decrease (or gradient) of the cost function ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0015)D). Such modification is described in **Equation 1.3**, where ***δ***l+1 is a vector of error terms associated with neurons ***x***l+1. The error terms for the last layer *L* are defined in **Equation 1.4** as the difference between the target activity ***t*** and the predicted activity. Thus, the error of an output neuron is positive if its target activity is higher than the predicted activity. For the earlier layers, the errors are computed according to **Equation 1.5** as a sum of the errors of neurons in the layer above weighted by the strengths of their connections (and further scaled by the derivative of the activation function; in **Equation 1.5** · denotes element-wise multiplication). For example, an error of a hidden unit is positive if it sends excitatory projections to output units with high error terms, so increasing the activity of such a hidden neuron would reduce the error on the output. Once the errors are computed, each weight is changed according to **Equation 1.3** in proportion to the product of the error term associated with a postsynaptic neuron and the activity of a presynaptic neuron.

![gr1b1.jpg](../_resources/b3ac93e90047ae3ba6d4121592141b3b.jpg)

Figure IArtificial Neural Networks. (A) Layers of neuron-like nodes are represented by sets of stacked blue circles. Feedforward connections are indicated by green arrows. (B) Prediction. (C) Learning. (D) Schematic of the directions of two consecutive weight modifications (thick arrows) in the space of weights (for simplicity, only two dimensions are shown). Contours show points in weight space with equal cost function values.

- [View Large Image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/345556de-8e46-4b73-adc8-f4aee79911ce/gr1b1.jpg)
- |[Figure Viewer](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)
- |[Download Hi-res image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/afb10f97-fba5-456d-a930-21d8fe7fca00/gr1b1_lrg.jpg)
- |[Download (PPT)](https://www.cell.com/action/downloadFigures?pii=S1364-6613(19)30012-9&id=gr1b1.jpg)

Although the described procedure is used to train artificial neural networks, analogous steps may take place during learning in the brain. For example, in the case of the child naming letters mentioned above, the input pattern corresponds to an image of a letter. After seeing an image, the child makes a guess at the name (predicted pattern) via a neural network between visual and speech areas. On supervision by his or her parent of the correct pronunciation (target pattern), synaptic weights along the processing stream are modified so that it is more likely that the correct sound will be produced when seeing that image again.

## Biologically Questionable Aspects of the Back-Propagation Algorithm

Although the algorithmic process described above appears simple enough, there are a few problems with implementing it in biology. Below, we briefly discuss three key issues.

###  Lack of Local Error Representation

Conventional artificial neural networks are only defined to compute information in a forward direction, with the back-propagating errors computed separately by an external algorithm. Without local error representation, each synaptic weight update depends on the activity and computations of all downstream neurons. Since biological synapses change their connection strength based solely on local signals (e.g., the activity of the neurons they connect), it appears unclear how the synaptic plasticity afforded by the back-propagation algorithm could be achieved in the brain. Historically, this is a major criticism; thus it is a main focus of our review article.

###  Symmetry of Forwards and Backwards Weights

In artificial neural networks, the errors are back-propagated using the same weights as those when propagating information forward during prediction. This weight symmetry suggests that identical connections should exist in both directions between connected neurons. Although bidirectional connections are significantly more common in cortical networks than expected by chance, they are not always present [

[15](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Furthermore, even if bidirectional connections were always present, the backwards and forwards weights would still have to correctly align themselves.

###  Unrealistic Models of Neurons

Artificial neural networks use artificial neurons that send a continuous output (corresponding to a firing rate of biological neurons), whereas real neurons use spikes. Generalising the back-propagation algorithm to neurons using discrete spikes is not trivial, because it is unclear how to compute the derivate term found in the back-propagation algorithm ([Box 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0005)). Away from the back-propagation algorithm, the description of computations inside neurons in artificial neural networks is also simplified as a linear summation of inputs.

## Models of Biological Back-Propagation

Each of the above-mentioned issues has been investigated by multiple studies. The lack of local error representation has been addressed by early theories by proposing that the errors associated with individual neurons are not computed, but instead the synaptic plasticity is driven by a global error signal carried by neuromodulators [

[16](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[17](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[18](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[19](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. However, it has been demonstrated that learning in such models is slow and does not scale with network size [

[20](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. More promisingly, in the past few years, several models have been proposed that do represent errors locally and thus more closely approximate the back-propagation algorithm. These models perform similarly to artificial neural networks on standard benchmark tasks (e.g., handwritten digit classification) [

[12](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[21](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], and we summarise several of them in more detail in the following sections.

The criticism of weight symmetry has been addressed by demonstrating that even if the errors in artificial neural networks are back-propagated by random connections, good performance in classification tasks can still be achieved [

[21](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[23](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[24](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[25](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[26](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[27](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. This being said, there is still some concern regarding this issue [

[28](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. With regard to the biological realism of neurons, it has been shown that the back-propagation algorithm can be generalised to neurons producing spikes [

[29](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] and that problems with calculating derivatives using spikes can be overcome [

[23](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Furthermore, it has been proposed that when more biologically realistic neurons are considered, they themselves may approximate a small artificial neural network in their dendritic structures [

[30](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

There is a diversity of ideas on how the back-propagation algorithm may be approximated in the brain [

[31](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[32](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[33](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[34](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[35](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[36](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]; however, we review the principles behind a set of related models [

[11](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[37](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] that have substantial connections with biological data while closely paralleling the back-propagation algorithm. These models operate with minimal external control, as they can compute the errors associated with individual neurons through the dynamics of the networks. Thus, synaptic weight modifications depend only on the activity of presynaptic and postsynaptic neurons. Furthermore, these models incorporate important features of brain biology, such as **spike time-dependent plasticity**, patterns of neural activity during learning, and properties of **pyramidal neurons** and cortical microcircuits. We emphasise that these models rely on fundamentally similar principles. In particular, the models include both feedforward and feedback connections, thereby allowing information about the errors made by the network to propagate throughout the network without requiring an external program to compute the errors. Furthermore, these dynamics, as well as the synaptic plasticity, can be described within a common framework of energy minimisation. We divide the reviewed models in two classes differing in how the errors are represented, and we summarise them in the following sections.

###  Temporal-Error Models

This class of model encodes errors in the differences in neural activity across time. The first model in this class is the contrastive learning model [

[37](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. It relies on an observation that weight changes proportional to an error (difference between predicted and target pattern) can be decomposed into two separate updates: one update based on activity without the target present and the other update with the target pattern provided to the output neurons [

[38](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] ([Box 2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0010)). Thus, the error back-propagation algorithm can be approximated in a network in which the weights are modified twice: during prediction according to **anti-Hebbian plasticity** and then according to **Hebbian plasticity** once the target is provided and the network converges to an equilibrium (after the target activity has propagated to earlier layers via feedback connections) [

[37](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. The role of the first modification is to ‘unlearn’ the existing association between input and prediction, while the role of the second modification is to learn the new association between input and target.

[-Box 2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

**Temporal-Error Models**

Temporal-error models describe learning in networks with recurrent feedback connections to the hidden nodes ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0020)A). The rate of change of activity of a given node is proportional to the summed inputs from adjacent layers, along with a decay term proportional to the current level of activity ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0020)B). As the network is now recurrent, it is no longer possible to write a simple equation describing how the activity depends on other nodes (such as **Equation 1.1** in [Box 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0005)); instead, the dynamics of neurons is described by the differential **Equation 2.1** [

[72](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], where ![si2.gif](../_resources/49ca70d595734b8dea77eac624a19466.gif) denotes the rate of change over time of ***x***l (all equations in this figure ignore nonlinearities for brevity).

In the contrastive learning model, the weight modifications based on errors are decomposed into two separate changes occurring at different times. To understand learning in this model, it is easiest to consider how the weights connecting to the output layer are modified. Substituting **Equation 1.4** into **Equation 1.3**, we see in **Equation 2.2** that the weight modification required by the back-propagation algorithm can be decomposed into two terms. The first term corresponds to anti-Hebbian plasticity that should take place when the output activity is predicted based on the input propagated through the network. The second term corresponds to Hebbian plasticity that should take place when the output layer is set to the target pattern. O’Reilly [

[37](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] demonstrated that in the presence of backward connections, the information about the target pattern propagates to earlier layers, and an analogous sequence of weight modifications in the hidden layers also approximates a version of the back-propagation algorithm for recurrent networks [

[72](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

In the continuous update model, the output nodes are gradually changed from the predicted pattern (*x*3|¬t) towards the target values (*t*), as shown for a sample neuron in [Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0020)D. Thus, the temporal derivative of output activity (![](../_resources/3133c54fb23876cfa6bf344f0b94576c.gif)) is proportional to (*t* −*x*3|¬t), that is, to the error on the output (defined in **Equation 1.4**). Hence, the weight modification required by back-propagation is simply equal to the product of presynaptic activity and the rate of change of the postsynaptic activity (**Equation 2.3**).

![gr1b2.jpg](../_resources/d44880fbb7e0c046ec975a0439f3b236.jpg)

Figure ITemporal-Error Models. (A) Network architecture. (B) Dynamics. (C) Contrastive learning. (D) Continuous update.

- [View Large Image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/88905bf9-f0f7-46c5-91b8-f5d296b18712/gr1b2.jpg)
- |[Figure Viewer](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)
- |[Download Hi-res image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/32e7bb06-71ca-487f-934b-ab9c5f62b588/gr1b2_lrg.jpg)
- |[Download (PPT)](https://www.cell.com/action/downloadFigures?pii=S1364-6613(19)30012-9&id=gr1b2.jpg)

Although the weight modifications in the contrastive learning model involve locally available information, implementing them biologically would require a global signal informing the network which phase it is in (whether the target pattern influences the network or not) as that determines whether the plasticity should be Hebbian or anti-Hebbian. It is not clear whether such a control signal exists in the brain. This concern can be alleviated if the determination of learning phases is coordinated by information locally available in the **oscillatory rhythms** [

[39](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], such as hippocampal theta oscillations [

[40](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. In these models, the neurons in the output layer are driven by feedforward inputs in one part of the cycle and forced to take the value of the target pattern in the other.

The complications of separate phases have been recently addressed in the continuous update model [

[11](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], where during training the output neuron activities are gradually changed from the predicted pattern towards the target. In this case, the rate of change of the output units is proportional to the error terms ([Box 2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0010)). Consequently, the weight modification required by the back-propagation algorithm could arise from local plasticity based on the rate of change of activity. Although the continuous update model does not involve two different learning rules during prediction and learning, it still requires a control signal indicating whether the target pattern is present or not, because plasticity should not take place during prediction.

###  Explicit-Error Models

In this section, we describe alternative models that do not require control signals but as a trade-off have more complex architectures that explicitly compute and represent errors.

It has been recently noticed [

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[41](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] that the error back-propagation algorithm can be approximated in a widely used model of information processing in hierarchical cortical circuits called predictive coding [

[42](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. In its original formulation, the predictive coding model was developed for **unsupervised learning**, and it has been shown that when the model is presented with natural images, it learns representations similar to those in visual cortex [

[42](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Predictive coding models have also been proposed as a general framework for describing different types of information processing in the brain [

[43](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. It has been recently shown that when a predictive coding network is used for **supervised learning**, it closely approximates the error back-propagation algorithm [

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

An architecture of a predictive coding network contains **error nodes** that are each associated with corresponding **value nodes**. During prediction, when the network is presented with an input pattern, activity is propagated between the value nodes via the error nodes. The network converges to an equilibrium, in which the error nodes decay to zero and all value nodes converge to the same values as the corresponding artificial neural network ([Box 3](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0015)). During learning, both the input and the output layers are set to the training patterns. The error nodes can no longer decrease their activity to zero; instead, they converge to values as if the errors had been back-propagated [

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Once the state of the predictive coding network converges to equilibrium, the weights are modified, according to a Hebbian plasticity rule. These weight changes closely approximate that of the back-propagation algorithm.

[-Box 3](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

**Predictive Coding Model**

Predictive coding networks include error nodes each associated with corresponding value nodes ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0025)A). The error nodes receive inhibition from the previous layer and excitation from the corresponding value nodes and thus compute the difference between them (**Equation 3.1**). The value nodes get feedforward inhibition from corresponding error nodes and feedback from the error nodes in the next layer. In the predictive coding network, the value nodes act as integrators, so they add their input to their current activity level (**Equation 3.2**).

During prediction, when the network is presented only with an input pattern, the information is propagated between the value nodes via the error nodes. As the output layer is unconstrained, the activity of error nodes converges to zero, because the value nodes change their activity until the feedback they send to their corresponding error nodes balances the feedforward inhibition received by error nodes. At this state, the left side of **Equation 3.1** is equal to 0, and by rearranging terms ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0025)C), we observe that the activity of value nodes is equal to the weighted sum of value nodes in the previous layer, exactly as in artificial neural networks [**Equation 1.1** with ![underline.59f82f5f5bbed90fd72132ef98662fe3.png](../_resources/593f619649549f584fa259f4b6c89c39.gif)].

During learning, when the network is presented with both input and target patterns, the activity of error nodes may not decrease to zero. Learning takes place when the network is in equilibrium (![spoiler.eff5de8f72591c5ceeb4fa26a117c6d1.png](../_resources/cc3ddfb563263259ca6297b7df9f2e4f.gif)). At this stage the left side of **Equation 3.2** is equal to 0, and by rearranging terms ([Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0025)D), we observe that the activity of error nodes is equal to a weighted sum of errors from the layer above, bearing the same relationship as in the back-propagation algorithm [**Equation 1.5** with ![si3.gif](../_resources/593f619649549f584fa259f4b6c89c39.gif)]. At convergence, the weights are modified according to **Equation 1.3**, which here corresponds to Hebbian plasticity dependent on the activity of pre- and postsynaptic neurons.

![gr1b3.jpg](../_resources/67b0e63c3b0d5185eb0d962c5274ec8b.jpg)

Figure IPredictive Coding. (A) Network architecture. Blue and red circles denote the value and error nodes, respectively. Arrows and lines ending with circles denote excitatory and inhibitory connections, respectively; green double lines indicate connections between all neurons in one layer and all neurons in the next layer, while single black lines indicate within layer connections between a corresponding error and value node (see key). (B) Dynamics (for a simple case of linear function *f*; for details of how nonlinearities can be introduced, see

[

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]
). (C) Prediction. (D) Learning.

- [View Large Image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/b4eb0d1d-d99d-43d7-bbab-7ed76259ee7d/gr1b3.jpg)
- |[Figure Viewer](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)
- |[Download Hi-res image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/ec7ad5e7-8dbd-4bc7-b747-63e0219751d3/gr1b3_lrg.jpg)
- |[Download (PPT)](https://www.cell.com/action/downloadFigures?pii=S1364-6613(19)30012-9&id=gr1b3.jpg)

An important property of the predictive coding networks is that they work autonomously: irrespective of the target pattern being provided, the same rules for node dynamics and plasticity are used. If the output nodes are unconstrained, the error nodes converge to zero, so the Hebbian weight change is equal to zero. Thus, the networks operate without any need for external control except for providing different inputs and outputs. However, the one-to-one connectivity of error nodes to their corresponding value nodes is inconsistent with diffused patterns of neuronal connectivity in the cortex.

A solution to this inconsistency has been proposed in several models in which the error is represented in dendrites of the corresponding neuron [

[44](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[45](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[46](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. In this review article, we focus on a popular model called the dendritic error model [

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. This model describes networks of pyramidal neurons and assumes that the errors in the activity of pyramidal neurons are computed in their **apical dendrites**. In this model, the apical dendrites compare the feedback from the higher levels with a locally generated prediction of higher-level activity computed via interneurons.

An easy way to understand why such an architecture approximates the back-propagation algorithm is to notice that it is closely related to predictive coding networks, which approximate artificial neural networks. Simply rearranging the equations describing the dynamics of predictive coding model gives a description of a network with the same architecture as the dendritic error model, in which dendrites encode the error terms ([Box 4](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0020)).

[-Box 4](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

**Dendritic Error Model**
The architecture of the dendritic error model [

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] is shown in [Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0030)A. In this network, the activity is propagated through the layers via connections between pyramidal neurons. The errors in the activity of pyramidal neurons are computed in their apical dendrites.

The relationship between predictive coding and dendritic error models can be established by observing that substituting the definition of error nodes from the predictive coding model, **Equation 3.1**, into **Equation 3.2**, produces **Equation 4.1**, which describes the dynamics of pyramidal neurons in [Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0030)A. The right side of **Equation 4.1** consists of four terms corresponding to various connections in the figure. The first is simply a decay, the second is a feedforward input from the previous layer, the third is a feedback from the layer above, and the fourth term is a within layer recurrent input. This last term has a negative sign, while pyramidal neurons are excitatory, so it needs to be provided by interneurons. If we assume that the interneurons have activity ***i***l =***W***l***x***l, they need to be connected with the pyramidal neurons via weights ***W***l.

The key property of this network is that when it converges to the equilibrium, the neurons with activity ***x***l encode their corresponding error terms ***δ***l in their apical dendrites. To see why this is the case, note that the first two terms on the right of **Equation 4.1** are equal to −***δ***l according to the definition of **Equation 3.1**. At equilibrium ![link.5ef9a39f22ce49f926e304567b9d611b.png](../_resources/cc3ddfb563263259ca6297b7df9f2e4f.gif), the two last terms in **Equation 4.1** must be equal to ***δ***l (so that the right-hand side of **Equation 4.1** adds up to 0), and it is these two terms that define the input to the apical dendrite. As the errors ***δ***l are encoded in apical dendrites, the weight modification required by the back-propagation algorithm (**Equation 1.3**) only involves quantities encoded in pre- and postsynaptic neurons.

Appropriately updating weights between pyramidal and interneurons is more challenging. This is because the interneurons must learn to produce activity encoding the same information as the higher-level pyramidal neurons. To allow training of the interneurons, the dendritic error model includes special one-to-one connections to the interneurons from corresponding higher-level pyramidal neurons (black dashed arrows in [Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0030)A).

![gr1b4.jpg](../_resources/4849d194bde77f3248a2126905a51d11.jpg)

Figure IDendritic Error Model. (A) Network architecture. Blue circles indicate pyramidal neurons, red rectangles indicate their apical dendrites, and purple circles denote interneurons. (B) Dynamics.

- [View Large Image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/eb05ba7b-9e7f-4235-97a8-56738f664044/gr1b4.jpg)
- |[Figure Viewer](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)
- |[Download Hi-res image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/621441eb-f291-434d-98b9-75ff43cb5676/gr1b4_lrg.jpg)
- |[Download (PPT)](https://www.cell.com/action/downloadFigures?pii=S1364-6613(19)30012-9&id=gr1b4.jpg)

As the error term is now encoded within a neuron’s compartment, the update of weights between pyramidal neurons required by the back-propagation algorithm corresponds to local synaptic plasticity. Error information can be transmitted from the apical dendrite to the rest of the neuron through internal signals. For example, a recent computational model proposed that errors encoded in apical dendrites can determine the plasticity in the whole neuron [

[12](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. The model is based on observations that activating apical dendrites induces **plateau potentials** via calcium influx, leading to a burst of spikes by the neuron [

[47](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Such bursts of spikes may subsequently trigger synaptic plasticity [

[48](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[49](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

Although the dendritic error network makes significant steps to increase the biological realism of predictive coding models, it also introduces extra one-to-one connections (dotted arrow in [Box 4](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0020)) that enforce the interneurons to take on similar values to the neurons in next layer and thus help them to predict the feedback from the next level. Furthermore, the exact dynamics in the dendritic error model are much more complex than that given in [Box 4](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0020), as it describes details of changes in membrane potential in multiple compartments. Nevertheless, it is important to highlight that the architecture of dendritic error networks can approximate the back-propagation algorithm, and it offers an alternative hypothesis on how the computations assumed by the predictive coding model could be implemented in cortical circuits.

## Comparing the Models

Given the biological plausibility of the above-mentioned models, in this and the coming sections, we compare the models in terms of their computational properties (as more efficient networks may be favoured by evolution) and their relationships to experimental data (summarised in [Table 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tbl0005)).

Table 1Comparison of Models

|     | Temporal-error model | Explicit-error model |
| --- | --- | --- |
| Contrastive learning | Continuous update | Predictive coding | Dendritic error |
| Properties<br>[a](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#) | Control signal | Required | Required | Not required | Not required |
| Connectivity | Unconstrained | Unconstrained | Constrained | Constrained |
| Propagation time | L-1 | L-1 | 2L-1 | L-1 |
| Pre-training | Not required | Not required | Not required | Required |
| Error encoded in | Difference in activity between separate phases | Rate of change of activity | Activity of specialised neurons | Apical dendrites of pyramidal neurons |
| Data accounted for | Neural responses and behaviour in a variety of tasks | Typical spike-time-dependent plasticity | Increased neural activity to unpredicted stimuli | Properties of pyramidal neurons |
| MNIST performance<br>[b](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#) | ∼2–3 | –   | ∼1.7 | ∼1.96 |

a Green indicates properties desired for biological plausibility, while red indicates less desired properties.

b These are error percentages reported on a testing set in a benchmark task of handwritten digit classification (lower is better), for predictive coding [

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], dendritic error [

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], and contrastive learning models [

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] (in this simulation, the output neurons were not set to the target pattern, but slightly moved or ‘nudged’ towards it). We are not aware of reported simulations of the continuous update model on this benchmark problem. MNIST, Modified National Institute of Standards and Technology database.

- [Open table in a new tab](https://www.cell.com/action/showFullTableHTML?isHtml=true&tableId=tbl0005&pii=S1364-6613%2819%2930012-9)

###  Computational Properties

For correct weight modification, the temporal-error models require a mechanism informing whether the target pattern constrains the output neurons, while the explicit-error models do not. However, as a trade-off, the temporal-error models have simpler architectures, while the explicit-error models need to have intricate architectures with certain constraints on connectivity, and both predictive coding and the dendritic error model include one-to-one connections in their network structure. As mentioned, there is no evidence for such one-to-one connectivity in the neocortex.

The models differ in the time required for signals to propagate through the layers. To make a prediction in networks with *L* layers, predictive coding networks need to propagate information through 2*L* − 1 synapses, whereas the other models only need to propagate through *L* − 1 synapses. This is because in a predictive coding network, to propagate from one layer to the next, the information must travel via an error neuron, whereas in the other models the information is propagated directly to the neurons in the layer above. There is a clear evolutionary benefit to propagating information via fewer synapses, as it would result in faster responses and a smaller number of noise sources.

In the dendritic error model, for errors to be computed in the dendrites, the inhibitory interneurons first need to learn to predict the feedback from the higher level. Thus, before the network can learn feedforward connections, ideally the inhibitory neurons need to first be pre-trained. Although it has been shown that the feedforward and inhibitory weights can be learned in parallel, learning in the dendritic error model may well be slower as the reported number of iterations required to learn a benchmark task was higher for the dendritic error model [

[13](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] than for contrastive learning [

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] and predictive coding [

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] models. Such statements, however, should be taken with reservations as not only were simulations not necessarily comparable but also computations in standard von-Neumann computers may not be representative of computations in biological hardware.

###  Relationship to Experimental Data

The models differ in their predictions on whether errors should be explicitly represented in neural activity. In particular, the predictive coding model includes dedicated neurons encoding errors, and the dendritic error model suggests that errors computed in dendrites may trigger bursts of firing of pyramidal neurons, while in temporal models there is no direct association between error and the overall activity level at a given time. In line with the explicit-error models, increased neural activity has been observed when sensory input does not match the expectations encoded by higher-level areas. For example, responses of neurons in the primary visual cortex were increased at brief intervals in which visual input did not match expectation based on animal movements [

[50](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. An increase in neural activity when expectations about stimuli were violated has also been found with fMRI [

[51](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Further details are discussed in several excellent reviews [

[52](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[53](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[54](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[55](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. The two explicit models differ in predictions on whether errors and values are represented by separate neuronal populations or within the same neurons. Experimental data relevant to this question have been reviewed in an excellent chapter by Kok and de Lange [

[56](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Although they conclude that there is ‘no direct unequivocal evidence for the existence of separate populations’, they discuss several studies suggesting preferential encoding of errors and values by different neurons. For example, in a part of visual cortex (inferior temporal cortex), the inhibitory neurons tended to have higher responses to novel stimuli, while excitatory neurons typically produced highest response for their preferred familiar stimuli [

[57](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Kok and de Lange point that these responses may potentially reflect error and value nodes, respectively [

[56](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

Each model accounts for specific aspects of experimental data. The models based on contrastive learning rules have been shown to reproduce neural activity and behaviour in a wide range of tasks [

[58](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. The learning rule in the continuous update model (in which the synaptic modification depends on the rate of change of the postsynaptic neuron; [Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)A), can be implemented with classic spike-time-dependent plasticity ([Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)B) [

[11](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. In this form of plasticity, the direction of modification (increase or decrease) depends on whether the spike of a presynaptic neuron precedes or follows the postsynaptic spike [

[59](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. [Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)C shows the effect of such plasticity in a case when the postsynaptic neuron increases its firing. If the postsynaptic spike follows the presynaptic spike, the synaptic weight is increased (pink area), while if the postsynaptic spike precedes the presynaptic spike, the weight is decreased (yellow area). If the postsynaptic neuron increases its firing rate (as in the example), there will be more postsynaptic spikes in pink than in yellow area on average, so the overall weight change will be positive. Analogously, the weight is weakened if the postsynaptic activity decreases ([Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)D). In summary, with asymmetric spike-time-dependent plasticity, the direction of weight change depends on the gradient of a postsynaptic neuron activity around a presynaptic spike, as in the continuous update model.

![gr1.jpg](../_resources/09c69595a7a18b11cf9f29c6ac758abe.jpg)

Figure 1Relationship between Learning Rules and Spike-Time-Dependent Plasticity. (A) Plasticity dependent on the rate of change of postsynaptic activity, illustrated by the left column of panels. (B) Asymmetric spike-time-dependent plasticity often observed in cortical neurons

[

[59](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]

. The curve schematically shows the change in synaptic weights as a function of the difference between the timings of postsynaptic and presynaptic spikes. Red and orange parts of the curve correspond to increases and decreases in synaptic weights, respectively. (C) Strengthening of a synaptic weight due to increasing postsynaptic activity. Hypothetical spike trains of two neurons are shown. The top sequence corresponds to an output neuron, which increases its activity over time towards the target (see [Figure I](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0020)D in [Box 2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tb0010)). The bottom sequence corresponds to a neuron in the hidden layer; for simplicity, only a single spike is shown. The pink and yellow areas correspond to spike timings in which the weights are increased and decreased, respectively. In these areas the differences in spike timing result in weight changes indicated by red and orange parts of the curve in the panel B. (D) Weakening of weight due to decrease in postsynaptic activity. (E) Plasticity dependent on postsynaptic activity, illustrated by the right column of panels. In the equation, *x*0 denotes the baseline firing rate. (F) Symmetric spike-time-dependent plasticity, where weight change depends on spike proximity. (G) Increase in synaptic weight due to high activity of the postsynaptic neuron. (H) Decrease in synaptic weight when the postsynaptic neurons is less active.

- [View Large Image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/8c2155e2-9c45-4870-b38a-62d3e96faf2a/gr1.jpg)
- |[Figure Viewer](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)
- |[Download Hi-res image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/f1b74ce5-9269-426d-b30b-e7a5c889cdb3/gr1_lrg.jpg)
- |[Download (PPT)](https://www.cell.com/action/downloadFigures?pii=S1364-6613(19)30012-9&id=gr1.jpg)

The relationship of spike-time-dependent plasticity to other models requires further clarifying work. Nevertheless, Vogels and colleagues [

[60](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] demonstrated that a learning rule in which the direction of modification depends on activity of neurons in equilibrium ([Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)E), as in the predictive coding model, can arise from an alternate form of spike-time-dependent plasticity. They considered a form of plasticity where the weight is increased by nearly coincident pre- and postsynaptic spikes, irrespectively of their order, and additionally the weight is slightly decreased by each presynaptic spike. The overall direction of weight modification in this rule is shown in [Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)F. Such a form of plasticity may exist in a several types of synapse in the brain [

[61](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. [Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)G illustrates that with such plasticity, the weights are increased if the intervals between pre- and postsynaptic spikes are short, which is likely to occur when the two neurons have high activity. When the postsynaptic neuron is less active ([Figure 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0005)H), the short intervals (pink area) are less common, while longer intervals are more common (yellow area), so overall the weight change is negative. In summary, with symmetric spike-time-dependent plasticity the direction of weight change depends on whether the postsynaptic neuron activity is above or below a certain level (which may correspond to a baseline level typically denoted with zero in computational models), as in the predictive coding model.

The dendritic error model describes the computations in apical dendrites of pyramidal neurons and features of cortical micro-circuitry such as connectivity of a group of interneurons called the **Martinotti cells**, which receive input from pyramidal neurons in the same cortical area [

[62](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] and project to their apical dendrites [

[63](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Furthermore, there is some evidence that inhibitory interneurons also receive feedback from higher areas in the cortical hierarchy [

[64](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

## Integrating Models

The above-mentioned comparison shows that each model has its own computational advantages, accounts for different data, and describes plasticity at different types of synapses. It is important to note that the cortical circuitry is much more complicated than any of the proposed models’ architectures. Therefore, the models presented above need not be viewed as competitors but may be considered as descriptions of learning in different motifs of more complex brain networks.

Different classes of models may be more suited for different tasks faced by brain networks. One task engaging the primary sensory areas is predicting the next value of sensory input from the previous ones. A recent modelling study suggests that primary visual and auditory cortices may use an algorithm similar to back-propagation while learning to predict sensory input [

[65](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. This study demonstrated that the temporal properties of receptive field in these areas are similar to those in artificial neural networks trained to predict the next video or audio frames on the basis of past history in clips of natural scenes [

[65](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. In such sensory prediction tasks, the target (i.e., the next ‘frame’ of sensory input) always arrives, so the temporal-error models may be particularly suited for this task, as there is no need for the control signal indicating target presence.

The explicit-error models are suitable for tasks where the timing of target pattern presentation is more uncertain. Although the predictive coding and dendritic error networks are closely related, they also exhibit a trade-off: the predictive coding networks are slow to propagate information once trained, while the dendritic error networks are slower to train. It is conceivable that cortical networks include elements of predictive coding networks in addition to dendritic error motifs, as the cortical networks include many other interneuron types in addition to the Martinotti cells and have a much richer organisation than either model. Such a combined network could initially rely on predictive coding motifs to support fast learning and, with time, the dendritic error models could take over, allowing faster information processing. Thus, by combining different motifs, brain networks may ‘beat the trade-offs’ and inherit advantages of each model.

Furthermore, predictive coding models may describe information processing in subcortical parts of brain networks that do not include pyramidal cells and thus may not be able to support computations of the dendritic error model. Indeed, it has been recently suggested how the predictive coding model can be mapped on the anatomy of cerebellum [

[66](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], and the model may also describe aspects of information processing in basal ganglia, where the dopaminergic neurons are well known to encode reward prediction error in their activity [

[67](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

].

As the brain networks may incorporate elements of different models, it is important to understand how individual models relate to each other and how they can be combined. Such insights have been revealed by a recently proposed framework called **equilibrium propagation** [

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[68](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. Here, it was noticed that the dynamics of many models of neuronal networks can be defined in terms of the optimisation of a particular function. This function is known as the network energy. For example, recurrently connected networks of excitatory neurons, such as the temporal-error models, under certain assumptions converge to an equilibrium in which strongly connected neurons tend to have similar levels of activity. Indeed, they minimise a function that summarises the dissimilarity in the activity of strongly connected nodes, called the Hopfield energy [

[69](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. The predictive coding networks are also known to minimise a function during their dynamics, called the free energy [

[70](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]. The free energy has a particularly nice statistical interpretation, as its negative provides a lower bound on the log probability of predicting the target pattern by the network [

[70](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

,

[71](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

] (in case of supervised learning, this probability is conditioned on the input patterns). Since the dendritic error models have approximately similar dynamics as the predictive coding models, all models reviewed above can be considered as energy-based models described within the equilibrium propagation framework ([Figure 2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0010)).

![gr2.jpg](../_resources/f600eeeb78570c55d2c2deb2a5d0c245.jpg)

Figure 2Equilibrium Propagation. The framework considers networks with dynamics described by the minimisation of an energy function. As the activity of these networks converges to an equilibrium, the energy simultaneously decays (blue arrows) to a minimum given the current weights. Once in equilibrium, the weighs are modified (green arrows). It has been shown that network error can be minimised if the synaptic weights are modified in two steps (schematically illustrated by the two displays in the top box;

[

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]

). First, with only the input pattern provided, once the network converges, weights are modified in the direction in which the energy increases. Second, the output layer is additionally constrained to values closer to the target pattern (particular details described in

[

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]

). Constraining the output nodes changes the energy landscape for the units in the middle layers. Once these units converge to a new equilibrium, weights are modified in the direction in which the energy decreases. Scellier and Bengio

[

[22](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]

noted that for temporal-error networks, this procedure gives the contrastive learning rule (**Equation 2.2**). The predictive coding networks, however, converge to an equilibrium in the first step where the free-energy function reaches its global minimum

[

[14](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

]

; thus, there is no weight modification required by the equilibrium propagation framework. Therefore, only a single phase (i.e., the second phase) and a single weight update are required in the explicit-error models, and it only involves Hebbian plasticity.

- [View Large Image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/53ea8269-a556-43e6-91db-46c0a03ac6c9/gr2.jpg)
- |[Figure Viewer](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)
- |[Download Hi-res image](https://els-jbs-prod-cdn.literatumonline.com/cms/attachment/91523188-0e32-4a96-a976-0500e2c80087/gr2_lrg.jpg)
- |[Download (PPT)](https://www.cell.com/action/downloadFigures?pii=S1364-6613(19)30012-9&id=gr2.jpg)

The framework also prescribes how synaptic weights should be modified in any network that minimises energy, and the weight modifications in the reviewed models indeed follow this general rule ([Figure 2](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#fig0010)). Importantly, the framework can describe learning in more complex networks, which could include the elements of the different models. For any network for which an energy function can be defined, the framework describes the plasticity rules of individual synapses required for efficient learning.

Nevertheless, the form of energy function minimised by a network may influence its performance. So far, the biologically plausible networks that perform best in a handwritten digit classification task are those that minimise energies analogous to the free energy ([Table 1](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#tbl0005)). The superior performance of networks minimising free energy may stem from the probabilistic interpretation of free energy, which ensures that the networks are trained to maximise the probability of predicting target patterns.

## Concluding Remarks

This review article has not been exhaustive of all current biological models but nevertheless has described main classes of recent models; those that represent errors temporally and those that represent them explicitly, as well as a framework unifying these methods. These theoretic results elucidate the constraints required for efficient learning in hierarchical networks. However, much more work needs to be done both empirically and theoretically, for example, on how the networks scale to larger architectures [

[28](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

], as well as linking theory to neurobiological data (see Outstanding Questions).

It is crucial to map the models implementing efficient deep learning on biological networks in the brain. In particular, mapping the nodes in the model on distinct cell types in the cortex may be a fruitful route to identifying their computational function. The framework of equilibrium propagation (or its future extensions) may prove particularly useful in this endeavour. Based on known patterns of connectivity, models could be defined and their energy function formulated. The framework could then be used to predict properties of synaptic plasticity that could be compared with experimental data, and the results of such comparisons could be iteratively used to improve the models.

[-Outstanding Questions](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)

Are biologically plausible deep learning implementations robust to the lack of symmetry between the feedforward and feedback connections? The four models reviewed use symmetric feedforward and feedback weights. In these models, both sets of weights are modified during learning, and the plasticity rules maintain the symmetry. As mentioned, such symmetry does not exist in brain networks, so it is important to continue investigations into whether biologically plausible networks still perform robustly without weight symmetry.

How can researchers make biologically plausible deep learning implementations scale? Although the above-mentioned models perform well on some tasks, it is unclear whether they scale to larger problems. This is in part due to the multiple iterations required to update node activity via network dynamics. The number of iterations required does not currently scale well for larger networks. Further work optimising this process is required if high depth networks are to be trained.

How can efficient learning of temporal sequences be implemented in biological networks? The models reviewed above focus on a case of static input patterns, but the sensory input received by the brain is typically dynamic, and the brain has to learn to recognise sequences of stimuli (e.g. speech). To describe learning in such tasks, artificial neural networks have been extended to include recurrent connections among hidden units, which provide a memory of the past. It is important to extend the models reviewed above for learning through time.

How can the dynamics of neural circuits be optimised to support efficient learning? This question can be first studied in models of primary sensory areas predicting sensory input from its past values. In such tasks, the dynamics will play an important role, as networks need to generate their predictions at the right time to compare it with incoming sensory data.

## Acknowledgements

This work was supported by Medical Research Council grant MC_UU_12024/5 and the Engineering and Physical Sciences Research Council. We thank Lindsey Drayton, Tim Vogels, Friedemann Zenke, Joao Sacramento, and Benjamin Scellier for thoughtful comments.

## References

1. 1.

    - LeCun Y. •
    - et al.

Deep learning.
*Nature.*  2015; 521: 436-444

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0005)

    - [Scopus (7575)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_1_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84930630277&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_1_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=26017442&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_1_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnature14539&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=521&publication_year=2015&pages=436-444&journal=Nature&author=LeCun+Y.&title=Deep+learning&)

2. 1.

    - Mnih V. •
    - et al.

Human-level control through deep reinforcement learning.
*Nature.*  2015; 518: 529-533

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0010)

    - [Scopus (1880)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_2_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84924051598&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_2_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=25719670&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_2_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnature14236&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=518&publication_year=2015&pages=529-533&journal=Nature&author=Mnih+V.&title=Human-level+control+through+deep+reinforcement+learning&)

3. 1.

    - Silver D. •
    - et al.

Mastering the game of Go with deep neural networks and tree search.
*Nature.*  2016; 529: 484-489

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0015)

    - [Scopus (1866)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_3_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84963949906&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_3_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=26819042&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_3_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnature16961&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=529&publication_year=2016&pages=484-489&journal=Nature&author=Silver+D.&title=Mastering+the+game+of+Go+with+deep+neural+networks+and+tree+search&)

4. 1.

    - Rumelhart D.E. •
    - et al.

Learning representations by back-propagating errors.
*Nature.*  1986; 323: 533-536

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0020)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_4_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2F323533a0&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=323&publication_year=1986&pages=533-536&journal=Nature&author=Rumelhart+D.E.&title=Learning+representations+by+back-propagating+errors&)

5. 1.

    - Banino A. •
    - et al.

Vector-based navigation using grid-like representations in artificial agents.
*Nature.*  2018; 557: 429-433

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0025)

    - [Scopus (2)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_5_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85046892207&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_5_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=29743670&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_5_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fs41586-018-0102-6&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=557&publication_year=2018&pages=429-433&journal=Nature&author=Banino+A.&title=Vector-based+navigation+using+grid-like+representations+in+artificial+agents&)

6. 1.

Whittington, J.C.R. *et al*. (2018) Generalisation of structural knowledge in the hippocampal-entorhinal system. In *31st Conference on Neural Information Processing Systems (NIPS 2018)*, Montreal

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0030)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=6)

7. 1.

    - Yamins D.L. •
    - DiCarlo J.J.

Using goal-driven deep learning models to understand sensory cortex.
*Nat. Neurosci.*  2016; 19: 356-365

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0035)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_7_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=26906502&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_7_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnn.4244&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=19&publication_year=2016&pages=356-365&journal=Nat.+Neurosci.&author=Yamins+D.L.&author=DiCarlo+J.J.&title=Using+goal-driven+deep+learning+models+to+understand+sensory+cortex&)

8. 1.

    - Bowers J.S.

Parallel distributed processing theory in the age of deep networks.
*Trends Cogn. Sci.*  2017; 21: 950-961

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0040)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_8_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85033706929&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_8_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=29100738&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_8_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.tics.2017.09.013&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_8_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.tics.2017.09.013&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_8_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.tics.2017.09.013&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=21&publication_year=2017&pages=950-961&journal=Trends+Cogn.+Sci.&author=Bowers+J.S.&title=Parallel+distributed+processing+theory+in+the+age+of+deep+networks&)

9. 1.

    - Crick F.

The recent excitement about neural networks.
*Nature.*  1989; 337: 129-132

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0045)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_9_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=2911347&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_9_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2F337129a0&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=337&publication_year=1989&pages=129-132&journal=Nature&author=Crick+F.&title=The+recent+excitement+about+neural+networks&)

10. 1.

    - Grossberg S.

Competitive learning: from interactive activation to adaptive resonance.
*Cogn. Sci.*  1987; 11: 23-63

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0050)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_10_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1111%2Fj.1551-6708.1987.tb00862.x&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=11&publication_year=1987&pages=23-63&journal=Cogn.+Sci.&author=Grossberg+S.&title=Competitive+learning%3A+from+interactive+activation+to+adaptive+resonance&)

11. 1.

    - Bengio Y. •
    - et al.

STDP-Compatible approximation of backpropagation in an energy-based model.
*Neural Comput.*  2017; 29: 555-577

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0055)

    - [Scopus (7)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_11_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85013683708&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_11_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28095200&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_11_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2FNECO_a_00934&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=29&publication_year=2017&pages=555-577&journal=Neural+Comput.&author=Bengio+Y.&title=STDP-Compatible+approximation+of+backpropagation+in+an+energy-based+model&)

12. 1.

    - Guerguiev J. •
    - et al.

Towards deep learning with segregated dendrites.
*eLife.*  2017; 6e22901

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0060)

    - [Scopus (18)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_12_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85040925989&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_12_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=29205151&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_12_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.7554%2FeLife.22901&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=6&publication_year=2017&journal=eLife&author=Guerguiev+J.&title=Towards+deep+learning+with+segregated+dendrites&)

13. 1.

Sacramento, J. *et al*. (2018) Dendritic cortical microcircuits approximate the backpropagation algorithm. In *31st Conference on Neural Information Processing Systems (NIPS 2018)*, Montreal

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0065)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=13)

14. 1.

    - Whittington J.C.R. •
    - Bogacz R.

An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity.

*Neural Comput.*  2017; 29: 1229-1262

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0070)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_14_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85017439802&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_14_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28333583&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_14_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2FNECO_a_00949&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=29&publication_year=2017&pages=1229-1262&journal=Neural+Comput.&author=Whittington+J.C.R.&author=Bogacz+R.&title=An+approximation+of+the+error+backpropagation+algorithm+in+a+predictive+coding+network+with+local+Hebbian+synaptic+plasticity&)

15. 1.

    - Song S. •
    - et al.

Highly nonrandom features of synaptic connectivity in local cortical circuits.
*PLoS Biol.*  2005; 3: 507-519

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0075)

    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=3&publication_year=2005&pages=507-519&journal=PLoS+Biol.&author=Song+S.&title=Highly+nonrandom+features+of+synaptic+connectivity+in+local+cortical+circuits&)

16. 1.

    - Mazzoni P. •
    - et al.

A more biologically plausible learning rule for neural networks.
*Proc. Natl. Acad. Sci. U. S. A.*  1991; 88: 4433-4437

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0080)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_16_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=1903542&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_16_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1073%2Fpnas.88.10.4433&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=88&publication_year=1991&pages=4433-4437&journal=Proc.+Natl.+Acad.+Sci.+U.+S.+A.&author=Mazzoni+P.&title=A+more+biologically+plausible+learning+rule+for+neural+networks&)

17. 1.

    - Williams R.J.

Simple statistical gradient-following algorithms for connectionist reinforcement learning.

*Mach. Learn.*  1992; 8: 229-256

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0085)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_17_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1007%2FBF00992696&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=8&publication_year=1992&pages=229-256&journal=Mach.+Learn.&author=Williams+R.J.&title=Simple+statistical+gradient-following+algorithms+for+connectionist+reinforcement+learning&)

18. 1.

    - Unnikrishnan K.P. •
    - Venugopal K.P.

Alopex: a correlation-based learning algorithm for feedforward and recurrent neural networks.

*Neural Comput.*  1994; 6: 469-490

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0090)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_18_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2Fneco.1994.6.3.469&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=6&publication_year=1994&pages=469-490&journal=Neural+Comput.&author=Unnikrishnan+K.P.&author=Venugopal+K.P.&title=Alopex%3A+a+correlation-based+learning+algorithm+for+feedforward+and+recurrent+neural+networks&)

19. 1.

    - Seung H.S.

Learning in spiking neural networks by reinforcement of stochastic synaptic transmission.

*Neuron.*  2003; 40: 1063-1073

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0095)

    - [Scopus (178)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_19_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0347362917&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_19_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=14687542&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_19_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2FS0896-6273%2803%2900761-X&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_19_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2FS0896-6273%2803%2900761-X&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_19_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2FS0896-6273%2803%2900761-X&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=40&publication_year=2003&pages=1063-1073&journal=Neuron&author=Seung+H.S.&title=Learning+in+spiking+neural+networks+by+reinforcement+of+stochastic+synaptic+transmission&)

20. 1.

    - Werfel J. •
    - et al.

Learning curves for stochastic gradient descent in linear feedforward networks.
*Neural Comput.*  2005; 17: 2699-2718

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0100)

    - [Scopus (35)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_20_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-27144462270&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_20_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=16212768&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_20_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2F089976605774320539&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=17&publication_year=2005&pages=2699-2718&journal=Neural+Comput.&author=Werfel+J.&title=Learning+curves+for+stochastic+gradient+descent+in+linear+feedforward+networks&)

21. 1.

    - Lillicrap T.P. •
    - et al.

Random synaptic feedback weights support error backpropagation for deep learning.

*Nat. Commun.*  2016; 713276

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0105)

    - [Scopus (64)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_21_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84994417427&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_21_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=27824044&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_21_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fncomms13276&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=7&publication_year=2016&journal=Nat.+Commun.&author=Lillicrap+T.P.&title=Random+synaptic+feedback+weights+support+error+backpropagation+for+deep+learning&)

22. 1.

    - Scellier B. •
    - Bengio Y.

Equilibrium propagation: bridging the gap between energy-based models and backpropagation.

*Front. Comput. Neurosci.*  2017; 11: 24

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0110)

    - [Scopus (18)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_22_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85019257820&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_22_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28522969&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_22_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.3389%2Ffncom.2017.00024&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=11&publication_year=2017&pages=24&journal=Front.+Comput.+Neurosci.&author=Scellier+B.&author=Bengio+Y.&title=Equilibrium+propagation%3A+bridging+the+gap+between+energy-based+models+and+backpropagation&)

23. 1.

    - Zenke F. •
    - Ganguli S.

SuperSpike: supervised learning in multilayer spiking neural networks.
*Neural Comput.*  2018; 30: 1514-1541

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0115)

    - [Scopus (3)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_23_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85047469212&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_23_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=29652587&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_23_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2Fneco_a_01086&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=30&publication_year=2018&pages=1514-1541&journal=Neural+Comput.&author=Zenke+F.&author=Ganguli+S.&title=SuperSpike%3A+supervised+learning+in+multilayer+spiking+neural+networks&)

24. 1.

Mostafa, H. *et al*. (2017) Deep supervised learning using local errors. arXiv preprint arXiv:1711.06756

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0120)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=24)

25. 1.

Scellier, B. *et al*. (2018) Generalization of equilibrium propagation to vector field dynamics. arXiv 1808.04873

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0125)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=25)

26. 1.

Liao, Q. *et al*. (2016) How important is weight symmetry in backpropagation? In *AAAI Conference on Artificial Intelligence*, pp. 1837–1844, AAAI

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0130)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=26)

27. 1.

    - Baldi P. •
    - Sadowski P.

A theory of local learning, the learning channel, and the optimality of backpropagation.

*Neural Netw.*  2016; 83: 51-74

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0135)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_27_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84983514119&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_27_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=27584574&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_27_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neunet.2016.07.006&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=83&publication_year=2016&pages=51-74&journal=Neural+Netw.&author=Baldi+P.&author=Sadowski+P.&title=A+theory+of+local+learning%2C+the+learning+channel%2C+and+the+optimality+of+backpropagation&)

28. 1.

Bartunov, S. *et al*. (2018) Assessing the scalability of biologically-motivated deep learning algorithms and architectures. In *31st Conference on Neural Information Processing Systems (NIPS 2018)*, Montreal

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0140)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=28)

29. 1.

    - Sporea I. •
    - Grüning A.

Supervised learning in multilayer spiking neural networks.
*Neural Comput.*  2013; 25: 473-509

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0145)

    - [Scopus (50)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_29_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84877839888&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_29_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=23148411&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_29_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2FNECO_a_00396&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=25&publication_year=2013&pages=473-509&journal=Neural+Comput.&author=Sporea+I.&author=Gr%C3%BCning+A.&title=Supervised+learning+in+multilayer+spiking+neural+networks&)

30. 1.

    - Schiess M. •
    - et al.

Somato-dendritic synaptic plasticity and error-backpropagation in active dendrites.

*PLoS Comput. Biol.*  2016; 12e1004638

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0150)

    - [Scopus (14)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_30_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84959534381&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_30_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=26841235&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_30_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1371%2Fjournal.pcbi.1004638&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=12&publication_year=2016&journal=PLoS+Comput.+Biol.&author=Schiess+M.&title=Somato-dendritic+synaptic+plasticity+and+error-backpropagation+in+active+dendrites&)

31. 1.

Balduzzi, D. *et al*. (2015) Kickback cuts backprop’s red-tape: biologically plausible credit assignment in neural networks. In *AAAI Conference on Artificial Intelligence*, pp. 485–491, AAAI

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0155)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=31)

32. 1.

Krotov, D. and Hopfield, J. (2018) Unsupervised learning by competing hidden units. arXiv preprint arXiv:1806.10181

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0160)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=32)

33. 1.

    - Kuśmierz Ł. •
    - et al.

Learning with three factors: modulating Hebbian plasticity with errors.
*Curr. Opin. Neurobiol.*  2017; 46: 170-177

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0165)

    - [Scopus (7)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_33_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85029405329&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_33_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28918313&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_33_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.conb.2017.08.020&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=46&publication_year=2017&pages=170-177&journal=Curr.+Opin.+Neurobiol.&author=Ku%C5%9Bmierz+%C5%81.&title=Learning+with+three+factors%3A+modulating+Hebbian+plasticity+with+errors&)

34. 1.

    - Marblestone A.H. •
    - et al.

Toward an integration of deep learning and neuroscience.
*Front. Comput. Neurosci.*  2016; 10: 94

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0170)

    - [Scopus (43)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_34_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84989345063&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_34_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=27683554&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_34_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.3389%2Ffncom.2016.00094&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=10&publication_year=2016&pages=94&journal=Front.+Comput.+Neurosci.&author=Marblestone+A.H.&title=Toward+an+integration+of+deep+learning+and+neuroscience&)

35. 1.

Bengio, Y. (2014) How auto-encoders could provide credit assignment in deep networks via target propagation. arXiv preprint arXiv:1407.7906

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0175)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=35)

36. 1.

Lee, D.-H. *et al*. (2015) Difference target propagation. In *Joint European Conference on Machine Learning and Knowledge Discovery in Databases*, pp. 498–515, Springer

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0180)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=36)

37. 1.

    - O’Reilly R.C.

Biologically plausible error-driven learning using local activation differences: the generalized recirculation algorithm.

*Neural Comput.*  1996; 8: 895-938

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0185)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_37_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2Fneco.1996.8.5.895&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=8&publication_year=1996&pages=895-938&journal=Neural+Comput.&author=O%E2%80%99Reilly+R.C.&title=Biologically+plausible+error-driven+learning+using+local+activation+differences%3A+the+generalized+recirculation+algorithm&)

38. 1.

    - Ackley D.H. •
    - et al.

A learning algorithm for Boltzmann machines.
*Cogn. Sci.*  1985; 9: 147-169

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0190)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_38_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1207%2Fs15516709cog0901_7&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=9&publication_year=1985&pages=147-169&journal=Cogn.+Sci.&author=Ackley+D.H.&title=A+learning+algorithm+for+Boltzmann+machines&)

39. 1.

    - Baldi P. •
    - Pineda F.

Contrastive learning and neural oscillations.
*Neural Comput.*  1991; 3: 526-545

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0195)

    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_39_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2Fneco.1991.3.4.526&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=3&publication_year=1991&pages=526-545&journal=Neural+Comput.&author=Baldi+P.&author=Pineda+F.&title=Contrastive+learning+and+neural+oscillations&)

40. 1.

    - Ketz N. •
    - et al.

Theta coordinated error-driven learning in the hippocampus.
*PLoS Comput. Biol.*  2013; 9e1003067

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0200)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_40_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=23762019&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_40_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1371%2Fjournal.pcbi.1003067&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=9&publication_year=2013&journal=PLoS+Comput.+Biol.&author=Ketz+N.&title=Theta+coordinated+error-driven+learning+in+the+hippocampus&)

41. 1.

Ororbia, A.G. and Mali, A. (2018) Biologically motivated algorithms for propagating local target representations. arXiv preprint arXiv:1805.11703

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0205)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=41)

42. 1.

    - Rao R.P.N. •
    - Ballard D.H.

Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects.

*Nat. Neurosci.*  1999; 2: 79-87

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0210)

    - [Scopus (1556)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_42_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0033360288&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_42_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=10195184&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_42_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2F4580&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=2&publication_year=1999&pages=79-87&journal=Nat.+Neurosci.&author=Rao+R.P.N.&author=Ballard+D.H.&title=Predictive+coding+in+the+visual+cortex%3A+a+functional+interpretation+of+some+extra-classical+receptive-field+effects&)

43. 1.

    - Friston K.J.

The free-energy principle: a unified brain theory?.
*Nat. Rev. Neurosci.*  2010; 11: 127-138

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0215)

    - [Scopus (1547)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_43_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-75549090229&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_43_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=20068583&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_43_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnrn2787&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=11&publication_year=2010&pages=127-138&journal=Nat.+Rev.+Neurosci.&author=Friston+K.J.&title=The+free-energy+principle%3A+a+unified+brain+theory%3F&)

44. 1.

    - Richards B.A. •
    - Lillicrap T.P.

Dendritic solutions to the credit assignment problem.
*Curr. Opin. Neurobiol.*  2019; 54: 28-36

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0220)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_44_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85052963034&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_44_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=30205266&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_44_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.conb.2018.08.003&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=54&publication_year=2019&pages=28-36&journal=Curr.+Opin.+Neurobiol.&author=Richards+B.A.&author=Lillicrap+T.P.&title=Dendritic+solutions+to+the+credit+assignment+problem&)

45. 1.

    - Körding K.P. •
    - König P.

Supervised and unsupervised learning with two sites of synaptic integration.
*J. Comput. Neurosci.*  2001; 11: 207-215

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0225)

    - [Scopus (19)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_45_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0035713959&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_45_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=11796938&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_45_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1023%2FA%3A1013776130161&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=11&publication_year=2001&pages=207-215&journal=J.+Comput.+Neurosci.&author=K%C3%B6rding+K.P.&author=K%C3%B6nig+P.&title=Supervised+and+unsupervised+learning+with+two+sites+of+synaptic+integration&)

46. 1.

    - Körding K.P. •
    - König P.

Learning with two sites of synaptic integration.
*Network.*  2000; 11: 25-39

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0230)

    - [Scopus (25)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_46_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0001917668&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_46_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=10735527&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_46_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1088%2F0954-898X_11_1_302&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=11&publication_year=2000&pages=25-39&journal=Network&author=K%C3%B6rding+K.P.&author=K%C3%B6nig+P.&title=Learning+with+two+sites+of+synaptic+integration&)

47. 1.

    - Larkum M.E. •
    - et al.

A new cellular mechanism for coupling inputs arriving at different cortical layers.

*Nature.*  1999; 398: 338-341

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0235)

    - [Scopus (588)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_47_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0033602368&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_47_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=10192334&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_47_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2F18686&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=398&publication_year=1999&pages=338-341&journal=Nature&author=Larkum+M.E.&title=A+new+cellular+mechanism+for+coupling+inputs+arriving+at+different+cortical+layers&)

48. 1.

    - Pike F.G. •
    - et al.

Postsynaptic bursting is essential for ‘Hebbian’ induction of associative long-term potentiation at excitatory synapses in rat hippocampus.

*J. Physiol.*  1999; 518: 571-576

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0240)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_48_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0033565675&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_48_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=10381601&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_48_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1111%2Fj.1469-7793.1999.0571p.x&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=518&publication_year=1999&pages=571-576&journal=J.+Physiol.&author=Pike+F.G.&title=Postsynaptic+bursting+is+essential+for+%E2%80%98Hebbian%E2%80%99+induction+of+associative+long-term+potentiation+at+excitatory+synapses+in+rat+hippocampus&)

49. 1.

    - Roelfsema P.R. •
    - Holtmaat A.

Control of synaptic plasticity in deep cortical networks.
*Nat. Rev. Neurosci.*  2018; 19: 166

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0245)

    - [Scopus (9)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_49_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85042207956&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_49_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=29449713&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_49_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnrn.2018.6&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=19&publication_year=2018&pages=166&journal=Nat.+Rev.+Neurosci.&author=Roelfsema+P.R.&author=Holtmaat+A.&title=Control+of+synaptic+plasticity+in+deep+cortical+networks&)

50. 1.

    - Attinger A. •
    - et al.

Visuomotor coupling shapes the functional development of mouse visual cortex.
*Cell.*  2017; 169: 1291-1302

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0250)

    - [Scopus (9)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_50_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85020308094&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_50_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28602353&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_50_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.cell.2017.05.023&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_50_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.cell.2017.05.023&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_50_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.cell.2017.05.023&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=169&publication_year=2017&pages=1291-1302&journal=Cell&author=Attinger+A.&title=Visuomotor+coupling+shapes+the+functional+development+of+mouse+visual+cortex&)

51. 1.

    - Summerfield C. •
    - et al.

Neural repetition suppression reflects fulfilled perceptual expectations.
*Nat. Neurosci.*  2008; 11: 1004

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0255)

    - [Scopus (316)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_51_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-50249162007&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_51_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=19160497&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_51_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnn.2163&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=11&publication_year=2008&pages=1004&journal=Nat.+Neurosci.&author=Summerfield+C.&title=Neural+repetition+suppression+reflects+fulfilled+perceptual+expectations&)

52. 1.

    - Summerfield C. •
    - de Lange F.P.

Expectation in perceptual decision making: neural and computational mechanisms.
*Nat. Rev. Neurosci.*  2014; 15: 745-756

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0260)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_52_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=25315388&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_52_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2Fnrn3838&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=15&publication_year=2014&pages=745-756&journal=Nat.+Rev.+Neurosci.&author=Summerfield+C.&author=de+Lange+F.P.&title=Expectation+in+perceptual+decision+making%3A+neural+and+computational+mechanisms&)

53. 1.

    - Bastos A.M. •
    - et al.

Canonical microcircuits for predictive coding.
*Neuron.*  2012; 76: 695-711

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0265)

    - [Scopus (568)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_53_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84869753419&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_53_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=23177956&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_53_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2012.10.038&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_53_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2012.10.038&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_53_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2012.10.038&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=76&publication_year=2012&pages=695-711&journal=Neuron&author=Bastos+A.M.&title=Canonical+microcircuits+for+predictive+coding&)

54. 1.

    - de Lange F.P. •
    - et al.

How do expectations shape perception?.
*Trends Cogn. Sci.*  2018; 22: 764-779

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0270)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_54_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85049327101&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_54_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=30122170&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_54_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.tics.2018.06.002&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_54_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.tics.2018.06.002&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_54_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.tics.2018.06.002&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=22&publication_year=2018&pages=764-779&journal=Trends+Cogn.+Sci.&author=de+Lange+F.P.&title=How+do+expectations+shape+perception%3F&)

55. 1.

    - Clark A.

Whatever next? Predictive brains, situated agents, and the future of cognitive science.

*Behav. Brain Sci.*  2013; 36: 181-204

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0275)

    - [Scopus (1132)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_55_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84872566721&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_55_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=23663408&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_55_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1017%2FS0140525X12000477&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=36&publication_year=2013&pages=181-204&journal=Behav.+Brain+Sci.&author=Clark+A.&title=Whatever+next%3F+Predictive+brains%2C+situated+agents%2C+and+the+future+of+cognitive+science&)

56. 1.

    - Kok P. •
    - de Lange F.P.

Predictive coding in sensory cortex.

An Introduction to Model-Based Cognitive Neuroscience.   Springer, ; 2015: 221-244

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0280)

    - [Scopus (9)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_56_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84944544716&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_56_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1007%2F978-1-4939-2236-9_11&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&publication_year=2015&pages=221-244&author=Kok+P.&author=de+Lange+F.P.&isbn=An+Introduction+to+Model-Based+Cognitive+Neuroscience&title=Predictive+coding+in+sensory+cortex)

57. 1.

    - Woloszyn L. •
    - Sheinberg D.L.

Effects of long-term visual experience on responses of distinct classes of single units in inferior temporal cortex.

*Neuron.*  2012; 74: 193-205

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0285)

    - [Scopus (61)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_57_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84859640105&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_57_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=22500640&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_57_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2012.01.032&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_57_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2012.01.032&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_57_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2012.01.032&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=74&publication_year=2012&pages=193-205&journal=Neuron&author=Woloszyn+L.&author=Sheinberg+D.L.&title=Effects+of+long-term+visual+experience+on+responses+of+distinct+classes+of+single+units+in+inferior+temporal+cortex&)

58. 1.

    - O’Reilly R.C. •
    - Munakata Y.

Computational Explorations in Cognitive Neuroscience: Understanding the Mind by Simulating the Brain.

 MIT Press, ; 2000

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0290)

    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&publication_year=2000&author=O%E2%80%99Reilly+R.C.&author=Munakata+Y.&title=Computational+Explorations+in+Cognitive+Neuroscience%3A+Understanding+the+Mind+by+Simulating+the+Brain)

59. 1.

    - Bi G.Q. •
    - Poo M.M.

Synaptic modifications in cultured hippocampal neurons: dependence on spike timing, synaptic strength, and postsynaptic cell type.

*J. Neurosci.*  1998; 18: 10464-10472

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0295)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_59_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=9852584&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_59_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1523%2FJNEUROSCI.18-24-10464.1998&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=18&publication_year=1998&pages=10464-10472&journal=J.+Neurosci.&author=Bi+G.Q.&author=Poo+M.M.&title=Synaptic+modifications+in+cultured+hippocampal+neurons%3A+dependence+on+spike+timing%2C+synaptic+strength%2C+and+postsynaptic+cell+type&)

60. 1.

    - Vogels T.P. •
    - et al.

Inhibitory plasticity balances excitation and inhibition in sensory pathways and memory networks.

*Science.*  2011; 334: 1569-1573

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0300)

    - [Scopus (206)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_60_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-83755181763&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_60_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=22075724&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_60_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1126%2Fscience.1211095&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=334&publication_year=2011&pages=1569-1573&journal=Science&author=Vogels+T.P.&title=Inhibitory+plasticity+balances+excitation+and+inhibition+in+sensory+pathways+and+memory+networks&)

61. 1.

    - Abbott L.F. •
    - Nelson S.B.

Synaptic plasticity: taming the beast.
*Nat. Neurosci.*  2000; 3: 1178-1183

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0305)

    - [Scopus (1054)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_61_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0033667165&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_61_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=11127835&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_61_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1038%2F81453&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=3&publication_year=2000&pages=1178-1183&journal=Nat.+Neurosci.&author=Abbott+L.F.&author=Nelson+S.B.&title=Synaptic+plasticity%3A+taming+the+beast&)

62. 1.

    - Silberberg G. •
    - Markram H.

Disynaptic inhibition between neocortical pyramidal cells mediated by martinotti cells.

*Neuron.*  2007; 53: 735-746

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0310)

    - [Scopus (372)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_62_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-33847222518&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_62_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=17329212&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_62_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2007.02.012&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_62_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2007.02.012&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_62_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2007.02.012&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=53&publication_year=2007&pages=735-746&journal=Neuron&author=Silberberg+G.&author=Markram+H.&title=Disynaptic+inhibition+between+neocortical+pyramidal+cells+mediated+by+martinotti+cells&)

63. 1.

    - Kubota Y.

Untangling GABAergic wiring in the cortical microcircuit.
*Curr. Opin. Neurobiol.*  2014; 26: 7-14

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0315)

    - [Scopus (56)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_63_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84887597933&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_63_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=24650498&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_63_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.conb.2013.10.003&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=26&publication_year=2014&pages=7-14&journal=Curr.+Opin.+Neurobiol.&author=Kubota+Y.&title=Untangling+GABAergic+wiring+in+the+cortical+microcircuit&)

64. 1.

    - Leinweber M. •
    - et al.

A sensorimotor circuit in mouse cortex for visual flow predictions.
*Neuron.*  2017; 95 (1420–1432.e5)

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0320)

    - [Scopus (23)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_64_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85030610486&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_64_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28910624&cf=)•
    - [Abstract](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_64_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2017.08.036&cf=abstract&site=cell-site)•
    - [Full Text](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_64_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2017.08.036&cf=fulltext&site=cell-site)•
    - [Full Text PDF](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_64_2&dbid=4&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.neuron.2017.08.036&cf=pdf&site=cell-site)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=95&publication_year=2017&journal=Neuron&author=Leinweber+M.&title=A+sensorimotor+circuit+in+mouse+cortex+for+visual+flow+predictions&)

65. 1.

    - Singer Y. •
    - et al.

Sensory cortex is optimised for prediction of future input.
*eLife.*  2018; 7e31557

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0325)

    - [Scopus (0)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_65_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-85051926034&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_65_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=29911971&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_65_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.7554%2FeLife.31557&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=7&publication_year=2018&journal=eLife&author=Singer+Y.&title=Sensory+cortex+is+optimised+for+prediction+of+future+input&)

66. 1.

    - Friston K. •
    - Herreros I.

Active inference and learning in the cerebellum.
*Neural Comput.*  2016; 28: 1812-1839

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0330)

    - [Scopus (3)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_66_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84983043496&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_66_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=27391681&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_66_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1162%2FNECO_a_00863&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=28&publication_year=2016&pages=1812-1839&journal=Neural+Comput.&author=Friston+K.&author=Herreros+I.&title=Active+inference+and+learning+in+the+cerebellum&)

67. 1.

    - Schultz W. •
    - et al.

A neural substrate of prediction and reward.
*Science.*  1997; 275: 1593-1599

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0335)

    - [Scopus (4450)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_67_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0030896968&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_67_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=9054347&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_67_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1126%2Fscience.275.5306.1593&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=275&publication_year=1997&pages=1593-1599&journal=Science&author=Schultz+W.&title=A+neural+substrate+of+prediction+and+reward&)

68. 1.

Scellier, B. and Bengio, Y. (2017) Equivalence of equilibrium propagation and recurrent backpropagation. arXiv preprint arXiv:1711.08416

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0340)

    - [Google Scholar](http://scholar.google.com/scholar?hl=en&q=68)

69. 1.

    - Hopfield J.J.

Neurons with graded response have collective computational properties like those of 2-state neurons.

*Proc. Natl. Acad. Sci. U. S. A.*  1984; 81: 3088-3092

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0345)

    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_69_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=6587342&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_69_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1073%2Fpnas.81.10.3088&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=81&publication_year=1984&pages=3088-3092&journal=Proc.+Natl.+Acad.+Sci.+U.+S.+A.&author=Hopfield+J.J.&title=Neurons+with+graded+response+have+collective+computational+properties+like+those+of+2-state+neurons&)

70. 1.

    - Friston K.J.

A theory of cortical responses.
*Philos. Trans. R. Soc. B Biol. Sci.*  2005; 360: 815-836

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0350)

    - [Scopus (1381)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_70_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-21244472727&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_70_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=15937014&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_70_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1098%2Frstb.2005.1622&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=360&publication_year=2005&pages=815-836&journal=Philos.+Trans.+R.+Soc.+B+Biol.+Sci.&author=Friston+K.J.&title=A+theory+of+cortical+responses&)

71. 1.

    - Bogacz R.

A tutorial on the free-energy framework for modelling perception and learning.
*J. Math. Psychol.*  2017; 76: 198-211

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0355)

    - [Scopus (16)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_71_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-84949908580&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_71_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=28298703&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_71_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1016%2Fj.jmp.2015.11.003&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=76&publication_year=2017&pages=198-211&journal=J.+Math.+Psychol.&author=Bogacz+R.&title=A+tutorial+on+the+free-energy+framework+for+modelling+perception+and+learning&)

72. 1.

    - Pineda F.J.

Generalization of back-propagation to recurrent neural networks.
*Phys. Rev. Lett.*  1987; 59: 2229-2232

[View in Article **](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#back-bib0360)

    - [Scopus (395)](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_72_2&dbid=137438953472&doi=10.1016/j.tics.2018.12.005&key=2-s2.0-0000442791&cf=)•
    - [PubMed](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_72_2&dbid=8&doi=10.1016/j.tics.2018.12.005&key=10035458&cf=)•
    - [Crossref](https://www.cell.com/servlet/linkout?suffix=e_1_5_1_2_72_2&dbid=16&doi=10.1016/j.tics.2018.12.005&key=10.1103%2FPhysRevLett.59.2229&cf=)•
    - [Google Scholar](http://scholar.google.com/scholar_lookup?hl=en&volume=59&publication_year=1987&pages=2229-2232&journal=Phys.+Rev.+Lett.&author=Pineda+F.J.&title=Generalization+of+back-propagation+to+recurrent+neural+networks&)

## Glossary

****Anti-Hebbian plasticity****

synaptic weight modifications proportional to the negative product of the activity of the pre- and postsynaptic neurons. Thus, if both neurons are highly active, the weight of connection between them is reduced.

****Apical dendrite****

a dendrite emerging from the apex of a pyramidal neuron (i.e., from the part of a cell body closest to the surface of the cortex).

****Artificial neural networks****

computing systems loosely based on brain networks. They consist of layers of ‘neurons’ communicating with each other via connections of different weights. Their task is to transform input patterns to particular target patterns. They are trained to predict target patterns in a process in which weights are modified according to the error back-propagation algorithm.

****Deep learning****

learning in artificial neural networks with more than two layers (often >10). Deep networks have shown much promise in the field of machine learning.

****Equilibrium propagation****

a principled framework for determining network dynamics and synaptic plasticity within energy-based models.

****Error back-propagation****

the main algorithm used to train artificial neural networks. It involves computations of errors associated with individual neurons, which determine weight modifications.

****Error node****

neuron type of predictive coding networks. They compute the difference between a value node and its higher-level prediction.

****Hebbian plasticity****

synaptic weight modifications proportional to the product of the activity of the pre- and postsynaptic neurons. It is called Hebbian in computational neuroscience, as it captures the idea of Donald Hebb that synaptic connections are strengthened between co-active neurons.

****Input pattern****

a vector containing the activity levels to which the neurons in the input layer are set. For example, in the handwritten digit classification problem, an input pattern corresponds to a picture of a digit. Here, the input pattern is a vector created by concatenating rows of pixels in the image, where each entry is equal to the darkness of the corresponding pixel.

****Martinotti cells****
small interneurons found in cortex.
****Oscillatory rhythms****

rhythmic patterns of neural activity, with activity of particular cells oscillating between higher and lower values.

****Plateau potential****

a sustained change in a membrane potential of a neuron, caused by persistent inwards currents.

****Predicted pattern****

a vector of activities generated by the network in the output layer, by propagating the input pattern through layers. In the handwritten digit classification problem, the output layer has ten neurons corresponding to ten possible digits. The activity of each output neuron encodes the network’s prediction for how likely the input pattern is to represent a particular digit.

****Pyramidal neuron****

an excitatory neuron with conically shaped cell body. Found in the cerebral cortex, hippocampus, and amygdala.

****Spike-time-dependent plasticity****

synaptic weight modification that depends on the relative timing between pre- and postsynaptic firing.

****Supervised learning****

a class of tasks considered in machine learning, where both an input and a target pattern are provided. The task for the algorithms is to learn to predict the target patterns from the input patterns.

****Target pattern****

a vector of activity in the output layer, which the network should generate for a given input pattern. For example, in the handwritten digit classification problem, the target pattern is equal to 1 at the position corresponding to the class of the corresponding image and is equal to 0 elsewhere.

****Unsupervised learning****

a class of tasks considered in machine learning where only an input pattern is provided (e.g., an image of a handwritten digit). The task for the learning algorithm is typically to learn an efficient representation of the data.

****Value node****

neuron type of predictive coding networks. Their activity represents the values computed by the network.

## Article Info

### Publication History

Published online: January 28, 2019

### Identification

DOI: https://doi.org/10.1016/j.tics.2018.12.005

### Copyright

© 2019 The Authors. Published by Elsevier Ltd.

### User License

 [Creative Commons Attribution (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) |

 [How you can reuse](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)  ![italic.a6e1da4a89899ae5e87db9ded9f84d5b.png](../_resources/58fac736dfb3327a7ecc7e5b2087c13b.png)

### ScienceDirect

[Access this article on ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1364661319300129)

## Figures

- ![gr1b1.jpg](../_resources/b3ac93e90047ae3ba6d4121592141b3b.jpg)

Figure IArtificial Neural Networks. (A) Layers of neuron-like nodes are represented by sets of stacked blue circles. Feedforward connections are indicated by green arrows. (B) Prediction. (C) Learning. (D) Schematic of the directions of two consecutive weight modifications (thick arrows) in the space of weights (for simplicity, only two dimensions are shown). Contours show points in weight space with equal cost function values.

- ![gr1b2.jpg](../_resources/d44880fbb7e0c046ec975a0439f3b236.jpg)

Figure ITemporal-Error Models. (A) Network architecture. (B) Dynamics. (C) Contrastive learning. (D) Continuous update.

- ![gr1b3.jpg](../_resources/67b0e63c3b0d5185eb0d962c5274ec8b.jpg)

Figure IPredictive Coding. (A) Network architecture. Blue and red circles denote the value and error nodes, respectively. Arrows and lines ending with circles denote excitatory and inhibitory connections, respectively; green double lines indicate connections between all neurons in one layer and all neurons in the next layer, while single black lines indicate within layer connections between a corresponding error and value node (see key). (B) Dynamics (for a simple case of linear function f; for details of how nonlinearities can be introduced, see [14Whittington J.C.R. Bogacz R. An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity.Neural Comput. 2017; 29: 1229-1262Crossref PubMed Scopus (0) Google Scholar]). (C) Prediction. (D) Learning.

- ![gr1b4.jpg](../_resources/4849d194bde77f3248a2126905a51d11.jpg)

Figure IDendritic Error Model. (A) Network architecture. Blue circles indicate pyramidal neurons, red rectangles indicate their apical dendrites, and purple circles denote interneurons. (B) Dynamics.

- ![gr1.jpg](../_resources/09c69595a7a18b11cf9f29c6ac758abe.jpg)

Figure 1Relationship between Learning Rules and Spike-Time-Dependent Plasticity. (A) Plasticity dependent on the rate of change of postsynaptic activity, illustrated by the left column of panels. (B) Asymmetric spike-time-dependent plasticity often observed in cortical neurons [59Bi G.Q. Poo M.M. Synaptic modifications in cultured hippocampal neurons: dependence on spike timing, synaptic strength, and postsynaptic cell type.J. Neurosci. 1998; 18: 10464-10472Crossref PubMed Google Scholar]. The curve schematically shows the change in synaptic weights as a function of the difference between the timings of postsynaptic and presynaptic spikes. Red and orange parts of the curve correspond to increases and decreases in synaptic weights, respectively. (C) Strengthening of a synaptic weight due to increasing postsynaptic activity. Hypothetical spike trains of two neurons are shown. The top sequence corresponds to an output neuron, which increases its activity over time towards the target (see Figure ID in Box 2). The bottom sequence corresponds to a neuron in the hidden layer; for simplicity, only a single spike is shown. The pink and yellow areas correspond to spike timings in which the weights are increased and decreased, respectively. In these areas the differences in spike timing result in weight changes indicated by red and orange parts of the curve in the panel B. (D) Weakening of weight due to decrease in postsynaptic activity. (E) Plasticity dependent on postsynaptic activity, illustrated by the right column of panels. In the equation, x0 denotes the baseline firing rate. (F) Symmetric spike-time-dependent plasticity, where weight change depends on spike proximity. (G) Increase in synaptic weight due to high activity of the postsynaptic neuron. (H) Decrease in synaptic weight when the postsynaptic neurons is less active.

- ![gr2.jpg](../_resources/f600eeeb78570c55d2c2deb2a5d0c245.jpg)

Figure 2Equilibrium Propagation. The framework considers networks with dynamics described by the minimisation of an energy function. As the activity of these networks converges to an equilibrium, the energy simultaneously decays (blue arrows) to a minimum given the current weights. Once in equilibrium, the weighs are modified (green arrows). It has been shown that network error can be minimised if the synaptic weights are modified in two steps (schematically illustrated by the two displays in the top box; [22Scellier B. Bengio Y. Equilibrium propagation: bridging the gap between energy-based models and backpropagation.Front. Comput. Neurosci. 2017; 11: 24Crossref PubMed Scopus (18) Google Scholar]). First, with only the input pattern provided, once the network converges, weights are modified in the direction in which the energy increases. Second, the output layer is additionally constrained to values closer to the target pattern (particular details described in [22Scellier B. Bengio Y. Equilibrium propagation: bridging the gap between energy-based models and backpropagation.Front. Comput. Neurosci. 2017; 11: 24Crossref PubMed Scopus (18) Google Scholar]). Constraining the output nodes changes the energy landscape for the units in the middle layers. Once these units converge to a new equilibrium, weights are modified in the direction in which the energy decreases. Scellier and Bengio [22Scellier B. Bengio Y. Equilibrium propagation: bridging the gap between energy-based models and backpropagation.Front. Comput. Neurosci. 2017; 11: 24Crossref PubMed Scopus (18) Google Scholar] noted that for temporal-error networks, this procedure gives the contrastive learning rule (Equation 2.2). The predictive coding networks, however, converge to an equilibrium in the first step where the free-energy function reaches its global minimum [14Whittington J.C.R. Bogacz R. An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity.Neural Comput. 2017; 29: 1229-1262Crossref PubMed Scopus (0) Google Scholar]; thus, there is no weight modification required by the equilibrium propagation framework. Therefore, only a single phase (i.e., the second phase) and a single weight update are required in the explicit-error models, and it only involves Hebbian plasticity.

## Tables

- [Table 1:Comparison of Models](https://www.cell.com/action/showFullTableHTML?isHtml=true&tableId=tbl0005&pii=S1364-6613%2819%2930012-9)

## Related Articles

- [Antigen-Primed CD8+ T Cells Call DCs for Back Up](https://www.cell.com/immunity/fulltext/S1074-7613(17)30035-3)

Burbage et al.
, *Immunity*, February 21, 2017

    - [In Brief](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)•
    - [Full-Text](https://www.cell.com/immunity/fulltext/S1074-7613(17)30035-3)•
    - [PDF](https://www.cell.com/immunity/pdf/S1074-7613(17)30035-3.pdf)

Open Archive

- [Looking Back: Aging and Regeneration](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30172-8)

, *Cell Stem Cell*, June 01, 2017

    - [In Brief](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)•
    - [Full-Text](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30172-8)•
    - [PDF](https://www.cell.com/cell-stem-cell/pdf/S1934-5909(17)30172-8.pdf)

Open Archive

- [Looking Back: Single-Cell Analysis](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30180-7)

, *Cell Stem Cell*, June 01, 2017

    - [In Brief](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)•
    - [Full-Text](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30180-7)•
    - [PDF](https://www.cell.com/cell-stem-cell/pdf/S1934-5909(17)30180-7.pdf)

Open Archive

- [Looking Back: Cancer Stem Cells](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30170-4)

, *Cell Stem Cell*, June 01, 2017

    - [In Brief](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)•
    - [Full-Text](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30170-4)•
    - [PDF](https://www.cell.com/cell-stem-cell/pdf/S1934-5909(17)30170-4.pdf)

Open Archive

- [Looking Back: Epigenomics](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30176-5)

, *Cell Stem Cell*, June 01, 2017

    - [In Brief](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(19)30012-9#)•
    - [Full-Text](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(17)30176-5)•
    - [PDF](https://www.cell.com/cell-stem-cell/pdf/S1934-5909(17)30176-5.pdf)

Open Archive

## Comments

- [0 comments]()
- [**Cell Press**](https://disqus.com/home/forums/cell-press/)
- [Marc Cohen](https://disqus.com/embed/comments/?base=default&f=cell-press&t_i=10.1016%2Fj.tics.2018.12.005&t_u=http%3A%2F%2Fwww.cell.com%2Fretrieve%2Fpii%2FS1364-6613(19)30012-9&t_e=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&t_d=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain&t_t=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&s_o=default#)
- [](https://disqus.com/home/inbox/)
- [ Recommend](https://disqus.com/embed/comments/?base=default&f=cell-press&t_i=10.1016%2Fj.tics.2018.12.005&t_u=http%3A%2F%2Fwww.cell.com%2Fretrieve%2Fpii%2FS1364-6613(19)30012-9&t_e=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&t_d=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain&t_t=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&s_o=default#)
- tTweetfShare
- [Sort by Newest](https://disqus.com/embed/comments/?base=default&f=cell-press&t_i=10.1016%2Fj.tics.2018.12.005&t_u=http%3A%2F%2Fwww.cell.com%2Fretrieve%2Fpii%2FS1364-6613(19)30012-9&t_e=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&t_d=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain&t_t=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&s_o=default#)

[![noavatar92.png](../_resources/675fb4b91ca717db030507f2d84bcfdf.png)](https://disqus.com/by/disqus_Q5LZbDr3pW/)

Start the discussion…

![bold.cb366e6a49396fb0e47a01df277563c8.png](../_resources/c6501c3f7d72fc1b6c5c664055aa9562.png)

![code.8f558a246aa4e9c41ef343f72f012f01.png](../_resources/a07b7e1fcec6807578565deaf67fee1b.png)

![si1.gif](../_resources/81c01ba2374c675c3aeaaa782bf2e78c.png)

![blockquote.69435f6faa8c7a193456c46bcb7fb1ed.png](../_resources/f7efeff64e3b50b6ed3ac56e033c7093.png)

![si4.gif](../_resources/77ac7d224499e3ad46945902c341b126.png)

![strikethrough.ced68e63961c6bc0e072ce907906b252.png](../_resources/c004e6b74d78957de021cd89afcfb140.png)

Be the first to comment.

- [Powered by Disqus](https://disqus.com/)
- [*✉*Subscribe*✔*](https://disqus.com/embed/comments/?base=default&f=cell-press&t_i=10.1016%2Fj.tics.2018.12.005&t_u=http%3A%2F%2Fwww.cell.com%2Fretrieve%2Fpii%2FS1364-6613(19)30012-9&t_e=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&t_d=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain&t_t=Theories%20of%20Error%20Back-Propagation%20in%20the%20Brain%3A%20Trends%20in%20Cognitive%20Sciences&s_o=default#)
- [*d*Add Disqus](https://publishers.disqus.com/engage?utm_source=cell-press&utm_medium=Disqus-Footer)
- [**Disqus' Privacy Policy](https://help.disqus.com/customer/portal/articles/466259-privacy-policy)

#### Cell Press Commenting Guidelines

To submit a comment for a journal article, please use the space above and note the following:

- We will review submitted comments within 2 business days.
- This forum is intended for constructive dialog. Comments that are commercial or promotional in nature, pertain to specific medical cases, are not relevant to the article for which they have been submitted, or are otherwise inappropriate will not be posted.
- We recommend that commenters identify themselves with full names and affiliations.
- Comments must be in compliance with our [Terms & Conditions](https://www.elsevier.com/legal/elsevier-website-terms-and-conditions).
- Comments will not be peer-reviewed.
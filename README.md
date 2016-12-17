# N-gram_model

One simple type of language model is an n-gram model. In these models, the probability of the next word in a sequence is calculated using the previous $n-1$ words as context. For example, if the first three words in a sentence are<br />
![equation](http://www.sciweavers.org/download/Tex2Img_1482018283.jpg)

a 4-gram language model might generate the following predictions:<br />
![equation](http://www.sciweavers.org/download/Tex2Img_1482018341.jpg)

The probability of a particular sequence of word tokens in an n-gram can be calculated using raw token frequences. Given a training corpus (i.e., a collection of texts), the probability of a word given the $n-1$ preceding tokens is simply<br />
![equation](http://www.sciweavers.org/download/Tex2Img_1482018396.jpg)

where $C(w_1, \ldots w_n)$ denotes the number of times the n-gram sequence $w_1, w_2, \ldots, w_n$ was observed in the training corpus. Note that the above definition corresponds to the **maximum likelihood estimate (MLE)** for the training data n-grams. Under this model, the probability of generating a particular sentence consisting of $k$ words (for $k > n$) is given by<br />
![equation](http://www.sciweavers.org/download/Tex2Img_1482018440.jpg)

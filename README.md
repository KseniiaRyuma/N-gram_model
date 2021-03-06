# N-gram_model

One simple type of language model is an n-gram model. In these models, the probability of the next word in a sequence is calculated using the previous **n-1** words as context. For example, if the first three words in a sentence are<br />
<br />![equation](http://www.sciweavers.org/download/Tex2Img_1482018283.jpg)<br />

a 4-gram language model might generate the following predictions:<br />
<br />![equation](http://www.sciweavers.org/download/Tex2Img_1482018341.jpg)<br />

The probability of a particular sequence of word tokens in an n-gram can be calculated using raw token frequences. Given a training corpus (i.e., a collection of texts), the probability of a word given the $n-1$ preceding tokens is simply<br />
<br />![equation](http://www.sciweavers.org/download/Tex2Img_1482018396.jpg)<br />

where the nominator denotes the number of times the n-gram sequence w1, w2, ... w_n was observed in the training corpus. Note that the above definition corresponds to the **maximum likelihood estimate (MLE)** for the training data n-grams. Under this model, the probability of generating a particular sentence consisting of **k** words (for k > n) is given by<br />
<br />![equation](http://www.sciweavers.org/download/Tex2Img_1482018440.jpg)<br />

import tensorflow as tf

import numpy as np

print(tf.__version__)

# Tensor examples -----------------

string = tf.Variable("this is a string", tf.string) 
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

# Rank / Degree of Tensors ----------------------

rank1_tensor = tf.Variable(["Test"], tf.string) 
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

""" Types of Tensors

- Variable
- Constant
- Placeholder
- SparseTensor """

# Evaluating Tensors ----------------

with tf.Session() as sess:
  tensor.eval()
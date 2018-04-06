import tensorflow as tf 
from './helper.py' import getTrainBatch, iterations

labels = tf.placeholder(tf.float32, [batchSize, numClasses])
input_data = tf.placeholder(tf.int32, [batchSize, maxSeqLength])

data = tf.Variable(tf.zeros([batchSize, maxSeqLength, numDimensions]),dtype=tf.float32)
data = tf.nn.embedding_lookup(wordVectors,input_data)

lstmCell = tf.contrib.rnn.BasicLSTMCell(lstmUnits)
lstmCell = tf.contrib.rnn.DropoutWrapper(cell=lstmCell, output_keep_prob=0.75)
value, _ = tf.nn.dynamic_rnn(lstmCell, data, dtype=tf.float32)

sess = tf.InteractiveSession()
saver = tf.train.Saver()
sess.run(tf.global_variables_initializer())

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=labels))
optimizer = tf.train.AdamOptimizer().minimize(loss)

for i in range(iterations):
  nextBatch, nextBatchLables = getTrainBatch()
  sess.run(optimizer, {input_data: nextBatch, labels: nextBatchLabels})

  if (i % 10000 == 0 and i != 0):
    save_path = saver.save(sess, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/models/pretrained_lstm.ckpt'), global_step=i)
    print("saved to %s" % save_path)
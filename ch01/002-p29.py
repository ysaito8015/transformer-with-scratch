import tensorflow as tf

a = tf.constant([[1., 2., 3.], [3., 4., 5.], [5., 6., 7.], [7., 8., 9.]])
a_v = tf.Variable(a, name='a')

b = tf.constant([0.1, 0.2, 0.3])
b_v = tf.Variable(b, name='b')

x = tf.constant([[1., 2., 3., 4.]])

print(tf.matmul(x, a_v) + b_v)

tgt = [[10., 20., 30.]]

loss = lambda: ((tf.matmul(x, a_v) + b_v)) ** 2

opt = tf.keras.optimizers.SGD()

opt.minimize(loss, var_list=[a_v, b_v])

print(a_v, b_v)

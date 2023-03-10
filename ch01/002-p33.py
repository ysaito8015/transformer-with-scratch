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

print(a_v)
print(b_v)

for _ in range(1000):
    opt.minimize(loss, var_list=[a_v, b_v])

print(a_v)
print(b_v)

print(tf.matmul(x, a_v) + b_v)


class fc4_3(tf.keras.layers.Layer):
    def __init__(self):
        super(fc4_3, self).__init__(name='fc4_3')
        a = tf.constant([[1., 2., 3.], [3., 4., 5.], [5., 6., 7.], [7., 8., 9.]])
        self.a_v = tf.Variable(a, name='a')
        b = tf.constant([0.1, 0.2, 0.3])
        self.b_v = tf.Varible(b, name='b')

    def call(self, x):
        return tf.matmul(x, self.a_v) + self.b_v


X = tf.keras.Input(dtype=tf.float32, shape=[4])

a = tf.constant([[1., 2., 3.], [3., 4., 5.], [5., 6., 7.], [7., 8., 9.]])
a_v = tf.Variable(a, name='a')

b = tf.constant([0.1, 0.2, 0.3])
b_v = tf.Variable(b, name='b')

y = tf.matmul(X, a_v) + b_v

model = tf.keras.models.Model(inputs=X, outputs=y)

print(model(tf.constant([[1., 2., 3., 4.]])))
print(model.predict(tf.constant([[1., 2., 3., 4.]])))


model.compile(opt, lambda p, t: (p-t)**2)

model.fit(x=[[1., 2., 3., 4.]], y=[[10., 20., 30.]])

model.save('save_model', save_format="tf")
restored_model = tf.keras.models.load_model('saved_model')

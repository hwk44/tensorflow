from tensorflow.python.framework.ops import enable_eager_execution

# enable_eager_execution()
import tensorflow as tf
print(tf.executing_eagerly()) # 에러 발생시에 런타임
a = tf.constant(1)
b = tf.constant(2)
c = a + b   # c= tf.add(a, b)
print(a)
print(b)
print(c)
print(a.numpy(), b.numpy(), c.numpy())

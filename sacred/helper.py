import tensorflow as tf


def prepare_tensors(df):
    Y = df["Price"]
    X = df.drop("Price", axis=1)
    X_tensor = tf.convert_to_tensor(X, dtype=tf.float32)
    Y_tensor = tf.convert_to_tensor(Y, dtype=tf.float32)
    return X_tensor, Y_tensor
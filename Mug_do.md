<h1>Lines to comment before starting server</h1>

1.  thyro_check/settings.py ->

    1. from keras.models import load_model
       import tensorflow as tf

    2. global model
       model = load_model('test/thyroid_model_216.h5')
       MODEL = model
       global graph
       graph = tf.get_default_graph()
       GRAPH = graph

2.  accounts/views.py ->

    1. from keras.preprocessing import image,

    2. result = get_result(image_path)

    uncomment -> # result = [[0.234224, 0.2424534]]
    to get dummy results.

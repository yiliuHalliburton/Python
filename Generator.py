##%
def get_generator(i):
    for x in range(2):
        yield(x+i)
my_generator = get_generator(3)
next(my_generator)
print(next(my_generator))

##%
'''
def get_pictures(image_files):
    for image in image_files:
        image_data = load(image)
        yield image_data

picture_generator = get_pictures(my_image_file_names)

for i in range(number_of_pictures):
    picture = next(picture_generator)
    display(picture)
'''
##%
import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices([1,2,3])
print(list(dataset.as_numpy_iterator()))

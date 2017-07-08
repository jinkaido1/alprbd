"""
For testing the trained model
"""
import os
from glob import glob
import cv2
import numpy as np
import tensorflow as tf
import config as cfg

def read_images(folder):
    """Read all images from a directory recursively"""
    return np.sort([file for file in glob(folder + '**/*.*', recursive=True)])
# end if

def trim_image(img):
    """Keep only important part"""
    # open
    rows, cols = img.shape
    # find area
    nzx, nzy = np.nonzero(img)
    x1 = max(0, np.min(nzx))
    x2 = min(rows, np.max(nzx) + 2)
    y1 = max(0, np.min(nzy))
    y2 = min(cols, np.max(nzy) + 2)
    # crop
    cropped = img[x1:x2, y1:y2]
    # resize
    resized = cv2.resize(cropped, cfg.IMAGE_DIM)
    return resized
# end function

def main():
    """Main function"""
    # Check sample directory
    if not os.path.exists(cfg.DIGIT_SAMPLES):
        return print("Samples not found")
    # end if

    # Create session
    sess = tf.Session()
    print()

    # Restore model
    folder = os.path.dirname(cfg.DIGIT_MODEL)
    saver = tf.train.import_meta_graph(cfg.DIGIT_MODEL + '.meta')
    saver.restore(sess, tf.train.latest_checkpoint(folder))
    
    graph = tf.get_default_graph()
    X = graph.get_tensor_by_name("X:0")

    files = read_images(cfg.DIGIT_SAMPLES)
    for file in files:
        # prepare image data
        image = cv2.imread(file, 0)
        image = trim_image(image)
        image = np.reshape(image, (1, 784))
        # predict outcome
        YY = graph.get_tensor_by_name("YY:0")
        Y = sess.run(YY, {X: image})        
        Y = Y.flatten()
        p = np.argmax(Y)
        # show result
        name = os.path.split(file)[-1]
        print("%s\t = %s (%.2f%% sure)" % (name, cfg.NUMERALS[p], Y[p] * 100))
    # end for
# end function

if __name__ == '__main__':
    main()
# end if

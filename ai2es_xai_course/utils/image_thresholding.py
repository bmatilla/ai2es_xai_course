"""Methods for thresholding image data."""

import numpy
from ai2es_xai_course.utils import image_utils


def get_binarization_threshold(percentile_level, image_file_names=None,
                               image_dict=None):
    """Computes binarization threshold for target variable.

    Binarization threshold will be [q]th percentile of all image maxima, where
    q = `percentile_level`.

    One of the input args `image_file_names` and `image_dict` must be
    specified.

    :param percentile_level: q in the above discussion.
    :param image_file_names: 1-D list of paths to input files.
    :param image_dict: Dictionary returned by `image_utils.read_file`.
    :return: binarization_threshold: Binarization threshold (used to turn each
        target image into a yes-or-no label).
    """

    if image_dict is None:
        max_target_values = numpy.array([])

        for this_file_name in image_file_names:
            print('Reading data from: "{0:s}"...'.format(this_file_name))
            this_image_dict = image_utils.read_file(this_file_name)

            these_max_target_values = numpy.max(
                this_image_dict[image_utils.TARGET_MATRIX_KEY], axis=(1, 2)
            )
            max_target_values = numpy.concatenate((
                max_target_values, these_max_target_values
            ))
    else:
        max_target_values = numpy.max(
            image_dict[image_utils.TARGET_MATRIX_KEY], axis=(1, 2)
        )

    binarization_threshold = numpy.percentile(
        max_target_values, percentile_level
    )

    print('\nBinarization threshold for "{0:s}" = {1:.4e}'.format(
        image_utils.TARGET_NAME, binarization_threshold
    ))

    return binarization_threshold


def binarize_target_images(target_matrix, binarization_threshold):
    """Binarizes target images.

    Specifically, this method turns each target image into a binary label,
    depending on whether or not (max value in image) >= binarization_threshold.

    E = number of examples (storm objects) in file
    M = number of rows in each storm-centered grid
    N = number of columns in each storm-centered grid

    :param target_matrix: E-by-M-by-N numpy array of floats.
    :param binarization_threshold: Binarization threshold.
    :return: target_values: length-E numpy array of target values (integers in
        0...1).
    """

    num_examples = target_matrix.shape[0]
    target_values = numpy.full(num_examples, -1, dtype=int)

    for i in range(num_examples):
        target_values[i] = (
            numpy.max(target_matrix[i, ...]) >= binarization_threshold
        )

    return target_values

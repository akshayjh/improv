import tensorflow as tf

from src.config import get_debug_params
from src.my_classifier import (
    get_model_and_estimator, evaluate, train, train_eval, predict
)


def main():
    params = get_debug_params()

    tf.gfile.MakeDirs(str(params.output_dir))

    # Colab script starts here, don't forget the imports
    model_fn, estimator = get_model_and_estimator(params)

    if params.do_train_eval:
        train_eval(params, estimator)

    if params.do_train:
        train(params, estimator)

    if params.do_eval:
        evaluate(params, estimator)

    # note that predictions are non-deterministic
    if params.do_predict:
        predict(params)


if __name__ == '__main__':
    main()

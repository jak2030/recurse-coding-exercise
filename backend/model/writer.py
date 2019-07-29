import os


class Writer(object):
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def write(self, model, model_name):
        """Serialize a model to json and write it to a file."""
        model_json = model.to_json()
        fpath = os.path.join(self.output_dir, model_name)
        with open(fpath, "w") as fh:
            fh.write(model_json)

import unittest

from pyconll.unit import Conll

from danlp.datasets.ner import load_ner_as_conllu, load_ner_with_flair


class TestNerDatasets(unittest.TestCase):

    def test_loading_non_existing_dataset(self):
        with self.assertRaises(AssertionError):
            load_ner_as_conllu('test')

    def test_loading_with_connllu(self):
        train, dev, test = load_ner_as_conllu('ddt', predefined_splits=True)

        self.assertIsInstance(train, Conll)
        self.assertIsInstance(dev, Conll)
        self.assertIsInstance(test, Conll)

        self.assertEqual([len(train), len(dev), len(test)], [4383, 564, 565])

        full_dataset = load_ner_as_conllu('ddt', predefined_splits=False)
        self.assertEqual(len(full_dataset), 5512)

    def test_loading_with_flair(self):
        corpus = load_ner_with_flair('ddt')

        self.assertEqual(len(corpus.train), 4383)
        self.assertEqual(len(corpus.dev), 564)
        self.assertEqual(len(corpus.test), 565)

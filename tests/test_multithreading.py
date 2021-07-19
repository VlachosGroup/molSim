""" Test multithreading to ensure consistent behavior with serial implementation."""
import unittest
from os import remove
from os.path import exists
import numpy as np
import pandas as pd
import rdkit
from rdkit.Chem import MolFromSmiles
from molSim.chemical_datastructures import Molecule, MoleculeSet
from molSim.ops import Descriptor, SimilarityMeasure
from molSim.tasks.visualize_dataset import VisualizeDataset
from time import time
from tabulate import tabulate

NO_SPEEDUP_TEST = False


class TestMultithreading(unittest.TestCase):
    """Unit tests to ensure consistency when running molSim as a single process
    or when using multiprocessing.
    """
    @classmethod
    def setUpClass(self):
        """Create a SMILES database to use for comparisons and find the similarity matrix.
        """
        print(" ~ ~ Testing Multithreading ~ ~ ")
        # basic consistency tests
        self.text_fpath = 'temp_multithread_smiles_seq.txt'
        print(f'Creating text file {self.text_fpath}')
        with open(self.text_fpath, "w") as file:
            for smiles in ['C', 'CC', 'CCC', 'O', 'CCCC', 'CO', 'CCOCC']:
                file.write(smiles + '\n')
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=1,
            fingerprint_type='morgan_fingerprint',
        )
        self.correct_similarity_matrix = test_molecule_set.get_similarity_matrix()

        if NO_SPEEDUP_TEST:
            return
        with open(r"tests\data\combinatorial_1.txt", "r") as file:
            data = file.readlines()
            _100_molecules = data[1:102]
            _500_molecules = data[1:502]
            _1000_molecules = data[1:1002]
            _5000_molecules = data[1:5002]
            _10000_molecules = data[1:10002]
        # data used for speedup and efficiency tests
        self._100_molecules_fpath = 'temp_multithread_speedup_100.txt'
        print(f'Creating text file {self._100_molecules_fpath}')
        with open(self._100_molecules_fpath, "w") as file:
            for smiles in _100_molecules:
                file.write(smiles)
        print("Running 100 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=1,
            fingerprint_type='morgan_fingerprint',
        )
        self._100_molecules_serial_time = time() - start

        self._500_molecules_fpath = 'temp_multithread_speedup_500.txt'
        print(f'Creating text file {self._500_molecules_fpath}')
        with open(self._500_molecules_fpath, "w") as file:
            for smiles in _500_molecules:
                file.write(smiles)
        print("Running 500 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=1,
            fingerprint_type='morgan_fingerprint',
        )
        self._500_molecules_serial_time = time() - start

        self._1000_molecules_fpath = 'temp_multithread_speedup_1000.txt'
        print(f'Creating text file {self._1000_molecules_fpath}')
        with open(self._1000_molecules_fpath, "w") as file:
            for smiles in _1000_molecules:
                file.write(smiles)
        print("Running 1000 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=1,
            fingerprint_type='morgan_fingerprint',
        )
        self._1000_molecules_serial_time = time() - start

        self._5000_molecules_fpath = 'temp_multithread_speedup_5000.txt'
        print(f'Creating text file {self._5000_molecules_fpath}')
        with open(self._5000_molecules_fpath, "w") as file:
            for smiles in _5000_molecules:
                file.write(smiles)
        print("Running 5000 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=1,
            fingerprint_type='morgan_fingerprint',
        )
        self._5000_molecules_serial_time = time() - start

        self._10000_molecules_fpath = 'temp_multithread_speedup_10000.txt'
        print(f'Creating text file {self._10000_molecules_fpath}')
        with open(self._10000_molecules_fpath, "w") as file:
            for smiles in _10000_molecules:
                file.write(smiles)
        print("Running 10000 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=1,
            fingerprint_type='morgan_fingerprint',
        )
        self._10000_molecules_serial_time = time() - start

        # data used for speedup and efficiency test 2
        print("Running 100 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=1,
            fingerprint_type='topological_fingerprint',
        )
        self._100_molecules_serial_time_2 = time() - start

        print("Running 500 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=1,
            fingerprint_type='topological_fingerprint',
        )
        self._500_molecules_serial_time_2 = time() - start

        print("Running 1000 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=1,
            fingerprint_type='topological_fingerprint',
        )
        self._1000_molecules_serial_time_2 = time() - start

        print("Running 5000 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=1,
            fingerprint_type='topological_fingerprint',
        )
        self._5000_molecules_serial_time_2 = time() - start

        print("Running 10000 molecules with 1 process.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=1,
            fingerprint_type='topological_fingerprint',
        )
        self._10000_molecules_serial_time_2 = time() - start

    def test_multithreading_consistency_2_threads(self):
        """
        Ensure that the similarity matrix produced with 2 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=2,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using two threads."
        )

    def test_multithreading_consistency_3_threads(self):
        """
        Ensure that the similarity matrix produced with 3 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=3,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using three threads."
        )

    def test_multithreading_consistency_4_threads(self):
        """
        Ensure that the similarity matrix produced with 4 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=4,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using four threads."
        )

    def test_multithreading_consistency_5_threads(self):
        """
        Ensure that the similarity matrix produced with 5 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=5,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using five threads."
        )

    def test_multithreading_consistency_6_threads(self):
        """
        Ensure that the similarity matrix produced with 6 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=6,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using six threads."
        )

    def test_multithreading_consistency_7_threads(self):
        """
        Ensure that the similarity matrix produced with 7 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=7,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using seven threads (equal to the number of molecules)."
        )

    def test_multithreading_consistency_10_threads(self):
        """
        Ensure that the similarity matrix produced with 10 threads is identical to
        that produced using a single thread and the serial implementation.
        """
        test_molecule_set = MoleculeSet(
            molecule_database_src=self.text_fpath,
            molecule_database_src_type="text",
            is_verbose=True,
            similarity_measure='tanimoto',
            n_threads=10,
            fingerprint_type='morgan_fingerprint',
        )
        self.assertIsNone(
            np.testing.assert_array_equal(test_molecule_set.get_similarity_matrix(),
                                          self.correct_similarity_matrix),
            "Similarity matrix not equal when using ten threads (more than the number of molecules)."
        )

    def test_speedup_efficiency_tanimoto(self):
        """
        Evaluate the speedup and efficieny of the multiprocessing approach.
        """
        if NO_SPEEDUP_TEST:
            return
        print("~" * 10, "\n", "Speedup and Efficiency Test\n", "~" * 10)
        # 100 molecules
        print("Running 100 molecules with 2 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=2,
            fingerprint_type='morgan_fingerprint',
        )
        _100_molecules_2_process_time = time() - start
        _100_molecules_2_process_speedup = self._100_molecules_serial_time / \
            _100_molecules_2_process_time
        _100_molecules_2_process_efficiency = _100_molecules_2_process_speedup / 2

        print("Running 100 molecules with 5 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=5,
            fingerprint_type='morgan_fingerprint',
        )
        _100_molecules_5_process_time = time() - start
        _100_molecules_5_process_speedup = self._100_molecules_serial_time / \
            _100_molecules_5_process_time
        _100_molecules_5_process_efficiency = _100_molecules_5_process_speedup / 5

        print("Running 100 molecules with 10 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=10,
            fingerprint_type='morgan_fingerprint',
        )
        _100_molecules_10_process_time = time() - start
        _100_molecules_10_process_speedup = self._100_molecules_serial_time / \
            _100_molecules_10_process_time
        _100_molecules_10_process_efficiency = _100_molecules_10_process_speedup / 10

        # 500 molecules
        print("Running 500 molecules with 2 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=2,
            fingerprint_type='morgan_fingerprint',
        )
        _500_molecules_2_process_time = time() - start
        _500_molecules_2_process_speedup = self._500_molecules_serial_time / \
            _500_molecules_2_process_time
        _500_molecules_2_process_efficiency = _500_molecules_2_process_speedup / 2

        print("Running 500 molecules with 5 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=5,
            fingerprint_type='morgan_fingerprint',
        )
        _500_molecules_5_process_time = time() - start
        _500_molecules_5_process_speedup = self._500_molecules_serial_time / \
            _500_molecules_5_process_time
        _500_molecules_5_process_efficiency = _500_molecules_5_process_speedup / 5

        print("Running 500 molecules with 10 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=10,
            fingerprint_type='morgan_fingerprint',
        )
        _500_molecules_10_process_time = time() - start
        _500_molecules_10_process_speedup = self._500_molecules_serial_time / \
            _500_molecules_10_process_time
        _500_molecules_10_process_efficiency = _500_molecules_10_process_speedup / 10

        # 1000 molecules
        print("Running 1000 molecules with 2 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=2,
            fingerprint_type='morgan_fingerprint',
        )
        _1000_molecules_2_process_time = time() - start
        _1000_molecules_2_process_speedup = self._1000_molecules_serial_time / \
            _1000_molecules_2_process_time
        _1000_molecules_2_process_efficiency = _1000_molecules_2_process_speedup / 2

        print("Running 1000 molecules with 5 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=5,
            fingerprint_type='morgan_fingerprint',
        )
        _1000_molecules_5_process_time = time() - start
        _1000_molecules_5_process_speedup = self._1000_molecules_serial_time / \
            _1000_molecules_5_process_time
        _1000_molecules_5_process_efficiency = _1000_molecules_5_process_speedup / 5

        print("Running 1000 molecules with 10 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=10,
            fingerprint_type='morgan_fingerprint',
        )
        _1000_molecules_10_process_time = time() - start
        _1000_molecules_10_process_speedup = self._1000_molecules_serial_time / \
            _1000_molecules_10_process_time
        _1000_molecules_10_process_efficiency = _1000_molecules_10_process_speedup / 10

        # 5000 molecules
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=2,
            fingerprint_type='morgan_fingerprint',
        )
        _5000_molecules_2_process_time = time() - start
        _5000_molecules_2_process_speedup = self._5000_molecules_serial_time / \
            _5000_molecules_2_process_time
        _5000_molecules_2_process_efficiency = _5000_molecules_2_process_speedup / 2

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=5,
            fingerprint_type='morgan_fingerprint',
        )
        _5000_molecules_5_process_time = time() - start
        _5000_molecules_5_process_speedup = self._5000_molecules_serial_time / \
            _5000_molecules_5_process_time
        _5000_molecules_5_process_efficiency = _5000_molecules_5_process_speedup / 5

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=10,
            fingerprint_type='morgan_fingerprint',
        )
        _5000_molecules_10_process_time = time() - start
        _5000_molecules_10_process_speedup = self._5000_molecules_serial_time / \
            _5000_molecules_10_process_time
        _5000_molecules_10_process_efficiency = _5000_molecules_10_process_speedup / 10

        # 10000 molecules
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=2,
            fingerprint_type='morgan_fingerprint',
        )
        _10000_molecules_2_process_time = time() - start
        _10000_molecules_2_process_speedup = self._10000_molecules_serial_time / \
            _10000_molecules_2_process_time
        _10000_molecules_2_process_efficiency = _10000_molecules_2_process_speedup / 2

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=5,
            fingerprint_type='morgan_fingerprint',
        )
        _10000_molecules_5_process_time = time() - start
        _10000_molecules_5_process_speedup = self._10000_molecules_serial_time / \
            _10000_molecules_5_process_time
        _10000_molecules_5_process_efficiency = _10000_molecules_5_process_speedup / 5

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='tanimoto',
            n_threads=10,
            fingerprint_type='morgan_fingerprint',
        )
        _10000_molecules_10_process_time = time() - start
        _10000_molecules_10_process_speedup = self._10000_molecules_serial_time / \
            _10000_molecules_10_process_time
        _10000_molecules_10_process_efficiency = _10000_molecules_10_process_speedup / 10
        print("Speedup:")
        print(tabulate([["~", 2, 5, 10],
                        [100, _100_molecules_2_process_speedup,
                            _100_molecules_5_process_speedup, _100_molecules_10_process_speedup],
                        [500, _500_molecules_2_process_speedup,
                         _500_molecules_5_process_speedup, _500_molecules_10_process_speedup],
                        [1000, _1000_molecules_2_process_speedup,
                        _1000_molecules_5_process_speedup, _1000_molecules_10_process_speedup],
                        [5000, _5000_molecules_2_process_speedup,
                         _5000_molecules_5_process_speedup, _5000_molecules_10_process_speedup],
                        [10000, _10000_molecules_2_process_speedup,
                        _10000_molecules_5_process_speedup, _10000_molecules_10_process_speedup]],
                       headers=["# mol", "", "# processes", ""])
              )
        print("Efficiency:")
        print(tabulate([["~", 2, 5, 10],
                        [100, _100_molecules_2_process_efficiency,
                            _100_molecules_5_process_efficiency, _100_molecules_10_process_efficiency],
                        [500, _500_molecules_2_process_efficiency,
                         _500_molecules_5_process_efficiency, _500_molecules_10_process_efficiency],
                        [1000, _1000_molecules_2_process_efficiency,
                        _1000_molecules_5_process_efficiency, _1000_molecules_10_process_efficiency],
                        [5000, _5000_molecules_2_process_efficiency,
                         _5000_molecules_5_process_efficiency, _5000_molecules_10_process_efficiency],
                        [10000, _10000_molecules_2_process_efficiency,
                        _10000_molecules_5_process_efficiency, _10000_molecules_10_process_efficiency]],
                       headers=["# mol", "", "# processes", ""])
              )
        print("Execution Time in seconds (serial/parallel):")
        print(tabulate([["~", 2, 5, 10],
                        [100, "{:.2f}/{:.2f}".format(float(self._100_molecules_serial_time), float(_100_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._100_molecules_serial_time),
                                                   float(_100_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._100_molecules_serial_time), float(_100_molecules_10_process_time))],
                        [500, "{:.2f}/{:.2f}".format(float(self._500_molecules_serial_time), float(_500_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._500_molecules_serial_time),
                                                   float(_500_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._500_molecules_serial_time), float(_500_molecules_10_process_time))],
                        [1000, "{:.2f}/{:.2f}".format(float(self._1000_molecules_serial_time), float(_1000_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._1000_molecules_serial_time),
                                                   float(_1000_molecules_5_process_time)),
                            "{:2f}/{:.2f}".format(float(self._1000_molecules_serial_time), float(_1000_molecules_10_process_time))],
                        [5000, "{:.2f}/{:.2f}".format(float(self._5000_molecules_serial_time), float(_5000_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._5000_molecules_serial_time),
                                                   float(_5000_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._5000_molecules_serial_time), float(_5000_molecules_10_process_time))],
                        [10000, "{:.2f}/{:.2f}".format(float(self._10000_molecules_serial_time), float(_10000_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._10000_molecules_serial_time),
                                                   float(_10000_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._10000_molecules_serial_time), float(_10000_molecules_10_process_time))]],
                       headers=["# mol", "", "# processes", ""])
              )

    def test_speedup_efficiency_cosine(self):
        """
        Evaluate the speedup and efficieny of the multiprocessing approach with a more complex metric.
        """
        if NO_SPEEDUP_TEST:
            return
        print("~" * 10, "\n", "Speedup and Efficiency Test 2\n", "~" * 10)
        # 100 molecules
        print("Running 100 molecules with 2 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=2,
            fingerprint_type='topological_fingerprint',
        )
        _100_molecules_2_process_time = time() - start
        _100_molecules_2_process_speedup = self._100_molecules_serial_time_2 / \
            _100_molecules_2_process_time
        _100_molecules_2_process_efficiency = _100_molecules_2_process_speedup / 2

        print("Running 100 molecules with 5 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=5,
            fingerprint_type='topological_fingerprint',
        )
        _100_molecules_5_process_time = time() - start
        _100_molecules_5_process_speedup = self._100_molecules_serial_time_2 / \
            _100_molecules_5_process_time
        _100_molecules_5_process_efficiency = _100_molecules_5_process_speedup / 5

        print("Running 100 molecules with 10 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._100_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=10,
            fingerprint_type='topological_fingerprint',
        )
        _100_molecules_10_process_time = time() - start
        _100_molecules_10_process_speedup = self._100_molecules_serial_time_2 / \
            _100_molecules_10_process_time
        _100_molecules_10_process_efficiency = _100_molecules_10_process_speedup / 10

        # 500 molecules
        print("Running 500 molecules with 2 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=2,
            fingerprint_type='topological_fingerprint',
        )
        _500_molecules_2_process_time = time() - start
        _500_molecules_2_process_speedup = self._500_molecules_serial_time_2 / \
            _500_molecules_2_process_time
        _500_molecules_2_process_efficiency = _500_molecules_2_process_speedup / 2

        print("Running 500 molecules with 5 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=5,
            fingerprint_type='topological_fingerprint',
        )
        _500_molecules_5_process_time = time() - start
        _500_molecules_5_process_speedup = self._500_molecules_serial_time_2 / \
            _500_molecules_5_process_time
        _500_molecules_5_process_efficiency = _500_molecules_5_process_speedup / 5

        print("Running 500 molecules with 10 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._500_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=10,
            fingerprint_type='topological_fingerprint',
        )
        _500_molecules_10_process_time = time() - start
        _500_molecules_10_process_speedup = self._500_molecules_serial_time_2 / \
            _500_molecules_10_process_time
        _500_molecules_10_process_efficiency = _500_molecules_10_process_speedup / 10

        # 1000 molecules
        print("Running 1000 molecules with 2 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=2,
            fingerprint_type='topological_fingerprint',
        )
        _1000_molecules_2_process_time = time() - start
        _1000_molecules_2_process_speedup = self._1000_molecules_serial_time_2 / \
            _1000_molecules_2_process_time
        _1000_molecules_2_process_efficiency = _1000_molecules_2_process_speedup / 2

        print("Running 1000 molecules with 5 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=5,
            fingerprint_type='topological_fingerprint',
        )
        _1000_molecules_5_process_time = time() - start
        _1000_molecules_5_process_speedup = self._1000_molecules_serial_time_2 / \
            _1000_molecules_5_process_time
        _1000_molecules_5_process_efficiency = _1000_molecules_5_process_speedup / 5

        print("Running 1000 molecules with 10 processes.")
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._1000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=10,
            fingerprint_type='topological_fingerprint',
        )
        _1000_molecules_10_process_time = time() - start
        _1000_molecules_10_process_speedup = self._1000_molecules_serial_time_2 / \
            _1000_molecules_10_process_time
        _1000_molecules_10_process_efficiency = _1000_molecules_10_process_speedup / 10

        # 5000 molecules
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=2,
            fingerprint_type='topological_fingerprint',
        )
        _5000_molecules_2_process_time = time() - start
        _5000_molecules_2_process_speedup = self._5000_molecules_serial_time_2 / \
            _5000_molecules_2_process_time
        _5000_molecules_2_process_efficiency = _5000_molecules_2_process_speedup / 2

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=5,
            fingerprint_type='topological_fingerprint',
        )
        _5000_molecules_5_process_time = time() - start
        _5000_molecules_5_process_speedup = self._5000_molecules_serial_time_2 / \
            _5000_molecules_5_process_time
        _5000_molecules_5_process_efficiency = _5000_molecules_5_process_speedup / 5

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._5000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=10,
            fingerprint_type='topological_fingerprint',
        )
        _5000_molecules_10_process_time = time() - start
        _5000_molecules_10_process_speedup = self._5000_molecules_serial_time_2 / \
            _5000_molecules_10_process_time
        _5000_molecules_10_process_efficiency = _5000_molecules_10_process_speedup / 10

        # 10000 molecules
        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=2,
            fingerprint_type='topological_fingerprint',
        )
        _10000_molecules_2_process_time = time() - start
        _10000_molecules_2_process_speedup = self._10000_molecules_serial_time_2 / \
            _10000_molecules_2_process_time
        _10000_molecules_2_process_efficiency = _10000_molecules_2_process_speedup / 2

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=5,
            fingerprint_type='topological_fingerprint',
        )
        _10000_molecules_5_process_time = time() - start
        _10000_molecules_5_process_speedup = self._10000_molecules_serial_time_2 / \
            _10000_molecules_5_process_time
        _10000_molecules_5_process_efficiency = _10000_molecules_5_process_speedup / 5

        start = time()
        test_molecule_set = MoleculeSet(
            molecule_database_src=self._10000_molecules_fpath,
            molecule_database_src_type="text",
            is_verbose=False,
            similarity_measure='cosine',
            n_threads=10,
            fingerprint_type='topological_fingerprint',
        )
        _10000_molecules_10_process_time = time() - start
        _10000_molecules_10_process_speedup = self._10000_molecules_serial_time_2 / \
            _10000_molecules_10_process_time
        _10000_molecules_10_process_efficiency = _10000_molecules_10_process_speedup / 10
        print("Speedup:")
        print(tabulate([["~", 2, 5, 10],
                        [100, _100_molecules_2_process_speedup,
                            _100_molecules_5_process_speedup, _100_molecules_10_process_speedup],
                        [500, _500_molecules_2_process_speedup,
                         _500_molecules_5_process_speedup, _500_molecules_10_process_speedup],
                        [1000, _1000_molecules_2_process_speedup,
                        _1000_molecules_5_process_speedup, _1000_molecules_10_process_speedup],
                        [5000, _5000_molecules_2_process_speedup,
                         _5000_molecules_5_process_speedup, _5000_molecules_10_process_speedup],
                        [10000, _10000_molecules_2_process_speedup,
                        _10000_molecules_5_process_speedup, _10000_molecules_10_process_speedup]],
                       headers=["# mol", "", "# processes", ""])
              )
        print("Efficiency:")
        print(tabulate([["~", 2, 5, 10],
                        [100, _100_molecules_2_process_efficiency,
                            _100_molecules_5_process_efficiency, _100_molecules_10_process_efficiency],
                        [500, _500_molecules_2_process_efficiency,
                         _500_molecules_5_process_efficiency, _500_molecules_10_process_efficiency],
                        [1000, _1000_molecules_2_process_efficiency,
                        _1000_molecules_5_process_efficiency, _1000_molecules_10_process_efficiency],
                        [5000, _5000_molecules_2_process_efficiency,
                         _5000_molecules_5_process_efficiency, _5000_molecules_10_process_efficiency],
                        [10000, _10000_molecules_2_process_efficiency,
                        _10000_molecules_5_process_efficiency, _10000_molecules_10_process_efficiency]],
                       headers=["# mol", "", "# processes", ""])
              )
        print("Execution Time in seconds (serial/parallel):")
        print(tabulate([["~", 2, 5, 10],
                        [100, "{:.2f}/{:.2f}".format(float(self._100_molecules_serial_time_2), float(_100_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._100_molecules_serial_time_2),
                                                   float(_100_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._100_molecules_serial_time_2), float(_100_molecules_10_process_time))],
                        [500, "{:.2f}/{:.2f}".format(float(self._500_molecules_serial_time_2), float(_500_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._500_molecules_serial_time_2),
                                                   float(_500_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._500_molecules_serial_time_2), float(_500_molecules_10_process_time))],
                        [1000, "{:.2f}/{:.2f}".format(float(self._1000_molecules_serial_time_2), float(_1000_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._1000_molecules_serial_time_2),
                                                   float(_1000_molecules_5_process_time)),
                            "{:2f}/{:.2f}".format(float(self._1000_molecules_serial_time_2), float(_1000_molecules_10_process_time))],
                        [5000, "{:.2f}/{:.2f}".format(float(self._5000_molecules_serial_time_2), float(_5000_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._5000_molecules_serial_time_2),
                                                   float(_5000_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._5000_molecules_serial_time_2), float(_5000_molecules_10_process_time))],
                        [10000, "{:.2f}/{:.2f}".format(float(self._10000_molecules_serial_time_2), float(_10000_molecules_2_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._10000_molecules_serial_time_2),
                                                   float(_10000_molecules_5_process_time)),
                            "{:.2f}/{:.2f}".format(float(self._10000_molecules_serial_time_2), float(_10000_molecules_10_process_time))]],
                       headers=["# mol", "", "# processes", ""])
              )

    @ classmethod
    def tearDownClass(self):
        print('Deleting smiles database files.')
        remove(self.text_fpath)
        if not NO_SPEEDUP_TEST:
            remove(self._100_molecules_fpath)
            remove(self._500_molecules_fpath)
            remove(self._1000_molecules_fpath)
            remove(self._5000_molecules_fpath)
            remove(self._10000_molecules_fpath)
        print(" ~ ~ Multithreading Test Complete ~ ~ ")


if __name__ == '__main__':
    if exists(".no-speedup-test"):
        NO_SPEEDUP_TEST = True
    unittest.main()
"""This module contains methods to find similarities between molecules."""
import numpy as np
from rdkit import DataStructs
from scipy.spatial.distance import cosine as scipy_cosine


class SimilarityMeasure:
    def __init__(self, metric):
        if metric.lower() in ['negative_l0']:
            self.metric = 'negative_l0'
            self.type_ = 'continuous'
            self.to_distance = lambda x: -x

        elif metric.lower() in ['negative_l1', 'negative_manhattan']:
            self.metric = 'negative_l1'
            self.type_ = 'continuous'
            self.to_distance = lambda x: -x

        elif metric.lower() in ['negative_l2', 'negative_euclidean']:
            self.metric = 'negative_l2'
            self.type_ = 'continuous'
            self.to_distance = lambda x: -x

        elif metric.lower() in ['cosine', 'driver-kroeber', 'ochiai']:
            self.metric = 'cosine'
            self.type_ = 'continuous'
            # angular distance
            self.to_distance = lambda x: np.arccos(x) / np.pi

        elif metric.lower() in ['dice', 'sorenson', 'gleason']:
            self.metric = 'dice'
            self.type_ = 'discrete'
            # convert to jaccard for distance
            self.to_distance = lambda x: 1 - x/(2-x)

        elif metric.lower() in ['jaccard', 'tanimoto']:
            self.metric = 'tanimoto'
            self.type_ = 'discrete'
            self.to_distance = lambda x: 1 - x

        elif metric.lower() in ['simple_matching', 'sokal-michener', 'rand']:
            self.metric = 'simple_matching'
            self.type_ = 'discrete'
            self.to_distance = lambda x: 1 - x

        elif metric.lower() in ['rogers-tanimoto']:
            self.metric = 'rogers_tanimoto'
            self.type_ = 'discrete'
            self.to_distance = lambda x: 1 - x
            
        elif metric.lower() in ['russel-rao']:
            self.metric = 'russel_rao'
            self.type_ = 'discrete'
            self.to_distance = lambda x: 1 - x
        
        elif metric.lower() in ['forbes']:
            self.metric = 'forbes'
            self.type_ = 'discrete'
            self.to_distance = lambda x: 1 - x
            
        elif metric.lower() in ['simpson']:
            self.metric = 'simpson'
            self.type_ = 'discrete'

        elif metric.lower() in ['braun-blanquet']:
            self.metric = 'braun_blanquet'
            self.type_ = 'discrete'
            self.to_distance = lambda x: 1 - x
        
        elif metric.lower() in ['baroni-urbani-buser']:
            self.metric = 'baroni_urbani_buser'
            self.type_ = 'discrete'
            self.to_distance = lambda  x: 1 - x
        
        elif metric.lower() in ['kulczynski']:
            self.metric = 'kulczynski'
            self.type_ = 'discrete'
        
        elif metric.lower() in ['sokal-sneath', 'sokal-sneath_1']:
            self.metric = 'sokal_sneath'
            self.type_ = 'discrete'
            self.to_distance = lambda  x: 1 - x

        else:
            raise ValueError(f"Similarity metric: {metric} is not implemented")
        self.normalize_fn = {'shift_': 0., 'scale_': 1.}

    def __call__(self, mol1_descriptor, mol2_descriptor):
        """Compare two descriptors.

        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            similarity_ (float): Similarity value
        """
        similarity_ = None
        if self.metric == 'negative_l0':
            similarity_ = -np.linalg.norm(
                mol1_descriptor.to_numpy() - mol2_descriptor.to_numpy(), ord=0
            )

        elif self.metric == 'negative_l1':
            similarity_ = -np.linalg.norm(
                mol1_descriptor.to_numpy() - mol2_descriptor.to_numpy(), ord=1
            )

        elif self.metric == 'negative_l2':
            similarity_ = -np.linalg.norm(
                mol1_descriptor.to_numpy() - mol2_descriptor.to_numpy(), ord=2
            )
        
        elif self.metric == 'baroni_urbani_buser':
            try:
                similarity_ = self._get_baroni_urbani_buser(mol1_descriptor, 
                                                            mol2_descriptor)
            except ValueError as e:
                raise e

        elif self.metric == 'braun_blanquet':
            try:
                similarity_ = self._get_braun_blanquet(mol1_descriptor, 
                                                       mol2_descriptor)
            except ValueError as e:
                raise e
        
        elif self.metric == "cosine":
            if mol1_descriptor.rdkit_ and mol2_descriptor.rdkit_:
                similarity_ = DataStructs.CosineSimilarity(
                    mol1_descriptor.rdkit_, mol2_descriptor.rdkit_
                )
            else:
                similarity_ = scipy_cosine(
                    mol1_descriptor.to_numpy(), mol2_descriptor.to_numpy()
                )

        elif self.metric == 'dice':
            try:
                similarity_ = DataStructs.DiceSimilarity(
                    mol1_descriptor.to_rdkit(), mol2_descriptor.to_rdkit()
                )
            except ValueError as e:
                raise ValueError(
                    "Dice similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        
        elif self.metric == 'forbes': 
            try:
                similarity_ = self._get_forbes(mol1_descriptor, 
                                               mol2_descriptor)
            except ValueError as e:
                raise e

        elif self.metric == 'kulczynski': 
            try:
                similarity_ = self._get_kulczynski(mol1_descriptor, 
                                                   mol2_descriptor)
            except ValueError as e:
                raise e

        elif self.metric == 'rogers_tanimoto': 
            try:
                similarity_ = self._get_rogers_tanimoto(mol1_descriptor, 
                                                        mol2_descriptor)
            except ValueError as e:
                raise e
        
        elif self.metric == 'russel_rao': 
            try:
                similarity_ = self._get_russel_rao(mol1_descriptor, 
                                                   mol2_descriptor)
            except ValueError as e:
                raise e

        elif self.metric == 'simple_matching': 
            try:
                similarity_ = self._get_simple_matching(mol1_descriptor, 
                                                        mol2_descriptor)
            except ValueError as e:
                raise e
        
        elif self.metric == 'simpson': 
            try:
                similarity_ = self._get_simpson(mol1_descriptor, 
                                                mol2_descriptor)
            except ValueError as e:
                raise e
        
        elif self.metric == 'sokal_sneath': 
            try:
                similarity_ = self._get_sokal_sneath(mol1_descriptor, 
                                                     mol2_descriptor)
            except ValueError as e:
                raise e
                
        elif self.metric == "tanimoto":
            try:
                similarity_ = DataStructs.TanimotoSimilarity(
                    mol1_descriptor.to_rdkit(), mol2_descriptor.to_rdkit()
                )
            except ValueError as e:
                raise e
            except ValueError as e:
                raise ValueError(
                    "Tanimoto similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )

        return similarity_
    
    def _get_baroni_urbani_buser(self, mol1_descriptor, mol2_descriptor):
        """Calculate Baroni-Urbani-Buser similarity between two molecules.
        This is defined for two binary arrays as:
        Baroni-Urbani-Buser similarity = (sqrt(a * d) + a)
                                         / (sqrt(a * d) + a + b + c), where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Baroni-Urbani-Buser similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Baroni-Urbani-Buser similarity is only useful for "
                    "bit strings generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, d = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        p = a + b + c + d
        if d == p:
            return 1.
        similarity_ = (np.sqrt(a * d) 
                       + a) / (np.sqrt(a * d) + a + b + c)
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)
    
    def _get_braun_blanquet(self, mol1_descriptor, mol2_descriptor):
        """Calculate braun-blanquet similarity between two molecules.
        This is defined for two binary arrays as:
        Braun-Blanquet Similarity = a / max{(a + b), (a + c)}, where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Braun-Blanquet similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Braun-Blanquet similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, _ = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        if a == 0:
            return 0.
        similarity_ = a / max((a + b), (a + c))
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)
        
    def _get_forbes(self, mol1_descriptor, mol2_descriptor):
        """Calculate forbes similarity between two molecules.
        This is defined for two binary arrays as:
        Forbes similarity = (p * a) / ((a + b) * (a + c)), where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)

        Note
        ----
        The forbes similarity is normalized to [0, 1]
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Forbes similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Forbes similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, d = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        if (a + b) == 0 or (a + c) == 0 or a == 0:
            return 0.
        p = a + b + c + d
        similarity_ = (p * a) / ((a + b) * (a + c))
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = p / a
        return self._normalize(similarity_)
    
    def _get_kulczynski(self, mol1_descriptor, mol2_descriptor):
        """Calculate kulczynski similarity between two molecules.
        This is defined for two binary arrays as:
        kulczynski similarity = 0.5 * a / ((a + b) + (a + c)), where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): kulczynski similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Kulczynski similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, _ = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        if a == 0:
            return 0.
        similarity_ = 0.5 * a / ((a + b) + (a + c))
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = p / a
        return self._normalize(similarity_)

    
    def _get_rogers_tanimoto(self, mol1_descriptor, mol2_descriptor):
        """Calculate rogers-tanimoto similarity between two molecules.
        This is defined for two binary arrays as:
        Rogers-Tanimoto = (a + d) / (p + b + c), where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Simple Matching similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Rogers-Tanimoto similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, d = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        p = a + b + c + d
        similarity_ = (a + d) / (p + b + c)
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)
    
    def _get_russel_rao(self, mol1_descriptor, mol2_descriptor):
        """Calculate russel-rao similarity between two molecules.
        This is defined for two binary arrays as:
        Russel-Rao = a / p, where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Simple Matching similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Russel-Rao similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, d = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        p = a + b + c + d
        similarity_ = a / p
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)

    def _get_simple_matching(self, mol1_descriptor, mol2_descriptor):
        """Calculate simple matching similarity between two molecules.
        This is defined for two binary arrays as:
        Simple Matching = (a + d) / p, where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Simple Matching similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Simple Matching similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, d = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        p = a + b + c + d
        similarity_ = (a + d) / p
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)
    
    def _get_simpson(self, mol1_descriptor, mol2_descriptor):
        """Calculate simpson similarity between two molecules.
        This is defined for two binary arrays as:
        Simpson Similarity = a / min{(a + b), (a + c)}, where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)

        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Simpson similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Simpson similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, _ = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        if (a + b) == 0 or (a + c) == 0 or a == 0:
            return 0.
        similarity_ = a / min((a + b), (a + c))
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)
    
    def _get_sokal_sneath(self, mol1_descriptor, mol2_descriptor):
        """Calculate Sokal-Sneath similarity between two molecules.
        This is defined for two binary arrays as:
        Sokal-Sneath similarity = a / (a + 2*b + 2*c) where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)

        Args:
            mol1_descriptor (molSim.ops Descriptor)
            mol2_descriptor (molSim.ops Descriptor)

        Returns:
            (float): Sokal-Sneath similarity value
        """
        if not(mol1_descriptor.is_fingerprint() 
               and mol2_descriptor.is_fingerprint()):
            raise ValueError(
                    "Sokal-Sneath similarity is only useful for bit strings "
                    "generated from fingerprints. Consider using "
                    "other similarity measures for arbitrary vectors."
                )
        a, b, c, _ = self._get_abcd(mol1_descriptor.to_numpy(), 
                                    mol2_descriptor.to_numpy())
        if a == 0:
            return 0.
        similarity_ = a / (a + 2*b + 2*c)
        self.normalize_fn["shift_"] = 0.
        self.normalize_fn["scale_"] = 1.
        return self._normalize(similarity_)
        
    def _get_abcd(self, arr1, arr2):
        """ Get a, b, c, d, where:
        a = bits(array 1) and bits(array 2)
        b = bits(array 1) and bits(~array 2)
        c = bits(~array 1) and bits(array 2)
        d = bits(~array 1) amd bits(~array 2)   // "~": complement operator
        p = a + b + c + d = bits(array 1 or array 2)
        
        Args:
            arr1 (np.ndarray)
            arr2 (np.ndarray)

        Returns:
            (tuple): (a, b, c, d)
        """

        def _to_equal_length(arr1, arr2):
            out_arr = (np.array(arr1), np.array(arr2))
            max_length = max(arr1.shape, arr2.shape)
            for arr_id, arr in enumerate(out_arr):
                out_arr[arr_id] =  np.pad(arr, 
                                          (0, max_length - arr.size), 
                                          mode='constant')
            return out_arr

        arr1, arr2 = _to_equal_length(arr1, arr2)
        not_arr1 = np.invert(arr1)
        not_arr2 = np.invert(arr2)
        a = np.sum(arr1 & arr2)
        b = np.sum(arr1 & not_arr2)
        c = np.sum(not_arr1 & arr2)
        d = np.sum(not_arr1 & not_arr2)
        assert (a + b + c + d) == arr1.size == arr2.size
        return a, b, c, d
    
    def _normalize(self, similarity_):
        return (similarity_ 
                + self.normalize_fn['shift_']) / self.normalize_fn['scale_']
    
    def is_distance_metric(self):
        """Check if the similarity measure is a distance metric.
        
        Returns:
            bool: True if it is a distance metric.
        """
        return hasattr(self, 'to_distance')

    @staticmethod
    def get_supported_metrics():
        """Return a list of strings for the currently implemented
        similarity measures, aka metrics.

        Returns:
            List: List of strings.
        """
        return [
            'negative_l0',
            'negative_l1',
            'negative_manhattan',
            'negative_l2',
            'negative_euclidean',
            'dice',
            'sorenson',
            'gleason',
            'jaccard',
            'tanimoto',
            "cosine",
            'driver-kroeber', 
            'ochiai'
            "simple_matching", 
            "sokal-michener", 
            "rand",
            "rogers-tanimoto",
            "russel-rao",
            'forbes',
            'simpson',
            'braun-blanquet',
            'baroni-urbani-buser',
            'kulczynski',
            'sokal-sneath',

        ]

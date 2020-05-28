import numpy as np 
class Searcher:
    def __init__(self, index):
        self.index = index
    def chi2_distance(self,histA, histB, eps = 1e-10):
        d = 0.5*np.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(histA, histB)])
        return d 
    def search(self, queryFeatures):
        results = {}
        for k,feature in self.index.items():
            d = self.chi2_distance(feature,queryFeatures)
            results[k] = d 
        results = sorted([(v,k) for k,v in results.items()])
        return results
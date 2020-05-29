import numpy as np
import cv2

class ConverMatcher:
    def __init__(self,descriptor, coverPaths):
        self.descriptor = descriptor
        self.coverPaths = coverPaths

    def search(self, queryKps, queryDescs):
        results = {}
        for coverPath in self.coverPaths:
            cover = cv2.imread(coverPath)
            gray = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)
            (kps, descs) = self.descriptor.describe(gray)
            score = self.match(queryKps,queryDescs,kps,descs)
            results[coverPath] = score
        if len(results) >0:
            results = sorted([(v,k) for (k,v) in results.items() if v >0], reverse=True)

        return  results

    def match(self,kpsA, featuresA, kpsB, featuresB, ratio = 0.7, minMatches = 50):
        matcher = cv2.DescriptorMatcher_create("BruteForce")
        rawMatches = matcher.knnMatch(featuresB, featuresA, 2)
        matches = []
        for m in rawMatches:
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))
            if len(matches) > minMatches:
                ptsA = np.float32([kpsA[i] for (i, _) in matches])
                ptsB = np.float32([kpsB[j] for (_, j) in matches])
                (_, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, 4.0)
                return float(status.sum())/status.size
        return -1.0

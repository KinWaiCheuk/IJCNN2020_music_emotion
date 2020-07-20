import random
import numpy as np
from itertools import permutations,combinations

def generate_triplet_R(x,y, positive_range, negative_range, testsize=0.3,ap_pairs=10,an_pairs=10):
    data_xy = tuple([x,y])

    trainsize = 1-testsize

    triplet_train_pairs = []
    triplet_test_pairs = []
    for label in data_xy[1]:

        same_class_idx = np.where((np.logical_and(label-positive_range<=y, y<=label+positive_range)))[0]
#         print('same_class_idx = ', same_class_idx)
        diff_class_idx = np.where(np.logical_or(label-negative_range>=y, y>=label+negative_range))[0]       
#         print('diff_class_idx = ', diff_class_idx)
        if same_class_idx.shape[0] <= 15:
            same_class_sampleer_idx = list(same_class_idx)
            try:
                A_P_pairs = (list(combinations(same_class_idx,2))) #Generating Anchor-Positive pairs
            except:
                print('Not enough sample on class {}, please change the positive condition'.format(label))
        else:
            same_class_sampleer_idx = random.choice(range(len(same_class_idx)-15))
            A_P_pairs = random.sample(list(combinations(same_class_idx[same_class_sampleer_idx:same_class_sampleer_idx+15],2)),k=ap_pairs) #Generating Anchor-Positive pairs
        if diff_class_idx.shape[0] <= 15:        
            Neg_idx = (list(diff_class_idx))
        else:
            Neg_idx = random.sample(list(diff_class_idx),k=an_pairs)
        

        #train
        A_P_len = len(A_P_pairs)
        Neg_len = len(Neg_idx)
        for ap in A_P_pairs[:int(A_P_len*trainsize)]:
            Anchor = data_xy[0][ap[0]]
            Positive = data_xy[0][ap[1]]
            for n in Neg_idx:
                Negative = data_xy[0][n]
                triplet_train_pairs.append([Anchor,Positive,Negative])               
        #test
        for ap in A_P_pairs[int(A_P_len*trainsize):]:
            Anchor = data_xy[0][ap[0]]
            Positive = data_xy[0][ap[1]]
            for n in Neg_idx:
                Negative = data_xy[0][n]
                triplet_test_pairs.append([Anchor,Positive,Negative])    
                
    return np.array(triplet_train_pairs), np.array(triplet_test_pairs)
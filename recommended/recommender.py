import numpy as np

class RecommenderEngine():
    
    def __init__(self, similarity_path):
        '''create recommender object
            similarity path = path to .npy similarity matrix'''
        self.similarity = np.load(similarity_path)
        print("Similarity matrix of", self.similarity.shape, "loaded")
        
    def recommend(self, in_mov, n=5, ratings=None):
        #similarity of all m in M to I := S
        #in_mov = #[23076, 911] #= interstellar, space odyssey
        
        S = np.zeros(self.similarity.shape[0])

        BETA = 0.5
        def movie_rating(idx):
                if ratings != None:
                    rat = ratings[idx]
                    if rat > 0:
                        return rat
                return 0
                    
        for m in range(len(self.similarity)):
            s = 0 #total sim to movies
            for i in in_mov:  #stupid, just half is enough
                if m != i:
                    s += self.similarity[m,i] + movie_rating(m) * BETA
            S[m] = s
            
        # #now argsort again and find several best ones
        print("max score:", np.max(S), " for id:", np.argmax(S))
        sort = np.argsort(S)
        
        return np.flip(sort[-n:])
class TrieNode:
    def __init__(self):
        self.children=[None]*26

        #isEndOfWord is True if node represents the end of word
        self.isEndOfWord=False

class Trie:
    def __init__(self):
        self.root=self.getNode()

    #function returns new trie node(initialized to NULLs)
    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        #private helper function
        #converts key current  chracter into index
        #use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')

    def insert(self,key):
        #if not present, inserts key into trie
        #if the key is prefix of trie node,
        #then marks leaf node
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])

            #if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index]=self.getNode()
            pCrawl=pCrawl.children[index]
            

        #mark last node as leaf
        pCrawl.isEndOfWord=True

    def search(self,key):
        #search key in the trie
        #returns true if key is present
        #else false
        pCrawl=self.root
        length=len(key)
        for level in range(length):
            index=self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl=pCrawl.children[index]
        return pCrawl!=None and pCrawl.isEndOfWord

keys=["the","a","three","anaswe","any","by","their"]
output=["Not present in trie","Present in trie"]

#Trie object
t=Trie()
#construct trie
for key in keys:
    t.insert(key)

#search for different keys
print("{} ---- {}".format("the",output[t.search("the")])) 
print("{} ---- {}".format("these",output[t.search("these")])) 
print("{} ---- {}".format("their",output[t.search("their")])) 
print("{} ---- {}".format("thaw",output[t.search("thaw")]))

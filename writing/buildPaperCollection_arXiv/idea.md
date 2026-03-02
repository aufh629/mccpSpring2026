arXiv has an API allowing free access to papers 
we take advantage of this tech and build a collection of papers 
the starting point is a url of one paper 
then the AI agent would fetch that paper and download it to local folder as paper1.html 
then the agent would go through all the papers cited in paper1 and search them in arXiv and place them into refPaper1 folder; then for each paper in refPaper1folder, we do the same - create one folder for the paper and fetch cited papers into the folder; we do this recursively until we reach N paper (N could be set as 500 or any other number)

another way to manage the size of corpus is to set up a filter 

we create a file filter.md and in this doc, describe the papers we are interested in; then we ask AI agent to check each paper against filter.md and only download those that can pass the filer 

this way we should be able to quickly build a corpus of papers on topics of our interest 

if a paper is not from arXiv, we can still search for the title in arXiv and find preprint version 
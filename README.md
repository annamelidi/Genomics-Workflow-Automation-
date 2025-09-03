# Genomics-Workflow-Automation-

Gene expression data analysis and also finally geting familiar with Docker without going too crazy. The project ended up being 
a little workflow that goes from downloading public datasets all the way to some basic stats and visuals.

*What I did:*
**Grabbed data from GEO**:
Pulled gene expression datasets straight from NCBI GEO. No messing around with weird file formats or downloading manually. More reproducable.

**Cleaned & normalized** it: 
Got the raw expression values into a standard format, so all genes were on the same playing field. Otherwise, some super-expressed genes would totally overshadow everything else.

Ran some basic stats:
Looked at the usual stuff — which genes are expressed the most, variability across samples, averages, medians… nothing fancy, but helps you “know your data.”
Made some visuals:
Barplots, heatmaps, whatever helps to quickly spot which genes are standing out.

Wrapped it all in Docker: Finally got a chance to play with Docker! Made everything containerized so I can run it anywhere without pulling my hair out over missing libraries. Reproducibility >>.

To built the Docker image:
docker build -t geo_workflow .


To run the workflow inside a container:
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/figures:/app/figures geo_workflow

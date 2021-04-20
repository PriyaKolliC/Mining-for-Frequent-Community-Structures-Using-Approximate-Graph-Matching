### Mining-for-Frequent-Community-Structures-Using-Approximate-Graph-Matching
#### This project aims at identifying Frequent Patterns in large graph Datasets.
#### Most of the work in the domain is focused on finding patterns that match exactly. 
#### A novel approach is proposed in this project to help determine the frequent patterns that approximately match with each other. 
#### This approach finds significant applications in the field of deanonymizing social networks, finding approximately matching molecules in protein networks and brain image data.

The algorithms works in three phases as shown below:

<img src="https://drive.google.com/uc?export=view&id=1sSDOCDaWGq4g7q4Gm1laO7wipAusrOPe" data-canonical-src="https://drive.google.com/uc?export=view&id=1sSDOCDaWGq4g7q4Gm1laO7wipAusrOPe" width="600" height="auto" />

Consider the dataset shown below:

<img src="https://drive.google.com/uc?export=view&id=1m02Ek4liJJlhHozJdwUJaIWQwSgpFveV" data-canonical-src="https://drive.google.com/uc?export=view&id=1m02Ek4liJJlhHozJdwUJaIWQwSgpFveV" width="600" height="auto" />

Phase 1: Below are the candidates generated for the dataset shown above at different time steps of by implementing Random Walks and Markovian Clustering


<img src="https://drive.google.com/uc?export=view&id=1n9nOmn6gbTM6Io6PnDC7J40HpbAupVWF" data-canonical-src="https://drive.google.com/uc?export=view&id=1n9nOmn6gbTM6Io6PnDC7J40HpbAupVWF" width="500" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1fAwTER2fhXkfltrmEHuK32Q06o8x_amf" data-canonical-src="https://drive.google.com/uc?export=view&id=1fAwTER2fhXkfltrmEHuK32Q06o8x_amf" width="500" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1vn29C0Ps73Scz0wrxMqu-f4e0icVDmds" data-canonical-src="https://drive.google.com/uc?export=view&id=1vn29C0Ps73Scz0wrxMqu-f4e0icVDmds" width="500" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1WEFZ_y6mqB9Vr16yUf5fcTgPJeYLfli5" data-canonical-src="https://drive.google.com/uc?export=view&id=1WEFZ_y6mqB9Vr16yUf5fcTgPJeYLfli5" width="600" height="auto" />

Phase 2: Phase 2 aims at filtering out the duplicate communitites and generates unique communities for a given dataset. The result generated by Phase 2 of the algorithm is as shown below:

<img src="https://drive.google.com/uc?export=view&id=1bpEWANU0MWVBxlW-JBGz6BikRIeJiQD1" data-canonical-src="https://drive.google.com/uc?export=view&id=1bpEWANU0MWVBxlW-JBGz6BikRIeJiQD1" width="800" height="auto" />

The signature to each community/cluster in the above table shows the "probability print" of ending up in each node of the cluster given you start at any node. This signature thus helps capture the structure of each cluster and is further used to compare the corresponding communities/subgraphs for matching.

Phase 3: This phase of the algorithm focuses on comparing the communities generated at phase 2 and determining the extent of matching between them.

<img src="https://drive.google.com/uc?export=view&id=1q5sQt0YNG7-pGVubMbbzbFEFT5wKFzZK" data-canonical-src="https://drive.google.com/uc?export=view&id=1q5sQt0YNG7-pGVubMbbzbFEFT5wKFzZK" width="800" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1O14QssktzkiAHrasY4R9ffU0t0eL0s_e" data-canonical-src="https://drive.google.com/uc?export=view&id=1O14QssktzkiAHrasY4R9ffU0t0eL0s_e" width="800" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1CUT-mdokAL4eMzDiAj8hp9y1vVFCgrzo" data-canonical-src="https://drive.google.com/uc?export=view&id=1CUT-mdokAL4eMzDiAj8hp9y1vVFCgrzo" width="800" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1a1_GeKT2qbhKBbfiyt5W9Qd1NTWIjf_F" data-canonical-src="https://drive.google.com/uc?export=view&id=1a1_GeKT2qbhKBbfiyt5W9Qd1NTWIjf_F" width="800" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1Q_q1S1fqf441bN809Z5i-bkSLRsctJ_z" data-canonical-src="https://drive.google.com/uc?export=view&id=1Q_q1S1fqf441bN809Z5i-bkSLRsctJ_z" width="800" height="auto" />

<img src="https://drive.google.com/uc?export=view&id=1pujBlKL2MFYbFEmXGJ91hINPcBnpyz5J" data-canonical-src="https://drive.google.com/uc?export=view&id=1pujBlKL2MFYbFEmXGJ91hINPcBnpyz5J" width="800" height="auto" />

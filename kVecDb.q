// TODO: try with haystack/langchain
// TODO: optimize data structure, cluster similar? nsw?
// vecs
.kvecdb.DB: ();
// vecs' data
.kvecdb.DATA: ();
// tags
.kvecdb.TAGS: ();

.kvecdb.put: {
    .kvecdb.DATA ,: enlist x;
    .kvecdb.DB ,: enlist y;
    .kvecdb.TAGS ,: enlist z;
    };

.kvecdb.find: {
    sims: .kvecdb.cosim[x] peach .kvecdb.DB;
    idxs: idesc sims;
    res: flip `data`sim!((.kvecdb.DATA idxs); sims idxs);
    :res
    };

.kvecdb.ann_find: {
    // TODO: implement an ANN vector search
    };

.kvecdb.cosim: {
    xy: .kvecdb.dot[x;y];
    xx: .kvecdb.dot[x;x];
    yy: .kvecdb.dot[y;y];

    res: xy % sqrt[xx] * sqrt[yy];
    :res
    };

.kvecdb.dot: {
    mmu[x; y]
    };

.kvecdb.reset: {
    .kvecdb.DB: ();
    .kvecdb.DATA: (); 
    .kvecdb.TAGS: ();
    };

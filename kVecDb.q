// vecs
DB: ();
// vecs' data
DATA: ();

put: {
    DATA ,: enlist x;
    DB ,: enlist y;
    };

find: {
    sims: cosim[x] peach DB;
    idxs: idesc sims;
    res: flip `data`sim!((DATA idxs); sims idxs);
    :res
    };

cosim: {
    xy: dot[x;y];
    xx: dot[x;x];
    yy: dot[y;y];

    res: xy % sqrt[xx] * sqrt[yy];
    :res
    };

dot: {mmu[x; y]};

reset: {
    DB: ();
    DATA: (); 
    };

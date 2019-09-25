def pair(fst_val):
    return lambda snd_val: {"_fst_key": fst_val, "_snd_key": snd_val}


def fst(pair_inst):
    return pair_inst["_fst_key"]


def snd(pair_inst):
    return pair_inst["_snd_key"]

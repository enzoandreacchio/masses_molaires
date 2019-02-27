def arrondir(nb_float, nb_dec):
	nb_float = float(nb_float)
	nb_dec = int(nb_dec)
	nb_float = str(nb_float)
	nb_float = nb_float.split(".")
	part_ent = nb_float[0]
	part_dec = nb_float[1]
	
	if len(part_dec) < nb_dec:
		while len(part_dec) < nb_dec:
			part_dec += "0"
	else:
		part_dec = nb_float[1][:nb_dec]
	nb_arrondi = part_ent + "." + part_dec
	return nb_arrondi
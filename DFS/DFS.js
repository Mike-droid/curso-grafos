const dfs = function (raiz, objetivo) {
	if (raiz === null) {
		return null;
	}
	if (raiz.valor === objetivo) {
		return raiz;
	}
	for (let hijo of raiz.hijos) {
		const resultado = dfs(hijo, objetivo);
		if (resultado !== null) {
			return resultado;
		}
	}
	return null;
};

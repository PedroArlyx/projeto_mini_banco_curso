import DAO

# Chamada de metodos - Executar um comando por VEZ

# Teste de inserção
DAO.inserir_usuario('Rafael', 'Rafael@teste.com', )
DAO.inserir_usuario('pedro', 'pedro@teste.com', )
DAO.inserir_usuario('José', 'jose@teste.com', )

# Teste de consulta
#saida = DAO.buscar_usuario('Natan')
#print(saida)

# Teste de listar todos
#saida = DAO.listar_usuarios()
#print(saida)

# Teste de atualização
saida = DAO.atualizar_usuario(2,'amanda2','amanda2@teste.com')
print(saida)

# Teste de remoção
#saida = DAO.deletar_usuario(2)=
#print(saida)
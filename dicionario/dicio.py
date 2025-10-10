def print_info_medico(medico_dict):
    print("="*20)
    print(f"Dados do medico: {medico_dict['nome']}")
    print(f"Especialidade: {medico_dict['especialidade']}")
    print(f"Hospitais:")
    for hospital in medico_dict['hospitais']:
        print(f"    Hospital: {hospital}")

d = {especialidade:[medicos]}

def get_medicos_por_especialidade(medicos_dict):
    d = {}
    for medico in medicos:
        nome = medico['nome']
        especialidade = medico['especialidade']
        if d.get(especialidade) ==None:
            d[especialidade] = []
        d[especialidade].append(nome)
    return d

gerar um dicionario {hospital->[nomes]}
gerar um dicionario {hospital -> [{nome,especilidade}]}
medicos = [
    {
        "nome": "Dr. João Silva",
        "especialidade": "Cardiologia",
        "hospitais": ["Hospital Central", "Clínica Coração Saudável"]
    },
    {
        "nome": "Dra. Maria Oliveira",
        "especialidade": "Ortopedia",
        "hospitais": ["Hospital Ortopédico", "Hospital das Clínicas"]
    },
    {
        "nome": "Dr. Pedro Santos",
        "especialidade": "Neurologia",
        "hospitais": ["Hospital Neurológico", "Hospital Central"]
    },
    {
        "nome": "Dra. Ana Costa",
        "especialidade": "Pediatria",
        "hospitais": ["Hospital Infantil", "Clínica São Lucas"]
    },
    {
        "nome": "Dr. Ricardo Lima",
        "especialidade": "Dermatologia",
        "hospitais": ["Clínica da Pele", "Hospital Universitário"]
    },
    {
        "nome": "Dra. Fernanda Rocha",
        "especialidade": "Cardiologia",
        "hospitais": ["Hospital Central", "Hospital Universitário"]
    },
    {
        "nome": "Dr. Marcos Pereira",
        "especialidade": "Ortopedia",
        "hospitais": ["Hospital Ortopédico", "Hospital Central"]
    },
    {
        "nome": "Dra. Carolina Mendes",
        "especialidade": "Pediatria",
        "hospitais": ["Hospital Infantil", "Hospital das Clínicas"]
    },
    {
        "nome": "Dr. Rafael Souza",
        "especialidade": "Neurologia",
        "hospitais": ["Hospital Neurológico", "Clínica São Lucas"]
    },
    {
        "nome": "Dra. Beatriz Almeida",
        "especialidade": "Dermatologia",
        "hospitais": ["Clínica da Pele", "Hospital das Clínicas"]
    }
]

def agrupa_medico_hospital(medicos_list):
    agrupamento = {}
    for medico in medicos_list:
        nome = medico['nome']
        for hospital in medico['hospitais']:
            if agrupamento.get(hospital)==None:
                agrupamento[hospital] = []
                

            agrupamento[hospital].append({"nome": nome,"especialidade": medico['especialidade']})
    return agrupamento

def mostra_agrupamento(agrumento):
    with open("relatorio.txt","w+") as f:

        for hospital, medicos in agrumento.items():
            f.write(f"Hospital:  {hospital}\n")
            f.write("Medicos\n")
            for medico in medicos:
                f.write(f" Nome: {medico['nome']}\n")
                f.write(f" Especialidade: {medico['especialidade']}\n")
                f.write('#'*50)
                f.write("\n")
            f.write("="*50)
            f.write("\n")

agrupamento = agrupa_medico_hospital(medicos)
mostra_agrupamento(agrupamento)

   
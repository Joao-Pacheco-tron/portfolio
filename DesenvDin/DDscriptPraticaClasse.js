class Funcionario {
    constructor(nome, idade, cargo) {
        this.nome = nome;
        this.idade = idade;
        this.cargo = cargo;
    }

    seApresentar() {
        console.log(`Olá, meu nome é ${this.nome}, tenho ${this.idade} anos e sou ${this.cargo}.`);
    }

    trabalhar() {
        console.log(`${this.nome} está trabalhando como ${this.cargo}.`);
    }
}

class Gerente extends Funcionario {
    constructor(nome, idade, cargo, departamento) {
        super(nome, idade, cargo);
        this.departamento = departamento;
    }

    gerenciar() {
        console.log(`${this.nome} está gerenciando o departamento de ${this.departamento}.`);
    }
}

class Desenvolvedor extends Funcionario {
    constructor(nome, idade, cargo, linguagem) {
        super(nome, idade, cargo); 
        this.linguagem = linguagem;
    }

    programar() {
        console.log(`${this.nome} está programando em ${this.linguagem}.`);
    }
}

// Ex_Ger
const gerente = new Gerente("Carlos", 45, "Gerente", "Vendas");
gerente.seApresentar();
gerente.trabalhar();
gerente.gerenciar();

// Ex_Dev
const desenvolvedor = new Desenvolvedor("Maria", 21, "Desenvolvedora", "JavaScript");
desenvolvedor.seApresentar();
desenvolvedor.trabalhar();
desenvolvedor.programar();
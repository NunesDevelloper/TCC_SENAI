CREATE DATABASE IF NOT EXISTS `sge`;
USE `sge` ;

-- -----------------------------------------------------
-- Table cliente
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(225) NOT NULL,
  `email` VARCHAR(225) NOT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table mesa
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`mesa` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numero` INT NOT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table funcionario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`funcionario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(120) NOT NULL,
  `login` VARCHAR(255) NOT NULL,
  `senha` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table turno
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`turno` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cargo` ENUM("atendente", "cozinheiro", "entregadore", "gerente") NOT NULL,
  `dt_inicio` DATETIME NOT NULL DEFAULT now(),
  `dt_final` DATETIME NULL,
  `funcionario_id` INT NOT NULL,
  PRIMARY KEY (`id`, `funcionario_id`),
  CONSTRAINT `fk_turno_funcionario`
    FOREIGN KEY (`funcionario_id`)
    REFERENCES `sge`.`funcionario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table produto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`produto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `categoria` ENUM("lanche", "bebida", "porcoe", "sobremesa") NOT NULL,
  `nome` VARCHAR(255) NOT NULL,
  `preco` DECIMAL(10,2) NOT NULL,
  `desc` TEXT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table combo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`combo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `preco` DECIMAL(10,2) NOT NULL,
  `desc` TEXT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table cupom_desconto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`cupom_desconto` (
  `id` INT NOT NULL,
  `codigo` VARCHAR(255) NOT NULL,
  `percentual_desconto` DECIMAL(10,2) NOT NULL,
  `dt_valida` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table estoque
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`estoque` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `intem_nome` VARCHAR(225) NOT NULL,
  `preco_uni` DECIMAL(10,2) NOT NULL,
  `quantidade` VARCHAR(225) NOT NULL,
  `unidade_medida` ENUM("Kg", "L", "Uni") NOT NULL DEFAULT 'Uni',
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table fornecidor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`fornecidor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cnpj` VARCHAR(100) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `contado` TEXT NOT NULL,
  PRIMARY KEY (`id`),
);

-- -----------------------------------------------------
-- Table estoque_fornecidor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`estoque_fornecidor` (
  `estoque_id` INT NOT NULL,
  `fornecidor_id` INT NOT NULL,
  PRIMARY KEY (`estoque_id`, `fornecidor_id`),
  CONSTRAINT `fk_estoque_has_fornecidor_estoque1`
    FOREIGN KEY (`estoque_id`)
    REFERENCES `sge`.`estoque` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_estoque_has_fornecidor_fornecidor1`
    FOREIGN KEY (`fornecidor_id`)
    REFERENCES `sge`.`fornecidor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table carrinho
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`carrinho` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `is_delivre` TINYINT NOT NULL DEFAULT 0,
  `is_retirada` TINYINT NOT NULL DEFAULT 0,
  `metedo_pagamento` ENUM("dinheiro", "pix", "credito", "debito") NOT NULL DEFAULT 'pix',
  `cliente_id` INT NOT NULL,
  `funcionario_id` INT NOT NULL,
  `mesa_id` INT NULL,
  `cupom_desconto_id` INT NULL,
  PRIMARY KEY (`id`, `cliente_id`, `funcionario_id`, `mesa_id`, `cupom_desconto_id`),
  CONSTRAINT `fk_carrinho_cupom_desconto1`
    FOREIGN KEY (`cupom_desconto_id`)
    REFERENCES `sge`.`cupom_desconto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carrinho_Cliente1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `sge`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carrinho_mesa1`
    FOREIGN KEY (`mesa_id`)
    REFERENCES `sge`.`mesa` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carrinho_funcionario1`
    FOREIGN KEY (`funcionario_id`)
    REFERENCES `sge`.`funcionario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table carrinho_produto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`carrinho_produto` (
  `carrinho_id` INT NOT NULL,
  `produto_id` INT NOT NULL,
  `combo_id` INT NOT NULL,
  PRIMARY KEY (`carrinho_id`, `produto_id`, `combo_id`),
  CONSTRAINT `fk_carrinho_has_produto_carrinho1`
    FOREIGN KEY (`carrinho_id`)
    REFERENCES `sge`.`carrinho` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carrinho_has_produto_produto1`
    FOREIGN KEY (`produto_id`)
    REFERENCES `sge`.`produto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_carrinho_produto_combo1`
    FOREIGN KEY (`combo_id`)
    REFERENCES `sge`.`combo` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table estoque_produto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`estoque_produto` (
  `produto_id` INT NOT NULL,
  `estoque_id` INT NOT NULL,
  PRIMARY KEY (`produto_id`, `estoque_id`),
  INDEX `fk_produto_has_estoque_estoque1_idx` (`estoque_id` ASC) VISIBLE,
  INDEX `fk_produto_has_estoque_produto1_idx` (`produto_id` ASC) VISIBLE,
  CONSTRAINT `fk_produto_has_estoque_produto1`
    FOREIGN KEY (`produto_id`)
    REFERENCES `sge`.`produto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_produto_has_estoque_estoque1`
    FOREIGN KEY (`estoque_id`)
    REFERENCES `sge`.`estoque` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table historico_pedidos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`historico_pedidos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `carrinho_id` INT NOT NULL,
  `status` ENUM("pago", "preparo", "pronto", "entregue", "cancelado") NOT NULL DEFAULT 'preparo',
  PRIMARY KEY (`id`, `carrinho_id`),
  CONSTRAINT `fk_status_carrinho1`
    FOREIGN KEY (`carrinho_id`)
    REFERENCES `sge`.`carrinho` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table delivre
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`delivre` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table delivre_carrinho
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`delivre_carrinho` (
  `delivre_id` INT NOT NULL,
  `carrinho_id` INT NOT NULL,
  PRIMARY KEY (`delivre_id`, `carrinho_id`),
  CONSTRAINT `fk_delivre_has_carrinho_delivre1`
    FOREIGN KEY (`delivre_id`)
    REFERENCES `sge`.`delivre` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_delivre_has_carrinho_carrinho1`
    FOREIGN KEY (`carrinho_id`)
    REFERENCES `sge`.`carrinho` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- -----------------------------------------------------
-- Table endereco
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`endereco` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `logradouro` VARCHAR(125) NOT NULL,
  `numero` INT NULL,
  `complemento` TEXT NULL,
  `bairro` VARCHAR(120) NOT NULL,
  `cep` VARCHAR(120) NOT NULL,
  PRIMARY KEY (`id`)
);

-- -----------------------------------------------------
-- Table cliente_endereco
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sge`.`cliente_endereco` (
  `cliente_id` INT NOT NULL,
  `endereco_id` INT NOT NULL,
  PRIMARY KEY (`cliente_id`, `endereco_id`),
  CONSTRAINT `fk_cliente_has_endereco_cliente1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `sge`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cliente_has_endereco_endereco1`
    FOREIGN KEY (`endereco_id`)
    REFERENCES `sge`.`endereco` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);



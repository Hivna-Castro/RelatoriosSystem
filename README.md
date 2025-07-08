# Padrões de Projeto - Prática 2

**Disciplina:** Qualidade de Software  
**Professor:** Anderson Gonçalves Uchôa  

---

## Projeto: Sistema de Montagem e Transmissão de Relatórios Empresariais

---

## Objetivo da Atividade

Esta atividade tem como objetivo exercitar o uso de padrões de projeto estruturais para compor sistemas com partes complexas e interfaces bem definidas. Foram utilizados os seguintes padrões:

- **Builder:** Montagem passo a passo de relatórios com diferentes seções.
- **Facade:** Interface simplificada para gerar, formatar e transmitir relatórios.
- **Proxy:** Controle de acesso e transmissão segura de relatórios via rede ou sistema de arquivos.

---

## Contexto do Problema

Imagine que você faz parte de uma equipe de engenharia de software responsável por automatizar o processo de criação e envio de relatórios corporativos em uma grande organização. Cada setor (vendas, logística, RH, TI) precisa gerar relatórios periódicos com informações específicas, formatadas conforme o público-alvo.

Os relatórios variam em estrutura e conteúdo conforme o perfil do destinatário: um executivo sênior precisa de um sumário executivo com gráficos e recomendações estratégicas, enquanto um analista operacional pode precisar de dados detalhados em tabelas. O sistema atual é manual e propenso a erros, envolvendo várias planilhas e documentos soltos, o que causa atrasos e inconsistências.

O desafio é criar um sistema modular, seguro e extensível, aproveitando padrões de projeto para garantir clareza, manutenibilidade e escalabilidade. Os relatórios podem conter diferentes seções e precisam ser entregues em formatos variados (PDF, HTML, texto simples). Por questões de segurança, apenas usuários autenticados podem acessar os relatórios. O sistema também deve ser fácil de usar para gerentes não técnicos.

---
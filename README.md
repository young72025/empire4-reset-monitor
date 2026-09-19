# EMPIRE4 — Monitor de Resets

Painel web que acompanha automaticamente os **Resets da Guild EMPIRE4** no MUCABRASIL.

Fonte:
https://www.mucabrasil.com.br/?go=guild&n=EMPIRE4

## Como funciona

1. O GitHub Actions consulta a página do MUCABRASIL.
2. O script identifica o campo `Resets`.
3. O valor é salvo em `data/resets.json`.
4. O GitHub Pages exibe o valor e atualiza o navegador automaticamente.
5. O workflow roda a cada 5 minutos e também pode ser executado manualmente.

> Observação: o agendamento do GitHub Actions não é garantia de atualização segundo a segundo. Para monitoramento contínuo, a página pode atualizar a interface a cada 30 segundos, enquanto o GitHub Actions busca um novo valor periodicamente.

## Ativar

1. Crie um repositório no GitHub.
2. Envie todos os arquivos deste projeto.
3. Em **Settings → Pages**, escolha **GitHub Actions** como fonte.
4. Em **Actions**, execute `Atualizar Resets EMPIRE4` manualmente na primeira vez.
5. A página será publicada pelo GitHub Pages.

## Personalização

O arquivo `data/resets.json` é atualizado automaticamente pelo workflow. Não edite esse arquivo manualmente depois que o monitor estiver ativo.

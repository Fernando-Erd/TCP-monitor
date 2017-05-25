Entrega: Todos os trabalhos serão acessados terça-feira dia 6 de junho de 2017; não serão aceitos trabalhos disponibilizados após esta data. Atenção, são quase 4 semanas de prazo, organize-se!

Os alunos devem informar por e-mail a URL do trabalho, usando o subject "TP REDES II 2017-1"

O trabalho deve obrigatoriamente ser feito em dupla; o código, os testes e o relatório devem ser feitos por ambos os membros da dupla. Use esta oportunidade para melhorar sua habilidade de trabalhar em equipe.

Descrição do Trabalho

Você vai implementar um sistema de N peers TCP que se monitoram e elegem um líder entre eles. Os peers estabelecem conexão entre eles -- o sistema deve ser executado com no mínimo N=3, idealmente N=4 peers. Cada peer tem um identificador no sistema, que inicia em 0 e vai até N-1.
De tempos em tempos cada peer envia uma mensagem aos demais, informando que está executando corretamente. Esta mensagem é chamada de heartbeat. O líder é o peer correto com o menor identificador. Por exemplo, em um sistema com N=4 peers, se todos os peers com id=0, 1, 2 e 3 estão corretos, o líder é o processo 0. Se o peer 0 falha, o líder então é o processo 1, e assim por diante.
A falha de um peer deve ser causada simplesmente matando o processo correspondente. A falha deve ser detectada pelo encerramento da conexão TCP correspondente. Observe que após detectar que a conexão caiu, o peer não manda mais heartbeats.
Quando um peer detecta que houve a troca de líder manda uma mensagem TCP urgente para os demais peers. Cada peer mantém e informa o id do líder ao usuário.
Atenção: a eleição só inicia após um peer detectar que todos os demais estão corretos e receberem mensagens de heartbeats de todos os peers. Em outras palavras: o resultado da primeira eleição resulta no peer 0 como líder.
Prepare um arquivo de log para cada execução, concatenando os logs gerados por cada peer individual.
Cada dupla pode fazer a implementação na linguagem que escolher, o professor sugere Python pela produtividade, mas são muito bem vindos trabalhos em C, C++, Java ou qualquer outra linguagem.

ENTREGA DO TRABALHO

Deve ser construída uma página Web, que contém em documentos HTML, os seguintes itens:

Relatório de como foi feito o trabalho e quais foram os resultados obtidos. Use desenhos, diagramas, figuras, todos os recursos que permitam ao professor compreender como a dupla estruturou o trabalho e quais resultados obteve. O objetivo é o professor entender como a dupla fez o trabalho, como o trabalho funciona.
Código Fonte comentado. ATENÇÃO: acrescente a todo programa a terminação ".txt" para que possa ser diretamente aberto em um browser. Exemplos: cliente.py.txt ou servidor.c.txt
Logs de execução dos processos cliente/servidores, que demonstrem a execução correta destes processos. Os testes devem ser exaustivos até o ponto que demonstrem com clareza a funcionalidade correta do sistema.

import discord
from discord import app_commands
from discord.ext import commands

#Codigo desenvolvido pelo O Braixen#0654 usando o apendizado do curso dominando o discord

        #Variaveis Necessarias
donoid = 1111111111 #Coloque sua ID para indicar que você é o dono do bot
id_cargo_atendente = 1111111111 #Coloque aqui o ID do cargo de atendente do primeiro servidor
id_cargo_tribunal = 1111111111 #Coloque aqui o ID do cargo de atendente do segundo servidor
id_categoria_staff = 1111111111 #Coloque aqui o ID da caregoria onde deseja que os tickets sejam criados (para primeiro servidor)
id_categoria_tribunal = 1111111111 #Coloque aqui o ID da caregoria onde deseja que os tickets sejam criados (para Segundo servidor)
token_bot = 'SEU_LINDO_TOKEN_AQUI' #Coloque aqui seu Token do BOT | OBS: Não compartilhe em hipótese alguma o Token

#Variaveis de USO GLOBAL| Se Quiser editar só edite o emojiglobal blz, o resto deixe do jeito que está
emojiglobal = "🦊"
tipoticket = "1"
staff = "1"
mensagemcanal = "1"
categoriadeatendimento = "1"

#PAINEL DE SUPORTE PARA O PRIMEIRO SERVIDOR
class Dropdown(discord.ui.Select): #a class aqui recebeu o nome de Dropdown para cada classe tem que ter Nomes diferentes viu nos proximos você vai ver que eu mudei
    def __init__(self):
        options = [ #Opções do dropdown (Aqui são listadas todas as opções do menu pode adicionar ou remover se necessario) divirta-se
            
            #Ajuda adicional Value(condição para buscar resposta no Callback)| Label (texto que será exibido no menu no chat do discord) | Emoji (é só o emoji)
            
            discord.SelectOption(value="duvidas",label="Dúvidas sobre temas gerais.", emoji="⁉️"),
            discord.SelectOption(value="denuncia",label="Faça uma Denúncia.", emoji="🚨"),
            discord.SelectOption(value="bugs",label="informe um bug no servidor.", emoji="🐞"),
            discord.SelectOption(value="solicitacao",label="Solicitações de cargos ou conversões.", emoji="🔔"),
            discord.SelectOption(value="premiacao",label="Resgatar um prêmio de evento.", emoji="🎁"),
            discord.SelectOption(value="vip",label="Compre seu vip.", emoji="🌟"),
            discord.SelectOption(value="sugestao",label="Envie uma sugestão.", emoji="💡"),
            discord.SelectOption(value="parceria",label="Desejo divulgar no Braixen's House.", emoji="🤝"),
            discord.SelectOption(value="Staff",label="Vire um Staff no Braixen's House.", emoji="💼"),
            discord.SelectOption(value="foxcloud",label="Estado do nosso servidor.", emoji="🖥️"),
            discord.SelectOption(value="outros",label="Nenhuma das opções acima.", emoji="🦊"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...", #Placeholder exibe um texto padrão quando não é selecionado nada pelo usuario
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help" #a ID do seu Dropdown | Importante caso tenha mais de 1 viu pois você tem que editar ele
        )
    async def callback(self, interaction: discord.Interaction): #Retorno do que foi selecionado no menu Dropdown
        # global = to puxando variaveis de fora do codigo para editar elas aqui, são as que estão na linha 5 a 19
        global emojiglobal #Puxa a variavel emoji global para editar posteriormente
        global tipoticket #Puxa a variavel do tipo de ticket para editar posteriormente
        global staff #Puxa a variavel staff para editar posteriormente
        global mensagemcanal #Puxa a variavel de mensagem do canal para editar posteriormente
        global categoriadeatendimento #Puxa a categoria de atendimento para editar posteriormente

        #Abaixo são as condições elas vão usar o VALUE para entrar em uma condição
        if self.values[0] == "duvidas": # < puxo o valor selecionado e verifico se ele é igual a duvidas se sim ele roda a condição, se não ele vai para as proximas.
            emojiglobal = "⁉️" #definindo o emoji antes "1" para o ⁉️
            tipoticket = "Ticket de dúvidas" #definindo o tipo de ticket
            staff = id_cargo_atendente #indicando qual é o staff para esse ticket
            mensagemcanal = "1" #define mensagem do canal | nesse aqui não é usado então eu deixei padrão 1 em outros você verá que terá isso.
            categoriadeatendimento = id_categoria_staff #definindo a categoria de atendimento onde ele deve criar o ticket
            await interaction.response.send_message("**Dúvidas Gerais?** \n\nSabia que temos um canal exclusivo onde você pode ser ajudado por todos. \nTodas as dúvidas estão centralizadas em <#1027376614054576138> e você pode pesquisar lá dentro, se não tiver sua dúvida você mesmo pode postar lá e aguardar alguém te responder.",ephemeral=True) #resposta para a interação texto padrão com o ephemeral ativado (ephemeral é aquelas mensagem que só o proprio membro ve)
    # Daqui para baixo e copia e cola mudando as variaveis, lembre-se as opções aqui devem iniciar primeiro com um if (linha 55) e depois tudo com elif blz, e a quantidade de opções aqui deve ser igual ao dropdown lá em cima, cada dropdown lá tem que ter uma condição aqui.
    # o CreateTicket é o botão de abertura de ticket, aqui puxamos ele mas o codigo dele ta lá em baixo perdido.
        elif self.values[0] == "denuncia":
            emojiglobal = "🚨"
            tipoticket = "Ticket de Denúncias"
            staff = id_cargo_atendente
            mensagemcanal = "**Para a sua denúncia por favor escreva detalhadamente o acontecimento e envia captura de tela ou anexo como prova da sua denuncia, agilize seu atendimento enviando agora mesmo as informações.**"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Deseja denúciar alguém?** \n\nPara **denúnciar** alguém por favor tenha em maos **motivo da denúncia, autor (usuario ou ID) e provas.** \n\nPara prosseguir com sua denúncia abra o ticket abaixo.",ephemeral=True,view=CreateTicket())
      
        elif self.values[0] == "bugs":
            emojiglobal = "🐞"
            tipoticket = "Ticket de Bugs e Problemas"
            staff = id_cargo_atendente
            mensagemcanal = "**Envie uma captura de tela do seu bug aqui neste canal e nos conte como você encontrou esse bug para que possamos resolver.**"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Encontrou um bug em nosso servidor?** \n\nPara reportar um bug em nosso servidor tenha em mãos o **maximo de detalhes** sobre o bug relatado, inclua **capturas de tela** e **descreva detalhadamente.** \nAbra o ticket com o botão abaixo.",ephemeral=True,view=CreateTicket())
        
        elif self.values[0] == "solicitacao":
            emojiglobal = "🔔"
            tipoticket = "Ticket de Solicitações"
            staff = id_cargo_atendente
            mensagemcanal = "**Adiante seu atendimento enviando as informações da sua solicitação, assim que o atendente chegar ele já resolve seu caso imediatamente.**"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Solicitações?** \n\nVocê pode solicitar por varios serviços como por exemplo: \n\n*Mudanças no servidor.* \n*Novos cargos. *\n*Novas Categorias.* \n*Novos Canais.* \n\nAbra o ticket com o botão abaixo.",ephemeral=True,view=CreateTicket())

        elif self.values[0] == "premiacao":
            emojiglobal = "🎁"
            tipoticket = "Ticket de Retirada de Prêmios"
            staff = id_cargo_atendente
            mensagemcanal = "**adiante seu atendimento informando qual é o prêmio que você deseja retirar assim que o atendente chegar ele já sabe do que se trata.**"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Ganhou um Prêmio?** \n\nRetire aqui mesmo seu prêmio de eventos realizados e que sejam entregues pelo Braixen's House. \nAbra o ticket com o botão abaixo.",ephemeral=True,view=CreateTicket())
        
        elif self.values[0] == "sugestao":
            emojiglobal = "💡"
            tipoticket = "Ticket de Sugestões"
            staff = id_cargo_atendente
            mensagemcanal = "1"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Sugestões?** \n\nSabia que temos um canal exclusivo para o envio de sugestões. \nTodas as Súgestões estão centralizadas no <#1027376614054576138> você pode filtrar sua busca ou escrever uma do zero, mas seja bastante detalhista em sua sugestão blz.",ephemeral=True)
        
        elif self.values[0] == "parceria":
            emojiglobal = "🤝"
            tipoticket = "Ticket de divulgações"
            staff = id_cargo_atendente
            mensagemcanal = "O Braixen's House está sujeito a avaliação de requisitos e a possiveis cobranças pela sua divulgação. \n\nNesta Modalidade **todas as parcerias** precisam ser feitas em conjunto com um **sorteio** pois será dessa forma que iremos efetuar **sua divulgação.**\n*Adiante seu atendimento enviando o link do seu servidor para fazermos a analise dele*"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Deseja divulgar algo no Braixen's House?** \n\nNo Momento o *Braixen's House* **Não está Aceitando** novas divulgações nem pedidos de parcerias.\n\nEm Breve voltaremos com esse sistema.",ephemeral=True)
           # await interaction.response.send_message("**Deseja divulgar algo no Braixen's House?** \n\nPara **divulgar seu servidor, bot ou outros projetos.**\nO Braixen's House está sujeito a avaliação de requisitos e a possiveis cobranças pela sua divulgação. \n\nNesta Modalidade **todas as parcerias** precisam ser feitas em conjunto com um **sorteio** pois será dessa forma que iremos efetuar **sua divulgação.**\n*Entre em contato com nossa equipe e tire todas as suas dúvidas*",ephemeral=True,view=CreateTicket())
        
        elif self.values[0] == "Staff":
            emojiglobal = "💼"
            tipoticket = "Ticket de Formulário staff"
            staff = id_cargo_atendente
            mensagemcanal = "1"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Deseja fazer parte do time Braixen's house?** \n\nSabia que temos um formulário para quem está interessado em se tornar um staff você pode abrir ele e verificar se estamos aceitando novos formulários, Olha ta aqui o link: \nhttps://docs.google.com/forms/d/e/1FAIpQLSeZGFDS7g5oiaFV6lE2KiErLCAQXazW3SY9tieWeT5zrlOF5g/viewform?usp=sf_link",ephemeral=True)

        elif self.values[0] == "vip":
            emojiglobal = "🌟"
            tipoticket = "Ticket de Compra de vip"
            staff = id_cargo_atendente
            mensagemcanal = "**Já sabe qual plano vai querer? se não visite <#971011814324334602> e escolha seu plano e depois volte aqui.**\n\n **Adiante seu atendimento indicando se deseja comprar por sonhos ou por Tails coin e o plano desejado.** \n Compras por tails coin use o comando T!pagar Valor @domembro"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Deseja Comprar seu Vip?** \n\nPara comprar seu vip mensal abra um ticket com o botão abaixo.\n\n*Sabia que você pode comprar a assinatura vitalícia diretamente pela loja do Tails usando `T!buy 1` super simples e fácil* ",ephemeral=True,view=CreateTicket())

        
        elif self.values[0] == "foxcloud":
            emojiglobal = "🖥️"
            tipoticket = "Ticket de serviços Foxcloud"
            staff = id_cargo_atendente
            mensagemcanal = "**adiante seu atendimento enviando seu problema incluindo captura de tela, assim que o atendente chegar ele já sabe do que se trata.**"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Problemas com o servidor FoxCloud?** \n\n*Já conhece nossos varios serviços?* \nconsulte todos em <#970376187606097980>. \n\nCaso você tenha dificuldades de acesso aos serviços ou percebeu que um de nossos bots está offline, verifique se já avisamos em <#888567677784829982> ou no nosso canal de <#1009948353251004557>\ncaso não tenhamos informado nada por favor abra um ticket abaixo",ephemeral=True,view=CreateTicket())
       
        elif self.values[0] == "outros":
            emojiglobal = "🦊"
            tipoticket = "Ticket de Outros Motivos"
            staff = id_cargo_atendente
            mensagemcanal = "**Por favor descreva o motivo do seu contato, assim que o atendente chegar ele já sabe do que se trata.**"
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Não tem sua Questão?** \n\nNão tem problema, por favor crie um ticket clicando no botão abaixo",ephemeral=True,view=CreateTicket())

# UFAAA, se chegou até aqui seu primeiro painel já está quase consigurado eu acho, daqui para baixo é mais coisa importante viu.
        
        # PAINEL DE CONTRATAÇÂO TAMBÉM PARA O PRIMEIRO SERVIDOR, MESMAS COISAS DO PRIMEIRO SÒ MUDA VARIAVEL
class Dropdown2(discord.ui.Select): # Olha a classe aqui antes a outra era Dropdown, pela minha falta de criatividade vai Dropdown2
    def __init__(self):
        options = [#Opções do dropdown| mesma pegada do outro porem com opções diferentes e bem menor rsrsrsr
            discord.SelectOption(value="bots",label="Quero desenvolver meu proprio bot.", emoji="🤖"),
            discord.SelectOption(value="servidor",label="Quero montar um servidor.", emoji="🛡️"),
            discord.SelectOption(value="outros",label="Outras Solicitações.", emoji="🌐"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_sevice" #OUUUUUU lembra disso aqui, cada dropdown tem sua propria ID para não ter erro, compare com o de cima e veja a diferença
        )
    async def callback(self, interaction: discord.Interaction): #Retorno seleção Dropdown do painel de contratação
        #mesma coisa do de cima, Puxando variaveis para usar e editar rsrsrs
        global emojiglobal
        global tipoticket
        global staff
        global mensagemcanal
        global categoriadeatendimento

            #mesmo esquema de condição do de lá de cima blz define as coisas, verifica o values e responde
        if self.values[0] == "bots":
            emojiglobal = "🤖"
            tipoticket = "Ticket de Desenvolvimento de Bots"
            staff = id_cargo_atendente
            mensagemcanal = "Conte para a gente como você deseja o seu bot? se já tem alguma coisa fale sobre ela para que possamos te ajudar."
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Deseja ter seu proprio bot?** \n\npois bem o Braixen tem alguns conhecimentos e é bem provável que ele tenha uma solução para você.\n\nabre um ticket ai para ele te ajudar.",ephemeral=True,view=CreateTicket())
       
        elif self.values[0] == "servidor":
            emojiglobal = "💻"
            tipoticket = "Ticket de Montagem de Servidores"
            staff = id_cargo_atendente
            mensagemcanal = "Você já tem uma ideia de como deseja seu servidor? qual tema ele irá abordar? escreva aqui para a gente saber e poder te ajudar."
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Deseja ajuda para montar seu proprio servidor?** \n\no Braixen oferece o serviço de montagem de servidores que inclui **planejamento** e **implantação** de toda a estrutura e configuração de bots populares.\n\no Valor inicial dos serviços é de R$ 40,00 Reais. \n*podendo haver acrecimos com base no tamanho do projeto* \n\n**Não aceitamos pagamento** em Sonhos, Foxcoin ou qualquer outra moeda de bot.",ephemeral=True,view=CreateTicket())
        elif self.values[0] == "outros":
            emojiglobal = "🌐"
            tipoticket = "Ticket de Outras Solicitações"
            staff = id_cargo_atendente
            mensagemcanal = "Conta para a gente oque você deseja solicitar de serviço."
            categoriadeatendimento = id_categoria_staff
            await interaction.response.send_message("**Não tem sua solicitação listada?** \n\nNão se preocupe, crie um ticket assim mesmo.",ephemeral=True,view=CreateTicket())


# PAINEL DO TRIBUNAL PARA O SEGUNDO SERVIDOR | esse é usado no segundo servidor blz mas é copia e cola dos outros só mudando as variaveis.
class Dropdown3(discord.ui.Select): # CLASSEE EDITADA DE NOVOOOOOO BIRL Dropdown3 agora
    def __init__(self):
        options = [#Opções do dropdown qe vão aparecer no dropdown
            discord.SelectOption(value="questionar",label="Quero questionar meu ban.", emoji="🔨"),
            discord.SelectOption(value="duvidas",label="Tenho dúvidas sobre meu ban.", emoji="❓"),
            discord.SelectOption(value="regras",label="Dúvidas sobre as regras.", emoji="📋"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_tribunal" #Olha a porra da ID aqui de novo e ela ta diferente viuuuu lembra disso que vamos usar depois
        )
    async def callback(self, interaction: discord.Interaction): #Retorno seleção Dropdown do painel do tribunal

        #(CTRL+V) mesma coisa do de cima, Puxando variaveis para usar e editar rsrsrs
        global emojiglobal
        global tipoticket
        global staff
        global mensagemcanal
        global categoriadeatendimento
        
        # Aqui é igualzinho aos outros, só muda as condições 🤙
        if self.values[0] == "questionar":
            emojiglobal = "🔨"
            tipoticket = "Ticket de Questionamento de Banimento"
            staff = id_cargo_tribunal
            mensagemcanal = "Por favor escreva no chat o horario que você foi banido e passe a sua ID de usuario ou seu Discord Tag."
            categoriadeatendimento = id_categoria_tribunal
            await interaction.response.send_message("**Deseja Questionar o seu banimento?** \n\nSe você foi banido do Braixen's House e acredita que seu banimento tenha sido injusto.\n\nabre um ticket ai e vamos revisar o seu caso.",ephemeral=True,view=CreateTicket())
       
        elif self.values[0] == "duvidas":
            emojiglobal = "❓"
            tipoticket = "Ticket de Dúvidas"
            staff = id_cargo_tribunal
            mensagemcanal = "nada"
            categoriadeatendimento = id_categoria_tribunal
            await interaction.response.send_message("**Está com dúvidas sobre o seu banimento?** \n\nBom todos os registros do Braixen's House estão disponívels de forma replicada neste servidor, no Canal <#1046777277582692393>.\n\nCaso você não entenda o motivo do seu banimento abra a opção de Questionar seu banimento e vamos exclarecer a todas as suas dúvidas.",ephemeral=True)
        
        elif self.values[0] == "regras":
            emojiglobal = "📋"
            tipoticket = "Ticket de Outras Solicitações"
            staff = id_cargo_tribunal
            mensagemcanal = "nada"
            categoriadeatendimento = id_categoria_tribunal
            await interaction.response.send_message("**Você tem dúvidas sobre as regras?** \n\nNão se preocupe, todas elas estão em <#1046764161398493340>.",ephemeral=True)


                        #PAINEIS PERSISTENTES 
# Isso aqui é importante, essa parte aqui indica que os paineis que criamos devem ser pesistentes, então toda vez que você reiniciar seu bot e já tiver um painel criado ele automaticamente puxa o já existente, assim você não precisa criar um novo toda vez blz.
# LEMBRA das IDS linhas 44, 161 e 209 então elas são diferentes para não confundir esse cara aqui, se elas forem iguais vai bugar esse cara
class DropdownView(discord.ui.View): # Olha a classe aqui, ela é diferente das lá de cima blz.
    def __init__(self): #não me pergunta pq eu não sei oque é só coloca que precisa.
        super().__init__(timeout=None) #isso aqui define o tempo que o painel vai expirar, nesse caso none é NUNCAAAAA.
        self.add_item(Dropdown()) #isso aqui eu to falando que ele vai adicionar o dropdown de novo no caso o painel lá da linha 21.

class DropdownView2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Dropdown2()) # igual o de cima mas esse puxa o da linha 149.

class DropdownView3(discord.ui.View):
    def __init__(self): 
        super().__init__(timeout=None)
        self.add_item(Dropdown3()) # igualzinho mas puxa o linha 197.


                        #Botão Criar Ticket
#lembra do botão que puxamos lá em cima em um monte de opção, ele ta aquiiii
class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None
    
    # visual do botão aqui, label é o texto que vai estar no botão| Style é a cor, consulte a documentação pois tem cores especificas | Emoji é o emoji do botão
    @discord.ui.button(label="Abrir Ticket",style=discord.ButtonStyle.blurple,emoji="🦊")#ESPECIFICAÇÂO DO BOTÂO
    async def ticket(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()
        ticket = None
        #Necessario adicionar verificação de tickets já abertos, por preguiça não fiz isso ainda então a pessoa cria ticket infinito

                #Embed do ticket depois de apertar o botão
        embedticket = discord.Embed(
            colour=discord.Color.yellow(),
            title="Atendimento Braixen's House",
            description=f"*Este é um {tipoticket}*\n*Atendente responsável <@&{staff}>*\n*Comandos dos bots é liberado neste canal*\n\nOlá {interaction.user.mention}, Bem-vindo(a) ao nosso atendimento.\n\n{mensagemcanal}"
        )
        embedticket.set_author(name="Braixen Atendimento",icon_url="https://cdn.discordapp.com/avatars/983000989894336592/58f826dbea65875d346e7820fa15a80a.png?size=2048")
        embedticket.set_thumbnail(url="https://abstract-technology.com/media/plog-2014/ticket.png/@@images/image.png")
        embedticket.set_footer(text="Você pode usar `/fecharticket` para encerrar o atendimento!")

                #comando para abrir canal normal
            #aqui defino novas condições para ser usado na verificação desse codigo.
        atendente = interaction.guild.get_role(staff)
        categoria = interaction.guild.get_channel(categoriadeatendimento)

        overwrites = { #definindo as permissões para o canal que será criado abaixo dica default_role é o everyone blz
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages=True,attach_files=True,use_application_commands=True),
            interaction.user: discord.PermissionOverwrite(read_messages=True,send_messages=True),
            atendente: discord.PermissionOverwrite(read_messages=True,send_messages=True)
        }
        ticket = await interaction.guild.create_text_channel(f"{emojiglobal}┃{interaction.user.name}-{interaction.user.id}",overwrites=overwrites,category=categoria)
        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! Acessa ele ai \n{ticket.mention}")
        await ticket.send(f"Avisando: <@&{staff}>",embed=embedticket)


                #Botão deletar ticket
class DeleteTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.value=None

    @discord.ui.button(label="Encerrar Ticket",style=discord.ButtonStyle.red,emoji="🦊")#ESPECIFICAÇÂO DO BOTÂO
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()
        # puxo os mods de ambos os servidores para fazer a verificação logo abaixo
        mod = interaction.guild.get_role(id_cargo_atendente)
        mod2 = interaction.guild.get_role(id_cargo_tribunal)
        
        # esse IF verifica se quem ta apertando o botão ou é o cara que abriu o ticket ou o mod do primeiro servidor ou do segundo servidor.
        if str(interaction.user.id) in interaction.channel.name or mod in interaction.user.roles or mod2 in interaction.user.roles:
            #se é verdadeiro encerra o atendimento e deleta o ticker
                await interaction.channel.send(f"Encerrando o seu atendimento...")
                await interaction.channel.delete()
        else:
            # se falso manda isso ai em baixo
            await interaction.response.send_message("Ue? Isso não funcionou como deveria...")

                #PARTE QUE LIGA O BOT DE FATO
class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez
   
    async def setup_hook(self) -> None:
        self.add_view(DropdownView())  #carrega o Painel de Suporte já existente
        self.add_view(DropdownView2()) #carrega o Painel de Serviços já existente
        self.add_view(DropdownView3()) #carrega o Painel do Tribunal já existente
    

    async def on_ready(self):
        await self.wait_until_ready()
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Braixen's House")) #atualiza o status que é exibido no bot
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            #await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            await tree.sync() # isso aqui é para comandos globais, necessario para multiplos servidores
            self.synced = True
        print(f"Entramos como {self.user}.") 

aclient = client()
tree = app_commands.CommandTree(aclient)

                #PARTE DOS COMANDOS POR SLASH /

#Variaveis adicionais
mensagemerro = "Ue? Isso não funcionou como deveria... \nAcho que você tentou usar isso em um canal errado ou não tem permissão para tal função..."

                #ABERTURA DE TICKETS POR APPS
@tree.context_menu(name= "Abrir Ticket")
@commands.has_permissions(manage_guild=True)
async def _abrirticket(interaction: discord.Interaction,membro: discord.Member):
    await interaction.response.defer(ephemeral=True)
    atendente = interaction.guild.get_role(id_cargo_atendente)
    categoria = interaction.guild.get_channel(categoriadeatendimento)

    overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages=True,attach_files=True,use_application_commands=True),
        interaction.user: discord.PermissionOverwrite(read_messages=True,send_messages=True),
        membro: discord.PermissionOverwrite(read_messages=True,send_messages=True),
        atendente: discord.PermissionOverwrite(read_messages=True,send_messages=True)
    }
    if str(interaction.user.id) in interaction.channel.name or atendente in interaction.user.roles:
        ticket = await interaction.guild.create_text_channel(f"🦊┃{membro.name}-{membro.id}",overwrites=overwrites,category=categoria)
        await interaction.followup.send(ephemeral=True,content=f"Criei um ticket para você! Acessa ele ai \n{ticket.mention}")
        await ticket.send(f"ticket aberto para {membro.mention} pelo {interaction.user.mention} ")
    else:
        await interaction.followup.send(ephemeral=True,content=mensagemerro)


                #PAINEL DE SUPORTE DO BRAIXEN'S HOUSE
        #esse aqui é o comando para puxar o primeiro painel com o dropdown aqui você pode editar todas as condições para a mensagem.
@tree.command(name = 'painel_suporte', description='Crie um Menu para atendimento de suporte')
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    #meu embed bonito
    embed1 = discord.Embed(
        colour=discord.Color.yellow(),
        title="Atendimento Braixen's House",
        description="Seja bem-vindo(a) a nossa **seção de ajuda** do **Braixen's House.** \n \nAqui você pode tirar dúvidas, pedir ajuda para alguns problemas, solicitar cargos, informar sobre problemas de acesso, sugestões de mudanças entre outros basta selecionar a opção desejada."
    )
    #imagem do meu embed
    embed1.set_image(url="https://cdn.discordapp.com/attachments/774046644114030632/1046881160174772345/Tickets.png")

    await interaction.channel.send(embed=embed1,view=DropdownView()) 


                #PAINEL DE SERVIÇOS DO BRAIXEN'S HOUSE
        #Mesmo do de cima
@tree.command(name = 'painel_servicos', description='Crie um Menu para atendimento de serviços.')
@commands.has_permissions(manage_guild=True)
async def setup2(interaction: discord.Interaction):
    #meu embed bonito
    embed2 = discord.Embed(
        colour=discord.Color.yellow(),
        title="Contratação Braixen's House",
        description="Seja bem-vindo(a) a nossa **seção de contrate** do **Braixen's House.** \n \nAqui você pode Contratar os meus serviços para **Consultoria, Planejamento, Desenvolvimento** de servidores e **Implantação** de bots.\n\n**Atenção** não abra ticket sem motivo, caso contrario poderemos lhe aplicar **punição**."

    )
    #imagem do meu embed
    embed2.set_image(url="https://cdn.discordapp.com/attachments/774046644114030632/970451269179306034/contrate.png")

    await interaction.channel.send(embed=embed2,view=DropdownView2()) 

                #PAINEL DO TRIBUNAL DO BRAIXEN'S HOUSE
        #mesmo do de cima 
@tree.command(name = 'painel_tribunal', description='Crie um Menu para atendimento do tribunal.')
@commands.has_permissions(manage_guild=True)
async def setup2(interaction: discord.Interaction):
    #meu embed bonito
    embed3 = discord.Embed(
        colour=discord.Color.yellow(),
        title="Tribunal Braixen's House",
        description="Seja bem-vindo(a) ao **Tribunal** do **Braixen's House.** \n \nAqui você pode verificar e contestar banimentos e avisos que aconteceram no Braixen's House.\n\n**Atenção** não abra ticket sem motivo, caso contrario poderemos ignorar sua solicitação."
    )
    #imagem do meu embed
    embed3.set_image(url="https://cdn.discordapp.com/attachments/774046644114030632/1046865780924489848/Tribunal.png")

    await interaction.channel.send(embed=embed3,view=DropdownView3()) 

                #COMANDO PARA FECHAR UM TICKET
        #esse cara manda um texto e manda junto o botão de fechar ticket 
@tree.command(name="fecharticket",description='Feche um atendimento atual.')
async def _fecharticket(interaction: discord.Interaction):
    mod = interaction.guild.get_role(id_cargo_atendente)
    mod2 = interaction.guild.get_role(id_cargo_tribunal)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.user.roles or mod2 in interaction.user.roles:
        await interaction.response.send_message("**Você deseja mesmo Encerrar seu atendimento?** \nuse o botão abaixo para confirmar.",view=DeleteTicket())
 
    else:
        await interaction.response.send_message(mensagemerro,ephemeral=True)


                #COMANDO DE ENVIO DE OBRIGADO
        #esse aqui manda um obrigado ao membro da equipe do servidor, necessario marcar o membro na condição desse comando.
@tree.command(name='atendimento_obrigado', description='Envia um agradecimento ao usuario atendido.')
async def _obrigado(interaction: discord.Interaction,membro: discord.Member):
    mod = interaction.guild.get_role(id_cargo_atendente)
    mod2 = interaction.guild.get_role(id_cargo_tribunal)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.user.roles or mod2 in interaction.user.roles:
        await interaction.response.send_message("enviando mensagem...",ephemeral=True)
        await interaction.channel.send(f"Olá {membro.mention}!!!, acho que esse é o fim do seu atendimento. \n\nO *Braixen's House* Agradece o contato\n**Use o comando /fecharticket para finalizar seu atendimento**")
    else:
        await interaction.response.send_message(mensagemerro,ephemeral=True)

        
                #COMANDO PARA ADICIONAR ALGUEM A ALGUM ATENDIMENTO
        #esse aqui adiciona um novo membro ao atendimento atual e notifica no chat que foi adicionado
@tree.command(name="atendimento_adicionar",description='Adicione um membro ao ticket.')
async def _adicionar(interaction: discord.Interaction,membro: discord.Member):
    mod = interaction.guild.get_role(id_cargo_atendente)
    mod2 = interaction.guild.get_role(id_cargo_tribunal)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.user.roles or mod2 in interaction.user.roles:
        resposta = discord.Embed(
            colour=discord.Color.green(),
            title="🦊 ⠂ Adicionado ao atendimento",
            description=f"Membro: {membro.mention} foi adicionado ao atendimento"
        )
        await interaction.response.send_message(embed=resposta)
        await interaction.channel.set_permissions(membro, read_messages=True,send_messages=True)
    else:
        await interaction.response.send_message(mensagemerro,ephemeral=True)


                #COMANDO PARA REMOVER ALGUEM A ALGUM ATENDIMENTO
        #esse aqui remove um membro do atendimento atual e notifica no chat que foi removido
@tree.command(name="atendimento_remover",description='Remove um membro do ticket.')
async def _remover(interaction: discord.Interaction,membro: discord.Member):
    mod = interaction.guild.get_role(id_cargo_atendente)
    mod2 = interaction.guild.get_role(id_cargo_tribunal)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.user.roles or mod2 in interaction.user.roles:
        resposta = discord.Embed(
            colour=discord.Color.red(),
            title="🦊 ⠂ Removeu do atendimento",
            description=f"Membro: {membro.mention} foi removido do atendimento"
        )
        await interaction.response.send_message(embed=resposta)
        await interaction.channel.set_permissions(membro, read_messages=False,send_messages=False)
    else:
        await interaction.response.send_message(mensagemerro,ephemeral=True)

        
                #COMANDO SAY
        #comando say padrão né, esse aqui só pode ser usado pelo dono blz 
@tree.command(name="say",description='Diga alguma coisa como o bot')
async def _say(interaction: discord.Interaction, mensagem: str):
    if interaction.user.id == donoid:
        await interaction.response.send_message("enviando sua mensagem...",ephemeral=True)
        await interaction.channel.send(f"{mensagem}")
    else:
        await interaction.response.send_message(mensagemerro,ephemeral=True)

        
                #COMANDO BAN
        #comandinho de banimento padrão
@tree.command(name="ban",description='Banir um membro do servidor')
@commands.has_permissions(ban_members=True)
async def _ban(interaction: discord.Interaction, membro: discord.Member, razão: str):
    if interaction.permissions.ban_members:
        resposta = discord.Embed(
            colour=discord.Color.red(),
            title="🦊 ⠂ Banido",
            description=f"Membro: {membro}\nRazão: {razão}"
        )
        await membro.ban(reason=razão)
        await interaction.response.send_message(embed=resposta)
    else: await interaction.response.send_message(mensagemerro,ephemeral=True)


                #COMANDO ADD ROLE
        #comandinho de Adicionar cargo a um membro padrão
@tree.command(name="cargo_adicionar",description='Adiciona um cargo a um membro')
@commands.has_permissions(manage_roles=True)
async def _roleadd(interaction: discord.Interaction, membro: discord.Member, cargo: discord.Role):
    if interaction.permissions.manage_roles:
        resposta = discord.Embed(
            colour=discord.Color.yellow(),
            title="🦊 ⠂ Cargo Adicionado",
            description=f"Membro: {membro.mention}\nCargo: {cargo}"
        )
        await membro.add_roles(cargo)
        await interaction.response.send_message(embed=resposta)
    else: await interaction.response.send_message(mensagemerro,ephemeral=True)


                #COMANDO REM ROL
        #comandinho de remover cargo de um membro padrão
@tree.command(name="cargo_remover",description='Adiciona um cargo a um membro')
@commands.has_permissions(manage_roles=True)
async def _rolerem(interaction: discord.Interaction, membro: discord.Member, cargo: discord.Role):
    if interaction.permissions.manage_roles:
        resposta = discord.Embed(
            colour=discord.Color.yellow(),
            title="🦊 ⠂ Cargo Removido",
            description=f"Membro: {membro.mention}\nCargo: {cargo}"
        )
        await membro.remove_roles(cargo)
        await interaction.response.send_message(embed=resposta)
    else: await interaction.response.send_message(mensagemerro,ephemeral=True)


                # RODA O BOT SÓ RODA
aclient.run(token_bot)

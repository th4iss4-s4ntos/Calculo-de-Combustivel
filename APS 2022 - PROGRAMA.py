print ( 'Bem vindo à pesquisa de Créditos de Carbono' )
z  = ( '---------------------------' )
print ( z )
e  = ( '' )
a  =  1
while  True :  
    b  =  1
    if  a  ==  1  or  a ==  2  or  a == 3  or  a == 4 :
        print ( '1 - Digite o número de uma das opções: ' )
        print ( '2 - Crédito de Carbono' )
        print ( '3 - Grupo' )
        print ( '4 - Cálculos' )
        print ( '5 - Fechar o Programa' )
    a  =  int ( input ())
    print ( z )
    if  a  ==  1 :
        while  b  ==  1  or  b  ==  2  or  b  ==  3  or  b  ==  4  or  b  ==  5  or  b  ==  6  or  b  ==  7  or  b  ==  8 :
            print ( '1-O que são créditos de carbono?' )
            print ( '2-Como os créditos de carbono são gerados e comercializados?' )
            print ( '3-Qual a relação do Brasil com isso?' )
            print ( '4 - Iluminação pública e emissão de CO2' )
            print ( '5 - Eletrodomésticos aumentam as emissões ?' )
            print ( '6-Como ocorrem as emissões de GEE na geração de energia elétrica?' )
            print ( '7 - Você sabe quanto os carros ou motos emitem de gases poluentes ?' )
            print ( '8 - Os carros que dirigimos no dia-a-dia, quanto poluem?' )
            print ( '9 - Voltar no programa' )
            b  =  int ( input ())
            print ( z )
            if  b  ==  1 :
                print ( 'O crédito de carbono é um conceito que surgiu no ano de 1997, dentro do acordo ambiental do Protocolo de Kyoto. O grande objetivo relacionado a esse conceito é reduzir a emissão dos gases do efeito estufa no planeta para combater as mudanças climáticas que gerou grande preocupação mundial. Basicamente, o crédito de carbono é caracterizado como uma moeda utilizada no mercado de carbono, onde um crédito equivale a uma tonelada de CO2 (dióxido de carbono) que deixou de ser produzido e liberado ao meio ambiente.')
                print (z)
            if  b  ==  2 :
                print ( 'Os créditos são gerados a partir do investimento em ações que promovem estratégias que gerem economia de baixo carbono, como o uso de energias renováveis, caso da energia eólica, solar e as diversas formas de biomassa.' )
                print ( z )
            if  b  ==  3 :
                print ( 'Pelas suas características alimentaram em sustentabilidade, o Brasil possui grande representatividade no mercado de carbono, ficando atrás somente da Índia e da China.' )
                print ( z )
            if  b  ==  4 :
                print ( 'A iluminação pública é responsável por quase 25% da emissão de CO2 no mundo, um gás causador do efeito estufa.' )
                print ( 'Por isso, ela se tornou parte das pautas globais sobre os impactos da emissão de C02 para o planeta. Para você entender melhor, saiba que apenas uma unidade de lâmpada incandescente solta 2,7 kg de CO2 na atmosfera.' )
                print ( 'Isso fez com que a sua participação no cenário da iluminação começasse a ser questionada. O fato é que os efeitos do aquecimento global são cada vez mais perceptíveis. Desse modo, toda tecnologia que representa uma ameaça deve ser trocada por outra mais sustentável .' )
                print ( z )
            if  b  ==  5 :
                print ( 'Não, nem todos os eletrodomésticos emitem gases de estufa diretamente, como se verá mais adiante. Mas todos consomem muita energia elétrica. E o setor de energia emite gases. eles consomem, mais gases o setor emite. As residências brasileiras foram responsáveis ​​por 29% de toda a energia consumida no País, em 2018.' )
                print ( z )
            if  b  ==  6 :
                print ( 'A queima de combustíveis fósseis para a geração de energia elétrica é o principal contribuinte para a emissão de GEE poluentes como dióxido de carbono (CO2), metano (CH4) e óxido nitroso (N2O), entre outros, impactando a saúde pública endo agravar a crise climática Isso quer dizer que além de utilizar recursos naturais finitos, a energia produzida por meio da queima do petróleo, do carvão mineral ou do gás natural (termelétrica) e da fissão nuclear são menos emitidos por emitir grande quantidade de GEE .' )
                print ( z )
            if  b  ==  7 :
                print ( 'Primeiramente, precisamos saber como quantificar o volume de emissões que os veículos automotores geram.' )
                print ( 'Em uma combustão ideal, todo o combustível queimado deveria virar gás carbônico (CO2). O gás carbônico não é considerado um poluente por não prejudicar o organismo humano, mas é um gás estufa. Daí a preocupação com a quantidade de sua emissão , pois seu volume gerado se mostra muito grande em relação aos outros poluentes.' )
                print ( 'Assim, os engenheiros de motores convencionaram medir o nível de emissão de poluentes de um veículo em gramas de gás carbônico por quilômetro rodado, cuja notação é gCO2/km.' )
                print ( 'No mundo real, a combustão nunca é completa, e outros poluentes muito mais negativos advêm do funcionamento dos motores, como o monóxido de carbono (CO), hidrocarbonetos (HC) e óxido nitroso (NOx). Saiba mais sobre os gases poluentes neste artigo:' )
                print ( z )
            if  b  ==  8 :
                print ( 'Os modelos menos poluentes são os híbridos comercializados atualmente no Brasil (2017), notadamente o Toyota Prius, Lexus CT200h e Ford Fusion. Todos emitem entre 50 e 80 gCO2/km. O grupo PSA fez um ótimo trabalho no seu motor 1.2 Puretech, com todos os modelos emitindo abaixo de 100 gCO2/km. A Volkswagen também possui modelos que emitem menos de 100 gCO2/km em 2017.' )
                print ( 'Na média, os modelos zero quilômetro emitem entre 100 e 300 gramas de gás carbônico por quilômetro, entre compactos de entrada e SUV´s grandes a diesel.' )
                print ( 'Confira o quanto seu carro emite neste documento de homologação da CONPET, entidade responsável pela homologação de eficiência energética.' )
                print ( z )
    if  a  ==  3 :
        b  =  3
        while  b  !=  1  and  b  !=  2 :
            print ( 'Qual o tipo de combustível do seu carro?' )
            print ( '1 - Gasolina' )
            print ( '2 - Diesel' )
            b  =  int ( input ())
            print ( 'Digite quantos km voce pretende andar' )
            km  =  float ( input ())
            if  b  ==  1 :
                l  =  km * 10
                c  =  l * 0,82  * 3,7
                cc  =  c / 1000 * 365
                print ( f'Você gastará { l } L para essa viagem e gerará { round ( c , 2 ) } kg de CO2, que em crédito carbono, vale R$ { round ( cc , 2 ) } ' )
                print ( z )
            elif  b  ==  2 :
                l  =  km * 3
                c  =  l * 0,83 * 3,7
                cc  =  c / 1000 * 365
                print ( f'Você gastará { l } L para essa viagem e gerará { round ( c , 2 ) } kg de CO2, que em crédito carbono, vale R$ { round ( cc , 2 ) } ' )
                print ( z )
            else :
                print ( 'Digite um valor valido' )
    if  a  ==  4 :
        break
    else :
        print ( 'Digite um valor valido: ' )
        print ( 'Obrigado por usar nosso programa' )

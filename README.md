# santander-cobranca-xml

Consumes the API given by Santander in order to register a *boleto bancário*.

In Brazil, Santander requires the use of a client ssl certificate.

## Example

Notice that one may not use the same ticket twice. Thus, in this examples, it is necessary to request two tickets, one to register the *boleto bancário* and the other to retrieve the status.

```
nosso_numero = '1'
data = {
	'cod_convenio': 'CONVENIO',
	'tp_doc': '01', # 01=CPF, 02=CNPJ
	'num_doc': '11111111111',
	'pagador_nome': '',
	'pagador_endereco': '',
	'pagador_bairro': '',
	'pagador_cidade': '',
	'pagador_uf': '',
	'pagador_cep': '',
	'nosso_numero': nosso_numero,
	'seu_numero': nosso_numero,
	'data_vencimento': '30062017',
	'data_emissao': '27062017',
	'especie': '02', # Duplicada mercantil
	'valor_nominal': '102', # R$ 1,02
	'multa': '0',
	'qt_dias_multa': '0',
	'juros': '0',
	'tipo_desconto': '0', # Isento
	'valor_desconto': '0',
	'data_limite_desconto': '00000000',
	'valor_abatimento': '0',
	'tipo_protesto': '0', # Não protestar
	'qt_dias_protesto': '0',
	'qt_dias_baixa': '15',
	'mensagem': 'Teste',
}
estacao = 'SUA_ESTACAO'
nsu = '1'
data_nsu = '28062017'
cert = ('path to certificate', 'path to private key')
ret1 = get_ticket(data, cert=cert)
print '-- solicita ticket --'
print 'retCode', ret1.return_code
print 'ticket', ret1.ticket
print ''
ret2 = incluir_titulo(ret1.ticket, estacao=estacao, nsu=nsu, data_nsu=data_nsu, cert=cert, teste=False)
print '-- incluir titulo --'
print 'nsu', nsu
print 'data nsu', data_nsu
print 'situacao', ret2.situacao
print 'descricao', ret2.descricao
print ''
ret3 = get_ticket(data, cert=cert)
print '-- solicita ticket --'
print 'retCode', ret3.return_code
print 'ticket', ret3.ticket
print ''
ret4 = consultar_titulo(ret3.ticket, estacao=estacao, nsu=nsu, data_nsu=data_nsu, cert=cert, teste=False)
print '-- consulta titulo --'
print 'situacao', ret4.situacao
print 'descricao', ret4.descricao
print ''
```

## Testing

I have tested using my company's client ssl certificate and it worked fine.
